# python -m venv .venv
# pip -m pip --upgrade pip install
# 1. /venv/Scripts/activate (command prompt = ctrl+j, ctrl+`)
# 2. pip install flask

## Jinja2 문법
# 1. 변수 {{ 변수명 }} 또는 {{ 변수명 | 함수명 }} 사용
#   기본제공 필터 : upper, lower, capitalize, length, replace, trim, int, float, string
# 2. 제어문
# 2-1. if 제어문 {% if 조건1 %} A태그 {% elif 조건2 %} B태그 {% else %} C태그 {% endif %}
# 2-2. for 제어문
    # {% for var in vars %} 
    #    loop.index:1부터 순번, loop.index0:0부터 순번 
    #    loop.first:첫번째 라인인지 여부, loop.last:마지막 라인인지 여부 
    # {% endfor %} 
# 3. 해더나 풋터 include  {%include 'header.html'%}
# 4. 서브 태그 {% block 블럭명 %} 내용 {% endblock %}
# 5. 주석 {% comment %} 내용 {% endcomment %} 

from flask import Flask, render_template
from flask import request # 파라미터 값 접근

app = Flask(__name__, 
            template_folder="templates", # 템플릿 폴더 지정
            static_folder="static")      # 정적 파일 폴더(css, js, img,..) 지정 

@app.errorhandler(404) #예외 처리 페이지와 로깅
def not_found(error):
    app.logger.error("없는 페이지입니다")
    return render_template("404.html"), 404

names_list = [] # post 방식으로 넘어온 name을 append

@app.route("/", methods=["GET", "POST"])
def index(no = None):
    if request.method == "POST":
        no = int(request.form.get("no")) # 전달받은 파라미터값(str) -> int  
    return render_template("quiz.html", no=no)

if __name__ == "__main__":
    app.run(debug=True)

