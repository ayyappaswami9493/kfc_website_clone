from django.urls import path
from .views import *

app_name='app2'

urlpatterns=[
    path('menu/',menu,name='menu'),
    path('cart/',cart,name='cart'),
    path('startorder/',startorder,name='startorder'),
]

