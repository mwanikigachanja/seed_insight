import streamlit as st
import pandas as pd

# Sample data for maize varieties and companies
data_varieties = {
    'Variety': ['H6213', 'H614D', 'H629', 'H6218', 'H513', 'H517', 'H516', 'H624', 'H520', 'DH04', 'PH04'],
    'Ecozone': ['Highlands', 'Highlands', 'Highlands', 'Highlands', 'Medium Altitude', 'Medium Altitude', 'Medium Altitude', 'Transitional Altitude', 'Transitional Altitude', 'Lowland', 'Lowland'],
    'Price (Ksh)': [420, 420, 420, 420, 420, 420, 420, 420, 420, 420, 420],
    'Availability': ['Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists', 'Branches, Agents, Stockists'],
    'Company': ['Kenya Seed Company Ltd', 'Kenya Seed Company Ltd', 'Kenya Seed Company Ltd', 'Kenya Seed Company Ltd', 'Kenya Seed Company Ltd', 'Kenya Seed Company Ltd', 'Kenya Seed Company Ltd', 'Kenya Seed Company Ltd', 'Kenya Seed Company Ltd', 'Kenya Seed Company Ltd', 'Kenya Seed Company Ltd']
}

data_companies = {
    'Company Name': ['Kenya Seed Company Ltd'],
    'Contact Information': ['Website: www.kenyaseed.co.ke, Phone: +254 123 456 789']
}

df_varieties = pd.DataFrame(data_varieties)
df_companies = pd.DataFrame(data_companies)

# Display companies
st.write('Companies')
st.write(df_companies)

# Display varieties
st.write('Varieties')
st.write(df_varieties)

# Allow users to register a new company
new_company_name = st.text_input('Register New Company Name')
new_company_contact = st.text_input('Register New Company Contact Information')
if st.button('Register Company'):
    if df_companies.empty:
        df_companies = pd.DataFrame([{'Company Name': new_company_name, 'Contact Information': new_company_contact}])
    else:
        df_companies = df_companies.append({'Company Name': new_company_name, 'Contact Information': new_company_contact}, ignore_index=True)
    st.write(f'Company "{new_company_name}" registered successfully!')

# Allow users to register a new variety
new_variety_name = st.text_input('Register New Variety Name')
new_variety_ecozone = st.text_input('Ecozone')
new_variety_price = st.number_input('Price (Ksh)')
new_variety_company = st.selectbox('Company', df_companies['Company Name'])
if st.button('Register Variety'):
    new_variety_data = {'Variety': new_variety_name, 'Ecozone': new_variety_ecozone, 'Price (Ksh)': new_variety_price, 'Availability': 'Branches, Agents, Stockists', 'Company': new_variety_company}
    df_varieties = df_varieties.append(new_variety_data, ignore_index=True)
    st.write(f'Variety "{new_variety_name}" registered successfully!')

# Display information about Kenya Seed Company Ltd
st.write('Kenya Seed Company Ltd')
st.write('Price per 2 kg: Ksh 420')
st.write('Available at branches, agents, and stockists countrywide.')
