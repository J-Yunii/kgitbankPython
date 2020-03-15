from flask import Flask, render_template
import pymysql, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bootstraptest.html')

# @app.route()
# def formTest():
#     return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8890, debug=True)