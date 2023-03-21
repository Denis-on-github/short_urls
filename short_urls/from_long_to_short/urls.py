from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about_me/', about_me, name='about_me'),
    path('feedback/', feedback, name='feedback')
]