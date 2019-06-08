from django.urls import path
from .views import IndexView


urlhomepatterns = ([
    path('', IndexView.as_view(), name="index"),
], 'home')