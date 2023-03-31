"""
Django settings for payment_service_api project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-shc+x0rwi0b^ormesa+ucub-#^bfwx*t(b2b0#8fe$_s9@fwc!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'UserAuth.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payment.apps.PaymentConfig',
    'UserAuth.apps.UserAuthConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

ROOT_URLCONF = 'payment_service_api.urls'

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

WSGI_APPLICATION = 'payment_service_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # Limited permissions strictly for runtime operations
    # GRANT SELECT, INSERT, UPDATE, DELETE ON db_name.* 
    #     TO 'django_user'@'127.0.0.1' 
    #     IDENTIFIED BY 'XYZ***'; 

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'payment$payment', # 'payment',
        'USER': 'payment', # 'payment_user',
        'PASSWORD': '@Password', # 'password',
        'HOST': 'payment.mysql.pythonanywhere-services.com', # 'localhost',
        'PORT': '3306',
    },

    # Full permissions to allow migration operations as they require schema access 
    # Run migrations with command 'python manage.py migrate --database=default_with_migration_rights'
    # GRANT ALL ON db_name.* 
    #     TO 'django_migration_user'@'127.0.0.1' 
    #     IDENTIFIED BY 'XYZ***'; 

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'payment',
    #     'USER': 'root',
    #     'PASSWORD': 'toor',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = Path.joinpath(BASE_DIR, 'StaticRoot')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True

# from corsheaders.defaults import default_headers

# CORS_ALLOW_HEADERS = list(default_headers) + [
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'cache-control',
#     'x-sessionid',
#     'upgrade-insecure-requests',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# ]

# CORS_EXPOSE_HEADERS = [
#     'accept',
#     'Access-Control-Allow-Origin',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'set-cookie',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# ]

# CORS_PREFLIGHT_MAX_AGE = 0

# CSRF_TRUSTED_ORIGINS =  ['https://osamwelian3.github.io', 'https://osamwelian3.github.io/STKPushPaymentService/']

# SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

# Daraja Credentials
Consumer_Key = 'jGK5j8GFyRQ8JGdBszlz1W1LA6Snm053'
Consumer_Secret = '1LoqARyPTGBsjhkl'
BusinessShortCode = 174379
Passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
TransactionType = 'CustomerPayBillOnline'
PartyB = 174379
AccountReference = 'Sasakazi Assesment'
