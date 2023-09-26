from mysite.settings import *

SECRET_KEY = 'django-insecure-1=8a&&vnc8m#p_gse(obkx)r6)dub2ps3c_8hk+t3!v(_o6_-f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

SITE_ID = 2


#Robot cnfigurations:
ROBOTS = {
    "User-agent": "*",
    "Disallow": ["/private/", "/admin/","http://kasratorabi.com/admin"],
    "Allow": ["/public/"],
    "Crawl-delay": 5,
}


INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website.apps.WebsiteConfig',
    'captcha',
    'django.contrib.sites',
    'robots',
]



# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#email server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'websiteback741@gmail.com'
EMAIL_HOST_PASSWORD = 'wglfhppkzljalikj'

