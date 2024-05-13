from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/comment_analysis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your SQLAlchemy models here
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

# Define your routes here
@app.route('/comments', methods=['POST'])
def receive_comments():
   # Get data from the request
    data = request.json
    
    # Extract relevant fields from the data
    platform = data.get('platform')
    date = data.get('date')
    post_content = data.get('post_content')
    comment_text = data.get('comment_text')
    sentiment = data.get('sentiment')
    likes = data.get('likes')
    replies = data.get('replies')
    user_info = data.get('user_info')
    topics_keywords = data.get('topics_keywords')
    action_required = data.get('action_required')
    notes = data.get('notes')
    
    # Create a new Comment object
    comment = Comment(
        platform=platform,
        date=date,
        post_content=post_content,
        comment_text=comment_text,
        sentiment=sentiment,
        likes=likes,
        replies=replies,
        user_info=user_info,
        topics_keywords=topics_keywords,
        action_required=action_required,
        notes=notes
    )
    
    # Add the comment to the database session
    db.session.add(comment)
    
    # Commit the transaction
    db.session.commit()
    
    return jsonify({'message': 'Comment received and stored successfully'})
    

@app.route('/analyze', methods=['GET'])
def perform_analysis():
    # Logic for performing analysis on comments
    # You can retrieve comments from the database, perform sentiment analysis, etc.
    # Example:
    # comments = Comment.query.all()
    # Perform sentiment analysis, keyword extraction, etc.
    # Return analyzed data as JSON response
    return jsonify({'message': 'Analysis performed successfully'})

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
