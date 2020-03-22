from flask import Flask,request,render_template,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import os


# pymysql => sqlalchmy로 바꿔서

# 서버에 있는 소스를 클라이언트 웹에 가져와서 실행
# html: 정적인 문서, 골격 잡는데 한계 => CSS로 보완
# 자바스크립터: 동적인 문서
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwer1234@maria/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(20))
    userpw = db.Column(db.String(20))
    username = db.Column(db.String(20))
    userage = db.Column(db.Integer)
    usermail = db.Column(db.String(20))
    useradd = db.Column(db.String(50))
    usergender = db.Column(db.String(20))
    usertel = db.Column(db.String(20))

    # 생성자에 id 넣으면 안됨
    def __init__(self,userid,userpw,username,userage,usermail,useradd,usergender,usertel):
        self.userid = userid
        self.userpw = userpw
        self.username = username
        self.userage = userage
        self.usermail = usermail
        self.useradd = useradd
        self.usergender = usergender
        self.usertel = usertel

@app.route('/')
def index():
    return render_template('bootstraptest.html')

@app.route('/bootstrap')
def bootstraptest():
    return render_template('bootstraptest.html')

@app.route('/form')
def formTest():
    return render_template('form.html')

@app.route('/formresult',methods=['POST'])  
def formresult():
    username = request.form['username']
    userpass = request.form.get('userpass')
    joblist=request.form.getlist('job')
    return render_template('formresult.html',username=username,userpass=userpass,joblist=joblist) 


# 인설트!
@app.route('/usersform',methods=['POST','GET'])
def usersform():
    if request.method == 'GET':
        return render_template('usersform.html')   
    else:
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        username = request.form.get('username')
        userage = request.form.get('userage')
        usermail = request.form.get('usermail')
        useradd = request.form.get('useradd')
        usergender = request.form.get('usergender')
        usertel = request.form.get('usertel')
        
        my_data = User(userid,userpw,username,userage,usermail,useradd,usergender,usertel)
        db.session.add(my_data)
        db.session.commit()

    return redirect('/list')

# sql="select * from users where userid = %s;"
@app.route('/updateform/<userid>',methods=['GET'])
def updateformget(userid):
    selected_data = User.query.get(request.form.args('userid'))

    return render_template('updateform.html',list=selected_data)  


# userid를 조건으로 update
@app.route('/updateform',methods=['POST'])
def updateformpost():

    my_data = User.query.get(request.form.get('userid'))

    my_data.userid = request.form.get('userid')
    my_data.userpw = request.form.get('userpw')
    my_data.username = request.form.get('username')
    my_data.userage = request.form.get('userage')
    my_data.usermail = request.form.get('usermail')
    my_data.useradd = request.form.get('useradd')
    my_data.usergender = request.form.get('usergender')
    my_data.usertel = request.form.get('usertel')

    db.session.commit()                      
    return redirect('/list')    



# userid값으로 select하기
# userid 주소로 받아오는 거 주의
# data는 괄호 안에! 쀼쀼
@app.route('/content/<userid>')
def content(userid):
    my_data = User.query.get(request.form.args('userid'))
    
    return render_template('content.html',list=my_data)


# userid를 key값으로 지우기
@app.route('/deleteform/<userid>')
def deleteformget(userid):
    my_data = User.query.get(userid)
    db.session.delete(my_data)
    db.session.commit()

    return redirect('/list')  

@app.route('/list')
def list():
    all_data = User.query.all()
    return render_template('list.html',list=all_data)      

# select all
@app.route('/ajaxlist',methods=['GET'])
def ajaxlistget():
    all_data = User.query.all()

    return render_template('ajaxlist.html',list=all_data)      

@app.route('/ajaxlist', methods=['POST'])
def ajaxlistpost():
    inputid = request.form.get('userid')
    inputid = '%'+inputid+'%'
    selected_data = User.query.filter_by(User.userid.like(inputid)).all()
    return jsonify(selected_data)    

@app.route('/imglist')
def imglist():
    print(os.path.dirname(__file__))
    dirname=os.path.dirname(__file__) + '/static/img/'
    filenames = os.listdir(dirname)
    print(filenames)
    return render_template('imglist.html',filenames=filenames)        

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=8890)