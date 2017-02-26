import tweepy
from time import sleep
from credentials import *


# Access and Authorize twitter credentials
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKENS_SECRET)
api = tweepy.API(auth)


my_file = open('book.txt', 'r')
file_lines = my_file.readlines()
my_file.close()
def tweet():
    for line in file_lines:
        try:
            print(line)

            if line != '\n':
                api.update_status(line) #it's a tweepy function to update status
                sleep(86400)
            else:
                pass
        except tweepy.TweepError as e:
            print (e.reason)
            sleep(10)

tweet()
