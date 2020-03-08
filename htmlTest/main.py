# flask는 장고보다 간단한 웹테스트 해볼 때
from flask import Flask, render_template
# 플라스크 객체 생성
# 생성자~!
# 생성된 개체의 주소값을 app에 전달(참조변수에 전달)
app = Flask(__name__)


# 웹 서비스하는 루트, '/'이렇게 호출이 됐을 때
# 밑의 함수를 실행하라는 뜻
@app.route('/')
def index():
    return 'Hello Flask'

# http://127.0.0.1:8890/info 호출되면 밑의 함수 실행됨
@app.route('/info')
def info():
    # 서비스하고자 하는 html문서를 작성
    # (templates폴더 안에 있는 거여야만 함)
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')


# 자기 파일안에서 호출될 때
if __name__ == "__main__":
    # 접근할 수 있게 port를 열어놓은 게 host설정에 나와있음
    # docker run --rm --name anaconda3 -itd -u vscode -p 8888-8890:8888-8890 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes --link maria:maria mrsono0/base_project:anaconda3
    # 8888은 주피터 8889는 vscode 8890만 비어있음
    # 127.0.0.1:8890 요렇게 접근
    # debug가 False면 코드를 끄고 다시 켜야 수정된 코드가 반영 됨
    app.run(host="0.0.0.0", port='8890', debug = True)
