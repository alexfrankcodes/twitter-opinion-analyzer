from flask import Flask, render_template, request
import tweepy
from textblob import TextBlob
import config
import re

app = Flask(__name__)

# Keep Flask from caching CSS file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Tweepy setup
auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)

api = tweepy.API(auth)


@app.route('/', methods=['POST', 'GET'])
def index():
    public_tweets = []
    aggregate_polarity = 0

    if request.method == 'POST':
        topic = request.form.get('topic')
        public_tweets = api.search(topic, count=100, result_type="mixed")
        for tweet in public_tweets:
            blob = TextBlob(tweet.text)
            # Sum polarity | Values above 0 represent a positive sentiment, values below 0 represent negative sentiment
            aggregate_polarity += blob.sentiment.polarity

    # Round aggregate polarity to two decimal places
    aggregate_polarity = round(aggregate_polarity, 2)
    return render_template('index.html', public_tweets=public_tweets, aggregate_polarity=aggregate_polarity)


if __name__ == "__main__":
    app.run(debug=True)
