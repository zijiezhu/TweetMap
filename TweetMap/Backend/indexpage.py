from django.http import HttpResponse
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

def display(request):
    html = "<html><body>Failed to load tweetmap.</body></html>"
    with open(os.path.join(BASE, '../../Frontend/index.html'), 'r') as file:
        html = file.read()
        file.close()
    return HttpResponse(html)