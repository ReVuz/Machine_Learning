import multiprocessing
from typing import Dict, List, Any

class PageRankMapReduce:
    def __init__(self, graph: Dict[str, List[str]], damping_factor: float = 0.8, iterations: int = 10):
        self.graph = graph
        self.DAMPING_FACTOR = damping_factor
        self.ITERATIONS = iterations
        self.N = len(graph)
        
        # Initialize PageRank equally
        self.pagerank = {node: 1.0 / self.N for node in graph}

    def mapper(self, node: str, mapped_data: Dict[str, Any]) -> None:
        neighbors = self.graph.get(node, [])    #outgoing liks edkkan
        rank = self.pagerank[node]      #current page rank calculate cheyyan
        num_neighbors = len(neighbors)
        
        #shared dictionary to store contributions
        contributions = {}

    #neighbors indel contributions kandpidikkan
        if num_neighbors > 0:
            share = rank / num_neighbors        # Divide PageRank among neighbors
            for neighbor in neighbors:
                contributions[neighbor] = share     # Each neighbor gets a share
        
        # Storing adjacency list
        contributions[node] = (None, neighbors)
        mapped_data[node] = contributions

   #Update PageRank
    def reducer(self, node: str, values: List[Any]) -> tuple:
       
       #Random Jump Factor(Loop indel)
        new_rank = (1 - self.DAMPING_FACTOR) / self.N  # Base rank to avoid dead ends
        adjacency_list = []
        
        for value in values:
            if isinstance(value, tuple):  # This is the adjacency list
                adjacency_list = value[1]
            else:
                new_rank += self.DAMPING_FACTOR * value  # Add contribution
        
        return new_rank, adjacency_list

    def map_reduce(self) -> Dict[str, float]:

        for _ in range(self.ITERATIONS):
            with multiprocessing.Manager() as manager:
                mapped_data = manager.dict()
                processes = []
                
                # Creates separate processes for each node to execute mapper in parallel.
                for node in self.graph:
                    p = multiprocessing.Process(target=self.mapper, args=(node, mapped_data))
                    p.start()
                    processes.append(p)
                
                for p in processes:
                    p.join()
                
                # Aggregate contributions and update PageRank
                reduced_data = {}
                for node in mapped_data.keys():
                    values = []
                    for n in mapped_data.keys():
                        if node in mapped_data[n]:
                            values.append(mapped_data[n][node])
                    reduced_data[node] = self.reducer(node, values)
                
                # Update PageRank
                self.pagerank = {node: rank for node, (rank, *_) in reduced_data.items()}
        
        return self.pagerank

def main():

    graph = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C"]
    }
    
    pagerank_calculator = PageRankMapReduce(graph)
    final_pagerank = pagerank_calculator.map_reduce()
    print("PageRank Results:")
    for node, rank in final_pagerank.items():
        print(f"Node {node}: {rank:.4f}")

if __name__ == "__main__":
    main()