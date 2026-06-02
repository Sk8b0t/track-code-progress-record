import tweepy as tw
from tkinter import *

consumer_key="bCSECCY6DUcLeFRvJDiWaqtVk"
secret_key="ebF9of8WqWLIDfNJn9djmyL4rdZT9PEkjGtv37xkqUZkcRR8Bd"
bearer_token="AAAAAAAAAAAAAAAAAAAAACnB9wEAAAAAmkKHhbUtsSXNGbhjkcYv7CG81cw%3DZeD3V338yUhKWAQ8KrrxBwQiXpzfIdO5CaE0E0N0qdnUJ52dnn"
access_token="1410436081376370688-VgKCFrXBHKgGV9zsYSj2q9eyzkHNud"
access_token_secret="um7Vt2cX3pOG0aSZ0HXvk8fkS4lZynL7BOWZratbNY1Ud"

auth=tw.OAuthHandler(consumer_key,secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tw.API(auth)
user=api.verify_credentials()
print(user.name)
print(user.location)
