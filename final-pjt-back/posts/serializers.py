from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model



# 전체 게시글 조회
class PostListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('name', 'id',)
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'created_at', 'num_seen', 'category')
        read_only_fields = ('user',)



# 게시글 생성, 수정
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'like_users', 'save_users')



# 단일 게시글 조회
class PostDetailSerializer(serializers.ModelSerializer):

    class CommentListSerializer(serializers.ModelSerializer):
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('name', 'id',)
        
        user = UserSerializer(read_only=True)
        
        class Meta:
            model = Comment
            fields = ('id', 'content', 'user',)
            read_only = ('user',)
    
    
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    save_count = serializers.IntegerField(source='save_users.count', read_only=True)
    comment_set = CommentListSerializer(many=True, read_only=True)
    name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user',)



# 댓글 생성
class CommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'post')