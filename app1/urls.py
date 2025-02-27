from django.urls import path
from .views import *

app_name='app1'

urlpatterns=[
    path('',home,name='home'),
    path('signin/',signin,name='signin'),
    path('deals/',deals,name='deals')
]