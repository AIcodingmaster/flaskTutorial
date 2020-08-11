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
- vscode에서 가상환경 실행시 powershell을 기본 terminal로 할경우 권한 오류 즉 가상환경이 실행되지 않는다. 이때 git bash 또는 cmd로 바꾸어준다.

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
myproject 하위에 pybo 디렉터리를 생성하고 pybo.py파일을 pybo 디렉터리 하위에 __init__.py 라는 파일명으로 변경후 이동하였다. 그리고 플라스크 실행시 로컬서버가 잘 실행되는 것을 볼 수 있다. 그 이유는  FLASK_APP=pybo는 pybo 패키지를 가리키는 것이기 때문이다.(파일 이름 x)
## 블루 프린트
@app.route들이 많아지면 한곳에 이 모든 경로들을 쓰는 것은 상당히 불편하고 어렵다. 블루프린트를 이용해 구조적으로(분리)관리해보자.

먼저 pybo/__init__.py파일의 hello_pybo함수에 블루 프린트를 적용해보자.
views 디렉토리를 pybo 하위에 생성 후 view 하위에 main_views.py를 만든다. 그리고 아래와 같이 적는다.

```python
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')#bp 객체
#blueprint는 이름, 모듈명, url prefix값을 입력으로 객체를 생성함.
#main이라는 이름은 나중에 함수명으로 url을 찾아내는 url_for함수에서 사용된다.
#url prefix는 url 앞에 항상 붙게 되는 프리픽스 url을 말한다. 만약 url_prefix='/'대신 url_prefix='/main' 이라면 http://localhost:5000/ 대신 http://localhost:5000/main/ 로 호출해야 한다.

@bp.route('/')
def hello_pybo():
    return 'Hello, Pybo!'
```
그리고 __init__.py를 수정하자
```python
from flask import Flask


def create_app():
    app = Flask(__name__)

    # ---------------------------------------- [edit] ---------------------------------------- #
    from .views import main_views
    app.register_blueprint(main_views.bp)
    # ---------------------------------------- [edit] ---------------------------------------- #    

    return app
```
 파일에서 생성한 블루프린트객체 bp를 app에 등록을 해준다.

 다시 main_views.py를 수정해보자
 ```python
 from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

# ---------------------------------------- [edit] ---------------------------------------- #
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo index'
# ---------------------------------------- [edit] ---------------------------------------- #     
 ```
블루 프린트에 대한 더 자세한 내용은 프로젝트를 진행하며 알아가보자(지금은 app 라우터들을 다른 파일로 확장하는 용도로 이해)

## 모델
우리가 만들 파이보는 질문과 답변 서비스이다. 질문을 작성하거나 답변을 작성하면 필수적으로 데이터가 생성된다. 따라서 데이터를 저장하고 읽고 수정하는 등의 기능들이 반드시 필요하다. 파이보와 같은 웹서비스는 이러한 데이터 처리를 위해 데이터베이스를 사용한다. DB는 데이터를 처리하는데 특화된 시스템을 의미한다.

