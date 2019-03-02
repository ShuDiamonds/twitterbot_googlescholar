# twitterbot_googlescholar
the app aim is to send the infomation which is the result of thesis title analysis from google scholar


## Main Features
* about search features.
* about twi bot.

## System Overview
<p align="center"> 
<img  src=""  title="system overview">
</p>
  
## Requirement  
* Raspberry pi 3  
* Rasbian 
* Python 3.x  

 
## Setting
###  config

1. [Twitter App](https://apps.twitter.com/)にアクセス
2. Create New Appで新規appを作成する
3. 各種keyを手に入れる

    Consumer Key(API Key)
    Consumer Secret(API Secret)
    Access Token
    Access Token Secret
    
### install library
```bash
$ pip3 install twitter

```

## Usage
### Basic Example
```bash
$ python3 streamingTimeline.py
```
### Send Message to @KanNotice 
sending like below, 
```bash
@KanNotice search:keywords
```
we will reply: Okay, let me search it!
search keywords from google scholar and finished it,
send a message to u, like this
```bash
@yourname result:
```




## Licence

  [MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Related Articles
* [embedded](https://github.com/topics/shu-embedded-systems)
* [Machine Learning data](https://github.com/topics/shu-machine-learning-data)

## Author
  [ShuDiamonds](https://github.com/ShuDiamonds)
