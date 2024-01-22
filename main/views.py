from django.http import HttpResponse
from django.shortcuts import render


from goods.models import Categories

def index(request):



    context = {
        'title': 'Головна',
        'content': '',

    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Про нас',
        'about_us': 'Про нас',



    }

    return render(request, 'main/about.html', context)







