from django.urls import path
from . import views


urlpatterns = [
    # 환율 조회
    path('', views.chatbot),
]
