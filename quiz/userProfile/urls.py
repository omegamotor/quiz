from django.urls import path
from userProfile import views

urlpatterns = [
    path('', views.profile, name='user_profile'),
]