웹프로그램에서 DB사용을 위해서는 DB에 접속하여 쿼리를 수행해야 한다.(쿼리란 DB에 어떤 규칙에 맞는 형식의 질문을 하는 것 => SQL : Structured Query Language)
## ORM
이때 ORM을 이요하면 개발자가 직접 쿼리문을 작성하지 않고 테이블과 매핑된 모델 객체를 통해서 데이터 작업을 처리할 수 있다.
예를 들어 질문 테이블에 데이터를 한건 입력하려면 다음과 같은 쿼리를 수행해야 한다. 특히 ORM을 사용시 MySQL, Oracle등 DB에 따라 다른 SQL문을 각각 다시 적을 필요가 없다. 그대로 모델을 사용하므로 독특한 쿼리문이 만들어지거나 잘못 작성할 가능성도 적어진다.
```SQL
insert into question (subject, content) values ('제목', '내용');
```
단 ORM을 사용하면 쿼리문 대신 모델을 이용하여 다음과 같이 데이터를 한건 입력할 수 있다. 단 ORM을 사용하더라도 내부적으로 쿼리문이 생성되어 보내지는 것임을 잊지 말자.
```python
question = Question(subject='제목', content='내용')
db.session.add(question)
```
pybo 서비스는 직접 쿼리문을 작성하지 않고 ORM을 사용할 것이다. SQLAlchemy를 사용할 예정이며 테이블을 생성하고 컬럼을 추가하는 일들을 DB에서 직접하는 것이 아닌 모델을 통해 변경할 수 있도록 Flask-Migrate 라이브러리를 설치할 것이다. Flask-Migrate를 설치시 SQLAlchemy도 함께 설치된다.  가상환경에서 다음 명령을 수행하자.
```linux
pip install Flask-Migrate
```
## ORM 적용
ORM을 적용해보자. 먼저 config.py파일을 myproject폴더 하위에 생성하자.
```python
import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False#이벤트 처리 위한 옵션으로 추가 메모리를 쓰므로 기능 끄기
```
BASE_DIR은 .\myproject 를 의미한다.
SQLALCHEMY_DATABASE_URI 변수는 데이터베이스의 접속주소를 의미하는데 파이보는 SQLite 데이터베이스의 접속주소를 위와 같이 입력하도록 하자. 데이터베이스 파일은 BASE_DIR 하위에 pybo.db 라는 파일에 저장한다고 정의하였다.

그리고 다음처럼 pybo/__init__.py 파일을 수정하자
```python
from flask import Flask
# ---------------------------------------- [edit] ---------------------------------------- #
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()
# ---------------------------------------------------------------------------------------- #

def create_app():
    app = Flask(__name__)
    # ---------------------------------------- [edit] ---------------------------------------- #
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    # ---------------------------------------------------------------------------------------- #

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
```
config.py에서 작성한 항목들을 app.config 환경변수로 읽어들이기 위해 app.config.from_object(config)를 추가한다.그리고 전역변수로 db. migrate객체를 만들고(함수 내부에 생성시 블루 프린트와 같은 다른 모듈에서 db객체를 import하여 사용할수 없기 떄문) 초기화는 crate_app에서 수행하는 패턴이다.
## ORM 수행
```
flask db init
```
를 수행하여 db를 수행하면 db관리를 위한 초기파일들이 migrations라는 디렉토리에 자동으로 생성된다. 이때 생성되는 파일들은 flask_migrate 라이브러리가 내부적으로 사용하는 파일들이므로 알 필요 없다.
위 명령어는 최초 한번만 수행하면 된다. 앞으로 모델을 추가하고 변경할 때는 flask db migrate와 flask db upgrade 명령 2개만 반복적으로 사용하면 된다.
```
1. flask db migrate - 모델을 신규로 생성하거나 변경할때 사용
2. flask db upgrade - 변경된 내용을 적용할 때 사용
```
다른 명령들은 flask db 명령을 수행하여 참고할 수 있다.(다른건 잘 안씀)

## 모델 생성
파이보가 사용할 데이터 모델을 만들어 보자.
파이보에는 질문과 답변에 해당하는 데이터 모델이 있어야 한다.

- 질문 모델

|속성명|설명|
|--|--|
|id|질문의 고유번호|
|subject|질문의 제목|
|content|질문의 내용|
|create_date|질문을 작성한 일시|

- 답변 모델

|속성명 |설명|
|--|--|
|id|	답변의 고유번호|
|question_id	|질문의 고유번호 (어떤 질문의 답변인지 알아야하므로 질문의 고유번호가 필요하다.)|
|content	|답변의 내용|
|create_date|	답변을 작성한 일시|

