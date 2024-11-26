# bankproject

### 금융 상품 비교 애플리케이션

### 목차

1. [🙋 팀원 정보 및 업무 분담 내역](#팀원-정보-및-업무-분담-내역)
2. [📊 설계 내용 (아키텍처 등) 및 실제 구현 정도](#설계-내용-아키텍처-등-및-실제-구현-정도)
3. [📑 데이터베이스 모델링(ERD)](#데이터베이스-모델링erd)
4. [💻 금융 상품 추천 알고리즘에 대한 기술적 설명](#금융-상품-추천-알고리즘에-대한-기술적-설명)
5. [💁 서비스 대표 기능들에 대한 설명](#서비스-대표-기능들에-대한-설명)
6. [🙇 느낀 점, 후기 등](#느낀-점-후기-등)

## 팀원 정보 및 업무 분담 내역

- 프로젝트 기간 : 2023/11/18 ~ 2023/11/27 (약 9일)

| 이름          | 역할 및 구현 기능                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 김선명 (팀장) | Front End - figma, 회원가입, 로그인, 마이페이지, 홈, 금융 상품 비교, 환율 계산기, 주변 은행 검색, 게시판 CRUD, 상품 관리, 상품 추천           |
| 김진실        | Back End - ERD, 회원 커스터마이징, 환율 정보 저장 및 업데이트, 금융 상품 정렬 및 필터링, 금융 상품 회원 저장, 게시판 CRUD, 추천 알고리즘 1, 2 |

## 설계 내용 (아키텍처 등) 및 실제 구현 정도

### 🖥 기술 스택

**🌕 front**

- language
  - javascript
- framework
  - Vue3
  - pinia (+pinia-plugin-persistedstate)
  - axios
  - chart.js

**🌑 back**

- language
  - python
- framework
  - django
  - django-rest-framework
  - dj-rest-auth
  - pillow
  - drf-spectacular

### 🎨 Figma

[**🔗 Figma Link**](https://www.figma.com/design/OXOygfoSCSRhi6z9zKahw0/Untitled?node-id=0-1&t=PuoAi7xxlDJCYQou-1)

<img src="./README_IMG/Figma.png" alt='Figma'/>

- 예, 적금 금리 비교, 환율 계산, 집 주변 은행 검색, 금융 상품 연동하기, 게시판 등의 필수 기능, 셀렉트 박스를 통해 은행 검색 시 해당 은행의 로고 및 전화번호, 위치, 영업시간 정보 제공. 네이버 환율 그래프 카드 및 redirect, 회원가입 & 로그인 유효성 검사, 프로필 페이지 내 금융 상품 이자율 시각화 기능을 구현함.

## 데이터베이스 모델링(ERD)

[**🔗 ERD drawio Link**] (https://www.erdcloud.com/d/8sJNJCYCQqfZjF2sG)

<img src="./README_IMG/ERD.png" alt='Figma'/>

### 🗂️ API 명세서

<img src='./README_IMG/API_명세서.png' alt='API 명세서' />

## 금융 상품 추천 알고리즘에 대한 기술적 설명

### 추천 알고리즘 1️⃣.

**000명의 유저 더미데이터**를 생성하여 나와 저축 목표가 유사한 유저가 많이 가입한 상품을 추천해주는 알고리즘입니다.

여기서 나와 저축 목표가 유사한 유저란, 회원가입 시 설정한 8개의 목표가 유사한 유저를 말합니다.

만약 저축 목표가 유사한 유저가 없을 시, 저축 목표 달성에 유리한 상품 5개를 추천해줍니다.

### 추천 알고리즘 2️⃣.

유저로부터 저축 목표, 자산, 저축 기간, 저축 금액등의 데이터를 회원 가입 당시 입력 받습니다.

<!-- 희망 금액의 경우 그보다 비슷하거나 큰 최고 한도를 가진 금융상품 & 희망 기간의 경우 그 예치 기간을 가진 금융상품을 필터링하여 두 경우를 모두 만족하는 금융 상품 중 이자율이 높은 top20 금융 상품을 추천합니다. --> // 이 부분 수정

## 서비스 대표 기능들에 대한 설명

### 1️⃣ 메인 페이지

<img src='./README_IMG/메인페이지.png' alt='메인페이지'/>

- 금융 상품을 카드로 만들어 메인 페이지를 꾸몄습니다. 또한 페이지 전체에 Slider 애니메이션을 추가하였습니다. Slider가 되는 속도에 맞춰 금융 상품 정보를 담은 카드 또한
  회전 되며 보여지도록 했습니다.

### 2️⃣ 로그인, 회원가입 페이지

<img src='./README_IMG/로그인페이지.png' alt='로그인페이지'/>
<img src='./README_IMG/회원가입페이지.png' alt='회원가입페이지'/>

- 로그인 실패 시 에러메세지를 띄워 사용자로 하여금 아이디와 비밀번호를 다시 확인할 수 있오록 하였습니다.
- 회원가입 시 ID는 이메일 형식, 생년월일은 체크박스를 선택할 수 있도록 구현하였습니다. 또한 윤달, 홀수와 짝수 달의 최대 일 수를 다르게 하였습니다.
- 비밀번호는 8~16자의 영어 대소문자, 숫자, 특수문자로 이루어져 있는지게 하였고, 유저 경험을 향상시키기 위해 비밀번호 입력란 밑에 안내 문구를 작성하였습니다.

### 3️⃣ 마이페이지

<img src='./README_IMG/마이페이지.png' alt='마이페이지'/>
<img src='./README_IMG/가입상품관리페이지.png' alt='가입상품관리페이지'/>
<img src='./README_IMG/상품추천페이지1.png' alt='상품추천페이지1'/>
<img src='./README_IMG/상품추천페이지2.png' alt='상품추천페이지2'/>

- 마이페이지에서 내가 현재 가입한 금융 상품, 그리고 나의 저축 목표와 맞는 금융 상품을 추가적으로 추천 받을 수 있습니다.
- 내 정보 수정하기에서는 회원가입 시 등록했던 정보를 수정하여, 다양한 금융 상품을 추천 받을 수 있는 기회를 넓혔습니다. 예를 들어 저축 목표를 수정하였을 때,
  변경된 저축 목표에 맞추어 금융 상품이 추천 됩니다.
- 비밀번호 변경의 경우, 버튼을 눌렀을 때만 창이 생성되는 기능을 구현하였고, 원하는 내용만 수정할 수 있도록 하였습니다. 이름이나 email, 생년월일 등
  유저를 식별하는 데 필요한 필수적인 정보는 고정된 값만 보여줌으로써, 데이터베이스에 대한 안전성을 높였습니다.

### 4️⃣ 금융 상품 상세 페이지

<img src='./README_IMG/정기예금페이지.png' alt='정기예금페이지'/>
<img src='./README_IMG/정기적금페이지.png' alt='정기적금페이지'/>
<img src='./README_IMG/예,적금상세페이지.png' alt='예,적금상세페이지'/>

- 추천된 금융 상품을 클릭함으로써 상품에 대한 상세 정보를 확인할 수 있습니다.
- 공식홈에서 더 알아보기 기능을 통해 해당 금융 상품 페이지로 이동할 수 있도록 했습니다. (이거 됨?????????????????????????????????????? 안되면 지워)

### 5️⃣ 환율 계산 페이지

<img src='./README_IMG/환율계산페이지.png' alt='환율계산페이지'/>

- 환율 계산 페이지에서는 바인딩을 통해 국가를 선택하고, 금액을 입력하면 원화로 변경된 값을 실시간으로 확인할 수 있도록 구현했습니다.
- 각 국가별 환율 변동 차트를 시각화 하여 제공하여 유저의 편의성을 높였습니다.

### 6️⃣ 주변 은행 검색 페이지

<img src='./README_IMG/주변은행검색페이지.png' alt='주변은행검색페이지'/>
<img src='./README_IMG/주변은행검색상세페이지.png' alt='주변은행검색상세페이지'/>

- 주변 은행 검색 페이지에서는 직접 광역시/도, 시/군/구를 선택하여 장소를 지정할 수도 있습니다. 이 후 범위내 위치한 은행의
  상세정보(지점명, 전화번호, 영업시간)를 함께 확인할 수 있습니다.
- 우측 리스트에 나열된 은행을 클릭하면 지도의 출력 범위가 자동으로 확대되어 정확한 위치를 보다 쉽게 확인할 수 있도록 하였습니다.

### 6️⃣ 금융 상품 자유 게시판

<img src='./README_IMG/게시판목록페이지.png' alt='게시판목록페이지'/>
<img src='./README_IMG/게시판글쓰기페이지.png' alt='게시판글쓰기페이지'/>
<img src='./README_IMG/게시판상세페이지.png' alt='게시판상세페이지'/>
<img src='./README_IMG/게시판댓글수정페이지.png' alt='게시판댓글수정페이지'/>
<img src='./README_IMG/게시판수정페이지.png' alt='게시판수정페이지'/>
<img src='./README_IMG/게시판삭제페이지.png' alt='게시판삭제페이지'/>

- 인증된 사용자들(로그인 된) 사용자들끼리 커뮤니티를 형성할 수 있도록 금융 상품 자유 게시판을 제공합니다. (비로그인 회원은 조회만 가능합니다.)
- 기본적인 게시물 CRUD와 댓글 CRUD를 제공합니다.
- 게시글 목록을 확인하기 위해 뒤로가기 버튼을 눌러야 하는 것이 아닌, 게시글의 리스트와 게시글 상세 페이지를 동시에 보여줌으로써 편의성을 높였습니다.
- 하트 아이콘으로 표현된 좋아요 기능을 추가하였습니다. 클릭시 하트가 확대되는 애니메이션을 구현하였습니다. // (이거 돼?????????????????????????????????????????????)

### 7️⃣ 404 Not Found 페이지

<img src='./README_IMG/404페이지.png' alt='404페이지'/>

- 사용자가 잘못된 url로 이동할 때 404페이지로 redirect하여 홈으로 돌아갈 수 있게 안내해줍니다.

## 느낀 점, 후기 등

- 김선명 : 백엔드를 맡아준 팀원이 성실한 자세로 프로젝트에 임해준 덕분에 계획 했던 UI/UX를 만족스럽게 구현할 수 있었습니다.
  그에 비해 저는 부족한 모습을 보여 미안하고, 고생 많았다는 말을 전하고 싶습니다. 굉장히 즐겁고, 의미있는 시간이었습니다.
  관통 프로젝트를 진행하면서 Vanila Javascript에 대한 지식이 부족하다는 것을 많이 느꼈습니다.
  부족한 부분은 추후 토이프로젝트를 꾸준히 진행하며 보충할 계획입니다.

- 송찬의 : 어렵게 생각했으니 어렵지 않았고 쉽게 생각했으나 쉽지 않았습니다.
  배운것이어도 정리가 되어있지 않았고, 많이 부족함을 느꼈었던 것 같습니다.
  같이하는 팀원에게도 항상 미안한 마음이 들었고 더 잘하고 싶은마음도 동시에 들었던 것 같습니다.
  2학기에도 많은 시간을 들여 프로젝트를 하게 될 것인데 그때도 이런마음이 들어서는 안되기 때문에
  2학기 시작하기 전까지의 시간을 잘보내야겠다고 다짐하게 되었습니다.