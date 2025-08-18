import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
import streamlit as st

 

# 1. Load dataset
df = pd.read_csv("house_price_prediction.csv")

# 3. Encode 'Location'
encoder = OneHotEncoder(sparse_output=False)
location_encoded = encoder.fit_transform(df[["Location"]])
location_df = pd.DataFrame(location_encoded, columns=encoder.get_feature_names_out(["Location"]))

# Merge encoded columns with main data
df_encoded = pd.concat([df.drop("Location", axis=1), location_df], axis=1)

# 4. Features & Target
X = df_encoded.drop("Price", axis=1)
y = df_encoded["Price"]

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Predictions & performance
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# -------------------------------
# STREAMLIT APP
# -------------------------------
st.set_page_config(page_title="House Price Predictor", layout="wide")
st.title("House Price Predictor")
st.write("Predict house prices based on **Area, Bedrooms, and Location**")

st.subheader("Model Evaluation")
st.write(f"**Mean Squared Error:** {mse:.2f}")
st.write(f"**R² Score:** {r2:.2f}")

st.subheader("Make a Prediction")
area = st.number_input("Enter house area (in sq ft)", min_value=500, max_value=50000, step=50)
bedrooms = st.selectbox("Select number of bedrooms", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
location = st.selectbox("Select location", ["Delhi", "Mumbai", "Bangalore", "Kolkata"])

if st.button("Predict Price"):
    location_input = encoder.transform(pd.DataFrame({"Location": [location]}))
    new_data = pd.DataFrame(
        [[area, bedrooms] + list(location_input[0])],
        columns=["Area", "Bedrooms"] + list(encoder.get_feature_names_out(["Location"]))
    )
    predicted_price = model.predict(new_data)[0]
    predicted_price_crore = predicted_price / 10000000
    st.success(f"Predicted House Price: ₹ {predicted_price_crore:.2f} Crore")
