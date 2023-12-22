from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина',
        'list': ['first', 'second', 'third'],
        'dict': {'first': 'first', 'second': 'second'},
        'is_auth': False
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About page" )


