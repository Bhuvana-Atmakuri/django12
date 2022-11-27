from . import views
from django.urls import path
urlpattrens=[
    path('/home',views.home,name='home')
]