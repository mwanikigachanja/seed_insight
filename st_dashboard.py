import streamlit as st

# Page title and description
st.title("Seed Insight App")
st.write("Welcome to the Seed Insight App! This app helps you explore maize varieties, companies, and eco-zones.")

# Features section
st.header("Features")
st.markdown("""
- Explore different maize varieties and their attributes.
- View information about companies and their specialties.
- Learn about various eco-zones and their characteristics.
- Register new companies, maize varieties, and eco-zones.
- Dynamic CRUD operations for managing data.
""")

# How to use section
st.header("How to Use")
st.markdown("""
1. Use the sidebar filters to select specific maize varieties, eco-zones, and more.
2. Explore the filtered data displayed in the main section.
3. Register new companies, maize varieties, or eco-zones by filling out the respective forms.
4. Enjoy exploring and managing seed-related information with ease!
""")

# About section
st.header("About")
st.markdown("""
The Seed Insight App is designed to provide valuable insights into maize seed varieties, companies, and eco-zones. 
Whether you're a farmer, researcher, or enthusiast, this app offers a convenient platform to explore, register, and manage seed-related information effectively.
""")

# Footer
st.markdown("---")
st.markdown("Developed by [Your Name]")

