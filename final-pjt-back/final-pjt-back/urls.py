"""
URL configuration for final-pjt-back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bank_products/', include('bank_products.urls')),
    path('piggy_banks/', include('piggy_banks.urls')),
    path('exchange/', include('exchange.urls')),
    # authorization 사이트 링크
    # 1. 로그인, 로그아웃, 비밀번호 변경 등
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    # 2. 회원가입
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('posts/', include('posts.urls')),
]