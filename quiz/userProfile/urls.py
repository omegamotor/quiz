from django.urls import path
from userProfile import views

urlpatterns = [
    path('', views.home1, name='user-profile'),
]
