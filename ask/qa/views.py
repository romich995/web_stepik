# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.core.paginator import Paginator
from models import *
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def questions_by_date(request, *args, **kwargs):
    questions  = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'question_by_date.html', {
                   'posts': page.object_list,
                   'paginator': paginator, 
                   'page': page,
                   })

def questions_by_popular(request, *args, **kwargs):
    questions  = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'question_by_date.html', {
                   'posts': page.object_list,
                   'paginator': paginator, 
                   'page': page,
                   })

def question(request,*args, **kwargs):
    question = get_object_or_404(Question, pk=kwargs['id'])
	#return HttpResponse(str(id))
    try:
		answers = question.answer_set.all()
    except Answer.DoesNotExist:
    	answers = None
    return render(request, 'questionWithAnswers.html', {
     'question': question,
     'answers': answers,
     })


