# AUTHOR : SHAFAY
# checking the twitter tokens as
import tweepy
import time
import datetime
import urllib.request
import json  # importing the json header file

ckey = 'Ru74Ybfzyws3q2JSNZTOUv4gv'
csecret = 'auVpDi7tbPR6K9hARUDPx58GwdmB24VyAOenXg6jfJ2uiK03nZ'
atoken = '558084273-QWy1ZFg5ZO6G0BvuJbVAyZNxinUfKERLmWfPPMBc'
asecret = 'PjA8TYtCNUyc1dhDv7BqWeCQstDx2fbGn8ZrqXitxkPet'
print("Consumer Key: ", ckey)
print("Consumer secret: ", csecret)
print("Access Token key :", atoken)
print("Access Token secrets: ", asecret)
# First Providing the OAuthHandler the Consumer key and the Consumer secret
auth = tweepy.OAuthHandler(ckey, csecret)  # setting the consumer key and the consumer secret there
# Setting the headers of the access tokens of the twitter
auth.set_access_token(atoken, asecret)  # setting the access tokens and the access secrets.
auth.secure = True  # setting the connection to be secure

api = tweepy.API(auth)  # specifing the api the respectable authentication and applying the auth

print(str(api.get_user(screen_name ='@ShafayB')))  # accessing the twitter api, and then specifing the
# Trying to access the tweets , q is the searching , while lang represents the language and the apisearch is the pointing
Query_to_search = input("Please enter the tag you want to search for Without (#) : ")
Query_to_search = "#" + Query_to_search.strip()  # removing the extra white spaces from the query

for tweet in tweepy.Cursor(api.search, q=Query_to_search,lang='en').items():
    try:
        # Trying to access the tweet .
        print("\n\nFound Tweet by :" + tweet.user.screen_name)  # just pointing out the tweet. and checking the user name
        # Retweet it and follow the user
        if (tweet.retweet == False) or (tweet.favorited == False):
            # Checking if the tweet is not been teeated . As
            tweet.retweet()   # retweeting the particular tweet , (in your profile)
            tweet.favorite() # adding to the favourite (the tweet .)
            print("Retweeted and favourite the tweet")
        if tweet.user.following == False:
            tweet.user.follow() # Following the User so that it follows the particuar user.
            a = tweet.text
            print('Followed the user')
    except tweepy.TweepError as e:
        print(e.reason) # printing the reason behind the error
        time.sleep(2)   # sleeping the user so that we can see , the problem
        continue
    except StopIteration:
        break  # When the iteration is about to be finished , stop the iteration

