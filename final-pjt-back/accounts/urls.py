from django.urls import path
from . import views

urlpatterns = [
    # 회원가입 URL
    path('register/', views.register_user),
    # 다른 사용자 프로필 조회
    path('profile/<int:user_pk>/', views.user_profile),
    # 프로필 수정 URL
    path('profile/update/', views.update_profile),
    # 회원탈퇴 URL
    path('profile/delete/', views.delete_account),
    path('follow/<int:following_user_pk>/', views.follow),
]