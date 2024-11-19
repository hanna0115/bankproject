from allauth.account.adapter import DefaultAccountAdapter
from django.utils import timezone

class CustomAccountAdapter(DefaultAccountAdapter):
    """
    사용자 계정 관리를 위한 커스텀 어댑터
    - 실제 DB 저장 및 부가 기능 구현
    """
    def save_user(self, request, user, form, commit=True):
        """
        사용자 정보 저장 메서드
        - request: HTTP 요청 객체
        - user: 저장할 User 모델 인스턴스
        - form: 검증된 폼 데이터
        - commit: DB 저장 여부 (기본값: True)
        """
        # 기본 사용자 정보 저장 (DB 저장은 보류)
        user = super().save_user(request, user, form, False)
        # 검증된 폼 데이터 가져오기
        # data = request.cleaned_data
        
        # 추가 필드 데이터 저장
        user.name = request.data.get('name')
        user.birth_date = request.data.get('birth_date')
        user.asset = request.data.get('asset')
        user.saving_purpose = request.data.get('saving_purpose')
        user.saving_amount = request.data.get('saving_amount')
        user.saving_period = request.data.get('saving_period')
        
        # commit이 True인 경우에만 DB에 최종 저장
        if commit:
            user.save()
        return user
    

    def delete_user(self, request, user):
        """
        회원 탈퇴 처리를 위한 메서드
        
        Args:
            request: HTTP 요청 객체
            user: 탈퇴할 User 모델 인스턴스
        
        Returns:
            bool: 탈퇴 처리 성공 여부
        """
        try:
            # 1. 탈퇴 시간 기록
            withdrawal_time = timezone.now()
            
            # 2. 사용자 관련 데이터 처리
            self._handle_user_data(user, withdrawal_time)
            
            # 3. 사용자 계정 삭제
            user.delete()
            
            return True
            
        except Exception as e:
            # 로깅 추가
            print(f"회원 탈퇴 처리 중 오류 발생: {str(e)}")
            return False


    def _handle_user_data(self, user, withdrawal_time):
        """
        사용자 관련 데이터 처리
        - 게시글, 댓글, 좋아요 등 연관 데이터 처리
        """
        # 1. 게시글 처리
        if hasattr(user, 'posts'):
            user.posts.update(
                is_deleted=True,
                deleted_at=withdrawal_time,
                content="삭제된 게시글입니다.",
                author_name="탈퇴한 사용자"
            )
        
        # 2. 댓글 처리
        if hasattr(user, 'comments'):
            user.comments.update(
                is_deleted=True,
                deleted_at=withdrawal_time,
                content="삭제된 댓글입니다.",
                author_name="탈퇴한 사용자"
            )
        
        # 3. 팔로우 관계 제거
        user.followers.clear()
        user.followings.clear()