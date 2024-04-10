from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from carts.models import Cart

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def create_order(request):
    order_exists = Order.objects.filter(user=request.user).exists()
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product=cart_item.product
                            name=cart_item.product.name
                            price=cart_item.product.sell_price()
                            quantity=cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостатня кількість товару {name} на складі\
                                                       В наявності - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, "Замовлення оформлено, наш менеджер зв'яжеться з вами найближчим часом!")
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('orders:create_order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Оформлення замовлення',
        'form': form,
        'create_order_page': True,
        'order_exists': order_exists
    }

    return render(request, 'orders/create_order.html', context=context)