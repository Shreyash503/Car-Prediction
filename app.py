import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Car Price Predictor", layout="centered")
st.title('🚗 Car Price Prediction App')

# Brand options and encoding
brand_list = [
    'Honda', 'Toyota', 'Volkswagen', 'Maruti Suzuki', 'BMW', 'Ford',
    'Kia', 'Mercedes-Benz', 'Hyundai', 'Audi', 'Renault', 'MG',
    'Volvo', 'Skoda', 'Tata', 'Mahindra', 'Mini', 'Land Rover', 'Jeep',
    'Chevrolet', 'Jaguar', 'Fiat', 'Aston Martin', 'Porsche', 'Nissan',
    'Force', 'Mitsubishi', 'Lexus', 'Isuzu', 'Datsun', 'Ambassador',
    'Rolls-Royce', 'ICML', 'Bajaj', 'Opel', 'Ashok', 'Bentley',
    'Ssangyong', 'Maserati'
]
brand_mapping = {brand: idx for idx, brand in enumerate(brand_list)}
brand = st.selectbox('Select Brand', brand_list)
brand_encoded = brand_mapping[brand]

# Other input fields
Year = st.selectbox('Select Year', list(range(1990, 2025)))
kmDriven = st.number_input('Enter Distance Driven (in Km)', min_value=0)
Transmission = st.radio('Select Transmission Type', ['Manual', 'Automatic'], index=0)
trans_encoded = 0 if Transmission == 'Manual' else 1

Owner = st.selectbox('Ownership Status', ['First', 'Second'], index=0)
owner_encoded = 0 if Owner == 'First' else 1

FuelType = st.selectbox('Select Fuel Type', ['Petrol', 'Diesel'], index=0)
fuel_encoded = 0 if FuelType == 'Petrol' else 1

# Predict button
if st.button('Predict'):
    # Input validation
    if kmDriven == 0:
        st.warning("⚠️ Please enter a non-zero value for distance driven.")
    elif Year < 1990 or Year > 2024:
        st.warning("⚠️ Please select a valid year.")
    else:
        try:
            model = pickle.load(open('car_model.pkl', 'rb'))
            input_data = [[brand_encoded, Year, kmDriven, trans_encoded, owner_encoded, fuel_encoded]]
            prediction = model.predict(input_data)
            price = int(prediction[0])

            # Check for negative predicted price
            if price < 0:
                st.error("⚠️ Predicted price is negative. Please increase the car's year or check inputs.")
            else:
                st.success(f'🚘 The predicted price of the car is: ₹{price:,}')
        except FileNotFoundError:
            st.error("Model file not found. Please ensure 'car_model.pkl' exists in the project folder.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
