from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(),  name='home'),
    path('about_me/', about_me, name='about_me'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('<str:subpart>/', redirected),
    ]