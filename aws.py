from time import time
import boto3
from datetime import date, datetime, timedelta

DYNAMO_TABLE_NAME = "space-pics"
DYNAMO_PARTITION_KEY = "last-ran-at"


class AwsAPI:
    def __init__(self, access_key: str, secret_key: str):
        self.access_key = access_key
        self.secret_key = secret_key

        self.partition_key = DYNAMO_PARTITION_KEY
        self.table_name = DYNAMO_TABLE_NAME
        self.db = boto3.resource('dynamodb')

    # writes time.time to db
    def write_execution_time_to_db(self):
        current_time = time()
        item = {
            self.partition_key: int(current_time),
            "expires-at": int(current_time) + 60 * 60 * 24 * 7,
        }

        response = self.db.Table(self.table_name).put_item(
            Item=item
        )
        return response

    def check_if_ran_in_last_n_hours(self, hours: int) -> bool:
        response = self.db.Table(self.table_name).scan()

        items = response["Items"]
        if len(items) < 1:
            return False
        # by default, the largest int in
        # results will be returned first
        item = items[0]
        # dates are stored in timestamp format
        # (seconds since unix epoch, time.time())
        last_execution_time = item["last-ran-at"]

        last_execution_time_date = datetime.utcfromtimestamp(int(last_execution_time))
        current_time = datetime.utcnow()

        diff = current_time - last_execution_time_date
        if diff < timedelta(hours=hours):
            return True

        return False
