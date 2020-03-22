from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')
# test는 영화
# index는 파일
@app.route('/index1')
def index1():
    return render_template('test1.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8890,debug=True)