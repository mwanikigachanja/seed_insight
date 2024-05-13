from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Seed(db.Model):
    __tablename__ = 'seeds'

    id = db.Column(db.Integer, primary_key=True)
    ecozone = db.Column(db.String(100), nullable=False)
    crop_name = db.Column(db.String(100), nullable=False)
    seed_rate = db.Column(db.Float, nullable=False)
    maturity_period = db.Column(db.Integer, nullable=False)
    yield_amount = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.String(100), nullable=False)

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

class Ecozone(db.Model):
    __tablename__ = 'ecozones'

    id = db.Column(db.Integer, primary_key=True)
    zone_name = db.Column(db.String(100), nullable=False)
    altitude = db.Column(db.Integer, nullable=False)
    rainfall = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    soil_type = db.Column(db.String(100), nullable=False)
    attributes = db.Column(db.String(100), nullable=False)

