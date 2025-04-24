# Customer 클래스 선언. 
class Customer:
    ' 고객데이터와 as_dic(), to_list_style(txt백업시), __str__()'
    def __init__(self, name, phone, email, age, grade, etc):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.grade = grade
        self.etc = etc
        
    def as_dict(self): #객체를 딕셔너리데이터로 반환 (csv 파일 저장시)
        return {
            'name':self.name,
            'phone':self.phone,
            'email':self.email,
            'age':self.age,
            'grade':self.grade,
            'etc':self.etc
        }
    
    def to_list_style(self): #객체를 list return([ 홍길동 010 8999 9999, e@e.com, 20, 3, 까칠해]_
        temp = [
            self.name,
            self.phone,
            self.email,
            str(self.age),
            str(self.grade),
            self.etc
        ]
        return ','.join(temp)
            
    def __str__(self): # ***홍길동 010 8999 9999 e@e.com 20 까칠해
                return "{:>5}\t{:^4}\t{:13}\t{:16}\t{:3}\t{:5}".format('*'*self.grade,
                                                                        self.name,
                                                                        self.phone,
                                                                        self.email,
                                                                        self.age,
                                                                        self.etc
                                                                         )
# txt 파일내용 한 줄을 row 매개변수로 받아 Customer 객체로 return
def to_customer(row):
    '''
    row = "홍길동 , 010 8999 9999, e@e.com, 20, 3, 까칠해"(txt파일 내용)을 매개변수로 받아 Customer 객체로 return
    '''
    data = row.split(',')
    name = data[0].strip()
    phone = data[1].strip()
    email = data[2].strip()
    age = int(data[3].strip())
    grade = int(data[4].strip())
    etc = data[5].strip()
    return Customer(name, phone, email, age, grade, etc)

# 0.실행하면 data/ch09_customers.txt 파일의 내용을 load(customer_list)
# data/ch09_customers.txt 이 존재하지 않으면
#빈 data/ch09_customers.txt 파일을 생성하고
#데이터는 customer_list=[]

def load_customers():
    customer_list=[]
    try:
        with open('data/ch09_customs.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                customer = to_customer(line)
                customer_list.append(customer)
        print('데이터가 로드 되었습니다.')
    except:
        with open('data/ch09_customs.txt', 'w', encoding='utf-8') as f:
            f.writelines(customer_list)
            print('고객 리스트 파일이 없어, 새로운 파일을 생성합니다')
    return customer_list 

# 1.입력
def fn1_insert_customer_info():
    '''
    사용자로 부터 이름, 번호, 메일, 나이, 등급, etc를 입력받아 Customer형 객체 반환
    '''
    name = input('이름 : ')
    phone = input('전화번호 : ')
    email = input('이메일 : ')
    while True:
        try:
            age = int(input('나이 : '))
            break
        except:
            print('나이를 잘못 입력하셨습니다. 정수를 입력하세요')
    while True:
        try:
            grade = int(input('고객등급(1~5) : '))
            if 1<=grade<=5:
                break
        except:
            print('고객등급을 잘못 입력하셨습니다. 1~5 사이의 수를 입력하세요')
    etc = input('기타정보 : ')
    new_data=Customer(name, phone, email, age, grade, etc)
    return new_data

# 2.전체 출력
def fn2_print_customers(customer_list):
        print('='*80)
        print('\t\t고객  정보')
        print('-'*80)
        print("{:>5}\t{:^4}\t{:13}\t{:16}\t{:3}\t{:5}".format('Grade', '이름', '전화', '메일', '나이','기타'))
        print('='*80)
        for customer in customer_list:
            print(customer)
        print('='*80)

# 3. 삭제 - 동명이인 있을 경우 선택 삭제
def fn3_delete_customer(customer_list):
    delete_name = input('삭제할 고객 이름은? ')
    delelte_idx = []
    for idx, customer in enumerate(customer_list):        
        if customer.name == delete_name:
            delelte_idx.append(idx)
  
    if delelte_idx:
        for idx in delelte_idx[::-1]: 
            print(customer_list[idx], '지우겠습니까?', end='')
            answer = input('(Y/N)')
            if answer.upper() == 'Y':
                print(f'{delete_name}님 ({customer_list[idx].phone})데이터를 삭제했습니다.')
                del customer_list[idx]
    else:
        print(f'{delete_name}님 데이터가 존재하지 않습니다')
        
# 4.찾기
def fn4_search_customer(customer_list):
    search_name = input('찾을 고객 이름은? ')
    search_list = []
    for customer in customer_list:
        if search_name == customer.name:
            search_list.append(customer)
    if search_list:
        fn2_print_customers(search_list)
    else:
        print(f'{search_name} 고객님을 찾지 못했습니다.')
        

# 5.내보내기 (csv)
def fn5_save_customer_csv(customer_list):
    '매개변수로 받은 customer_list를 딕셔너리리스트로 변환해서 csv출력'
    if customer_list:
        import csv
        customer_dict_list = []
        for customer in customer_list:
            customer_dict_list.append(customer.as_dict())

        fieldnames = list(customer_dict_list[0].keys())
        fieldname = input('저장할 csv 파일명은?')
        with open('data/{}.csv'.format(fieldname), 'w', encoding='utf-8', newline='') as f: 
                                                                # newline=''을 안쓰면 기본값이 \n이기 때문에 줄바꿈이 된다. 필수로 챙겨야겠다.
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            dict_writer.writeheader() # 헤더
            dict_writer.writerows(customer_dict_list)
            print(f'data/{fieldname}.csv 내보내기 완료')
    else:
        print('입력된 회원이 없습니다. 내보내기가 취소됩니다.')

        
# 9. 종료하기 (저장)
def fn9_save_customer_txt(customer_list):
    "매개변수로 받은 customer_list를 ['홍길동, 010-8999-9999, e@e.com, 20, 3, 까칠해'] 로 바꿔서 저장"
    customer_txt_list = []
    for customer in customer_list:
        customer_txt_list.append(customer.to_list_style()+'\n')
    with open('data/ch09_customs.txt', 'w', encoding='utf-8') as f:
        f.writelines(customer_txt_list)

        
# 컨트롤러 함수 설정
def main():
    global customer_list
    customer_list = load_customers() # ch09_customers.txt 의 내용을 load
    while True:
            print("1:입력","2:전체출력","3:삭제","4:이름찾기","5:내보내기(CSV)", "9.종료", sep='|', end=' ')
            print()
            fn = int(input('메뉴선택 : '))
            if fn == 1:
                customer = fn1_insert_customer_info() #입력받은 내용으로 customer 객체를 반환
                customer_list.append(customer)
            elif fn == 2:
                fn2_print_customers(customer_list)
            elif fn == 3:
                fn3_delete_customer(customer_list)
            elif fn == 4:
                fn4_search_customer(customer_list)
            elif fn == 5:
                fn5_save_customer_csv(customer_list)
            elif fn == 9:
                fn9_save_customer_txt(customer_list)
                break
            else:
                print('메뉴를 잘못 입력하셨습니다')   

                
# 회원관리 프로그램 시작                
if __name__ == '__main__':
    main()