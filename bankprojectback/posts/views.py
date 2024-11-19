from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import F

from .models import Post, Comment
from .serializers import PostListSerializer, PostSerializer, PostDetailSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def post_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        # 조회수 기준으로 내림차순
        posts = Post.objects.all().order_by('-num_seen')
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    # 게시글 작성
    elif request.method == 'POST':
        # 로그인 되지 않았을 경우에는 게시글 작성 권한 없음
        if not request.user.is_authenticated:
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 단일 게시글 조회
    if request.method == 'GET':
        # F 객체를 이용하면 추가적인 데이터베이스 읽기 작업 없이 값이 바로 증가
        post.num_seen = F('num_seen') + 1
        post.save(update_fields=['num_seen'])
        post.refresh_from_db()  # F() 사용 후 최신 데이터를 가져오기
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
    
    if post.user == request.user:
        # 게시글 수정
        if request.method == 'PUT':
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)

        # 게시글 삭제
        elif request.method == 'DELETE':
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    # 게시글을 작성한 유저가 아닐 경우
    else:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def like_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 좋아요 취소
    if post.like_users.filter(user=request.user).exists():
        post.like_users.remove(request.user)
    # 좋아요
    else:
        post.like_users.add(request.user)

    serializer = PostDetailSerializer(post)
    return Response(serializer.data)



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def save_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 저장 취소
    if post.save_users.filter(user=request.user).exists():
        post.save_users.remove(request.user)
    # 저장
    else:
        post.save_users.add(request.user)

    serializer = PostDetailSerializer(post)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # 댓글 생성
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if comment.user == request.user:
        # 댓글 삭제
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 댓글을 작성한 유저가 아닐 경우
    else:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)