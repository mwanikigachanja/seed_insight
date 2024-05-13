from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create engine and session
db_user = "mwaniki"
db_pass = "admin@254"
DATABASE_URL = f"mysql://{db_user}:{db_pass}@localhost/seed_insight"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String, unique=True, index=True)
    sname = Column(String, unique=True, index=True)
    gender = Column(Enum("Male", "Female", "Other"))
    location = Column(String)
    email = Column(String, unique=True, index=True)
    pword = Column(String)
    role = Column(Enum("Farmer", "Extension Officer", "Admin", "Other", "Guest"))
    # Add other user information as needed

class CropType(Base):
    __tablename__ = "crop_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    classification = Column(Enum("Cereal", "Legume", "Root", "Tuber", "Vegetable", "Fruit", "Other", "Unknown"))
    description = Column(String)
    # Add other crop type information as needed

class SeedVariety(Base):
    __tablename__ = "seed_varieties"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    ecozone_id = Column(Integer, ForeignKey("climate_ecozones.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    price = Column(Integer)
    crop_type_id = Column(Integer, ForeignKey("crop_types.id"))
    # Define relationships
    ecozone = relationship("ClimateEcozone", back_populates="seed_varieties")
    company = relationship("Company", back_populates="seed_varieties")
    crop_type = relationship("CropType", back_populates="seed_varieties")

class ClimateEcozone(Base):
    __tablename__ = "climate_ecozones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    altitude = Column(Integer)
    rainfall = Column(Integer)
    classification = Column(Enum("Tropical", "Subtropical", "Temperate", "Arid", "Semi-arid", "Other", "Unknown","Highland", "Lowland", "Coastal", "Dryland", "Medium", "Transitional", "Plateau", "Plain"))
    description = Column(String)
    # Add other climate/ecozone information as needed
    seed_varieties = relationship("SeedVariety", back_populates="ecozone")

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    contact_info = Column(String)
    website = Column(String)
    speciality = Column(Enum("Seeds", "Fertilizers", "Pesticides", "Machinery", "Other", "Unknown"))
    # Add other company information as needed
    seed_varieties = relationship("SeedVariety", back_populates="company")

# Create tables in the database
Base.metadata.create_all(bind=engine)
