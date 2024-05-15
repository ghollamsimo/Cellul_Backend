from django.urls import path
from website.Views.AuthView import *
from website.Views.EventView import *

urlpatterns = [
    path('register/', create),
    path('login/', post),
    path('logout/', UserLogout),
    path('addEvent/', add_event),
    path('update_event/<int:pk>/', update_event),
    path('allEvents/', all_event),
    path('delete_event/<int:pk>/', delete_event),
]












