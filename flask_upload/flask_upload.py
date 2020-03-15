# jsonify: flask에서 joson형태로 바꿔주는 라이브러리
# redirect: 함수에서 바로 호출
# url_for: url 형태로 바꿔주는 것
from flask import Flask, render_template, jsonify, request, send_from_directory, redirect, url_for
import os

# 폴더에 업로드 해주는 경로
# __file__: 현재 파일 정보
# dirname: 해당파일의 경로를 알려줌
# 현재 파일의 경로 아래에 files를 생성 or 접근
UPLOAD_DIRECTORY = os.path.dirname(__file__) + '/files'
print(UPLOAD_DIRECTORY)

# 없으면 경로에 맞게 폴더를 만듭니다.
if not os.path.exists(UPLOAD_DIRECTORY):
    # makedirs: 폴더 만드는 함수
    os.makedirs(UPLOAD_DIRECTORY)

# Flask 객체에 instance를 만들어서 참조변수에 넣어줌
app = Flask(__name__)

# 업로드 HTML 렌더링
@app.route('/upload')
# 업로드 페이지로 넘겨줌
def render_file():
    return render_template('upload.html')

# 파일 업로드 처리
# methods를 get,post 둘 다 해놓으면 두 방식 다 받을 수 있음
@app.route('/fileupload', methods = ['GET','POST'])
def upload_file():
    # POST로 받을 때에만 실행
    if request.method == 'POST':
        # 클라이언트에서 파일관련 정보는 request.files에서 찾는다.
        # form 태그의 이름과 같아야 합니다!!
        # f는 파일 개체가 됨
        f = request.files['file']
        # 저장할 경로 + 파일명
        # 확장자명도 같이 저장 / 구분해서 걸러내 받을 수도 있음
        dirname = os.path.dirname(__file__) + '/files/' + f.filename
        print(dirname)
        f.save(dirname)
    return redirect('/files')

@app.route("/files")
def list_files():
    """end to list files on the server."""
    # 특정 경로에 있는 파일들을 가져와 리스트로 만들 것
    files = []
    # listdir은 경로에 있는 파일 목록들을 뽑아서 list로 만듬(파일이름만 가져옴)
    for filename in os.listdir(UPLOAD_DIRECTORY):
        # join은 경로를 하나로 합쳐줌
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        # 폴더인지 아닌지 확인! 파일일때만 리스트에 append
        if os.path.isfile(path):
            files.append(filename)
    # jsonify: json형태로 데이터를 가공
    # return jsonify(files)

    # list.html로 files 리스트를 files라는 이름으로 쏴줌
    return render_template('list.html',files=files)

# data를 넘길때 form: post방식 url의?,/주소값: get방식 
# path타입(경로를 넘길 때)으로 path변수를 넘겨줌
@app.route('/files/<path:path>')
def get_file(path):
    """Download a file."""
    # 전체경로명, 파일명
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

# 파일을 직접 호출했을 때만 동작할 수 있도록 한다.
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8890)
