# Deep Learning Projects

A collection of my Deep Learning projects and experiments built while learning and implementing concepts such as **Perceptrons, Artificial Neural Networks (ANNs), Convolutional Neural Networks (CNNs), backpropagation, optimization, and computer vision**.

The projects in this repository focus on applying deep learning concepts to practical problems using Python and popular machine learning frameworks.

## Projects

### 1. HEART Upgrade

An existing heart disease prediction project that I upgraded by implementing **Perceptron and Artificial Neural Network (ANN)** models.

**Concepts implemented:**

* Perceptron
* Artificial Neural Network (ANN)
* Neural network architecture
* Forward propagation
* Backpropagation
* Activation functions
* Model training and evaluation
* Heart disease prediction

**Technologies:**

* Python
* NumPy
* Pandas
* Scikit-learn
* TensorFlow / Keras

---

### 2. Cats vs Dogs CNN

A **Convolutional Neural Network (CNN)** project for classifying images as either **Cats or Dogs**.

The project includes image preprocessing, resizing, CNN model training, and image classification.

**Concepts implemented:**

* Image preprocessing
* Image resizing
* Convolutional layers
* Pooling layers
* CNN architecture
* Binary image classification
* Model evaluation
* Prediction on new images

**Technologies:**

* Python
* TensorFlow / Keras
* NumPy
* OpenCV
* Matplotlib

### Dataset

The dataset is **not included in this repository** because of its size.

The `cnn_model.pkl` is also **not included in this repository** because of its size.

You can download the dataset and model from the following Google Drive links:

**Dataset:** https://drive.google.com/drive/folders/1L5QZfAvUXmJ1gmSpBJWj79iaTShNp8ik?usp=drive_link

**Model:** https://drive.google.com/file/d/1o8_7pbEOz8RtU1J2CM91PdnzK2OD4ev2/view?usp=drive_link

After downloading the dataset, place it in the appropriate dataset folder before running the project.

---

### 3. Bone Fracture Detection

A **Deep Learning image classification project** that uses a trained CNN model to detect bone fractures from **X-ray images**.

The application allows the user to upload an X-ray image, preprocesses and resizes the image to **256 × 256 pixels**, and uses a trained **Keras model** to predict whether a fracture is present.

The project also includes a **Streamlit web interface** for easy interaction with the trained model.

**Concepts implemented:**

* Image preprocessing
* Image resizing
* Convolutional Neural Networks (CNN)
* Binary image classification
* X-ray image classification
* Model prediction
* Model deployment
* Streamlit application

**Technologies:**

* Python
* TensorFlow / Keras
* NumPy
* Pillow
* Streamlit

**Model:**

The project uses a trained `bone-fracture.keras` model for making predictions.
**Dataset:** https://www.kaggle.com/datasets/osamajalilhassan/bone-fracture-dataset

**Application:**

The Streamlit application provides an interface where users can upload an X-ray image and receive a model prediction.

---

## Requirements

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

Or install the main dependencies manually:

```bash
pip install numpy pandas matplotlib scikit-learn tensorflow opencv-python pillow streamlit jupyter
```

## Repository Structure

```text
Deep-Learning-Projects/
│
├── HEART upgrade/
│   ├── ...
│   └── README.md
│
├── Cats-v-Dogs CNN/
│   ├── ...
│   └── README.md
│
├── Bone-Fracture-Detection/
│   ├── app.py
│   ├── bone-fracture.keras
│   ├── ...
│   └── README.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/asad673-creator/Deep-Learning-Projects.git
```

Navigate into the project:

```bash
cd Deep-Learning-Projects
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then open the desired project and run its Python script or Jupyter Notebook.

### Running Bone Fracture Detection

Navigate to the Bone Fracture Detection project:

```bash
cd Bone-Fracture-Detection
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser, where you can upload an X-ray image for prediction.

> **Disclaimer:** This project is for educational and experimental purposes only. The model's predictions should not be used as a medical diagnosis.

## Learning Goals

This repository documents my practical learning journey in Deep Learning, including:

* Perceptrons
* Artificial Neural Networks
* Convolutional Neural Networks
* Forward and backward propagation
* Activation functions
* Loss functions
* Optimizers
* Model training
* Computer vision
* Image preprocessing
* Image classification
* Medical image classification
* Model evaluation
* Model deployment
* Streamlit applications

More projects and experiments will be added as I continue learning Deep Learning.

## Author

**Asad Ajaz**

GitHub: https://github.com/asad673-creator
