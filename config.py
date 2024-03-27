from typing import List
import os
from dotenv import load_dotenv


class Config:
    def __init__(self, secrets: List[str] = None):
        if secrets is None:
            secrets = [
                "TWITTER_CONSUMER_KEY",
                "TWITTER_CONSUMER_SECRET_KEY",
                "TWITTER_ACCESS_TOKEN",
                "TWITTER_ACCESS_TOKEN_SECRET",
                "NASA_API_DEMO_KEY",
            ]

        self.secrets_list = secrets
        self.secrets: dict[str, str] = {}
        self.__get_secrets()

    def __get_secrets(self):
        if not os.path.exists(".env.local"):
            print("WARNING: ./.env.local file doesn't exist!")
        load_dotenv(".env.local")

        for secret in self.secrets_list:
            env_variable = os.environ.get(secret)

            if env_variable is None:
                raise EnvironmentError(f"Environment variable '{secret}' isn't set!")

            self.secrets[secret] = env_variable
