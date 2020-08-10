Flask Tutorial(private)
=============
![flask](https://media.vlpt.us/images/rimu/post/f8cf75a6-a80e-41ed-bab6-96a7e29374a9/flask.png)
# - 순서
## 0. [들어가기 앞서](#들어가기-앞서)
## 1. [플라스크 기초](#플라스크-기초)
 - [어플리케이션 팩토리](#어플리케이션-팩토리)
 - [블루프린트](#블루프린트)
 - [모델](#모델)
 - [조회와 템플릿](#조회와-템플릿)
 - [데이터 저장](#데이터-저장)
 - [스태틱](#스태틱)
 - [부트스트랩](#부트스트랩)
 - [템플릿 상속](#템플릿-상속)
 - [폼](#폼)
## 2. [플라스크 심화](#플라스크-심화)
 - [네비게이션 바](#네비게이션-바)
 - [페이징](#페이징)
 - [템플릿 필터](#템플릿-필터)
 - [게시물 번호](#게시물-번호)
 - [답변 갯수 표시](#답변-갯수-표시)
 - [계정 생성](#계정-생성)
 - [로그인 & 로그 아웃](#로그인-&-로그-아웃)
 - [모델 변경](#모델-변경)
 - [글쓴이 표시](#글쓴이-표시)
 - [수정과 삭제](#수정과-삭제)
 - [댓글](#댓글)
 - [추천](#추천)
 - [앵커](#앵커)
 - [마크다운](#마크다운)
 - [검색과 정렬](#검색과-정렬)
 - [파이보의 추가기능](#파이보의-추가기능)
## 3. [플라스크 서비스](#플라스크-서비스)
 - [깃](#깃)
 - [깃허브](#깃허브)
 - [서버](#서버)
 - [AWS Lightsail](#AWS-Lightsail)
 - [파이보 오픈](#파이보-오픈)
 - [config 분리](#config-분리)
 - [터미널 접속](#터미널-접속)
 - [WSGI](#WSGI)
 - [Gunicorn](#Gunicorn)
 - [Nginx](#Nginx)
 - [production](#production)
 - [오류페이지](#오류페이지)
 - [로깅](#로깅)
 - [도메인](#도메인)
 - [PostgreSQL](#PostgreSQL)






# 들어가기 앞서
## 가상환경 설정
다른 환경 개발을 한 컴퓨터에서 관리해야 한다고 할때 사용
venvs라는 폴더 하나를 만들고 그곳에 가상환경들을 관리
```linux
python -m venv myproject
cd .\myproject\Scripts
activate
```
 후에 가상환경이 활성화 된 것을 볼수 있음
 ## 플라스크 설치
 가상환경에 들어가서 flask 설치(반드시)
 ```
 (myproject) C:\venvs\myproject\Scripts>pip install Flask
 ```
 ## pip upgrade
 ```
 (myproject) C:\venvs\myproject\Scripts>python -m pip install --upgrade pip
 ```
## 프로젝트
플라스크는 하나의 프로젝트가 곧 하나의 웹사이트이다.
한 프로젝트에는 여러 앱이 존재할 수 있다.
myproject 폴더를 만들자.
```
mkdir myproject
```

그리고 프로젝트 실행시 가상환경 자동화를 위해 venvs 폴더 아래 배치파일을 생성해야한다. echo off는 명령어들이 자동실행시 커맨드에 뜨지 않게 하는 옵션이다.
```
@echo off
@cd c:/projects/myproject
@c:/venvs/myproject/scripts/activate
```
그리고 venvs 폴더를 시스템 환경변수에 써 놓으면 어디서든 가상환경 활성화를 배치파일을 통해 실행 가능하다.
```
c:/>myproject
```

 visualcode를 쓰고 있을시 배치파일이 사용자 권한으로 인해 문제가 생기는 것 같다. cmd를 이용하도록 하자.

 - 추가
    - flask run을 돌리기 위해서는 FLASK_APP 변수 값을 모듈 이름으로 지정해 주거나 모듈이름을 app.py로 해야 한다)
        ```
        set FLASK_APP=pydo
        ```
    - FLASK_ENV
        디버그를 웹사이트로 보기 위해서는 env를 development로 변경해야 한다.
        ```
        set FLASK_ENV=development
        ```
    - 단 이러한 환경 변수 설정은 일시적인 것이라 매번 가상환경을 활성화 할때마다 초기화를 해주어야 한다. 이를 방지하기 위해 해당 명령들을 배치파일에 적어놓으면 좋다.

# 플라스크 기초
## 프로젝트 구조
플라스크는 장고와 같이 프로젝트 구조가 정해져 있지 않다. 그러므로 우리가 스스로 프로젝트 구조를 다음과 같이 구상해볼 필요가 있다.
```
c:/projects/myproject
├── pybo/
│      ├─ __init__.py
│      ├─ models.py
│      ├─ forms.py
│      ├─ views/
│      │   └─ main_views.py
│      ├─ static/
│      │   └─ style.css
│      └─ templates/
│            └─ index.html
└── config.py
```
### pybo 패키지
먼저 pybo.py앱은 pybo 패키지로 변경할 수 있다. pybo 디렉터리의 __init__.py가 pybo.py의 역할을 수행할 수 있다.
- models.py
    - 파이보 프로젝트는 ORM을 지원하는 파이썬 데이터베이스 툴킷인 SQLAlchemy를 사용할 것이다. SQLAlchemy는 모델기반으로 데이터베이스를 처리하기 때문에 모델 클래스들을 정의하는 models.py 파일이 필요하다.

- forms.py
    - 파이보 프로젝트는 브라우저에서 서버로 전송된 폼을 처리하기 위해서 WTForms라는 라이브러리를 사용할 것이다. WTForms 역시 모델기반으로 폼을 처리하기 때문에 폼 클래스들을 정의하는 forms.py 파일이 필요하다.

- views folder
    - pybo.py 파일에 등록되어 있던 hello_pybo와 같은 함수를 뷰(views) 디렉터리를 생성하여 그 하위에 기능별로 저장하도록 하자. 파이보 프로젝트는 만들어야 할 뷰 함수가 상당히 많기 때문에 기능별로 분리하여 main_views.py, question_views.py, answer_views.py, ... 등의 뷰 파일들을 계속 만들어 갈 것이다.

- static folder
    - 스태틱(static) 디렉터리는 파이보 프로젝트의 스타일시트(*.css), 자바스크립트(*.js) 그리고 이미지파일(*.jpg, *.png)등을 저장하는 디렉터리로 사용할 것이다.

- templates folder
    - 템플릿(templates) 디렉터리는 파이보의 질문목록, 질문상세등의 HTML 파일을 저장하는 디렉터리이다. 위에 구조에는 index.html 파일만 있지만 프로젝트가 진행되면 question_list.html, question_detail.html 등의 템플릿 파일들이 계속 추가될 것이다.

- config.py
    - config.py 파일은 파이보 프로젝트의 환경변수등을 저장하는 파일이다. 데이터베이스 환경등에 대한 설정을 이 파일에 저장할 것이다.
## 어플리케이션 팩토리
## 블루 프린트
## 모델
## 조회와 템플릿
## 데이터 저장
## 스태틱
## 부트스트랩
## 템플릿 상속
## 폼
 # 플라스크 심화
## 네비게이션 바
## 페이징
## 템플릿 필터
## 게시물 번호
## 답변 갯수 표시
## 계정 생성
## 로그인 & 로그 아웃
## 모델 변경
## 글쓴이 표시
## 수정과 삭제
## 댓글
## 추천
## 앵커
## 마크다운
## 검색과 정렬
## 파이보의 추가기능
 # 플라스크 서비스
## 깃
## 깃허브
## 서버
## AWS Lightsail
## 파이보 오픈
## config 분리
## 터미널 접속
## WSGI
## Gunicorn
## Nginx
## production
## 오류페이지
## 로깅
## 도메인
## PostgreSQL
 [참고 : 점프 투 플라스크](https://wikidocs.net/book/4542)

