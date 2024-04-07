import json
import main


def lambda_handler(event, context):
    message = main.post_tweet()

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
