from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'djfofoejfnfnnefem934483948mcnd4ango-inselffeklfenrkkercure-&(z--.0um32m0bbw9-kd7j0hdi44n8_rj%ahf*dv30hlidsvjklslkjsdvnlsvdjl0987397878390737300u....87373iefhfeifhoeofhie@&6*t!@kaqly&n$-'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

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

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
