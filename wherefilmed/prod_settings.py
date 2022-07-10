import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ('django-insecure-!6%ic*pkkdkeu#-#8g3i0l2$mq$6an*)y6f-+l$823zq#5z3c7a+wo')


DEBUG = False

ALLOWED_HOSTS = ['']
#ALLOWED_HOSTS = ['https://wherefilmed.org/']

STATICFILES_DIRS = [
    BASE_DIR / "static",
 
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wherefilmed',
        'USER': 'ugrobug',
        'PASSWORD': 'Mkm695nbv45fa8phg',
        'HOST': 'wherefilmed_db',
        'PORT': '5432'
    }
}