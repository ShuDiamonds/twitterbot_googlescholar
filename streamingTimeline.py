import twitter
import json
import random

SCREEN_NAME="KanNotice"

if __name__ == '__main__':
    rawfiletmp = open("account.json" , "r")
    accountjsonfile = json.load(rawfiletmp)

    auth = twitter.OAuth(consumer_key=accountjsonfile["consumer_key"],
    consumer_secret=accountjsonfile["consumer_secret"],
    token=accountjsonfile["token"],
    token_secret=accountjsonfile["token_secret"])
    
    """
    t = twitter.Twitter(auth=auth)
    #Userstreamを用いる
    t_userstream = twitter.TwitterStream(auth=auth,domain='userstream.twitter.com')

    #自分のタイムラインのツイートおよびユーザーの情報が流れる
    for msg in twitter.userstream.user():
        print(msg)
    """
    # Retrieve friends IDs
    twitter_api = twitter.Twitter(auth=auth)
    friends = twitter_api.friends.ids(screen_name=SCREEN_NAME, count=5000)
    friends_ids = ','.join(map(str, friends['ids']))

    stream = twitter.TwitterStream(auth=auth, secure=True)
    for tweet in stream.statuses.filter(follow=friends_ids):
        #print(tweet) # tweet data format is dictionay,
        try: #when tweet data is about deletion, there is no keyword, user and so on.
            if 'user' in tweet and tweet['user']['id'] in friends['ids']:
                print(tweet['user']['screen_name'], tweet['text'])
                
            
            if tweet['in_reply_to_screen_name']==SCREEN_NAME: #when reply to @KanNotice
                if "search:" in tweet['text']:
                    tweet = "@"+tweet['user']['screen_name']+" "+"Okay, let me search it!"+ " "+str(random.random())
                    twitter_api.statuses.update(status=tweet)
                else:
                    tweet = "@"+tweet['user']['screen_name']+" "+"Reply Thanks you"+ " "+str(random.random())
                    twitter_api.statuses.update(status=tweet)
        except:
            pass