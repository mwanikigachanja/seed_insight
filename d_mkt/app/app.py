from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

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
    # Retrieve comments from the database
    comments = Comment.query.all()
    
    # Perform sentiment analysis
    analyzed_comments = []
    for comment in comments:
        # Perform sentiment analysis using NLTK's SentimentIntensityAnalyzer
        sentiment_score = analyze_sentiment(comment.comment_text)
        
        # Create a dictionary containing the analyzed data
        analyzed_comment = {
            'id': comment.id,
            'platform': comment.platform,
            'comment_text': comment.comment_text,
            'sentiment_score': sentiment_score
            # Add more analyzed data as needed
        }
        analyzed_comments.append(analyzed_comment)
    
    # Return analyzed data as JSON response
    return jsonify({'analyzed_comments': analyzed_comments})

def analyze_sentiment(comment_text):
    # Perform sentiment analysis using NLTK's SentimentIntensityAnalyzer
    sentiment_scores = sid.polarity_scores(comment_text)
    # The compound score ranges from -1 (most negative) to 1 (most positive)
    return sentiment_scores['compound']

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
