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

## Domain

**Data Science & Machine Learning (Regression)**

---
