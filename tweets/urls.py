from django.contrib import admin
from django.urls import path, include, re_path  # para mainclude ung views ng tweets app
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from templates import *
from .models import *
app_name = 'tweets'

urlpatterns = [
    path('', TweetListView.as_view(), name='list-view'),

    re_path(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail-view'),
    re_path(r'^(?P<pk>\d+)update/$', TweetUpdateView.as_view(), name='update-view'),
    re_path(r'^(?P<pk>\d+)delete/$', TweetDeleteView.as_view(), name='delete-view'),
]
