import twitter
import json

rawfiletmp = open("account.json" , "r")
accountjsonfile = json.load(rawfiletmp)

auth = twitter.OAuth(consumer_key=accountjsonfile["consumer_key"],
consumer_secret=accountjsonfile["consumer_secret"],
token=accountjsonfile["token"],
token_secret=accountjsonfile["token_secret"])

t = twitter.Twitter(auth=auth)

#ツイートのみ
status="Hello,World" #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿

"""
#画像付きツイート
pic=""　#画像を投稿するなら画像のパス
with open(pic,"rb") as image_file:
 image_data=image_file.read()
pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
t.statuses.update(status=status,media_ids=",".join([id=img1]))
"""