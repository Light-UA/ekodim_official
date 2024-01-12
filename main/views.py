from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Головна',
        'content': '',
        'categories': categories,

    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Про нас',
        'content': 'Про нас',



    }

    return render(request, 'main/about.html', context)


