from django.contrib import admin

from carts.admin import CartTabAdmin
from users.models import User


@admin.register( User )
class UserAdmin( admin.ModelAdmin ):
    list_display = ('username', 'first_name', 'last_name',)
    search_fields = ('username', 'first_name', 'last_name')

    inlines = [CartTabAdmin]
