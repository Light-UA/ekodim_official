from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Products
from goods.models import Categories


def index(request):
    # Отримати акційні товари
    sale_products = Products.objects.filter(category__slug='akcijni-propiziciyi', discount__gt=0)

    context = {
        'title': 'EkoDim',
        'sale_products': sale_products,
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Про нас',


    }
    return render( request, 'main/about.html', context )


def contacts(request):
    context = {
        'title': 'Наші контакти'

    }
    return render( request, 'main/contacts.html', context )


def delivery(request):
    context = {
        'title': 'Доставка та оплата'

    }
    return render( request, 'main/delivery.html', context )





