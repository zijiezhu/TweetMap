
from tweepy.streaming import StreamListener
import json
from elasticsearch import Elasticsearch

maxTweets = 1000000

class listener (StreamListener):
    __raw_data = []
    def __init__(self):
        self.index = 0
        __domain = "search-tweetmap-tx3gypzkmdsydrnlqv44ojd5qq.us-east-1.es.amazonaws.com"
        self.__es = Elasticsearch(hosts= [{'host': __domain, 'port': 80,'use_ssl': False}])
        __body = {"mappings": { "tweet":{ "properties": {"username": {"type": "string"}, "timestamp": {"type": "date"}, "location": {"type": "geo_point"}, "text": {"type": "string"} } } } }
        if self.__es.indices.exists(index="tweet") is True:
            self.__es.indices.create(index="tweet", ignore=400, body = __body)



    def on_data(self, __raw_data):
        if __raw_data :
            __count = 0
            json_data = json.loads(__raw_data)
            if json_data.get("user") is not None and json_data.get("user").get("name") is not None:
                 name = json_data.get("user").get("name")
                 __count = __count + 1
            if json_data.get("coordinates") :
                geo = json_data.get("coordinates").get("coordinates")
                long = geo[0]
                lan =  geo[1]
                __count = __count + 1
            elif json_data.get("place") :
                geo = json_data.get("place").get("bounding_box").get("coordinates")[0]
                long = geo[0][0]
                lan = geo[0][1]
                __count = __count + 1
            if json_data.get("text") :
                content = json_data.get("text")
                __count = __count + 1
            if json_data.get("timestamp_ms") :
                time = json_data.get("timestamp_ms")
                __count = __count + 1

            if __count == 4:
                self.index = self.index % maxTweets + 1
                dictionary = {"location": {"lat": lan, "lon":long}, "username": name,"timestamp": time, "text": content}
                print(dictionary)
                self.__es.index(index="tweet", doc_type='tweet', id=self.index, body=json.dumps(dictionary))









