from django.conf.urls import url
from django.contrib import admin
from board.views import *

urlpatterns = [
    url(r'', indexView.as_view())
]
