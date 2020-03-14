from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

# <name>는 url로 들어오는 값
# url로 들어오는 값은 반드시 함수 인자로 받아야함
# <name>이 들어올때 안들어올때 2가지 상황이 있음, 기본값을 세팅해줘서
# 오류가 나지 않도록 한다.
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    if name is None:
        return "No name"
    else:
        return 'A horse named %s'%name

# default 값은 GET / 하나만 적어도 ok
@app.route('/login', methods=['GET','POST'])
def login():
    # request 개체 필요(서버에서 클라이언트로 들어올 때 필요)
    # method에 저장되어 있다. GET or POST인지
    if request.method=='POST':
        # 딕셔너리로 전달 -> key값으로 value접근 가능
        # return request.form

        # redirect는 바로 함수 실행
        # url_for에는 실행할 함수명 인자로 넣어줌
        # 데이터(request.form, ex>id,pw)를 넘겨받음
        # request.form은 딕셔너리 형태이므로 key를 통해 찾는다!
        # return redirect(url_for('listdata', name=request.form['Name']))

        # request.form을 data라는 이름으로 listdata.html에 쏴줌
        return render_template('listdata.html', data = request.form) 
    else:
        return "get"

@app.route('/form/')
def form():
    return render_template('form.html')

@app.route('/listdata/<name>')
def listdata(name=None):
    return name
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8890',debug=True)