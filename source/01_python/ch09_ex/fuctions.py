# functions.py => fn1()~fn9() 입력, 출력, 삭제, 찾기, 종료(+저장)
from customer import Customer
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