from models.database import db

class YieldForecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    forecast = db.Column(db.Float)
    # Add more fields as needed
