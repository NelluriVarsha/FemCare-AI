# FemCare AI

## AI-Powered Women's Health & Wellness Platform

FemCare AI is an intelligent women's healthcare and wellness application designed to provide personalized health insights through **PCOS prediction, health assessment, menstrual tracking, health-score calculation, personalized recommendations, and report generation**.

The application combines machine learning, Python-based data processing, and an interactive multi-page interface to provide users with a centralized platform for monitoring and understanding important aspects of women's health.

> **Disclaimer:** FemCare AI is an academic/research project intended for educational and informational purposes. Its predictions and recommendations should not be considered a medical diagnosis or a substitute for consultation with a qualified healthcare professional.

---

## 📌 Project Overview

Women's health involves multiple interconnected factors such as menstrual health, lifestyle, symptoms, and conditions such as Polycystic Ovary Syndrome (PCOS).

FemCare AI aims to provide a convenient digital platform where users can:

- Create and manage a profile
- Register and securely log in
- Perform a health assessment
- Obtain a PCOS risk prediction using a trained machine learning model
- Calculate a personalized health score
- Track menstrual cycles
- View health information through a dashboard
- Receive personalized health recommendations
- Generate health reports

The project demonstrates how **machine learning and Python-based application development** can be combined to build an interactive healthcare-support application.

---

## ✨ Key Features

### 🔐 User Registration & Login
- User registration interface
- Login functionality
- User profile management
- Local database-based user management

### 🩺 Health Assessment
Users can provide relevant health information through the health assessment module.

The application processes the provided information and generates health-related insights.

### 🧠 PCOS Prediction

FemCare AI includes a trained machine learning model for PCOS prediction.

The project contains:

```text
pcos_model.pkl
PCOS_data.csv
pcos_predictor.py
```

The trained model is used by the prediction module to process assessment-related inputs and generate a prediction.

### 📊 Health Score

The application calculates a health score using the implemented health-score module.

```text
health_score.py
```

The score can be presented through the application's dashboard to provide users with an easy-to-understand overview of their assessed health information.

### 🌸 Menstrual Tracker

The application provides a dedicated menstrual tracking page where users can record and monitor menstrual-cycle information.

### 📈 Dashboard

The dashboard provides a centralized view of relevant user health information and application results.

### 💡 Personalized Recommendations

The recommendation module generates health-related recommendations based on the information processed by the application.

```text
recommendation.py
```

### 📄 Health Report

FemCare AI includes report-generation functionality and a sample report:

```text
FemCare_Report.pdf
```

The report module allows health-related information and results to be presented in a structured format.

---

## 🏗️ Project Architecture

The overall application workflow can be represented as:

```text
                 ┌──────────────────────┐
                 │      User Access     │
                 └──────────┬───────────┘
                            │
                ┌───────────▼───────────┐
                │ Registration / Login  │
                └───────────┬───────────┘
                            │
                   ┌────────▼────────┐
                   │  User Profile   │
                   └────────┬────────┘
                            │
              ┌─────────────▼─────────────┐
              │      Health Assessment    │
              └─────────────┬─────────────┘
                            │
                ┌───────────▼───────────┐
                │    ML-based PCOS      │
                │       Prediction       │
                └───────────┬───────────┘
                            │
             ┌──────────────▼──────────────┐
             │       Health Score          │
             │     & Recommendations       │
             └──────────────┬──────────────┘
                            │
              ┌─────────────▼─────────────┐
              │          Dashboard        │
              └─────────────┬─────────────┘
                            │
                 ┌──────────▼──────────┐
                 │ Menstrual Tracking  │
                 │ & Health Reports    │
                 └─────────────────────┘
```

---

## 📁 Project Structure

```text
FemCare-AI/
│
├── app.py
├── database.py
├── model.py
├── health_score.py
├── hero.py
├── pcos_predictor.py
├── recommendation.py
├── theme.py
│
├── PCOS_data.csv
├── pcos_model.pkl
├── FemCare_Report.pdf
│
├── style.css
├── check_db.py
├── clear_users.py
│
├── pages/
│   ├── 1_register.py
│   ├── 2_login.py
│   ├── 3_profile.py
│   ├── 4_Health_Assessment.py
│   ├── 5_dashboard.py
│   ├── 6_report.py
│   └── 7_Menstrual_Tracker.py
│
├── .gitignore
└── README.md
```


