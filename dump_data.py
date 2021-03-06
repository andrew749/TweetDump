import twitter
from uuid import uuid4
import json
import os

# REPLACE KEYS AS NEEDED
api = twitter.Api(
    consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxx',
    consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    access_token_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
)

# verify that the credentials still work
api.VerifyCredentials()
stream = api.GetStreamSample()

def get_new_tweet_data():
    # get a small batch of tweets to precent going over limits
    tweets = [stream.next() for x in xrange(20)]
    return tweets

# how many tweets to store in a single file
FILE_SIZE_NUM_TWEETS = 1000

def write_tweets_to_file(tweets, file):
    file.write(json.dumps(tweets))

# Continually dump.
while True:
    # keep dumping data to disk
    current_file_size = 0
    file_id = uuid4()

    print "Creating new file with id %s" % file_id
    file = open(os.path.join("data", str(uuid4())), "w")

    tweets = []
    while current_file_size < FILE_SIZE_NUM_TWEETS:
        tweets.extend(get_new_tweet_data())
        current_file_size += len(tweets)

    write_tweets_to_file(tweets, file)

    file.close()

