import streamlit as st
import pandas as pd

# Sample data for maize varieties
data = {
    'Variety': ['H6213', 'H614D', 'H629', 'H6218', 'H513', 'H517', 'H516', 'H624', 'H520', 'DH04', 'PH04'],
    'Ecozone': ['Highlands', 'Highlands', 'Highlands', 'Highlands', 'Medium Altitude', 'Medium Altitude', 'Medium Altitude', 'Transitional Altitude', 'Transitional Altitude', 'Lowland', 'Lowland'],
    'Price (Ksh)': [420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420],
    'Availability': ['Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists']
}

df = pd.DataFrame(data)

# Sidebar filters
variety = st.sidebar.selectbox('Variety', df['Variety'].unique())
ecozone = st.sidebar.selectbox('Ecozone', df['Ecozone'].unique())
availability = st.sidebar.selectbox('Availability', ['Branches, Agents, Stockists'])
price_range = st.sidebar.slider('Price Range (Ksh)', min(df['Price (Ksh)']), max(df['Price (Ksh)']), (0, max(df['Price (Ksh)']) + 100))

# Filtering data based on user selection
filtered_data = df[(df['Variety'] == variety) & (df['Ecozone'] == ecozone) & (df['Availability'].str.contains(availability)) & (df['Price (Ksh)'] >= price_range[0]) & (df['Price (Ksh)'] <= price_range[1])]

# Display filtered data
st.write(filtered_data)

# Allow users to register a new company
new_company = st.text_input('Register New Company')
if st.button('Register Company'):
    st.write(f'Company "{new_company}" registered successfully!')

# Allow users to register a new variety
new_variety = st.text_input('Register New Variety')
new_ecozone = st.selectbox('Ecozone', df['Ecozone'].unique())
new_price = st.number_input('Price (Ksh)')
if st.button('Register Variety'):
    st.write(f'Variety "{new_variety}" registered successfully!')

# Display information about Kenya Seed Company Ltd
st.write('Kenya Seed Company Ltd')
st.write('Price per 2 kg: Ksh 420')
st.write('Available at branches, agents, and stockists countrywide.')
