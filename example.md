## **1️⃣ Understanding the Inputs**
Let's assume our graph is:
```python
graph = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"],
    "D": ["C"]
}
```
Each node initially has an **equal PageRank**:
```python
pagerank = {
    "A": 0.25,
    "B": 0.25,
    "C": 0.25,
    "D": 0.25
}
```

Now, after running the **mapper function**, we get the `mapped_data`, which stores how much PageRank each node distributes:

```python
mapped_data = {
    "A": {"B": 0.125, "C": 0.125},  # A splits its 0.25 PageRank to B and C
    "B": {"C": 0.25},               # B gives all of its PageRank to C
    "C": {"A": 0.25},               # C gives all of its PageRank to A
    "D": {"C": 0.25}                # D gives all of its PageRank to C
}
```
This means:
- `A` gives **0.125 to B** and **0.125 to C**.
- `B` gives **0.25 to C**.
- `C` gives **0.25 to A**.
- `D` gives **0.25 to C**.

---

## **2️⃣ How the Reduce Step Works**
Now, let's process the reduce step **line by line** with this `mapped_data`.

```python
reduced_data = {}  
for node in mapped_data.keys():  
    values = []  
    for n in mapped_data.keys():  
        if node in mapped_data[n]:  
            values.append(mapped_data[n][node])  
    reduced_data[node] = self.reducer(node, values)  
```

### **Step 1: Initialize an Empty Dictionary**
```python
reduced_data = {}
```
This dictionary will store the **new PageRank values** after aggregation.

---

### **Step 2: Iterate Through Each Node in `mapped_data`**
For each **node**, we collect all incoming PageRank contributions.

#### **Processing Node `A`**
```python
values = []
for n in mapped_data.keys():
    if "A" in mapped_data[n]:  
        values.append(mapped_data[n]["A"])
```
- `"A"` is **not** present in `mapped_data["A"]`, so skip.
- `"A"` is **not** present in `mapped_data["B"]`, so skip.
- `"A"` **is present** in `mapped_data["C"]` → **Append `0.25`**.
- `"A"` is **not** present in `mapped_data["D"]`, so skip.

Thus, `values = [0.25]`.

#### **Processing Node `B`**
```python
values = []
for n in mapped_data.keys():
    if "B" in mapped_data[n]:  
        values.append(mapped_data[n]["B"])
```
- `"B"` **is present** in `mapped_data["A"]` → **Append `0.125`**.
- `"B"` is **not** present in `mapped_data["B"]`, so skip.
- `"B"` is **not** present in `mapped_data["C"]`, so skip.
- `"B"` is **not** present in `mapped_data["D"]`, so skip.

Thus, `values = [0.125]`.

#### **Processing Node `C`**
```python
values = []
for n in mapped_data.keys():
    if "C" in mapped_data[n]:  
        values.append(mapped_data[n]["C"])
```
- `"C"` **is present** in `mapped_data["A"]` → **Append `0.125`**.
- `"C"` **is present** in `mapped_data["B"]` → **Append `0.25`**.
- `"C"` is **not** present in `mapped_data["C"]`, so skip.
- `"C"` **is present** in `mapped_data["D"]` → **Append `0.25`**.

Thus, `values = [0.125, 0.25, 0.25]`.

#### **Processing Node `D`**
```python
values = []
for n in mapped_data.keys():
    if "D" in mapped_data[n]:  
        values.append(mapped_data[n]["D"])
```
- `"D"` is **not** present in any `mapped_data`, so `values = []`.

---

## **3️⃣ Apply the Reducer Function**
For each node, we now pass its collected values to `self.reducer(node, values)`, which calculates the **new PageRank**.

```python
reduced_data["A"] = self.reducer("A", [0.25])
reduced_data["B"] = self.reducer("B", [0.125])
reduced_data["C"] = self.reducer("C", [0.125, 0.25, 0.25])
reduced_data["D"] = self.reducer("D", [])
```

### **Example Calculation in `reducer()`**
```python
def reducer(self, node, values):
    new_rank = (1 - self.DAMPING_FACTOR) / self.N  # Base rank
    adjacency_list = []
    
    for value in values:
        new_rank += self.DAMPING_FACTOR * value  # Add contributions
    
    return new_rank, adjacency_list
```
- **Damping Factor** `= 0.85`
- **Total Nodes (`N`)** `= 4`
- **Base Rank** `= (1 - 0.85) / 4 = 0.0375`

#### **Updating `A`**
```python
new_rank = 0.0375 + (0.85 * 0.25)
         = 0.0375 + 0.2125
         = 0.25
```

#### **Updating `B`**
```python
new_rank = 0.0375 + (0.85 * 0.125)
         = 0.0375 + 0.10625
         = 0.14375
```

#### **Updating `C`**
```python
new_rank = 0.0375 + (0.85 * (0.125 + 0.25 + 0.25))
         = 0.0375 + (0.85 * 0.625)
         = 0.0375 + 0.53125
         = 0.56875
```

#### **Updating `D`**
```python
new_rank = 0.0375 + (0.85 * 0)  
         = 0.0375
```

### **Final `reduced_data`**
```python
reduced_data = {
    "A": (0.25, []),
    "B": (0.14375, []),
    "C": (0.56875, []),
    "D": (0.0375, [])
}
```

---

## **4️⃣ Final Outcome**
- **Node `A`'s PageRank stays 0.25**.
- **Node `B`'s PageRank drops to 0.14375**.
- **Node `C`'s PageRank increases to 0.56875** (since it received a lot of contributions).
- **Node `D`'s PageRank is very low at 0.0375** (it gets no contributions).

---

### **Summary**
🔹 **`mapped_data` stores PageRank contributions from the Mapper step**.  
🔹 **The Reduce step gathers these contributions for each node**.  
🔹 **Each node's new PageRank is computed using the reducer function**.  
🔹 **Higher PageRank means a node gets more importance in the graph**.