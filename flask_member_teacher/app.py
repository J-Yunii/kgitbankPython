from flask import Flask,request,render_template,redirect,url_for,jsonify
import pymysql,os

# 서버에 있는 소스를 클라이언트 웹에 가져와서 실행
# html: 정적인 문서, 골격 잡는데 한계 => CSS로 보완
# 자바스크립터: 동적인 문서
app=Flask(__name__)

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

@app.route('/usersform',methods=['POST','GET'])
def usersform():
    if request.method == 'GET':
        return render_template('usersform.html')   
    else:
        #print(type(request.values))
        #for key in request.values:
        #    print(key," : ",request.values[key])
        #userid = request.form.get('userid')
        #print('userid :',userid)
        #for key in request.values:
        #    eval(str(key)+"= '"+str(request.values[key])+"'")
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        username = request.form.get('username')
        userage = request.form.get('userage')
        usermail = request.form.get('usermail')
        useradd = request.form.get('useradd')
        usergender = request.form.get('usergender')
        usertel = request.form.get('usertel')

        # html에서 받은 것을 변수에 저장한 다음, db에 저장
        try:
            connection=pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
            
            with connection.cursor() as cursor:
                sql='''
                    insert into users values(%s,%s,%s,%s,%s,%s,%s,%s);
                    '''
                cursor.execute(sql,(userid,userpw,username,userage,usermail,useradd,usergender,usertel))
                connection.commit()
                     
        finally:
            connection.close()                            

    return redirect('/list')

@app.route('/updateform/<userid>',methods=['GET'])
def updateformget(userid):
    connection=pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
       
    try:
        with connection.cursor() as cursor:
            sql="select * from users where userid = %s;"
            cursor.execute(sql,userid)
            result=cursor.fetchone()
            print(result)
    finally:
        connection.close()
    return render_template('updateform.html',list=result)  

@app.route('/updateform',methods=['POST'])
def updateformpost():
    connection=pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    userid = request.form.get('userid')
    userpw = request.form.get('userpw')
    username = request.form.get('username')
    userage = request.form.get('userage')
    usermail = request.form.get('usermail')
    useradd = request.form.get('useradd')
    usergender = request.form.get('usergender')
    usertel = request.form.get('usertel')
    
    try:
        with connection.cursor() as cursor:
            sql='''
                UPDATE users 
                SET 
                userpw=%s,
                username=%s,
                userage=%s,
                usermail=%s,
                useradd=%s,
                usergender=%s,
                usertel=%s
                WHERE userid=%s;
                '''
            cursor.execute(sql,(userpw,username,userage,usermail,useradd,usergender,usertel,userid))
            connection.commit()
    finally:
        connection.close()                            
    return redirect('/list')    

# data는 괄호 안에! 쀼쀼
@app.route('/content/<userid>')
def content(userid):
    connection=pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
       
    try:
        with connection.cursor() as cursor:
            # like는 일부 where은 완전 일치
            sql="select * from users where userid = %s;"
            cursor.execute(sql, userid)
            result=cursor.fetchone()
            print(result)
    finally:
        connection.close()
    return render_template('content.html',list=result)


@app.route('/deleteform/<userid>')
def deleteformget(userid):
    connection=pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
       
    try:
        with connection.cursor() as cursor:
            sql="delete from users where userid = %s;"
            cursor.execute(sql,userid)
            connection.commit()
    finally:
        connection.close()
    return redirect('/list')  

@app.route('/list')
def list():
    connection=pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
                sql="select  * from users;"
                cursor.execute(sql)
                result=cursor.fetchall()
                print(result)
    finally:
            connection.close()
    return render_template('list.html',list=result)      

@app.route('/ajaxlist',methods=['GET'])
def ajaxlistget():
    connection=pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
                sql="select  * from users;"
                cursor.execute(sql)
                result=cursor.fetchall()
                print(result)
    finally:
            connection.close()
    return render_template('ajaxlist.html',list=result)      

@app.route('/ajaxlist',methods=['POST'])
def ajaxlistpost():
    userid = request.form.get('userid')
    connection=pymysql.connect(host='maria',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
                sql="select * from users where userid like %s;"
                userid=userid+'%'
                cursor.execute(sql,userid+'%')
                result=cursor.fetchall()
                print(result)
    finally:
            connection.close()
    return jsonify(result)    

@app.route('/imglist')
def imglist():
    print(os.path.dirname(__file__))
    dirname=os.path.dirname(__file__) + '/static/img/'
    filenames = os.listdir(dirname)
    print(filenames)
    return render_template('imglist.html',filenames=filenames)        

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=8890)