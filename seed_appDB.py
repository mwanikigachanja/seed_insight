import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Set up the database
DATABASE_URL = "sqlite:///seed_insight.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database models
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    contact_info = Column(String)

class Variety(Base):
    __tablename__ = "varieties"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ecozone = Column(String)
    price = Column(Integer)
    company_id = Column(Integer, index=True)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Streamlit app
def main():
    st.title("Seed Insight Dashboard")

    # Sidebar for adding a new company
    st.sidebar.header("Register New Company")
    new_company_name = st.sidebar.text_input("Company Name")
    new_company_contact = st.sidebar.text_input("Contact Information")
    if st.sidebar.button("Register"):
        register_company(new_company_name, new_company_contact)

    # Sidebar for adding a new variety
    st.sidebar.header("Register New Variety")
    new_variety_name = st.sidebar.text_input("Variety Name")
    new_variety_ecozone = st.sidebar.text_input("Ecozone")
    new_variety_price = st.sidebar.number_input("Price (Ksh)")
    companies = get_companies()
    company_names = [company.name for company in companies]
    selected_company = st.sidebar.selectbox("Company", company_names)
    if st.sidebar.button("Register"):
        company_id = get_company_id(selected_company)
        register_variety(new_variety_name, new_variety_ecozone, new_variety_price, company_id)

    # Main content to display registered companies and varieties
    st.subheader("Registered Companies")
    display_companies()
    st.subheader("Registered Varieties")
    display_varieties()

# Helper functions to interact with the database
def register_company(name: str, contact_info: str):
    session = SessionLocal()
    company = Company(name=name, contact_info=contact_info)
    session.add(company)
    session.commit()
    session.close()
    st.success(f"Company '{name}' registered successfully!")

def get_companies():
    session = SessionLocal()
    companies = session.query(Company).all()
    session.close()
    return companies

def get_company_id(name: str):
    session = SessionLocal()
    company = session.query(Company).filter(Company.name == name).first()
    session.close()
    return company.id

def register_variety(name: str, ecozone: str, price: int, company_id: int):
    session = SessionLocal()
    variety = Variety(name=name, ecozone=ecozone, price=price, company_id=company_id)
    session.add(variety)
    session.commit()
    session.close()
    st.success(f"Variety '{name}' registered successfully!")

def display_companies():
    companies = get_companies()
    for company in companies:
        st.write(f"- {company.name}: {company.contact_info}")

def display_varieties():
    session = SessionLocal()
    varieties = session.query(Variety).all()
    session.close()
    for variety in varieties:
        st.write(f"- {variety.name}: Ecozone: {variety.ecozone}, Price: {variety.price} Ksh, Company: {get_company_name(variety.company_id)}")

def get_company_name(company_id: int):
    session = SessionLocal()
    company = session.query(Company).filter(Company.id == company_id).first()
    session.close()
    return company.name

if __name__ == "__main__":
    main()
