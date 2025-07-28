# app.py
from flask import Flask, render_template, request, abort
from models import Member
from filters import mask_password  

app = Flask(__name__)
app.template_filter('mask_pw')(mask_password)  # 필터링 추가

@app.errorhandler(404)  # 404 예외페이지 처리
def errorhandler(error):
    return render_template("404_pageNotFound.html"), 404

@app.route("/")
def index():
    return render_template('2_postetc/index.html')

@app.route("/join", methods=["GET","POST"])
def join():
    if request.method == "GET":
        return render_template("2_postetc/join.html")
    elif request.method == "POST":
        # name = request.form.get('name')
        # id = request.form.get('id')
        # #print(type(id))  # class 'str'
        # pw = request.form.get('pw')
        # addr = request.form.get('addr')
        member = Member(**request.form.to_dict()) # 파라미터를 dict로 변환
        return render_template("2_postetc/result.html", member=member)

@app.route("/update/<name>/<id>/<pw>/<addr>", methods=["PATCH"])
def update(name, id, pw, addr):
    print(name, 'update')
    return f"{name}님 정보가 수정되었습니다"

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    # delte from 테이블명 where id = id를 DBMS에 전송하기
    return f"{id}님 정보가 삭제되었습니다"