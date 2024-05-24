from app import create_app, db
from app.models import Pest, Disease

app = create_app()

with app.app_context():
    db.create_all()

    # Sample Pests
    pest1 = Pest(
        name="Armyworm",
        description="Armyworms are a common pest that affects many crops.",
        image_url="url_to_image",
        symptoms="Leaf damage, visible larvae",
        treatment="Pesticides, natural predators",
        crops_affected="Maize, Rice"
    )

    pest2 = Pest(
        name="Aphids",
        description="Aphids are small sap-sucking insects.",
        image_url="url_to_image",
        symptoms="Sticky residue on leaves, stunted growth",
        treatment="Insecticidal soap, neem oil",
        crops_affected="Various vegetables, fruits"
    )

    # Sample Diseases
    disease1 = Disease(
        name="Powdery Mildew",
        description="Powdery mildew is a fungal disease that affects many plants.",
        image_url="url_to_image",
        symptoms="White powdery spots on leaves",
        treatment="Fungicides, proper air circulation",
        crops_affected="Cucumbers, Squash"
    )

    disease2 = Disease(
        name="Late Blight",
        description="Late blight is a serious disease of potatoes and tomatoes.",
        image_url="url_to_image",
        symptoms="Dark spots on leaves and stems",
        treatment="Fungicides, resistant varieties",
        crops_affected="Potatoes, Tomatoes"
    )

    db.session.add_all([pest1, pest2, disease1, disease2])
    db.session.commit()
