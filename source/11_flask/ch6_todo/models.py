# pip install pydantic
from pydantic import BaseModel

class TodoRequest(BaseModel):

    id: int
    content: str
    is_done: bool | None=False

if __name__ == '__main__':
    todo = TodoRequest(id=1, content='predict 테이블 만들기(구성확인)', is_done=True)
    # print(todo.dict) # todo 객체를 dict로 변환
    print(todo.model_dump()) # todo 객체를 dict로 변환
    todo = TodoRequest(id="2", content='EDA 테스트 코드 만들기') 
    print(todo.model_dump())