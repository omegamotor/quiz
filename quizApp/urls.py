from django.urls import path
from quizApp import views

from .views import PostListView, PostDetailView, PostCreateView, QuestionCreateView, CategoryDetailView, UserListView


urlpatterns = [
    path('', PostListView.as_view(), name='quizApp-home'),
    path('user/<str:username>', UserListView.as_view(), name='user_quiz'),
    path('quiz/<int:pk>/', PostDetailView.as_view(), name='quiz-detail'),
    path('quiz/new', PostCreateView.as_view(), name='quiz-create'),

    path('quiz/newQuestion', QuestionCreateView.as_view(), name='question-create'),

    path('ranking/', views.ranking, name='ranking'),
    path('category/', views.category, name='category'),


    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

]


def javascript_settings():
    js_conf = {
        'page_title': 'Home',
    }
    return js_conf