해당하는 모델을 pybo/model.py에 정의해 보자.
```python
# ---------------------------------------- [edit] ---------------------------------------- #
from pybo import db


class Question(db.Model):#각 속성들은 어떤 타입인지 첫 인자로 명시
    id = db.Column(db.Integer, primary_key=True)# 키값은 고유함
    subject = db.Column(db.String(200), nullable=False)# nullable은 빌수 없고, string은 글자수가 제한된 텍스트
    content = db.Column(db.Text(), nullable=False)#글자수가 제한되지 않은 text
    create_date = db.Column(db.DateTime(), nullable=False)#dateTime 시간


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# ---------------------------------------------------------------------------------------- #
```

- db.Column이 없다고 뜰 경우 다음을 참고
    - pip install pylint-flask
    - pip install pylint-flask-sqlalchemy
    - "python.linting.pylintArgs": ["--load-plugins", "pylint-flask", "pylint-flask-sqlalchemy"] //vscode setting.json

db.Model을 상속하여 모델 2개를 만든다. 여기서 사용된 DB는 pybo패키지의 __init__.py에서 생송한 SQLAlchemy의 객체다. 모델클래스의 각각 속성은 db.Column을 사용하여 생성할 수 있다.
각각의 설명은 코드 주석에 달려 있다.

Answer모델은 질문에 대한 답변에 해당되므로 Question모델을 속성으로 가져갈 수 있다는 점이 특이하다. 기존 모델을 속성으로 가저가기 위해서는 다음처럼 2개의 추가 속성이 필요하다.
```python
question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
question = db.relationship('Question', backref=db.backref('answer_set'))
```

question id는 Quesion모델의 id값을 의미하며 이를 나타내기 위해 db.ForeignKey를 사용해야 한다. db.ForeignKey는 다른 모델과의 연결을 의미한다. ondelete=CASACADE의 의미는 이답변과 연결된 질문이 삭제될 경우 답변도 같이 삭제된다는 의미이다.

question 속성은 답변모델에서 질문모델을 참조하기 위해서 추가된 속성이다. 즉 answer.question.subject 처럼 답변 모델 객체(answer)를 통해서 질문모델 객체를 참조할 수 있게 된다. 이를 위해서는 db.relationship을 이용하여 속성을 추가해 주어야 한다. db.relationship에서 사용된 backref속성은 answer.question.subject와는 반대로 질문에서 답변모델을 참조하기 위해서 사용되는 속성이다. 하나의 질문에는 여러개의 답변이 작성될 수 있는데 어떤 질문에 해당하는 객체가 a_qus이라면 이 질문에 작성된 답변들을 참조하기 위해서 a_qus.answer_set과 같이 사용할 수 있다.

SQLAlchemy에서 사용되는 속성(Field)의 타입은 이것 외에도 많다.
 - 참고 https://docs.sqlalchemy.org/en/13/core/type_basics.html


## Table 생성
이제 모델을 생서앴으므로 플라스크의 Migrate을 이용하여 데이터베이스 테이블을 생성할 수 있게 되었다. 하지만 테이블 생성전에 한가지 먼저 해주어야 할 일이 있다.

테이블을 생성하기 위해서는 플라스크의 Migrate를 사용해야 하는데 이 Migrate가 우리가 작성한 모델을 인식할 수 있도록 다음을 pybo/__init__.py 파일 함수안에 추가하자.

```python
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    # ---------------------------------------- [edit] ---------------------------------------- #
    from . import models#import models 해도 상관 무(접근자 차이)
    # ---------------------------------------------------------------------------------------- #

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
```
이러면 migrate 객체가 우리가 작성한 모델인 models.py를 참조할 수 있게 된다.

다음을 수행하자(모델을 신규로 생성하거나 변경할 때 아래 명령어)
```
flask db migrate
```
이렇게 하면 myproject하에 pybo.db가 생성될 것이다. pybo.db 파일을 SQLite 데이터베이스의 데이터파일이다. 아마도 여기에 question 테이블과 answer 테이블이 생성되었다. 테이블명은 모델클래스의 이름과 동일하게 생성된다. 따라서 Question 모델의 테이블명은 question, Answer 모델의 테이블명은 answer가 될 것이다.

