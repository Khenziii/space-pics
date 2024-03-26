from config import Config
import tweepy

configManager = Config()
secrets = configManager.secrets

client = tweepy.Client(
    consumer_key=secrets["CONSUMER_KEY"],
    consumer_secret=secrets["CONSUMER_SECRET_KEY"],
    access_token=secrets["ACCESS_TOKEN"],
    access_token_secret=secrets["ACCESS_TOKEN_SECRET"]
)
client.create_tweet(text="Hello, World!")
