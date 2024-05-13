import requests

# Set up authentication parameters
access_token = 'YOUR_ACCESS_TOKEN'
page_id = 'YOUR_PAGE_ID'
api_version = 'v12.0'  # Specify the API version

# Make API request to retrieve posts from the page
url = f'https://graph.facebook.com/{api_version}/{page_id}/posts'
params = {'access_token': access_token}
response = requests.get(url, params=params)
data = response.json()

# Extract post IDs from the response
post_ids = [post['id'] for post in data['data']]

# Iterate over post IDs and retrieve comments for each post
for post_id in post_ids:
    comment_url = f'https://graph.facebook.com/{api_version}/{post_id}/comments'
    comment_params = {'access_token': access_token}
    comment_response = requests.get(comment_url, params=comment_params)
    comment_data = comment_response.json()
    
    # Process comment data as needed
    comments = comment_data['data']
    for comment in comments:
        # Extract relevant information from each comment
        comment_id = comment['id']
        commenter_name = comment['from']['name']
        comment_message = comment['message']
        # Process further or store in the database
        print(f"Comment ID: {comment_id}, Commenter: {commenter_name}, Comment: {comment_message}")
