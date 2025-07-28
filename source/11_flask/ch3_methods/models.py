# class Member:
#     def __init__(self, name, id, pw, address):
#         self.name = name
#         self.id = id
#         self.pw = pw
#         self.address = address
# pip install pydantic

from pydantic import BaseModel, Field

class Member(BaseModel):  # 유효성 검증을 해주는 클래스
    name:str = Field(min_length=2, max_length=10, description="이름")
    id:int  = Field(gt=0, lt=100, description="아이디")
    # gt=0 : id>0, ge=0 : id>=0, lt=100 : id<100, le=100 : id<=100
    pw:str
    address:str  = Field(default="서울", description="주소")
if __name__=="__main__":
    member=Member(name="hong", id=11, pw="1234", address="서울")
    print(member)