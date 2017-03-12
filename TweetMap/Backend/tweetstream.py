from tweepy import OAuthHandler
import  time
from tweepy import  Stream
from tweepy import  OAuthHandler
from TweetMap.Backend.listener import listener


if __name__ == '__main__':
    __customerKey = "b3Ajqqy9fiv3rsV0MzfUS9RUJ"
    __customerSecret = "bcDKUb4OEto0KruBHHxvCOk6Hwp5bpdIk8MsnZBqYhpGxWjwPm"
    __accessToken = "840816291204202497-TtRzC6HM5Tz0H3G0pGZt018D2oQqENw"
    __accessSecret = "grYg6bgKNrQC9fPaiqTtbSfJQuJTzLnBlwiab7T5Vfnh4"
    autho = OAuthHandler(__customerKey, __customerSecret)
    autho.set_access_token(__accessToken, __accessSecret)
    url = "https://stream.twitter.com/1.1/statuses/sample.json"
    stream = Stream(autho, listener())
    while True:
        try:
            stream.filter(locations=[-180,-90,180,90], stall_warnings = True)
        except :
            time.sleep(10)
            continue