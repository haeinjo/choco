from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



#####################################################
# mysql 설정
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django_locker', # DB명
#         'USER': '', # 데이터베이스 계정
#         'PASSWORD': '', # 계정 비밀번호
#         'HOST': '', # 데이테베이스 주소(IP)
#         'PORT': '', # 데이터베이스 포트(보통은 3306)
#     }
# }
#####################################################