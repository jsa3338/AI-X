# pip install flask

todo_data = {
    1 : {
        'id' : 1,
        'title' : 'predict 테이블 만들기(구성확인)',
        'is_done' : True
    },
    2 : {
        'id' : 2,
        'title' : 'EDA 테스트 코드 만들기',
        'is_done' : False
    },
    
}

ret = list(todo_data.values()) # 딕셔너리 리스트
print('첫 실행시 할일들: ', ret)
next_id = max(todo_data.keys()) + 1 if len(todo_data) > 0 else 1
print('다음 추가할 id: ', next_id)
todo_data[next_id] = {
    'id' : next_id,
    'title' : '머신러닝 모델 만들기',
    'is_done' : False
}
ret = list(todo_data.values())
for todo in ret:
    print(todo['id'], todo['title'], '완료' if todo['is_done'] else '미완료')
    print(todo)
    