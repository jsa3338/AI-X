from flask import Flask
app = Flask(__name__) # 웹인스턴스 생성
@app.route("/")
def handler_viewFunc():  # 핸들러 혹은 뷰 함수라고 한다
    return "<h1>Hello, World</h1>"

# 파일명이 app.py 이면 실행은 flask run --debug --port=80   / --debug --port=80은 생략 가능
# 파일명이 app.py가 아니면 if문을 구현하고 python 파일명
if __name__=="__main__":
    app.run(port=80, debug=True)