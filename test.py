import re
p=re.compile("( - .*?\n)|(## [0-9][.] .*?\n)")
a="""
 - 어플리케이션 팩토리
 - 블루프린트
 - 모델
 - 조회와 템플릿
 - 데이터 저장
 - 스태틱
 - 부트스트랩
 - 템플릿 상속
 - 폼
 ## 2. 플라스크 심화
 - 네비게이션 바
 - 페이징
 - 템플릿 필터
 - 게시물 번호
 - 답변 갯수 표시
 - 계정 생성
 - 로그인 & 로그 아웃
 - 모델 변경
 - 글쓴이 표시
 - 수정과 삭제
 - 댓글
 - 추천
 - 앵커
 - 마크다운
 - 검색과 정렬
 - 파이보의 추가기능
 ## 3. 플라스크 서비스
 - 깃
 - 깃허브
 - 서버
 - AWS Lightsail
 - 파이보 오픈
 - config 분리
 - 터미널 접속
 - WSGI
 - Gunicorn
 - Nginx
 - production
 - 오류페이지
 - 로깅
 - 도메인
 - PostgreSQL
 """
match=p.findall(a)
print(match)
def deleteBlank(x):
    a,b=x
    return a+b
match=list(map(deleteBlank,match))
def change(x):
    if '#' not in x:
        word=x.replace(' - ','')
        word=word.strip()
        wordbf=word
        wordaf='['+word+']'+'(#'+word.replace(' ','-')+')'
        c=x.replace(wordbf,wordaf)
        return c
    else:
        word=re.sub("## \d{1,2}[.] (.+?)\n","\\1",x)
        c=x.replace(word,'['+word+']'+'(#'+word.replace(' ','-')+')')
        return c
l=list(map(change,match))
l.reverse()
abcd=""
while l:
    abcd+=l.pop()
with open("test.txt",'wb') as f:
    f.write(abcd.encode('utf-8'))