## DB Browser for SQLite
pybo.db파일에 어떤 테이블들이 만들어졌는지 잠깐 확인해보자. SQLite의 GUI 도구인 "DB Browser for SQLite"를 설치하면 데이터베이스의 테이블들을 확인해 볼 수 있다.

https://sqlitebrowser.org/dl/

단 설치시 desktop에도 설치한다는 항목에 표시를 해주어야 한다.

데이터베이스 열기를 하고 pybo.db를 열어보면 테이블들이 생성된 것을 확인할 수 있다.  alembic_version테이블은 db Migrate작업을 위해 flask-migrate가 내부적으로 사용하는 테이블이다.

## 모델 사용하기

이번에는 모델을 어떻게 사용할 수 있는지 플라스크 쉘을 사용하여 그 사용법에 대해서 잠시 알아보도록 하자.
플라스크 쉘은 다음과 같이 실행할 수 있다.
```
(myproject) c:\projects\myproject>flask shell
```
파이썬 쉘이 아니라 플라스크 쉘로 플라스크 실행에 필요한 환경들이 자동으로 설정되어 실행된다.

## Question 생성

Questio과 Answer 모델은 플라스크 쉘에서 다음처럼 import하여 사용할 수 있다.
d
```
>>> from pybo.models import Question, Answer
>>> from datetime import datetime
>>> q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())
```
위에서 생성한 Question 모델의 q 객체를 데이터베이스에 저장하기 위해서는 다음과 같이 SQLAlchemy의 db객체를 이요해야 한다.
session은 db와 연결된 세션을 의미한다. 이 세션을 이용하여 데이터를 저장하고 삭제하는등의 데이터베이스 처리를 할수 있다.
git bash와 의미가 상통하니 이해가 쉬울 것이다.
db.seesion.rollback()을 통해 add 했던 것들을 모두 취소 할 수 있다. 마찬가지로 커밋을 한 다음은 롤백이 되지 않는다.db.
```
>>> from pybo import db
>>> db.session.add(q)
>>> db.session.commit()
```
## Question 조회

아래 명령을 수행시 현재 커밋된 모델 데이터들을 조회 할 수 있다. 리턴 값은 Query객체를 담은 리스트이다. 아래에서 숫자는 id 값을 의미한다. 중요한 것은 db를 통해 조회하는 것이 아닌 모델명을 통해 조회가 가능하다.
```
>>> Question.query.all()
[<Question 1>, <Question 2>]
```

filter를 이용해 조회할 수 있다. 리턴값은 filter이므로 여러개가 될 수 있어 리스트 형태로 리턴된다. %는 아무 문자열이라는 뜻이다(최소 1개이상) 예를 들어 '플라스크%'의 경우 플라스크로 시작되는 뒤에 어떤 문자가오는 제목 컬럼을 가진 데이터 조회라고 볼 수 있다.
```
>>> Question.query.filter(Question.id==1).all()
[<Question 1>]
>>> Question.query.filter(Question.subject.like('%플라스크%')).all()
[<Question 2>]
```

다음은 id값을 통해 조회 하는 것이다. 리턴 값은 Question 모델 객체이다.
```
>>> Question.query.get(1)
<Question 1>
```
연습으로 subject가 플라스크인 Question을 db에 추가해 보자.

데이터 조회 SQLAlchemy 문서: https://docs.sqlalchemy.org/en/13/orm/query.html
## Question 수정
이번에는 저장된 Question model 데이터를 수정해보자
2번 째 데이터를 조회해보자

```
>>> q = Question.query.get(2)
>>> q
<Question 2>
>>> q.subject="modified subject"
```
단 항상 수정을 해준다음에는 commit을 해주어야 한다.
```
db.session.commit()
```
## Question 삭제
```
>>> q = Question.query.get(1)
>>> db.session.delete(q)
>>> db.session.commit()
```

