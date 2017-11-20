import os, django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'n9aiw95@vu^^6^6$z(@tqd=12d90(e96kc@c$ch!2-5(91b4q5'
DEBUG = True
ALLOWED_HOSTS = [
 '10.10.1.58',
 'localhost:8081',
 'localhost:8082',
 'localhost',  
]

PROJECT_APPS = [
    'widget_tweaks',
    'member',
    'orm',
    'login',
    'library',
]

REQUIRED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = REQUIRED_APPS + PROJECT_APPS

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

from app.config.auth import *
from app.config.database import *
from app.config.international import *
from app.config.static import *
django.setup()
from app.config.template import * 
