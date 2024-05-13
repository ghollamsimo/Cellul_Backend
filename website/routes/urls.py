from django.urls import path
from website.Views.AuthView import *

urlpatterns = [
    path('register/', create),
    path('login/', post),
    path('logout/', UserLogout)
]












