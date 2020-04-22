import os
import tweepy
import random
from random import randint

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        raise e
    return api

def main(keywords):
    api = create_api()
    line = random_line("the_night_watch.txt")

    # for long sentences lets just pick a random part
    while len(line) > 280:
        words = line.split()
        length = len(words)
        start = randint(0,length-2)
        end = randint(start,length-1)
        del words[0:start]
        del words[end:length]
        words[0] = words[0].capitalize()
        line = " ".join(words)
        if line[-1] != '.':
            line = line + "."

    print(line)

    api.update_status(line)

if __name__ == "__main__":
    main(["Python", "Tweepy"])
