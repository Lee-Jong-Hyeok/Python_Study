# DemoStr.py
import re


strA = "python is very powerful"
strB = "파이썬은 강력해"
print( len(strA) )
print( len(strB) )
print( strA.capitalize() ) # 첫문자를 대문자로 변경
print( strA.count("p") ) # p가 몇번 나왔는지
print( strA.count("p", 7) ) # ?
print( strA.startswith("py") ) #py로 시작?
print( strA.endswith("ful") ) #py로 끝나?

print( "MBC2580".isnumeric() )
print( "MBC:2580".isnumeric() )
print( "2580".isnumeric() )

#문자열 전처리(데이터)
strC = "<<< spam and ham >>>"
result = strC.strip("<> ")
print(strC)
print(result)

#문자열 전처리(데이터)
print("---치환---")
result = result.replace("spam","spam egg")
print(result)
lst = result.split()
print(lst)
print("---다시 합치기---")
print( ":)".join(lst) ) # 합칠때 구분자 ":)"