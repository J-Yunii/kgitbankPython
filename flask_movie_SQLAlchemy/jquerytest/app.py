from flask import Flask,render_template

app=Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=8890)