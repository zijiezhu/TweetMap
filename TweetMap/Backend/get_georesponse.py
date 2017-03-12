import json
from django.http import HttpResponse
from elasticsearch import Elasticsearch



domain = "search-tweetmap-tx3gypzkmdsydrnlqv44ojd5qq.us-east-1.es.amazonaws.com"
index = "tweet"


def get_geo(request, latitude, longitude):
    es = Elasticsearch([{'host': domain, 'port': 80,'use_ssl': False}])
    data = es.search(index= index , body={ "query": { "bool" : { "must" : { "match_all" : {} }, "filter" : { "geo_distance" : { "distance" : "200km", "location" : str(latitude) + "," + str(longitude) } } } } })['hits']
    response = HttpResponse(json.dumps(data), content_type="application/json")
    return response

