# 🚀 AI-Powered Predictive Maintenance System for IoT Devices

## 📌 Overview

Predictive Maintenance is a cutting-edge application of Artificial Intelligence (AI) in industrial systems. This project simulates a real-world **IoT-based predictive maintenance system** that analyzes sensor data and predicts machine failures before they occur.

Instead of reacting to failures, this system enables **proactive maintenance**, reducing downtime and saving operational costs.

---

## 🎯 Problem Statement

In industries like manufacturing, power plants, and automotive systems, unexpected machine failures lead to:

* Production downtime
* Increased maintenance costs
* Safety risks
* Reduced efficiency

This project solves the problem by using **Machine Learning to predict failures in advance** based on sensor data.

---

## 💡 Solution

This system uses **historical sensor data (temperature, vibration, pressure, etc.)** to train a Machine Learning model that predicts whether a machine is likely to fail.

---

## 🏭 Industry Relevance

This project mimics real-world applications used in:

* Manufacturing Plants
* Smart Factories (Industry 4.0)
* Power Generation Systems
* Automotive Diagnostics
* Aviation Maintenance Systems

---

## ⚙️ Tech Stack

* **Programming Language:** Python
* **Libraries:**

  * Pandas
  * NumPy
  * Scikit-learn
  * Matplotlib
  * Seaborn
  * Joblib

---

## 📊 Dataset

* Type: **Time-series / sensor data**
* Features include:

  * Temperature
  * Vibration
  * Pressure
  * Humidity
* Target:

  * `0` → Normal
  * `1` → Machine Failure

> 📌 Note: Dataset is simulated to represent real IoT sensor readings.

---

## 🧠 Machine Learning Model

* Model Used: **Random Forest Classifier**
* Task: **Binary Classification (Failure Prediction)**
* Output:

  * Predicts whether a machine will fail or not

---

## 🏗️ Project Architecture

```
Sensor Data (CSV)
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Machine Learning Model
        ↓
Prediction (Failure / No Failure)
        ↓
Alert System
        ↓
Visualization
```

---

## 📁 Project Structure

```
AI-Predictive-Maintenance-IoT/
│
├── data/                # Dataset files
├── notebooks/           # Jupyter notebooks (experiments)
├── src/                 # Source code modules
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── evaluate.py
│   └── visualize.py
│
├── models/              # Saved ML models
├── outputs/             # Predictions & graphs
├── images/              # Screenshots for README
├── docs/                # Architecture diagrams
│
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── README.md
└── .gitignore
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/kodurumanisha84/AI-Predictive-Maintenance-IoT.git
cd AI-Predictive-Maintenance-IoT
```

---

### 2️⃣ Create Virtual Environment

#### Windows

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

```
python main.py
```

---

## 📈 Expected Output

* Accuracy Score displayed in terminal
* Classification report (Precision, Recall, F1-score)
* Failure prediction graph saved in `outputs/`
* Trained model saved in `models/`

---

## 📊 Visualization

The system generates:

* 📉 Prediction vs Actual Graph
* 📊 Failure Trend Visualization

## 🔍 Key Features

* ✅ Machine Failure Prediction
* ✅ Data Preprocessing Pipeline
* ✅ Feature Engineering
* ✅ Model Training & Evaluation
* ✅ Visualization of Results
* ✅ Modular Code Structure
* ✅ Industry-Oriented Design

---

## 🧪 Virtual Simulation

Since real IoT hardware is not available, this project uses **simulated sensor data** to represent:

* Machine health conditions
* Operational stress levels
* Failure scenarios

This approach ensures:

* Practical understanding
* Real-world applicability
* Easy reproducibility

---

## 📊 Model Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

---

## 🚀 Future Improvements

* 🔹 Real-time IoT data integration
* 🔹 Dashboard using Streamlit / Flask
* 🔹 Deep Learning (LSTM for time-series)
* 🔹 Deployment on cloud (AWS / Azure)
* 🔹 Alert system (Email/SMS notifications)

---

## 📚 Learning Outcomes

Through this project, you will learn:

* Machine Learning workflow
* Data preprocessing techniques
* Feature engineering
* Model evaluation
* Industrial AI applications
* GitHub project structuring



## 🔥 Final Note

This project showcases how AI can transform traditional maintenance into **smart predictive systems**, making industries more efficient, safe, and cost-effective.

##Author##
Koduru Manisha
