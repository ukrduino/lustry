# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ya_bu6+ax-214ei4b2r!hg0s37c_q5r)fzdfb9@t6w%!9d48=2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'bootstrapform',  # суперски бутстрапит стандартные формы django
    'south',
    'captcha',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lustry.urls'

WSGI_APPLICATION = 'lustry.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

from .settings_db import DATABASES

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Kiev'  # я с Украины, драсьте

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


#  доступ к сессии из шаблона
TEMPLATE_CONTEXT_PROCESSORS = (  # http://stackoverflow.com/questions/2551933/
                                 # django-accessing-session-variables-from-within-a-template
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth'
)
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Alex.Vlasov.ukr@gmail.com'
EMAIL_HOST_PASSWORD = 'sasha7777'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "Alex.Vlasov.ukr@gmail.com"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#CAPTCHA_FONT_SIZE ='30'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_LETTER_ROTATION = (-5, 5)
CAPTCHA_BACKGROUND_COLOR = 'white'
CAPTCHA_FOREGROUND_COLOR = '#000'
CAPTCHA_NOISE_FUNCTIONS = ()
