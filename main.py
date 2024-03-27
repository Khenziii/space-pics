from config import Config
from nasa import NasaAPI
import tweepy
from datetime import date

configManager = Config()
secrets = configManager.secrets

nasa_client = NasaAPI(
    api_key=secrets["NASA_API_DEMO_KEY"]
)

# twitter_client = tweepy.Client(
#     consumer_key=secrets["CONSUMER_KEY"],
#     consumer_secret=secrets["CONSUMER_SECRET_KEY"],
#     access_token=secrets["ACCESS_TOKEN"],
#     access_token_secret=secrets["ACCESS_TOKEN_SECRET"]
# )
# twitter_client.create_tweet(text="Hello, World!")

from_when: date = date.today()
print(nasa_client.get_pictures(from_when, True))
