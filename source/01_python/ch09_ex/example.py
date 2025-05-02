
from customer import to_customer, load_customers
from fuctions import fn1_insert_customer_info, fn2_print_customers, fn3_delete_customer, fn4_search_customer, fn5_save_customer_csv, fn9_save_customer_txt 


# 컨트롤러 설정
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
    
