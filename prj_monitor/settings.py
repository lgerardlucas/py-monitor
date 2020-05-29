import os
import psycopg2
from decouple import config
from dj_database_url import parse as dburl


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY',default='y)3gkd-@+0d^sn^iq7c5)bse)ex@a@_y^b4ozp$cn&c$@+qm41')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = config('DEBUG',default=False,cast=bool)

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app_monitor',
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

ROOT_URLCONF = 'prj_monitor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'prj_monitor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

''' DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
} '''

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE', default='django.db.backends.postgresql'),
        'NAME': config('NAME', default=''),
        'USER': config('ROLE', default=''),
        'PASSWORD': config('PASSWORD', default=''),
        'HOST': config('HOST', default=''),
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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



# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# Arquivos usados na renderização, exemplo: HTML
# STATICFILES_DIRS = Define os diretórios que serão vasculhados pelo FileSystemF$
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# STATIC_ROOT = Define o diretório onde serão armazenados os arquivos estáticos coletados
STATIC_ROOT = 'staticfiles'
# STATIC_URL = Define o prefixo de URL para referência aos arquivos estáticos. exemplo: { static }
STATIC_URL = '/static/'

# Arquivos usados pelo usuário, exemplo: uploads imagens
# MEDIA_ROOT = Define o diretório onde serão armazenados os arquivos de mídia (uploads).
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static/media/'))
# MEDIA_URL = Define o prefixo de URL para referência a arquivos de mídia (uploads).
MEDIA_URL = '/media/'

# Comando que faz um backup do arquivo .env renomeando para que o git o carregue consigo
# O conteúdo deste arquivo, deverá substituir o conteúdo do arquivo .env em outro computador
if os.path.isfile('.env'):
    os.system("cp -r -f .env .env.backup")


ADMINS = [('Marcos','lgerardlucas@gmail.com',)]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'lgerardlucas@gmail.com' 
EMAIL_HOST_PASSWORD = 'LbAm1971@mga'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SEND_EMAIL_SIS = config('SEND_EMAIL_SIS', default=True, cast=bool)
