## space-pics

[space-pics](https://twitter.com/3a29_space_pics) is a Twitter bot, that posts cosmos images daily.

A new image is posted every 00:00 UTC.

### How does this work?

The bot is hosted on AWS. It's defined as a Lambda function, that gets called by EventBridge every 24 hours.

On every run, we:
1. Fetch an image from NASA's [APOD](https://apod.nasa.gov/apod/astropix.html) API
2. Create a tweet using it.
