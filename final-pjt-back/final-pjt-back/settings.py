"""
Django settings for final-pjt-back project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$ercoli9le@$+b4oe0b_&641r-fgopcq8#*-x_$1dq1gq3th22'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 커스텀앱
    'posts',
    'bank_products',
    'piggy_banks',
    'accounts',
    'exchange',
    # DRF
    'rest_framework',
    'rest_framework.authtoken',
    # cors
    'corsheaders',
    # rest_authorization
    'dj_rest_auth',
    'allauth',
    'allauth.account',

    # social login 필요 시 추가
    'django.contrib.sites',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    # django 내장 앱
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# social login 필요 시 추가
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # cors
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # authorization
    'allauth.account.middleware.AccountMiddleware',
]

# cors 사이트 등록
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5174',
    'http://localhost:5174',
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]


REST_FRAMEWORK = {
    # DRF Authentication : token 인증 사용 설정
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# User 모델 커스텀
AUTH_USER_MODEL = 'accounts.User'

# 이메일 인증 관련 설정
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # 이메일 인증 비활성화

# 비밀번호 유효성 검사 설정
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# dj-rest-auth 설정
# 1. 회원가입 시 사용할 Serializer 지정
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}

# 2. 사용자 정보 조회 및 수정 시 사용할 Serializer 지정
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.CustomUserDetailsSerializer',
}

# 3. allauth 설정 : 회원가입 시 사용자 저장 로직을 커스터마이징
ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'


# Django 환경변수 관리
BASE_DIR = Path(__file__).resolve().parent.parent

import os
import environ

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

EXCHANGE_API_KEY = env('EXCHANGE_API_KEY')



ROOT_URLCONF = 'final-pjt-back.urls'

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

WSGI_APPLICATION = 'final-pjt-back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
'default' : {
                'ENGINE' : 'django.db.backends.mysql', # 벡엔드 엔진
                'NAME' : 'bank_project', # 'mysql'의 이름을 가진 데이터베이스
                'USER' : 'root', # 계정
                'PASSWORD' : '961226', #rootpassword로 지정할 숫자(6번에 나와있음)
                'HOST' : '127.0.0.1',
                'PORT' : '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
