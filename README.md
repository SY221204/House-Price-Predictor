# House Price Predictor

A Data Science & Machine Learning project to predict **house prices** based on **Area, Bedrooms, and Location**.
This project uses **Linear Regression** from Scikit-Learn and provides predictions in **Crores** for user-friendly understanding.

---

## Problem Statement

Estimating house prices manually is often **inconsistent and inaccurate**.
This project builds a **predictive regression model** to automate the process and deliver more reliable results.

---

## Objectives

* Build a regression model using **Scikit-Learn**.
* Predict prices using:

  * Area (sq. ft)
  * Bedrooms
  * Location (4 cities).
* Evaluate performance using **MSE & R² Score**.
* Predict price for **new house details** entered by the user.

---

## Dataset

Custom dataset created with the following columns:

* `Area` (sq. ft)
* `Bedrooms` (number of rooms)
* `Location` (Delhi, Mumbai, Bangalore, Kolkata)
* `Price` (in ₹)

---

## Methodology (Workflow)

1. Load dataset using Pandas
2. Preprocess data (OneHotEncoder for Location)
3. Train-test split (80-20)
4. Train a **Linear Regression** model
5. Evaluate performance with **Mean Squared Error (MSE)** and **R² Score**
6. Take user input and predict price in **Crores**

---

## Model Evaluation

* **Mean Squared Error (MSE):** *your value here*
* **R² Score:** *your value here*

👉 Lower MSE = better accuracy
👉 Higher R² = better fit of model

---

## Example Prediction

**Input:**

* Area: 1500 sq.ft
* Bedrooms: 3
* Location: Mumbai

**Output:**
Predicted House Price = ₹ 2.45 Crore

---

## How to Run the Project

Option 1 – Run as Python Script
      1. Clone this repository:
    
          git clone https://github.com/your-username/House-Price-Predictor.git
          cd House-Price-Predictor

   2. Install dependencies:

          pip install pandas scikit-learn

   3. Run the project:
      
          python house_price_predictor.py

You will be asked to enter: Area, Bedrooms, Location
The model will predict the house price in Crores.


 Option 2 – Run with Streamlit (Interactive Web App)

  1. Install Streamlit:

           pip install streamlit pandas scikit-learn


   2. Run the app:

           streamlit run house_price_streamlit.py

 **Option 3 - Running in VS Code**

 *1. Open VS Code

 *2. Go to File → Open Folder → select the project folder (House-Price-Predictor).

 *3. Make sure you have Python installed and selected in VS Code (bottom right status bar).

 *4. Open the terminal in VS Code (Ctrl+`) and run:

   *5. Run Python Script
   
        python house_price_predictor.py

   *6. Run Streamlit App

        streamlit run house_price_streamlit.py


*6. For the script → enter details in terminal and get house price.

*7. For Streamlit → browser window opens with interactive interface.         

---

## Domain

**Data Science & Machine Learning (Regression)**

---

     
