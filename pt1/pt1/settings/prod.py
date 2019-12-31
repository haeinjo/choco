###############################
# mysql 사용시 설치 필요
# pip install pymysql

#import pymysql

#pymysql.install_as_MySQLdb()
###############################

from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }



#####################################################
# mysql 설정
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'choco_db', # DB명
        'USER': 'choco', # 데이터베이스 계정
        'PASSWORD': 'ckdwltlf', # 계정 비밀번호
        'HOST': '127.0.0.1', # 데이테베이스 주소(IP)
        'PORT': '3306', # 데이터베이스 포트(보통은 3306)
    }
}
#####################################################
