"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from qa import urls as qa_urls
import qa

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', qa.views.questions_by_date, name='index' ),
    url(r'^login/', include(qa_urls), name='login'),
    url(r'^signup/', include(qa_urls), name='signup'),
    url(r'^ask/', include(qa_urls), name='ask'),
    url(r'^popular/', qa.views.questions_by_popular, name='popular'),
    url(r'^new/', include(qa_urls), name='new'),
    url(r'^login/', include(qa_urls), name='login'),
    url(r'^question/(?P<id>\d+)/', qa.views.question, name='question'),
]
