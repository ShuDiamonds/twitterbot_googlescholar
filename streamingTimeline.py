import twitter
import json

rawfiletmp = open("account.json" , "r")
accountjsonfile = json.load(rawfiletmp)

auth = twitter.OAuth(consumer_key=accountjsonfile["consumer_key"],
consumer_secret=accountjsonfile["consumer_secret"],
token=accountjsonfile["token"],
token_secret=accountjsonfile["token_secret"])

t = twitter.Twitter(auth=auth)
#Userstreamを用いる
t_userstream = twitter.TwitterStream(auth=auth,domain='userstream.twitter.com')

#自分のタイムラインのツイートおよびユーザーの情報が流れる
for msg in twitter.userstream.user():
 print(msg)