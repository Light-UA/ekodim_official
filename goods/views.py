from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from goods.models import Products
from goods.utilits import q_search


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)

    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 6)
    current_page = paginator.page(page)



    context = {
        'title': 'Каталог',
        'goods': current_page,
        "slug_url": category_slug,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context )
