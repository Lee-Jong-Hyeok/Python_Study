# DemoFunction2.py
# 이름을 해석하는 규칙 순서(Local(지역), Global(전역), built-in: LGB규칙)

# 전역변수
x = 5
#함수정의 
def func1(a):
    return a+x
#호출
print(func1(1))

#함수정의
def func2(a):
    #지역변수
    x = 2
    return a+x
#호출
print(func2(1))
