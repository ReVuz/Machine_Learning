# 🧠 Machine Learning & Digital Image Processing – Academic Projects

This repository includes my academic work in Machine Learning and Digital Image Processing. It consists of practical implementations, conceptual notebooks, and lab-style explorations developed as part of my coursework.

---

## 📁 Contents

### 🔍 Machine Learning Projects

#### 1. `Depression_detection_with_neural_nets.ipynb`
A neural network–based approach to detecting depressive sentiment in text data. Focuses on preprocessing, feature extraction, and model training using deep learning.

#### 2. `EDA_using_python.ipynb`
Exploratory Data Analysis (EDA) notebook using pandas, matplotlib, and seaborn. Analyzes data distributions, outliers, and trends.

#### 3. `Text_to_SQL.ipynb`
A basic implementation for converting natural language questions into SQL queries. Includes tokenization, classification, and SQL query generation.

---

## 🔁 Cross-Validation Techniques

This section provides a concise overview of key cross-validation techniques used in model evaluation:

1. **K-Fold Cross-Validation**  
   - Splits the dataset into *k* equal-sized folds.
   - Each fold is used once as the validation set, while the remaining *k-1* folds form the training set.

2. **Hold-Out Cross-Validation**  
   - Splits the dataset into separate training and testing sets (e.g., 80/20 or 70/30).
   - Simple and fast but less reliable due to single random split.

3. **Stratified K-Fold Cross-Validation**  
   - Extension of K-Fold that maintains class distribution across all folds.
   - Especially useful for imbalanced datasets.

4. **Leave-P-Out Cross-Validation (LPOCV)**  
   - Repeatedly trains the model using all data except *p* samples, which are used for testing.
   - Computationally intensive but exhaustive.

5. **Leave-One-Out Cross-Validation (LOOCV)**  
   - A special case of LPOCV where *p = 1*.
   - Each sample is used once as a test set; best for small datasets.

6. **Monte Carlo (Shuffle-Split) Cross-Validation**  
   - Randomly splits data into training and testing sets multiple times.
   - Flexible but may lead to test sets overlapping.

7. **Time Series (Rolling) Cross-Validation**  
   - Used when data is time-dependent.
   - Training set includes past data, and the test set includes future data to preserve temporal order.

📘 Notebook coming soon: `cross_validation_techniques.ipynb`

---

## 🖼️ Digital Image Processing (DIP) Projects

This section includes foundational techniques used in image preprocessing and analysis.

### Topics Covered:

- **Image Enhancement**: Histogram Equalization, Contrast Stretching  
- **Noise Removal**: Gaussian Blur, Median Filtering  
- **Edge Detection**: Sobel, Prewitt, Canny Operators  
- **Morphological Operations**: Dilation, Erosion, Opening, Closing  
- **Color Space Conversions**: RGB ↔ Grayscale, HSV  
- **Frequency Domain Analysis**: Fourier Transform  
- **Image Segmentation**: Thresholding, Region Growing, Contour Detection  

📘 Notebook coming soon: `dip_lab_experiments.ipynb`

---

## 🛠️ Tech Stack

- Python
- Jupyter Notebook
- pandas, NumPy, matplotlib, seaborn
- scikit-learn, TensorFlow / PyTorch
- OpenCV (for image processing)

---

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/ReVuz/Machine_Learning.git
cd Machine_Learning