## Answer 작성
이번에는 Answer 모델 데이터를 작성해보자.
```
>>> from datetime import datetime
>>> from pybo.models import Question, Answer
>>> from pybo import db
>>> q = Question.query.get(2)
>>> a = Answer(question=q, content='네 자동으로 생성됩니다.', create_date=datetime.now())
>>> db.session.add(a)
>>> db.session.commit()
```
답변 데이터를 만들기 위해서는 먼저 질문이 필요하므로 id가 2인 질문을 먼저 조회하여 q라는 변수로 저장한 후 Answer 모델의 question 속성에 대입해 주었다. Answer 모델에는 question_id 속성이 있는데 위처럼 question=q와 같이 relationship으로 연결된 Question모델속성인 question에 값을 대입하면 question_id에 갑을 지정하지 않아도 자동으로 저장 된다.
## Answe 조회, 수정, 삭제
답변을 조회, 수정, 삭제 방법은 Question와 같다.
```
>>> a = Answer.query.get(1)
>>> a
<Answer 1>
```
마찬가지로 a객체에 연결된 질문을 보려면 모델에 정의 되어 있기 때문에 다음과 같이 매우 쉽다. 
```
>>> a.question
<Question 2>
```
그럼 질문을 통해 답변을 찾는 방법은 어떻게 할까?
```
>>> q.answer_set
[<Answer 1>]
```
다음과 같이 하면 된다.

즉 Question와 Answer는 서로 연결되어 있기 때문에 Answer모델에서 backref로 지정한 answer_set을 사용하면 질문과 연결된 답변을 가져올 수 있다. backref의 기능에 대해 놀라움을 느낀다. 이 기능은 매우 중요하니 기억하자.

## 조회와 템플릿
```
http://localhost:5000
```
위 페이지 요청시 등록한 질문들을 조회할 수 있도록 구현해보자.
지금은 위페이지를 요청하면 아까 적은 그냥 간단한 문장 정도가 출력될 것이다. 질문 목록이 출력되도록 main_views.py파일의 index함수를 다음과 같이 변경해보자.
```python
from pybo.models import Question
from flask import Blueprint, render_template

...

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_l.html', question_l=question_list)
```
질문목록 데이터는 
- question_list = Question.query.order_by(Question.create_date.desc()) 

로 얻을 수 있다. order_by는 조회 결과를 정렬하는 함수이다. 
- order_by(Question.create_date.desc()) 

의 의미는 조회된 데이터를 작성일시 기준으로 역순으로 정렬하라는 의미이다.

※ 역순이 아닌 작성일시 순으로 조회하기 위해서는 order_by(Question.create_date.asc()) 또는 asc() 를 생략하여 order_by(Question.create_date)와 같이 사용하면 된다.

render_template 함수는 템플릿 파일을 화면으로 렌더링하는 함수이다. 여기서 사용된 'question/question_list.html'을 템플릿 파일이라 부른다. 템플릿 파일은 HTML파일과 비슷하지만 플라스크에서 사용하는 특별한 태그들을 사용할 수 있는 HTML파일이다.
## 템플릿 디렉터리

이제 render_template함수에서 사용할 question/question_l.html을 작성하자. 템플릿 파일을 작성하기 전 template 파일을 저장할 디렉토리를 먼저 만들자. pybo앱의 경우 다음의 디렉토리를 생성하면 별다를 설정없이 템플릿 디렉터리로 인식한다.

템플릿 디렉터리가 준비되었으므로 이제 템플릿 파일을 만들어 보자. render_template 함수에서 사용된 템플릿 파일명은 다음과 같았다.
```
question/question_l.html
```

따라서 question_l.html 파일은 다음 경로에 저장해야 한다.

c:\projects\myproject\pybo\templates\question\question_l.html

해당 파일에 다음과 같이 작성하자
```html
{% if question_l %}
    <ul>
    {% for question in question_l %}
        <li><a href="/detail/{{ question.id }}/">{{ question.subject }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>질문이 없습니다.</p>
{% endif %}
```
템플릿을 보면 {% if question_list %} 처럼 {% 와 %} 로 둘러싸인 문장들을 볼 수 있는데 이러한 것들을 템플릿 태그라고 한다.
{% if question_list %}는 다음처럼 해석된다.

