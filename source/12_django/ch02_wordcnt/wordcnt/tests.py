from django.test import TestCase
# Create your tests here.
def test():
    fulltxt='홍길동 홍길동 아자'
    strlength = len(fulltxt) # 글자수
    words=fulltxt.split() # 단어로 분리
    wordcnt = len(words)
    words_dic = dict() # 빈 딕셔너리 {'홍길동' : 2, '아자' : 1}
    for word in words:
        if word in words_dic.keys():
            words_dic[word] +=1
        else:
            words_dic[word]=1

    print('글자수 :', strlength)
    print('단어들 :', words)
    print('단어수 :', wordcnt)
    print('출현단어(dict) :', words_dic)
    print('출현단어(list) :',  words_dic.items())

if __name__=='__main__':
    test()