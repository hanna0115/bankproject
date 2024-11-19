from django.urls import path
from . import views


urlpatterns = [
    # 게시글 조회, 생성
    path('', views.post_list),
    # 단일 게시글 조회, 수정, 삭제
    path('detail/<int:post_pk>/', views.post_detail),
    # 게시글 좋아요
    path('like_post/<int:post_pk>/', views.like_post),
    # 게시글 저장
    path('save_post/<int:post_pk>/', views.save_post),
    # 댓글 생성
    path('<int:post_pk>/comments/', views.create_comment),
    # 댓글 삭제
    path('delete_comment/<int:comment_pk>/', views.delete_comment),
]
