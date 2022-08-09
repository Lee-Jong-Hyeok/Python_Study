# DemoFunction1.py

#함수 정의
from copy import copy


def setValue(newValue):
    x = newValue

#호출
returnValue = setValue(5)
print(returnValue)

#함수 정의
def swap(x,y):
    return y,x

#호출
print( swap(3,4) )

print("---불변형식---")
a = 1.2
print( id(a) )

a = 2.3
print( id(a) )

print( globals() )

print("---가변형식---")
lst = [1,2,3]

print( id(lst) )

lst.append(4)
print( id(lst) )


#입력 + 출력이 되는 경우
def change(x):
    x[0] = "H"

#입력데이터
wordlist = ["J","A","M"]
change(wordlist)
print("호출후:", wordlist)

#deep copy 사용
print("---복사본 사용---")

def change(x):
    #deep copy를 통해 복사본을 수정
    x1 = x[:] #list
    x1[0] = "H"
    print("함수내부:", x1)

#입력데이터
wordlist = ["J","A","M"]
change(wordlist)
print("호출후:", wordlist)

#리스트가 아닌경우
import copy #copy함수 사용
device = {"아이폰":5, "아이패드":10} #dict
device2 = copy.deepcopy(device)
device2["맥북"]=20
print(device2)