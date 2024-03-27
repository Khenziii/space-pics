from config import Config
from nasa import NasaAPI
import tweepy
from datetime import date
import os

configManager = Config()
secrets = configManager.secrets

nasa_client = NasaAPI(
    api_key=secrets["NASA_API_DEMO_KEY"]
)

twitter_auth_dict = {
    "consumer_key": secrets["TWITTER_CONSUMER_KEY"],
    "consumer_secret": secrets["TWITTER_CONSUMER_SECRET_KEY"],
    "access_token": secrets["TWITTER_ACCESS_TOKEN"],
    "access_token_secret": secrets["TWITTER_ACCESS_TOKEN_SECRET"]
}
twitter_client = tweepy.Client(**twitter_auth_dict)
twitter_auth = tweepy.OAuth1UserHandler(**twitter_auth_dict)
twitter_api = tweepy.API(auth=twitter_auth)


def post_tweet():
    from_when: date = date.today()
    thumbs: bool = True
    download_image: bool = True
    data = nasa_client.get_pictures(from_when, thumbs, download_image)

    image_description = data["title"]
    media = twitter_api.media_upload("/tmp/image.png")
    os.remove("/tmp/image.png")

    tweet_content = f"{image_description}\n\n{from_when.strftime('%d/%m/%Y')}"
    twitter_client.create_tweet(text=tweet_content, media_ids=[media.media_id])
