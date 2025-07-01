# 🎙️ Speech Emotion Recognition using KNN 🔬  
**Full-Stack Speech Emotion Detection using KNN**  

![License](https://img.shields.io/badge/license-MIT-green.svg)  
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)  
![React](https://img.shields.io/badge/frontend-React-blue.svg)  
![Status](https://img.shields.io/badge/status-Completed-brightgreen.svg)  

---

## 🧠 Project Overview  

This project implements Speech Emotion Recognition (SER) by classifying human speech into emotional categories such as **Happy**, **Sad**, **Angry**, and **Neutral** using the **K-Nearest Neighbors (KNN)** algorithm.  

The system extracts relevant features from audio signals using **Mel Frequency Cepstral Coefficients (MFCCs)** and applies supervised machine learning for emotion classification. A **React-based frontend** provides an interactive user interface, while a **Python backend** handles model predictions.  

---

## ⚙️ Technologies Used  

### Backend  
- Python  
- Librosa (Audio Processing)  
- NumPy  
- Scikit-learn (Machine Learning)  
- Flask (Backend Framework)  

### Frontend  
- React  
- HTML & CSS  
- JavaScript  

---

## 📊 Dataset  

The speech emotion recognition model is trained and evaluated using a publicly available dataset from the **University of Toronto's Scholaris platform**, containing labeled speech samples representing different emotional states.  

**Dataset Link:** [Speech Emotion Dataset - Scholaris (University of Toronto)](https://utoronto.scholaris.ca/collections/036db644-9790-4ed0-90cc-be1dfb8a4b66)  

The dataset contains audio recordings labeled with emotions such as:  

- Happy  
- Sad  
- Angry  
- Neutral  

---

## 📦 Key Components  

- Audio pre-processing and feature extraction  
- Emotion classification with **K-Nearest Neighbors (KNN)**  
- REST API for handling predictions  
- React frontend for uploading audio files and displaying results  
- Model evaluation with Confusion Matrix and Accuracy Score  

---

## 📁 Project Structure  

```

├── backend/
│   ├── data/
│   ├── venv/
│   ├── emotion\_classification\_model.pkl
│   ├── main.py
│   ├── test.py
│   └── train.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── App.test.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── logo.svg
│   │   ├── reportWebVitals.js
│   │   └── setupTests.js
│   ├── .gitignore
│   ├── README.md
│   ├── package.json
│   └── package-lock.json
│
├── uploads/
└── README.md

```

---

## 🖼️ Screenshots  

| Upload Audio                                                                              | Emotion Prediction |  
|-------------------------------------------------------------------------------------------|-------------------|  
| ![Output](https://github.com/user-attachments/assets/b36d6602-1a0f-4920-8fa4-de2442934781)| ![Output Results](https://github.com/user-attachments/assets/b977edbf-6a3a-42d2-a0db-8107558897d0)
 |  

---

## 🔍 Features  

✅ Speech emotion detection from audio input  
✅ Interactive web interface to upload audio files  
✅ Real-time emotion classification  
✅ Model built using supervised learning (KNN)  
✅ Clear project structure separating frontend and backend  

---

## 🚀 Future Enhancements  

- Support for additional emotion categories  
- Real-time microphone input support  
- Improved model performance with advanced classifiers  
- Enhanced UI for better user experience  

---

## 🛠️ Setup & Installation  

### Backend  
1. Navigate to `backend/`  
2. Create virtual environment and activate:  
```

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

```
3. Install dependencies:  
```

pip install -r requirements.txt

```
4. Run the backend:  
```

python main.py

```

### Frontend  
1. Navigate to `frontend/`  
2. Install dependencies:  
```

npm install

```
3. Run the frontend:  
```

npm start

```

---

## 📬 Contact

**Sai Sruthi Karnatakapu**  
📧 [k.saisruthi913@gmail.com](mailto:k.saisruthi913@gmail.com)  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/saisruthi-karnatakapu/)

