# 🫁 Lung Cancer Detection Using Deep Learning

## 📌 Project Overview

Lung cancer is one of the leading causes of cancer-related deaths worldwide. Early detection significantly improves treatment outcomes and survival rates. This project presents a deep learning-based approach for automated lung cancer detection using medical imaging techniques.

The system leverages **Transfer Learning** with **ResNet-50** and **VGG-16** architectures to classify lung images into multiple categories and assist in early diagnosis. The models are trained on preprocessed lung image datasets and evaluated using various performance metrics including accuracy, loss, confusion matrix, precision, recall, and F1-score.

In addition to model development, the project includes a **web-based application** that enables users to securely log in, upload lung images, and receive real-time AI-powered predictions through an intuitive interface.

---

## 🎯 Objectives

* Develop an automated lung cancer detection system using Deep Learning.
* Compare the performance of ResNet-50 and VGG-16 architectures.
* Address class imbalance using SMOTE.
* Improve diagnostic accuracy through transfer learning.
* Assist healthcare professionals in early lung cancer detection.
* Deploy the trained model through a user-friendly web application.

---

## 🚀 Project Repository

https://github.com/s-raj02/Lung_Cancer_Detection

---

## 🧠 Technologies Used

### Deep Learning & Data Science

* Python
* TensorFlow
* Keras
* OpenCV
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Imbalanced-Learn (SMOTE)

### Web Development

* Flask
* HTML5
* CSS3
* JavaScript
* Bootstrap

### Development Environment

* Google Colab
* Jupyter Notebook

---

## 📊 Dataset

The dataset consists of lung cancer images categorized into the following classes:

* Normal Lung
* Adenocarcinoma
* Squamous Cell Carcinoma
* Stage 1 Cancer
* Stage 2 Cancer
* Advanced Stage Cancer

Images are preprocessed before training to ensure consistency and improve model performance.

### Data Preprocessing

* Image Resizing (150 × 150)
* Grayscale Conversion
* Normalization
* Dataset Shuffling
* Train-Test-Validation Split (70:15:15)
* SMOTE for Class Balancing

### Dataset Split

* Training Set – 70%
* Validation Set – 15%
* Testing Set – 15%

The preprocessing pipeline improves model robustness and reduces bias caused by class imbalance.

---

## 🏗️ Model Architecture

### ResNet-50

ResNet-50 is used as a feature extractor through transfer learning.

#### Key Components

* Pre-trained ResNet-50 Backbone
* Frozen Base Layers
* Flatten Layer
* Dense Layer (128 Units, ReLU)
* Softmax Output Layer
* Adam Optimizer
* Sparse Categorical Crossentropy Loss

The model achieved superior performance in classification tasks.

---

### VGG-16

VGG-16 is a deep convolutional neural network consisting of:

* 13 Convolution Layers
* 3 Fully Connected Layers
* Transfer Learning Approach
* Feature Extraction from Medical Images

VGG-16 demonstrated strong performance with an accuracy of 88%.

---

## ⚙️ Training Strategy

### Data Augmentation

ImageDataGenerator is used to generate augmented image batches and improve model generalization.

### Early Stopping

Training automatically stops when validation loss does not improve for three consecutive epochs, preventing overfitting.

### Training Configuration

* Maximum Epochs: 80
* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy
* Accuracy Tracking
* Validation Monitoring

---

## 📈 Results

### Model Comparison

| Metric        | ResNet-50 | VGG-16   |
| ------------- | --------- | -------- |
| Accuracy      | 92%       | 88%      |
| Epochs        | 80        | 80       |
| Minimum Loss  | 0.0450    | 0.214    |
| Training Time | 6215 sec  | 9220 sec |

ResNet-50 outperformed VGG-16 in terms of accuracy, loss reduction, and overall classification performance.

---

## 🔍 Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

Performance metrics indicate strong generalization on unseen data and reliable disease classification.

---

## 🩺 Sample Predictions

The trained model successfully classified various lung conditions including:

* Normal Lung
* Adenocarcinoma
* Squamous Cell Carcinoma
* Stage 1 Cancer
* Stage 2 Cancer
* Advanced Stage Cancer

The prediction results demonstrate the practical applicability of deep learning in medical diagnosis.

---

## 🌐 Web Application Interface

The project includes a fully functional web application that allows users to interact with the trained model through a simple and secure interface.

### 🔐 User Authentication

The application provides secure user authentication features:

* User Registration
* User Login
* Logout Functionality
* Session Management
* Secure Access Control

### 📤 Lung Image Upload

Users can upload lung images directly through the application.

Features include:

* Image Upload from Local Device
* Image Validation
* Automatic Image Preprocessing
* Real-Time Prediction

### 🤖 AI Prediction System

After uploading an image:

1. The image is preprocessed automatically.
2. The trained ResNet-50 model performs classification.
3. The system predicts the lung condition.
4. Results are displayed instantly.

### 📊 Result Dashboard

The dashboard displays:

* Uploaded Image Preview
* Predicted Disease Category
* Model Output
* Confidence Score (if implemented)
* User-Friendly Results Interface

### 💻 User Workflow

```text
User Login/Register
          │
          ▼
Upload Lung Image
          │
          ▼
Image Preprocessing
          │
          ▼
ResNet-50 Model Prediction
          │
          ▼
Disease Classification
          │
          ▼
Result Dashboard
```

### ✅ Benefits of the Web Application

* Easy-to-use interface.
* Real-time disease prediction.
* Accessible from any web browser.
* Bridges AI research with practical healthcare applications.
* Demonstrates end-to-end deployment of deep learning models.

---

## 📂 Project Structure

```text
Lung_Cancer_Detection/

│
├── Lung_Cancer_Detection.ipynb
├── Detection_of_Lung_Cancer.pdf
├── README.md
├── requirements.txt
├── app.py
│
├── Dataset/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── upload.html
│   ├── dashboard.html
│   └── result.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── uploads/
│
├── Data_Preprocessing
├── Data_Augmentation
├── SMOTE_Balancing
├── ResNet50_Model
├── VGG16_Model
├── Model_Training
├── Model_Evaluation
└── Prediction_System
```

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/s-raj02/Lung_Cancer_Detection.git
```

### Navigate to Project Directory

```bash
cd Lung_Cancer_Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```text
http://localhost:5000
```

---

## 📦 Required Libraries

```text
tensorflow
keras
numpy
pandas
matplotlib
opencv-python
scikit-learn
imbalanced-learn
flask
```

---

## 🔥 Key Features

* Deep Learning-Based Medical Image Classification
* Transfer Learning with ResNet-50 and VGG-16
* Automated Lung Cancer Detection
* SMOTE-Based Class Balancing
* Early Stopping and Data Augmentation
* Multi-Class Disease Classification
* Performance Visualization
* Medical Imaging Analysis
* Secure User Authentication
* Web-Based Image Upload
* Real-Time AI Prediction
* Interactive Result Dashboard
* End-to-End Healthcare Application

---

## 📚 Future Improvements

* Hyperparameter Optimization
* Ensemble Learning Techniques
* Real-Time Clinical Validation
* Larger Medical Datasets
* Cloud Deployment
* Mobile Application Development
* Explainable AI (XAI) Integration
* Healthcare Professional Dashboard

These enhancements can further improve accuracy and practical applicability in healthcare environments.

---

## ⚠️ Disclaimer

This project is developed for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis or treatment.

---

## 👨‍💻 Author

**Sudhanshu Raj**

GitHub: https://github.com/s-raj02

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
