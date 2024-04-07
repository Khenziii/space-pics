from config import Config
from nasa import NasaAPI
from aws import AwsAPI
import tweepy
from datetime import date, timedelta
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

aws_api = AwsAPI(
    access_key=secrets["AWS_ACCESS_KEY_ID"],
    secret_key=secrets["AWS_SECRET_ACCESS_KEY"]
)


def __post_tweet():
    today: date = date.today()
    yesterday: date = today - timedelta(days=1)

    thumbs: bool = True
    download_image: bool = True
    data = nasa_client.get_pictures(yesterday, thumbs, download_image)

    image_description = data["title"]
    media = twitter_api.media_upload("/tmp/image.png")
    os.remove("/tmp/image.png")

    tweet_content = f"{image_description}\n\n{today.strftime('%d/%m/%Y')}"
    twitter_client.create_tweet(text=tweet_content, media_ids=[media.media_id])


def post_tweet() -> str:
    if aws_api.check_if_ran_in_last_n_hours(23):
        return "Tweet wasn't created, as the function has already been executed today."

    __post_tweet()
    aws_api.write_execution_time_to_db()
    return "Successfully created new tweet!"
