# Generated by Django 4.2.7 on 2024-02-19 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0003_alter_products_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення замовлення')),
                ('first_name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=100, verbose_name='Прізвище')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефону')),
                ('requires_delivery', models.BooleanField(default=False, verbose_name='Спосіб доставки')),
                ('delivery_address', models.TextField(blank=True, null=True, verbose_name='Адреса доставки')),
                ('payment_on_get', models.BooleanField(default=False, verbose_name='Спосіб оплати')),
                ('status', models.CharField(default='В обробці', max_length=50, verbose_name='Статус замовлення')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Ціна')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кількість')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажу')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Замовлення')),
                ('product', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Проданий товар',
                'verbose_name_plural': 'Продані товари',
                'db_table': 'order_item',
            },
        ),
    ]