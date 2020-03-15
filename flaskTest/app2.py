from flask import Flask, json
# file employee에서 class Employee를 가져옴
from employee import Employee

app = Flask(__name__)

@app.route('/')
def getEmployeeList():
    try:
        employeeList = []
        # class를 넣어줌
        employeeList.append(Employee("최","정윤"))

        # dump : json형태의 문자열로 바꾸는 것(파일에)
        # dumps: 메모리상에
        # load : json형태의 문자열을 받아와서 파이썬 형태로 바꾸는 것(파일 상에)
        # loads: 메모리 상에

        # indent : 깔끔하게 띄어쓰기해서 표현
        jsonStr = json.dumps([e.toJSON() for e in employeeList], indent = 4, ensure_ascii=False)

    except:
        pass
    return jsonStr


if __name__ == "__main__":
    app.run(debug=True, host ='0.0.0.0',port=8890)