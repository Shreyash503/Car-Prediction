import streamlit as st
import pickle
import pandas as pd

st.title('Car Price Prediction  App')
# X=df[['brand_enc', 'Year', 'kmDriven_enc', 'Transmission_enc', 'Owner_enc', 'FuelType_enc']]
# Input fields
brand_list =( ['Honda', 'Toyota', 'Volkswagen', 'Maruti Suzuki', 'BMW', 'Ford',
              'Kia', 'Mercedes-Benz', 'Hyundai', 'Audi', 'Renault', 'MG',
              'Volvo', 'Skoda', 'Tata', 'Mahindra', 'Mini', 'Land Rover', 'Jeep',
              'Chevrolet', 'Jaguar', 'Fiat', 'Aston Martin', 'Porsche', 'Nissan',
              'Force', 'Mitsubishi', 'Lexus', 'Isuzu', 'Datsun', 'Ambassador',
              'Rolls-Royce', 'ICML', 'Bajaj', 'Opel', 'Ashok', 'Bentley',
              'Ssangyong', 'Maserati' ])

# Create a mapping starting from 0
brand_mapping = {brand: idx for idx, brand in enumerate(brand_list)}

# Streamlit selectbox
brand = st.selectbox('Select Brand', brand_list)

# Get the encoded value
brand_encoded = brand_mapping[brand]

Year= st.selectbox('Select Year',[1990,1991,1992,1993, 1994,1995, 1996,1997,
1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,
2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024])
kmDriven = st.number_input('Enter Km')
Transmission = st.radio('Select Transmission', ['Manual', 'Automatic'])
Transmission=0 if Transmission == 'Manual' else 1

Owner = st.selectbox('Select Owner', ['First', 'Second'])
Owner=0 if Owner == 'First' else 1
FuelType = st.selectbox('Select Fuel Type', ['Petrol', 'Diesel'])
FuelType=0 if FuelType == 'Petrol' else 1
# X_test=[[brand , Year, kmDriven, Transmission, Owner, FuelType]]
# Predict button
if st.button('Predict'): 
    # Load the model
    model = pickle.load(open('car_model.pkl', 'rb'))
    # Make predictions
    yp = model.predict([[brand_encoded , Year, kmDriven, Transmission, Owner, FuelType]])
    
    # Show price with commas in ₹
    st.success(f'The predicted price of the car is: ₹{int(yp[0]):,}')




    



  