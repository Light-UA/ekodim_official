from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = ("product", "price", "quantity")
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price", "quantity")


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "created_timestamp",
    )

    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "created_timestamp",
    )

    readonly_fields = ("created_timestamp",)
    inlines = (OrderItemTabulareAdmin,)
