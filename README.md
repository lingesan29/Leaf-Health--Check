# 🌿 Leaf Health Check AI

Leaf Health Check AI is a **machine learning based web application** that detects plant leaf diseases using image processing and deep learning.  
Users can upload a leaf image and the system will analyze it to identify whether the leaf is healthy or affected by a disease.

The application is built using **Python, TensorFlow, OpenCV, and Streamlit**.

---

## 🚀 Features

- Upload plant leaf image
- AI-based disease detection
- Shows prediction confidence
- Provides recommended solution for detected disease
- Simple web interface using Streamlit
- CNN model trained on plant leaf dataset

---

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Streamlit
- Pillow

---

## 📂 Project Structure

```
leaf-health-check-ai
│
├── app.py
├── train_model.py
│
├── model
│   └── leaf_model.h5
│
├── utils
│   ├── preprocess.py
│   ├── predict.py
│   └── solution.py
│
├── dataset
│   ├── healthy
│   ├── bacterial_spot
│   ├── early_blight
│   ├── late_blight
│   └── leaf_mold
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/leaf-health-check-ai.git
```

2. Navigate to the project folder

```bash
cd leaf-health-check-ai
```

3. Install required libraries

```bash
pip install -r requirements.txt
```

---

## 🧪 Train the Model

Run the training script to create the disease detection model.

```bash
python train_model.py
```

The trained model will be saved in:

```
model/leaf_model.h5
```

---

## ▶️ Run the Application

Start the Streamlit web application:

```bash
streamlit run app.py
```

Open the browser and visit:

```
http://localhost:8501
```

Upload a leaf image and the system will predict the disease.

---

## 🌱 Dataset

This project uses plant leaf images from the **PlantVillage dataset**.

Dataset includes:

- Healthy Leaf
- Bacterial Spot
- Early Blight
- Late Blight
- Leaf Mold

---

## 📊 Output Example

- Disease Name
- Confidence Percentage
- Recommended Treatment

Example:

```
Prediction: Early Blight
Confidence: 92.45%

Recommended Solution:
Use fungicide and maintain proper plant spacing.
```

---

## 🔮 Future Improvements

- Mobile camera input
- Real-time disease detection
- Support for more plant species
- Deployment using cloud platforms
- Mobile application integration

---

## 👨‍💻 Author

Lingesan Venkatesan  
BSc Computer Science with Artificial Intelligence  

---

## 📜 License

This project is created for **educational and research purposes**.
