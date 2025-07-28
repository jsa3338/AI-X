# (가성환경 생성 방법1) python -m venv .venv 
# (가성환경 생성 방법2) ctrl+shift+p => select interpreter => 가상환경 만들기 => 인터프리터 경로 선택 => 아나콘다 폴더 내에 python.exe 선택
# .venv\Scripts\activate  (가상환경 들어가기)
# python -m pip install --upgrade
# pip install flask
from flask import Flask, render_template, request, abort
# request : get/post 방식으로 파라미터 데이터 받기  / abort : 강제로 예외발생

from models import Member  # 조금 전 내가 만든 클래스

app = Flask(__name__)

# 필터링 추가 (str -> str문자 개수만큼 *)
@app.template_filter("mask_pw")
def mask_password(password):
    return len(password)*"*"

@app.route("/user/<name>", methods=["GET"])  # /user/hong,  methods=["GET"] 은 기본값.생략가능
def viewFunction_handlerFunction(name):
    return f"<h1>{name}님 환영합니다</h1>"

@app.route("/user")  # /user?name=hong
def user ():
    name = request.args.get('name')
    if name:
        return f"<h1>전달받은 파라미터 이름 : {name}님</h1>"
    else:
        abort(404)

@app.errorhandler(404)  # 404 예외페이지 처리
def errorhandler(error):
    return render_template("404_pageNotFound.html"), 404

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/join_form", methods=["GET"])
def join_form():
    return render_template("1_onlyget/join.html")

@app.route("/join", methods=["GET"])
def join():
    name = request.args.get('name') # get 방식
    id = request.args.get('id')
    pw = request.args.get('pw')
    addr = request.args.get('addr')
    member = Member(name, id, pw, addr)
    return render_template("result.html", member=member)


if __name__=="__main__":
    app.run(debug=True, port=80)