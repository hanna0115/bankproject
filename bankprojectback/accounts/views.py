from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import User
from .adapters import CustomAccountAdapter
from .serializers import CustomRegisterSerializer, CustomUserDetailsSerializer


# 회원가입
@api_view(['POST'])
def register_user(request):
    """
    회원가입 API 뷰
    - CustomRegisterSerializer를 통한 데이터 검증
    - CustomAccountAdapter를 통한 사용자 저장
    """
    # 요청 데이터 유효성 검사
    serializer = CustomRegisterSerializer(data=request.data)
    if serializer.is_valid():
        # CustomAccountAdapter를 통한 사용자 저장
        adapter = CustomAccountAdapter()
        user = adapter.save_user(request, serializer.user, serializer)
        return Response({
            'message': '회원가입이 완료되었습니다.',
            'user': serializer.data
        })

# 프로필 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request, user_pk):
    try:
        user = get_object_or_404(User, pk=user_pk)
        serializer = CustomUserDetailsSerializer(user)
        
        # serializer.data를 기반으로 추가 데이터 포함
        data = serializer.data
        data.update({
            'followers_count': user.followers.count(),
            'followings_count': user.followings.count(),
            'is_following': request.user.followings.filter(pk=user.pk).exists()
        })
        
        return Response(data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# 프로필 수정
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    """
    프로필 수정 API 뷰
    - 단순 정보 수정은 serializer.save() 사용
    """
    # 부분 업데이트를 위한 partial=True 설정
    serializer = CustomUserDetailsSerializer(
        request.user,
        data=request.data,
        partial=True    # 일부 필드만 업데이트 가능
    )
    if serializer.is_valid():
        # 단순 정보 수정은 save() 메서드로 충분
        user = serializer.save()
        return Response({
            'message': '프로필이 수정되었습니다.',
            'user': serializer.data
        })
    
# views.py
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_account(request):
    """
    회원탈퇴 API 뷰
    - Adapter를 통한 복잡한 탈퇴 처리 로직 실행
    """
    # CustomAccountAdapter 인스턴스 생성
    adapter = CustomAccountAdapter()
    # 탈퇴 처리 실행
    result = adapter.delete_user(request, request.user)
    
    if result:
        return Response({'message': '탈퇴가 완료되었습니다.'})
    return Response(
        {'error': '탈퇴 처리 중 오류가 발생했습니다.'}, 
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, following_user_pk):
    following_user = get_object_or_404(User, pk=following_user_pk)
    follower = request.user

    # 자기 자신을 팔로우하려는 경우 방지
    if follower == following_user:
        return Response(
            {'detail': '자기 자신을 팔로우할 수 없습니다.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    # 이미 팔로우한 경우 -> 언팔로우
    if follower.followings.filter(pk=following_user_pk).exists():
        follower.followings.remove(following_user)
        is_followed = False
    # 팔로우하지 않은 경우 -> 팔로우
    else:
        follower.followings.add(following_user)
        is_followed = True

    serializer = CustomUserDetailsSerializer(following_user)
    
    return Response({
        'is_followed': is_followed,
        'follower_count': following_user.followers.count(),
        'following_count': following_user.followings.count(),
        'user': serializer.data
    })