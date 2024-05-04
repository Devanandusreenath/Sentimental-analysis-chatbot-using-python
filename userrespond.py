import random
from textana import analyze_sentiment
from responses import responses

def respond_to_user(text):
    sentiment = analyze_sentiment(text)
    responses_for_sentiment = responses[sentiment]
    response = random.choice(responses_for_sentiment)
    return response