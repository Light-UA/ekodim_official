from django.db import models
from django.contrib.auth.models import AbstractUser


class User( AbstractUser ):
    email = models.EmailField( blank=True, null=True )

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
