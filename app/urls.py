# myapp/urls.py
from django.urls import path
from.views import*

urlpatterns = [
    path('',index),  
    path('register/',register),
    path('login/',login),
      ]