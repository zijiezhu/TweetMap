"""TweetMap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from TweetMap.Backend import indexpage
from TweetMap.Backend import get_response
from TweetMap.Backend import get_georesponse

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json/(?P<keyword>\w{0,50})/$', get_response.reply),
    url(r'^geo/(?P<latitude>-?\d*\.{0,1}\d+)/(?P<longitude>-?\d*\.{0,1}\d+)/$', get_georesponse.get_geo),
    url(r'', indexpage.display)

]
