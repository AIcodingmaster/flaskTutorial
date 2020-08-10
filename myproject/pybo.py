from flask import Flask #flask 파일에서 객체 Flask를 추가한 것
app= Flask(__name__)#name 변수는 실행된 모듈명을 의미하므로 pybo라는 문자열이 대입됨.

@app.route('/')#데코레이터
def hello_pybo():
    return 'Hello, pybo!'
