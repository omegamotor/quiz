from django.urls import path
from quizApp import views

urlpatterns = [
    path('', views.home, name='quizApp-home'),
]
