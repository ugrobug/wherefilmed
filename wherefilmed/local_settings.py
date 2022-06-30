import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-!6%ic*peu#-#8g3i0l2$mq$6an*)y6f-+l$823zq#5z3c7a+wo')


DEBUG = bool(os.environ.get('DJANGO_DEBUG', True) )

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wherefilmed',
        'USER': 'ugrobug',
        'PASSWORD': 'Mkm695nbv45fa8phg',
        'HOST': 'localhost'
        
    }
}



