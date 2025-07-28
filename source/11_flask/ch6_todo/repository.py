import cx_Oracle

conn = cx_Oracle.connect("scott", "tiger", "210.121.189.12:1521/xe")

from models import TodoRequest
from typing import List # 타입체크

def get_todos(order) -> List[TodoRequest]:
    cursor = conn.cursor()
    if order == "asc":
        sql = "SELECT * FROM TODO ORDER BY ID;"
    else:
        sql = "SELECT * FROM TODO ORDER BY ID DESC;"
    cursor.execute(sql)
    keys = [desc[0] for desc in cursor.description]  # ['id', content', 'is_done']
    todos = [dict(zip(keys, row)) for row in cursor.fetchall()]
    cursor.close()
    return todos

def get_next_id() -> int:
    cursor = conn.cursor()
    sql = "SELECT NVL(MAX(ID), 0)+1 FROM TODO"
    cursor.execute(sql)
    result = cursor.fetchone() # 튜플 (4,)
    cursor.close()
    return result[0]

def get_todo(id:int) -> dict:
    cursor = conn.cursor()
    sql = "SELECT * FROM TODO WHERE ID = :Sid"
    cursor.execute(sql, {'id': id})
    result = cursor.fetchone() # 튜플 (1, '바꿀내용', 0)
    cursor.close()
    return {'id': result[0], 'content': result[1], 'is_done': result[2]}

def craete_todo(todo:TodoRequest) -> int:
    cursor = conn.cursor()
    sql = """
    INSERT INTO TODO (ID, CONTENTS, IS_DONE) VALUES (:id, :content, :is_done);
    """
    cursor.execute(sql, todo.model_dump())  # todo를 dict 형태로 변환
    conn.commit()
    cursor.close()
    return cursor.rowcount # 추가 성공시 1, 실패시 0

def update_todo(todo:TodoRequest) -> int:
    cursor = conn.cursor()
    sql = """
    UPDATE TODO SET CONTENTS = :content, IS_DONE = :is_done WHERE ID = :id;
    """
    cursor.execute(sql, todo.model_dump())
    conn.commit()
    cursor.close()
    return cursor.rowcount

def delete_todo(id:int) -> int:
    cursor = conn.cursor()
    sql = "DELETE FROM TODO WHERE ID = :id"
    cursor.execute(sql, {'id': id})
    conn.commit()
    cursor.close()
    return cursor.rowcount

if __name__ == '__main__':
    print('/todos : ',get_todos('asc'))
    print('next_id : ', get_next_id())
    print('/todos/1', get_todo(1))
    