from django.urls import path

from website.Views.AdminView import AdminView
from website.Views.AdviseView import AdviseView
from website.Views.AuthView import *
from website.Views.EventView import *
from website.Views.AppointemenView import *
from website.Views.FeedbackView import FeedbackView
from website.Views.NotificationView import NotificationView

urlpatterns = [
    path('auth/<str:action>/', AuthView.as_view(), name='auth'),

    path('event/<str:action>/', EventView.as_view(), name='event_action'),
    path('notification/<str:action>/<int:pk>', NotificationView.as_view(), name='notification_action'),
    path('advise/<str:action>/<int:pk>', AdviseView.as_view(), name='advise_action'),
    path('feedback/<str:action>/<int:advise>', FeedbackView.as_view()),
    path('add_appointment/<int:id>', add_appointment),
    path('feedback/<str:action>/', FeedbackView.as_view()),
    path('updated_feedback/<str:action>/<int:pk>', FeedbackView.as_view()),
    path('stats/<str:action>', AdminView.as_view()),
]












