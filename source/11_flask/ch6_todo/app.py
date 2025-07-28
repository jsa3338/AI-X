from flask import Flask, render_template, request
from flask import redirect, url_for, session, abort  # abort 강제 예외 발생 # session 로그인/로그아웃
from models import TodoRequest
from repository import get_todos, get_next_id, get_todo
from repository import craete_todo, update_todo, delete_todo
import cx_Oracle

app = Flask(__name__)
app.secret_key = 'secret!'
# app.config['SECRET_KEY'] = 'secret!'  # 이렇게 설정하면 변경할 수 없음 둘다 사용가능


@app.route('/')
def index():
    '로그인 성공 로직(세션에 로그인 한 사람의 정보 넣기) 후 /todos 로 리다이렉트'
    session['user_id'] = 'ParkJS'
    session['user_name'] = '박진성'
    # return redirect('/todos')  # /todos(GET) 로 리다이렉트
    return redirect(url_for('todos'))  # todos 함수로 리다이렉트

@app.route('/todos')  # 전체 목록 보기
def todos():
    'todo_data를 list로 변환하여 렌더링'
    ret = get_todos('asc')  # 딕셔너리 리스트로 변환
    order = request.args.get('order', 'asc')  # 정렬 순서 가져오기
    ret = get_todos(order)
    next_id = get_next_id()
    return render_template('todo/todos.html', 
                            todos=ret, 
                            order=order, 
                            next_id=next_id)

@app.route('/logout')
def logout():
    '로그아웃 로직(세션에 로그인 한 사람의 정보 삭제) 후 /todos 로 리다이렉트'
    session.pop('user_id', None)  # 세션에 로그인 한 사람의 정보 삭제
    session.pop('user_name', None)
    return redirect(url_for('todos')) # /todos 함수 로 리다이렉트

@app.route('/todos/<int:id>') # 해당 id 상세보기
def todo(id):
    '해당 id의 todo_data를 렌더링'
    todo = get_todo
    if todo:
        return render_template('todo/todo.html', todo=todo)
    return abort(404, description='해당 id의 할일이 없습니다.')

@app.errorhandler(404)
def not_found(error):
    return render_template('page_not_found.html', error=error), 404

@app.route('/create', methods=['POST'])
def create():
    '새로운 할일 추가'
    # print(request.form.to_dict())
    todo = TodoRequest(**request.form.to_dict()) # type: ignore
    craete_todo(todo)
    return redirect(url_for('todos'))

@app.route('/update/<int:id>', methods=['GET']) # 수정할 수 있는 페이지 가기
def update(id):
    return render_template('todo/update.html', todo=get_todo(id))

@app.route('/update/<int:id>/<string:content>/<string:is_done>', methods=['PUT']) 
def update_data(id, content, is_done):
    todo = TodoRequest(id=id, content=content, is_done=is_done=='True')
    update_todo(todo)
    return f'{id}번 {content} 수정 완료'


if __name__ == '__main__':
    app.run(debug=True)
