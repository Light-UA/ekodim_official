from django.db.models import Q
from goods.models import Products


def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)

# from django.db.models import Q
# from goods.models import Products
#
# def q_search(query):
#     if query.isdigit() and len(query) <= 5:
#         return Products.objects.filter(id=int(query))
#
#     keywords = [word for word in query.split() if len(word) > 3]
#
#     result_list = []
#
#     for token in keywords:
#         # Додайте результати для кожного слова до загального списку
#         results = Products.objects.filter(Q(description__icontains=token) | Q(name__icontains=token))
#         result_list.extend(results)
#
#     # Видаліть дублікати, якщо вони виникають
#     result_list = list(set(result_list))
#
#     return result_list