question_list 가 있다면 (※ question_list는 render_template 함수에서 전달받은 "질문목록"에 해당되는 데이터이다.)

{% for question in question_list %}는 다음처럼 해석된다.

question_list 를 반복하며 순차적으로 하나씩 question에 대입

{{ question.id }} 는 다음처럼 해석된다.

for문에 의해 대입된 question 객체의 id번호를 출력

{{ question.subject }} 는 다음처럼 해석된다.

for문에 의해 대입된 question 객체의 제목을 출력

파이썬에 익숙하다면 여기에 사용된 태그들이 직관적으로 무엇을 의미하는지 쉽게 유추해 낼 수 있을 것이다.

## 탬플릿 태그

플라스크에서 사용되는 탬플릿 태그는 사실 다음 3가지 유형만 알면 된다.
1. 분기 
    - 분기문 태그의 사용법은 다음과 같다. 
    ```
    {% if 조건문1 %}
    <p>조건문1에 해당되는 경우</p>
    {% elif 조건문2 %}
    <p>조건문2에 해당되는 경우</p>
    {% else %}
    <p>조건문1, 2에 모두 해당되지 않는 경우</p>
    {% endif %}
    ```
2. 반복
    - 반복문은 다음과 같다.
    ```
    {% for item in list %}
    <p>순서: {{ loop.index }} </p>
    <p>{{ item }}</p>
    {% endfor %}
    ```
    다음과 같은 loop객체를 for문 안에서 사용 가능하다.

    |loop 속성|	설명|
    |---|---|
    |loop.index	|루프내의 순서로 1부터 표시|
    |loop.index0	|루프내의 순서로 0부터 표시|
    |loop.first	|루프의 첫번째 순서인 경우 True|
    |loop.last	|루프의 마지막 순서인 경우 True|

 3. 객체 출력
    - 객체 출력은 다음과 같이 가능하다. {{객체.속성}}

    ex) {{item}} or {{question.id}}

템플릿 문법 참고 : https://jinja.palletsprojects.com/en/2.11.x/templates/

## 상세 조회
이제 목록 조회 화면에 조회된 링크 url 템플릿에 대해 정의하자
클릭하면 Not Found가 뜰 것이다. 어떻게 해결할까? question_id 값마다 라우터를 추가한다? 정신나간 짓이다. 다음을 뷰 파일에 추가하자.
```python
@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)
```
http://localhost:5000/detail/2/ 와 같은 페이지가 요청되면 위 매핑룰에 의해 http://localhost:5000/detail/<int:question_id>/ 가 적용되어 question_id 에 2라는 값이 저장되고 detail 함수가 실행될 것이다. (※ 여기서 int는 숫자값이 매핑됨을 의미한다.) 중요한 것은 모델에서 정의한 컬럼값과 들어오는 값의 자료형이 같아야 한다. 라우터를 통해 들어온 값은 함수 파라미터로 전달되고 우리는 이 id값을 통해 어떤 question을 보여줘야 할지 화면에 rendering을 할 수 있다.

자 이제 뷰파일에서 detail 함수를 정의 한 것을 어떻게 해야 content와 subject를 보여줄 수 있을까? 직접 해보자

힌트 :  detail html 필요

## 오류 페이지
이번에는 http://localhost:5000/detail/30/을 요청해보자.
아마도 빈페이지가 나올 것이다. 해당 id가 없기 때문이다. 잘못된 페이지는 Not Found(404)오류를 리턴해야 한다.
다음은 웹 오류 기본이니 외워 두자

|오류코드|	설명|
|--|--|
|200	|성공 (OK)|
|500|	서버오류 (Internal Server Error )|
|404|	서버가 요청한 페이지(Resource)를 찾을 수 없음 (Not Found)|
뷰단을 간단하게 수정하면 이를 자동으로 할 수 있다.
## 블루 프린트
모든 것을 main_views.py에 구현할수도 있겠지만 기능별로 블루프린트 파일로 분리하여 관리하는것이 좋다.

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

