import json
import main


def lambda_handler(event, context):
    main.post_tweet()

    return {
        'statusCode': 200,
        'body': json.dumps("Successfully created new tweet!")
    }
