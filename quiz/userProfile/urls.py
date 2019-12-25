from django.urls import path
from userProfile import views
from userProfile.views import login

urlpatterns = [
    path('', views.profile, name='user_profile'),
    path('login/', login),
]
