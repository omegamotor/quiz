from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Question, Post_Question
from userProfile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import QuizCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User


def home(request):

    post_nr = Post.objects.all()[::-1][0].id

    full_deck = post_nr/3
    el_last_deck = post_nr%3

    context = {
        'posts': Post.objects.all(),
        'full_deck':range(int(full_deck)),
        'el_last_deck':el_last_deck
    }

    return render(request, "home.html", context)


def quiz(request):
    return render(request, template_name="quiz.html")


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6
    # <app>/<model>_<viewtype>.html>


class UserListView(ListView):
    model = Post
    template_name = 'user_quiz.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin,DetailView):
    extra_context = {
        'pytania':Question.objects.all()
    }
    model = Post


class CategoryDetailView(DetailView):
    extra_context = {
        'quizy':Post.objects.all()
    }
    model = Category


class PostCreateView(LoginRequiredMixin,CreateView):

    model = Post
    fields = ['title', 'description', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionCreateView(LoginRequiredMixin,CreateView):

    extra_context = {
        'this_quiz': Post.objects.order_by('-id')[0]
    }
    model = Question
    fields = ['title', 'correct_answer', 'answerA', 'answerB', 'answerC']

    def form_valid(self, form):
        form.instance.quiz = Post.objects.order_by('-id')[0]
        return super().form_valid(form)


class QuziQuestionCreate(LoginRequiredMixin,CreateView):
    model = Post_Question


@login_required
def add_quiz(request):

    return render(request,"add-quiz.html")


def ranking(request):

    context = {
        'names': Profile.objects.order_by('-punkty')
    }

    return render(request, "ranking.html", context)


def category(request):
    context = {
        'kategorie': Category.objects.all()}
    return render(request, 'category.html', context)

