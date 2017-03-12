import json
from django.http import HttpResponse
import re
from elasticsearch import Elasticsearch

domain = "search-tweetmap-tx3gypzkmdsydrnlqv44ojd5qq.us-east-1.es.amazonaws.com"

def reply(request, keyword):
    es = Elasticsearch([{'host': domain, 'port': 80,'use_ssl': False}])
    keyword = re.sub('[^A-Za-z0-9]+', '', keyword)
    data = es.search(index="tweet",
                     body={"sort":
         [{"timestamp":
               {"order": "desc"}
           }],
     "query":
         {"match":
              {"text": keyword
               }
          },
     "size": 100
     })['hits']
    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response
