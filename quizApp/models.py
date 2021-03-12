from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import random
from random import shuffle

from django.shortcuts import render

from django.views.generic import CreateView

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', upload_to='category_img')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question-create')


class Question(models.Model):
    #Pytanie Dodać-

    title = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    answerA = models.CharField(max_length=100)
    answerB = models.CharField(max_length=100)
    answerC = models.CharField(max_length=100)
    quiz = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question-create')

    def answers(self):

        odpowiedzi = [self.answerA, self.answerB, self.answerC, self.correct_answer]
        random.shuffle(odpowiedzi)


















class Post_Question(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return self.post.title

    def questions(self):
        return self.question


