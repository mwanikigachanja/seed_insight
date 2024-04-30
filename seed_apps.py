import streamlit as st
import pandas as pd

# Sample data for maize varieties
data = {
    'Variety': ['H6213', 'H614D', 'H629', 'H6218', 'H513', 'H517', 'H516', 'H624', 'H520', 'DH04', 'PH04'],
    'Ecozone': ['Highlands', 'Highlands', 'Highlands', 'Highlands', 'Medium Altitude', 'Medium Altitude', 'Medium Altitude', 'Transitional Altitude', 'Transitional Altitude', 'Lowland', 'Lowland'],
    'Price (Ksh)': [420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420],
    'Availability': ['Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists']
}

# Sample data for companies and eco-zones
company_data = {
    'Company Name': ['Company A', 'Company B', 'Company C'],
    'Contact Info': ['Contact A', 'Contact B', 'Contact C'],
    'Specialty': ['Seeds', 'Fertilizers', 'Pesticides']
}

ecozone_data = {
    'Ecozone': ['Highlands', 'Medium Altitude', 'Transitional Altitude', 'Lowland'],
    'Altitude': [2000, 1500, 1000, 500],
    'Rainfall': [1000, 800, 600, 400],
    'Classification': ['Temperate', 'Subtropical', 'Arid', 'Semi-arid']
}

# Convert data to DataFrames
df = pd.DataFrame(data)
company_df = pd.DataFrame(company_data)
ecozone_df = pd.DataFrame(ecozone_data)

# Define custom styles
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f0f0;
    }
    .sidebar .sidebar-content .block-container {
        padding: 1rem;
    }
    .st-bw {
        color: #ffffff;
        background-color: #4CAF50;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-size: 1.2rem;
    }
    .st-bw:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar filters
st.sidebar.title("Filters")
variety = st.sidebar.selectbox('Variety', df['Variety'].unique())
ecozone = st.sidebar.selectbox('Ecozone', df['Ecozone'].unique())
availability = st.sidebar.selectbox('Availability', ['Branches, Agents, Stockists'])
price_range = st.sidebar.slider('Price Range (Ksh)', min(df['Price (Ksh)']), max(df['Price (Ksh)']), (min(df['Price (Ksh)']), max(df['Price (Ksh)'])))

# Filtering data based on user selection
filtered_data = df[(df['Variety'] == variety) & (df['Ecozone'] == ecozone) & (df['Availability'].str.contains(availability)) & (df['Price (Ksh)'] >= price_range[0]) & (df['Price (Ksh)'] <= price_range[1])]

# Display filtered data
st.title("Filtered Data")
st.dataframe(filtered_data)

# CRUD operations for companies
st.title("Companies")

# Display existing companies
st.write("Existing Companies:")
st.dataframe(company_df)

# Add new company
st.write("Add New Company:")
new_company_name = st.text_input("Company Name")
new_company_contact = st.text_input("Contact Info")
new_company_specialty = st.selectbox("Specialty", ["Seeds", "Fertilizers", "Pesticides"])
if st.button("Add Company"):
    company_df = company_df.append({'Company Name': new_company_name, 'Contact Info': new_company_contact, 'Specialty': new_company_specialty}, ignore_index=True)
    st.success("Company added successfully!")

# CRUD operations for eco-zones
st.title("Eco-zones")

# Display existing eco-zones
st.write("Existing Eco-zones:")
st.dataframe(ecozone_df)

# Add new eco-zone
st.write("Add New Eco-zone:")
new_ecozone_name = st.text_input("Eco-zone Name")
new_ecozone_altitude = st.number_input("Altitude")
new_ecozone_rainfall = st.number_input("Rainfall")
new_ecozone_classification = st.selectbox("Classification", ["Temperate", "Subtropical", "Arid", "Semi-arid"])
if st.button("Add Eco-zone"):
    ecozone_df = ecozone_df.append({'Ecozone': new_ecozone_name, 'Altitude': new_ecozone_altitude, 'Rainfall': new_ecozone_rainfall, 'Classification': new_ecozone_classification}, ignore_index=True)
    st.success("Eco-zone added successfully!")
