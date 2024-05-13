from app import db

# Define the Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50))
    date = db.Column(db.Date)
    post_content = db.Column(db.Text)
    comment_text = db.Column(db.Text)
    sentiment = db.Column(db.String(10))
    likes = db.Column(db.Integer)
    replies = db.Column(db.Integer)
    user_info = db.Column(db.Text)
    topics_keywords = db.Column(db.Text)
    action_required = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50))
    date = db.Column(db.Date)
    content = db.Column(db.Text)
    # Add more fields as needed

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    followers = db.Column(db.Integer)
    # Add more fields as needed

