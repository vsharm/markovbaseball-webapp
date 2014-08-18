from django.conf.urls import patterns,url
from ccba import views

urlpatterns = [
    url(r'^$', views.index),
#    url(r'^(?P<urlpath>.*)/$', views.teamRouter),
]
