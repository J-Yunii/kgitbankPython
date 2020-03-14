from flask import Flask, render_template

# __name__에는 __main__ or 실행되는 파일명이 들어감
# 플라스크 개체 생성, 주소값 변수에 저장
app = Flask(__name__)

# url에 /info가 들어오면 함수 실행
@app.route('/')
def index():
    # 파일과 같은 경로의 templates폴더에서 html파일을 가져옴
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index copy.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/inputdata')
def inputdata():
    return "inputdata"

@app.route('/listdata')
def listdata():
    return render_template('listdata.html')

# 외부에서 호출되지 않을 때
if __name__ == '__main__':
    # run method 호출해서 실행
    # host 0.0.0.0은 어디서나 실행할 수 있음, 두번째 인자에는 port번호
    # port는 8888-8890까지 열려있는데, 88은 vscode 89는 주피터로 쓰고 있음
    # debug=True는 바로 웹페이지에 수정사항 반영
    app.run(host='0.0.0.0', port=8890, debug=True)