```

The prediction workflow can be summarized as:

```text
User Health Information
          │
          ▼
   Data Preparation
          │
          ▼
 Feature Processing
          │
          ▼
 Trained ML Model
          │
          ▼
   PCOS Prediction
          │
          ▼
 Health Insights &
 Recommendations
```

The prediction functionality is implemented through:

```text
pcos_predictor.py
```

The dataset used by the project is included as:

```text
PCOS_data.csv
```


---

## ▶️ Running the Application

After activating the virtual environment, run:

```powershell
streamlit run app.py
```

The application will start locally and Streamlit will provide a local URL, typically similar to:

```text
http://localhost:8501
```

Open the displayed URL in your browser.

---

## 🔄 Application Workflow

### Step 1 — Registration

The user creates an account using the registration page.

### Step 2 — Login

The registered user logs into the application.

### Step 3 — Profile

The user provides or views profile information.

### Step 4 — Health Assessment

The user provides health-related information through the assessment interface.

### Step 5 — PCOS Prediction

The trained machine learning model processes the relevant assessment information.

### Step 6 — Health Score

The application calculates the implemented health score.

### Step 7 — Recommendations

Based on the available assessment information and application logic, recommendations are generated.

### Step 8 — Dashboard

The user can view relevant results and health information through the dashboard.

### Step 9 — Menstrual Tracking

The user can record and monitor menstrual-cycle information.

### Step 10 — Report

The application provides health-report functionality for presenting the available results.

---

## 🎯 Project Objectives

The primary objectives of FemCare AI are:

1. Develop an interactive women's health application.
2. Implement machine learning-based PCOS prediction.
3. Provide a health assessment interface.
4. Calculate and display a health score.
5. Provide menstrual tracking functionality.
6. Generate personalized health recommendations.
7. Present health information through an interactive dashboard.
8. Generate structured health reports.
9. Demonstrate the practical application of machine learning in healthcare-support systems.

---

## 🌱 Future Enhancements

The project can be extended with several advanced features:

### 🤖 Advanced AI Models
- Experiment with ensemble learning and deep learning approaches.
- Compare multiple machine learning algorithms.
- Improve model evaluation using appropriate validation techniques.

### 🧬 Multimodal Health Analysis
Future versions could combine multiple information sources such as:

- Symptoms
- Lifestyle information
- Menstrual history
- Clinical measurements
- Laboratory results

### 📱 Mobile Application
Develop a dedicated Android/iOS application to make the platform more accessible.

### ☁️ Cloud Deployment
Deploy the application using cloud platforms for remote access and scalable infrastructure.

### 📊 Advanced Analytics
Add:

- Health trends
- Menstrual-cycle analytics
- Historical prediction tracking
- Interactive charts
- Personalized progress monitoring

### 🔔 Notifications
Implement reminders for:

- Menstrual-cycle tracking
- Health assessments
- Appointments
- Medication or wellness routines

### 🔐 Enhanced Security
Future versions could include:

- Password hashing
- Secure authentication
- Role-based access
- Improved database security
- Secure handling of sensitive health information

### 🩺 Clinical Integration
A future research version could explore integration with healthcare professionals and clinical systems, subject to appropriate validation, privacy, and regulatory requirements.

---

## 🔒 Privacy & Security

FemCare AI may process sensitive health-related information.

For a production deployment, additional security measures should be implemented, including:

- Secure authentication
- Password hashing
- Encryption
- Access control
- Secure database management
- Protection of personal and health information

Users should avoid uploading real sensitive medical information to an unsecured development deployment.

---

## ⚠️ Medical Disclaimer

FemCare AI is developed as an **academic and research project**.

The predictions, health scores, recommendations, and reports generated by the application are intended for **educational and informational purposes only**.

They should not be used as a substitute for:

- Professional medical advice
- Clinical diagnosis
- Medical treatment
- Laboratory testing
- Consultation with a qualified healthcare professional

Any healthcare-related decision should be made in consultation with an appropriate medical professional.

---

## 🚀 Future Vision

FemCare AI can serve as a foundation for developing a more comprehensive AI-assisted women's health platform.

Future development could focus on combining:

```text
Machine Learning
       +
Health Assessment
       +
Menstrual Tracking
       +
Personalized Recommendations
       +
Health Analytics
       +
Clinical Support
```

to create a more comprehensive and responsible digital health-support system.

---


