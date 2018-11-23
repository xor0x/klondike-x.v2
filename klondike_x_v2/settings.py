import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y%01bq$sohu9tsfh1kfl$ovues*v5f9c!pw=y%1xq59_yjcj40'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Email Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'alex@gmail.com'
EMAIL_HOST_PASSWORD = '123456'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#Config for SiteMap
SITE_ID = 2

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# Recaptcha Config
RECAPTCHA_PRIVATE_KEY = '6LfhhXMUAAAVwZ29Hx87i'
RECAPTCHA_PUBLIC_KEY = '6LfhhXMUEhv8Eyrpa39uh1cSMNe'

# Admin Suit Config
SUIT_CONFIG = {
    'ADMIN_NAME': 'Klondike-X Admin',
    'CONFIRM_UNSAVED_CHANGES': True,
    'LIST_PER_PAGE': 20,
    'MENU_ICONS': {
        'blog': 'icon-pencil',
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'accounts': 'icon-user',
        'taggit': 'icon-tags',
    }
}

# Ckeditor Config
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 700,
    },
}

# Application definition
INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'taggit',
    'taggit_templatetags2',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    'ckeditor',
    'ckeditor_uploader',
    'snowpenguin.django.recaptcha2',
    'rosetta',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'klondike_x_v2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #os.path.join(BASE_DIR, 'templates')
            'klondike_x_v2/templates'
        ],
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

WSGI_APPLICATION = 'klondike_x_v2.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'klondike_x',
        'USER':'postgres',
        'PASSWORD':'123456',
        'HOST':'localhost',
        #'PORT':'5432',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
    ('he', _('Hebrew')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'klondike_x_v2/static/'),

]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

try:
    from .local_settings import *
except ImportError:
    pass
