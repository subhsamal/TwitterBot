import tweepy, time, sys  #Includes three packages we need for our program
argfile = str(sys.argv[1])

#Information from twitter apps
CONSUMER_KEY = 'yzqTqj8QBYjSmELm17i1TA9xk'
CONSUMER_SECRET = '3hEGrHcHM0I6flhyQJglcQwoXqEnsqS7AVHml93GOPs2iPPBwG'
ACCESS_TOKEN = '4851490814-he7poYhOQDcLk6YGMHNObhAWQBeubHU2tfkNBzi'
ACCESS_TOKENS_SECRET = 'zCZueXTC3OWs920djGyadIGXMZN2r1nx9UXxxGpZrV8m2'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKENS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(status = line)
    time.sleep(50)
