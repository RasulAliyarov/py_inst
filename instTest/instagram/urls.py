from django.urls import path
from .views import *
urlpatterns=[
    path("", Auth, name='Auth'),
    path("home", Home, name='Home'),
    path("addInstagram", AddInstagram, name='AddInstagram'),
    path("", Logout, name='Logout'),
]