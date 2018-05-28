import tweepy
from textblob import TextBlob
import csv

# Step 1 - Authenticate
consumer_key='ldcdB1zPex9PvlJE3lZObn39s'
consumer_secret='1zDYs2k0yLeC3fkaamFPU0D8AZeEmdTCi34k1rnZJTuOQkSiRO'
access_token = '41557794-DZKSYfnj2u25auIF846oEkyfk26IOyGE67qBZlGLC'
access_token_secret = 'aPwNkI5JxnbGOPEyF3Pnxe4AuQQmCsrq30xbuaVXp3yfx'

#Step 2 - Establish connection with Twitter API
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('India')

#Step 4 - Analysing the tweets and writing them in CSV file
f = open('tweet.csv', 'w')
with f:
	writer = csv.DictWriter(f, fieldnames = ["Tweet", "Analysis 1"])
	writer.writeheader()
	writer = csv.writer(f)



	for tweet in public_tweets:
	    print(tweet.text)
	    
	    analysis = TextBlob(tweet.text)
	    tweet_polarity = analysis.sentiment.polarity
	    if tweet_polarity>0.0 and tweet_polarity<=1.0:
	    	data = 'positive'
	    else:
	    	data = 'negative'

	    inpt=[tweet.text,data]
	    
	    writer.writerow(inpt)
f.close()	    
