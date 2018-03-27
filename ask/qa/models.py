# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from ask  import settings

class QuestionManager(models.Manager):
    def new(self): #метод возвращающий последние добавленные вопросы
	    return self.order_by('-added_at')
    def popular(self): # - метод возвращающий вопросы отсортированные по рейтингу
	    return self.order_by('-rating')


class Question(models.Model):
	"""docstring for Question"""	
	title = models.CharField(max_length=120) # заголовок вопроса
	text = models.TextField(max_length=500) # полный текст вопроса
	added_at = models.DateTimeField(auto_now_add=True) # дата добавления вопроса
	rating = models.IntegerField() # рейтинг вопроса (число)
	author = models.ForeignKey(settings.AUTH_USER_MODEL) # автор вопроса
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes_set') # список пользователей, поставивших "лайк"
	objects = QuestionManager()
	class Meta:
		managed = True

class Answer(models.Model):
	"""Answer"""	
	text = models.TextField(max_length=2000)# текст ответа
	added_at = models.DateTimeField(auto_now_add=True) # дата добавления ответа
	question = models.ForeignKey('Question')# вопрос, к которому относится ответ
	author = models.ForeignKey(settings.AUTH_USER_MODEL)# автор ответа
