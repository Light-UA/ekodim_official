# from pathlib import Path
#
# BASE_DIR = Path( __file__ ).resolve().parent.parent
#
#
# SECRET_KEY = 'djfofoejfnfnnefem934483948mcnd4ango-inselffeklfenrkkercure-&(z--.0um32m0bbw9-kd7j0hdi44n8_rj%ahf*dv30@&6*t!@kaqly&n$-'
#
#
# DEBUG = True
#
# ALLOWED_HOSTS = [127.0.0.1]
#
# STATICFILES_DIRS = [
#     BASE_DIR / 'static'
# ]

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'djfofoejfnfnnefem934483948mcnd4ango-inselffeklfenrkkercure-&(z--.0um32m0bbw9-kd7j0hdi44n8_rj%ahf*dv30hlidsvjklslkjsdvnlsvdjl0987397878390737300u....87373iefhfeifhoeofhie@&6*t!@kaqly&n$-'

DEBUG = False  # Встановлення DEBUG на False для продукційного середовища

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Додано 'localhost' до ALLOWED_HOSTS для дозволу з'єднань з 127.0.0.1 та localhost

STATIC_ROOT = BASE_DIR / 'static'  # STATIC_ROOT для збору статичних файлів у продакшені
STATICFILES_DIRS = []  # Очищено STATICFILES_DIRS, оскільки воно зазвичай не використовується у продакшені і замінено на STATIC_ROOT


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shopDB',
        'USER': 'shopDB_Owner',
        'PASSWORD': 'Q1234Zxcpol',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}