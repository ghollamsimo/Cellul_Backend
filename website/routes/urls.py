from functools import partial

from django.urls import path

from website.Views.AdminView import AdminView
from website.Views.AdviseView import *
from website.Views.AuthView import *
from website.Views.CalendarView import *
from website.Views.EventView import *
from website.Views.AppointemenView import *
from website.Views.FeedbackView import FeedbackView
from website.Views.NotificationView import NotificationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from website.Views.RecordView import RecordView

urlpatterns = [
    path('auth/<str:action>/', AuthView.as_view(), name='auth'),
    path('auth/<str:action>/<int:id>', show_user, name='auth'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/reset-password/<str:token>/', AuthView.as_view(), {'action': 'reset_password'}, name='reset-password'),

    path('activate/<uidb64>/<token>/', AuthView.as_view(), name='activate-account'),
    path('events/', index),
    path('event/<int:pk>', show),
    path('event/<str:action>/', EventView.as_view(), name='event_action'),
    path('event_action/<str:action>/<int:pk>', EventView.as_view()),
    path('notification/<str:action>/<int:pk>', NotificationView.as_view(), name='notification_action'),
    path('notification/<str:action>', NotificationView.as_view(), name='notification'),
    path('advise/<str:action>/<int:pk>', AdviseView.as_view(), name='advise_action'),
    path('advisers/', get_all_advisers),
    path('advise/<int:pk>', get_advise),
    path('feedback/<str:action>/<int:advise>', FeedbackView.as_view()),
    path('appointment/<str:action>/<int:id>', AppointementView.as_view()),
    path('appointment_get/<str:action>', AppointementView.as_view()),
    path('feedback/<str:action>/', FeedbackView.as_view()),
    path('updated_feedback/<str:action>/<int:pk>', FeedbackView.as_view()),
    path('action/<str:action>', AdminView.as_view()),
    path('updated_user/<str:action>/<int:id>', AdminView.as_view()),
    path('deleted_user/<str:action>/<int:id>', AdminView.as_view()),
    path('record/<str:action>', RecordView.as_view()),
    path('record_action/<str:action>/<int:pk>', RecordView.as_view()),
    path('calendar/<str:action>', CalendarView.as_view()),
    path('calendar_action/<str:action>/<int:pk>', CalendarView.as_view()),
    path('all_calendar/<int:id>', index_availability),

]








