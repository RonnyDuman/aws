

from pathlib import Path
import os
import pymysql
pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-x_u4q(q(uo7jcd_d*6!*ofa$3=tsya6ts#$8rm(26e)ccqz^kx'

DEBUG = True

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Aplicaciones.usuarios',
    'Aplicaciones.categorias',
    'Aplicaciones.productos',
    'Aplicaciones.carrito',
    'Aplicaciones.carritoproductos',
    'Aplicaciones.pedidos',
    'Aplicaciones.pedidoproductos',
    'Aplicaciones.pagos',
    'Aplicaciones.reseñas',
    'Aplicaciones.descuentos',
    'Aplicaciones.core',

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

ROOT_URLCONF = 'proyectoFinal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Aplicaciones.carrito.context_processors.carrito_context',
                'Aplicaciones.carrito.context_processors.carrito_total_items',
                'Aplicaciones.categorias.context_processors.categorias_disponibles',

            ],
        },
    },
]

WSGI_APPLICATION = 'proyectoFinal.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mainDB',    
        'USER': 'root',                   
        'PASSWORD': 'admin',  
        'HOST': 'MYSQLPHP',              
        'PORT': '3306',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


LOGIN_URL = '/usuarios/login/'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



STATIC_URL = 'static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Aplicaciones/static"), 
]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dumankevin70@gmail.com'
EMAIL_HOST_PASSWORD = 'ygce hxkt lirj tjjh'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
