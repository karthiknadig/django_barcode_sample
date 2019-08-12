import os.path

DEBUG = True,
SECRET_KEY = '2=eo07b8owkvhw6-5)w$vbh8v&a-(!94=o*6#0-qh!h1cs3qc2'
#ALLOWED_HOSTS = [u'karthiknadig.pythonanywhere.com']
ROOT_URLCONF = 'pybarc.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates') + os.path.sep
        ]
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
#MEDIA_ROOT = u'/home/karthiknadig/barcode/media'
#MEDIA_URL = '/media/'
#STATIC_ROOT = u'/home/karthiknadig/barcode/static'
#STATIC_URL = '/static/'
