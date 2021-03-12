from django import forms
from .models import Question, Post_Question, Post


class QuizCreateForm():
    class Meta:
        model = Post
        fields = ['title', 'description', 'category']

class QuestionCreateForm():
    class Meta:
        model = Question
        fields = ['title', 'correct_answer', 'answerA', 'answerB', 'answerC', 'quiz']



