# http://127.0.0.1:80/5000/join?id=aaa&pw=111 (static)
# http://127.0.0.1:80/5000/join/aaa/111 (dynamic)
from flask import Flask, url_for
app = Flask(__name__)
@app.route("/")  # static(정적) 라우팅
def hello():
    return "<h1>hello</h1>"

@app.route("/porfile/<name>/<age>")  # dynamic(동적) 라우팅
def get_profile(name, age):
    return "<h1>profile : {}님 {}살입니다</h1>".format(name, age)

if __name__=="__main__":
    # 플라스크가 http 요청 관련 정보를 활성화 하여 정보 출력
    with app.test_request_context():
        print('hello 뷰함수의 요청경로 :', url_for('hello'))
        print("http://127.0.0.1:80"+url_for("get_profile", name='hong', age=24))
    app.run(debug=True, port=80)