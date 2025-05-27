# 피보나치 배열을 리턴하는 함수 만들기
def fibonaccii_print(n):
    '''
    매개변수로 들어온 n값 미만의 피보나치 수열을 출력
    ex. n=10 이면 0 1 1 2 3 4 8 을 출력
    '''
    f1, f2=0,1    
    while f1 < n:
        print(f1, end=" ")
        f1, f2 = f2, f1+f2
    print()
    
def fibonacci_return(n):
    '''
    매개변수로 들어온 n값 미만의 피보나치 수열을 리스트로 return
    ex. n=10 이면 [0 1 1 2 3 4 8] 를 만들어서 return
    '''
    F = []
    f1, f2=0,1
    while f1 < n:
        F.append(f1)
        f1, f2 = f2, f1+f2
    return F             # return은 하나 값만 리턴할 수 있다.
#'테스트 : python fibo.py / python fibo.py 100'
if __name__ == "__main__":
    import sys
    print(sys.argv)
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print('1, print test :', end='')
        fibonaccii_print(n)
        print('2. return test :', fibonacci_return(n))
    else:
        print('1, print test : ', end=' ')
        fibonaccii_print(100)
        print('2. return test :', fibonacci_return(100))



