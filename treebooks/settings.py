"""
Django settings for treebooks project.

Generated by 'django-admin startproject' using Django 1.11.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

#dj_database_url allow us to connect to a database URL
import dj_database_url

'''
My mentor Guido advise me to use the code below in order to import
the env file in development but not in production
'''
try:
    import env
except ImportError:
    pass
    

ENVIRONMENT = os.environ.get('ENVIRONMENT')

if ENVIRONMENT=='DEV':
    development = True
else:
    development = False


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

# will be True in development and False in production
DEBUG = development

# We need to add to allowed host the link to the app in Heroku
ALLOWED_HOSTS = ['127.0.0.1', 'treebooksproject.herokuapp.com']


# Application definition
'''
All the apps in the project are included in INSTALLED_APPS
And I've also included the following:
django_extensions - in order to use graph_models to create the db schema
storages - in  order to use AWS S3 to host the media and static files
django_forms_bootstrap - in order to apply bootstrap styles to the forms
django_template_check - in order to check for basic syntax errors in templates 
https://pypi.org/project/django-template-check/
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'home',
    'userprofile',
    'books',
    'cart',
    'search',
    'django_forms_bootstrap',
    'checkout',
    'favourites',
    'reviews',
    'waiting_list',
    'django_extensions',
    'storages',
    'django_template_check',
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

ROOT_URLCONF = 'treebooks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Specify that all the folders called 'templates' contain templates
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # context_processors are availables everywhere in the website
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # we add the media context processor because 
                # we are going to have media(images) in the project
                'django.template.context_processors.media',
                # we add the context that we have created in context.py(cart app)
                'cart.context.cart_content',
            ],
        },
    },
]

WSGI_APPLICATION = 'treebooks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


# in development
if development==True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
# in production
else:
    if "DATABASE_URL" in os.environ:
        # production database (Postgress)
        DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        print('Database URL not found. Using SQLite instead')
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

'''
Syntax needed in order to be able to sign in using 
the email address instead of using the username
'''
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# in development we keep the files locally
if development==True:

    # we need a static root. All static files will be in the static directory
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # we need a media root. All media will be in the media directory
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# in production we use AWS S3 to host the media and static files
else:
    # variables and keys needed in order to set up the connection with AWS S3
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000'
    }

    AWS_STORAGE_BUCKET_NAME = 'tree-books'
    AWS_S3_REGION_NAME  = 'eu-west-3'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    

# These are the variables needed to use Stripe to take payments
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')


#These are the variables needed to send email to reset the password
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_ADDRESS")
SERVER_EMAIL = os.environ.get("EMAIL_ADDRESS")

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

'''
In order to tell django that there is an extension of the User model
I followed the steps in the following tutorial
https://www.youtube.com/watch?v=qLRxkStiaUg '''

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

'''
GRAPH_MODELS is needed in order to create the data base schemas
tutorial -> https://django-extensions.readthedocs.io/en/latest/graph_models.html
tool to conver from .dot file to png -> https://dreampuf.github.io/GraphvizOnline/

'''
GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}