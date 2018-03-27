from django.conf.urls import include, url
## from django.contrib import admin
from qa import views

urlpatterns = [
    url(r'.*', views.test )
]

