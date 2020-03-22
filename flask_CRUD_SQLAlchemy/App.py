from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

# SqlAlchemy Database Configuration With Mysql
# 얘만 수정하면 오라클이든 mysql이든 maria든 어디서든 수정할 수 있음
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwer1234@maria/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
# class로 데이터 테이블 만듬.
# 이때 Data는 table이름이 됨.
class Data(db.Model):
    # 필드이름 = 컬럼이름()
    # 데이터베이스가 달라져도 소스 같이 쓸 수 있음: mysql, mariadb, pymysql등등
    # 앞에선 쿼리문으로 써서 데이터베이스마다 쿼리문이 달라질 수 있음
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


    # __init__은 생성자, 클래스 객체 생성할 때 필요한
    def __init__(self, name, email, phone):

        self.name = name
        self.email = email
        self.phone = phone



#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    # 테이블이름. 해서 쓰는게 가능해짐
    # Table.query.all()은 select * from Table과 같음
    all_data = Data.query.all()

    return render_template("index.html", employees = all_data)



# this route is for inserting data to mysql database via html forms
# post가 왔떠염, insert를 호출해염
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        # html에 name으로 match, form안의 string
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        # 개체생성
        my_data = Data(name, email, phone)
        # my_data를 추가(insert)
        db.session.add(my_data)
        # 저장하기
        db.session.commit()

        # flash를 쓰면 해당하는 곳으로 보낼 수 있음
        # {% with messages = get_flashed_messages() %} 진자에서 받아서 처리
        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))


#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        # Table.query.get: id를 조건으로 해서 하나만 들고 올 때
        my_data = Data.query.get(request.form.get('id'))

        # 개체생성x, 수정!
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index'))


#This route is for deleting our employee
# get방식으로 들어오니까 주소값
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
# id인자로 받아야 함 주소로 쏴주니까
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8890')