import tweepy

# Set up authentication parameters
consumer_key = 'NmArxlLfehbpMXXLoccgT4OyH'
consumer_secret = 'CLaOIYDUJv0GxT2FXrYIV2hh7qNSGuJzR4fUySSU0dEjepqEuf'
access_token = '550488804-0CPU2cO9VpAbywWplVH3OWLH6TakGawP4FYGBXYU'
access_token_secret = '6fYjPzUmjisWJinNvl46a3G7pBE6Zq9H6CmowfCptUnIq'

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Retrieve tweets from a specific user
user_tweets = api.user_timeline(screen_name='@kenyaseedltd', count=10)  # Replace 'username' with the Twitter username

# Iterate over tweets and retrieve associated comments (replies)
for tweet in user_tweets:
    print(f"Tweet ID: {tweet.id}, Text: {tweet.text}")
    
    # Retrieve replies to the tweet
    replies = api.search(q='to:@kenyaseedltd', since_id=tweet.id, count=10)  # Replace 'username' with the Twitter username
    
    # Iterate over replies and print them
    for reply in replies:
        print(f"Reply ID: {reply.id}, Text: {reply.text}")
