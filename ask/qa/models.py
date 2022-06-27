from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models):
    """Question - вопрос
    title - заголовок вопроса
    text - полный текст вопроса
    added_at - дата добавления вопроса
    rating - рейтинг вопроса (число)
    author - автор вопроса
    likes - список пользователей, поставивших лайк """
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='likes_questions_users')


class QuestionManager(models.Manager):
    """QuestionManager - менеджер модели Question
    new - метод возвращающий последние добавленные вопросы
    popular - метод возвращающий вопросы отсортированные по рейтингу"""
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Answer(models):
    """Answer - ответ
    text - текст ответа
    added_at - дата добавления ответа
    question - вопрос, к которому относится ответ
    author - автор ответа"""
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
