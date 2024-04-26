from models.database import db

class PestDiseaseManagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    recommendations = db.Column(db.Text)
    # Add more fields as needed
