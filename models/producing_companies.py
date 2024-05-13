from models.database import db

class ProducingCompany(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    seeds = db.relationship('Seed', back_populates='producing_company')
