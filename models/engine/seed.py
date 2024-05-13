from models.database import db

class Seed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    variety = db.Column(db.String(100), nullable=False)
    ecological_zone = db.Column(db.String(100), nullable=False)
    yield_data = db.Column(db.Float)
    producing_company_id = db.Column(db.Integer, db.ForeignKey('producing_company.id'))
    producing_company = db.relationship('ProducingCompany', back_populates='seeds')

class ProducingCompany(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    seeds = db.relationship('Seed', back_populates='producing_company')
