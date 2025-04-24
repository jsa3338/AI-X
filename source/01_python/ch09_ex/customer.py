# customer.py = Customer 클래스, to_customer(), load_customer()

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


# txt -> 객체 변환용
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