from . import views
from django.urls import path
urlpattrens=[
    path('',views.home,name='home')
]