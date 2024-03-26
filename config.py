from typing import List
import os
from dotenv import load_dotenv


class Config:
    def __init__(self, secrets: List[str] = None):
        if secrets is None:
            secrets = [
                "CONSUMER_KEY",
                "CONSUMER_SECRET_KEY",
                "ACCESS_TOKEN",
                "ACCESS_TOKEN_SECRET",
            ]

        self.secrets = secrets
        self.__get_secrets()

    def __get_secrets(self):
        if not os.path.exists(".env.local"):
            raise EnvironmentError(f"./.env.local file doesn't exist!")
        load_dotenv(".env.local")

        for secret in self.secrets:
            env_variable = os.environ.get(secret)

            if env_variable is None:
                raise EnvironmentError(f"Environment variable '{secret}' isn't set!")
