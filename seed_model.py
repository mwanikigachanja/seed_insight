import streamlit as st
import pandas as pd

# Sample data for maize varieties
data = {
    'Variety': ['H6213', 'H614D', 'H629', 'H6218', 'H513', 'H517', 'H516', 'H624', 'H520', 'DH04', 'PH04'],
    'Ecozone': ['Highlands', 'Highlands', 'Highlands', 'Highlands', 'Medium Altitude', 'Medium Altitude', 'Medium Altitude', 'Transitional Altitude', 'Transitional Altitude', 'Lowland', 'Lowland'],
    'Price (Ksh)': [420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420],
    'Availability': ['Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists']
}

df_varieties = pd.DataFrame(data)

# Sample data for companies
data_companies = {
    'Company': ['Company A', 'Company B', 'Company C'],
    'Location': ['Location A', 'Location B', 'Location C'],
    'Contact': ['Contact A', 'Contact B', 'Contact C']
}

df_companies = pd.DataFrame(data_companies)

# Sidebar filters for varieties
variety_id = st.sidebar.selectbox('Variety', range(len(df_varieties['Variety'])), format_func=lambda i: df_varieties['Variety'][i])
ecozone_id = st.sidebar.selectbox('Ecozone', range(len(df_varieties['Ecozone'])), format_func=lambda i: df_varieties['Ecozone'][i])
availability = st.sidebar.selectbox('Availability', ['Branches, Agents, Stockists'])
price_range = st.sidebar.slider('Price Range (Ksh)', min(df_varieties['Price (Ksh)']), max(df_varieties['Price (Ksh)']), (0, max(df_varieties['Price (Ksh)']) + 100))

# Filtering data based on user selection for varieties
filtered_varieties = df_varieties[(df_varieties['Variety'] == df_varieties['Variety'][variety_id]) & 
                   (df_varieties['Ecozone'] == df_varieties['Ecozone'][ecozone_id]) & 
                   (df_varieties['Availability'].str.contains(availability)) & 
                   (df_varieties['Price (Ksh)'] >= price_range[0]) & 
                   (df_varieties['Price (Ksh)'] <= price_range[1])]

# Display filtered varieties
st.write('Filtered Varieties')
st.write(filtered_varieties)

# Allow users to register a new variety
new_variety = st.text_input('Register New Variety')
new_ecozone = st.text_input('Ecozone')
new_price = st.number_input('Price (Ksh)')
company_options = df_companies['Company'].tolist()
selected_company = st.selectbox('Select Company', company_options)
if st.button('Register Variety'):
    st.write(f'Variety "{new_variety}" registered successfully to "{selected_company}"!')

# Display information about companies
st.write('Companies')
st.write(df_companies)
