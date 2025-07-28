# pip install flask_wtf : 플라스크에서 폼 관리하는 기능
    # CSRF 보호 정책 설정 : 동적 웹크롤링 등 방어
    # 쉽고 유연한 폼 적용하여 유효성 검증, input 태그 등 설정

from flask import Flask, render_template
from flask_wtf import FlaskForm # 유효성 검사를 위한 form 객체 생성
from flask_wtf.file import FileField, FileRequired # 파일 업로드 기능 추가
from werkzeug.utils import secure_filename # 암호화 처리
from fileinfo import info # 파일 정보 출력
import os
import uuid
from datetime import datetime


UPLOAD_FOLDER = './uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # 5 MB
app.config['SECRET_KEY'] = 'secret' # uuid.uuid4() # CSRF 보호 정책 설정하기위해 필요

class FileForm(FlaskForm):
    files = FileField(validators=[FileRequired()]) # 업로드한 파일 객체

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FileForm()
    if form.validate_on_submit(): # 폼 유효성 검사(POST 방식이 유효하게 들어왔는지 확인)
        pass
    else: # GET방식이거나 POST요청이 유효하지 않을 경우
        return render_template('upload.html', form=form) # upload.html 수정

if __name__ == '__main__':
    app.run(debug=True)