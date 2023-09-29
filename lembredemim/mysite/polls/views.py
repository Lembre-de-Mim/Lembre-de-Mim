from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    context = {}
    return render(request, 'index.html', context)

def home (request, question_id):
    context = {}
    return render(request, 'home.html', context)

def cartilhas (request, question_id):
    context = {}
    return render(request, 'cartilhas.html', context)

def prontuario (request, question_id):
    context = {}
    return render(request, 'prontuario.html', context)

def quemsomos (request, question_id):
    context = {}
    return render(request, 'quemsomos.html', context)

def minhaconta (request, question_id):
    context = {}
    return render(request, 'minhaconta.html', context)

