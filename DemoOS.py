# DemoOS.py
import imp
from os.path import *
from unittest import result

print( abspath("python.exe") )
print( basename("c:\\work\\demo.py:") )
print( getsize("c:\\python39\python.exe") )

from os import *
#system("notepad.exe") #notepad 실행
print("운영체제이름:", name)


#파일 목록
import glob
result = glob.glob(r"c:\work\*.py") # r -> \가 일반문자가 아니다라는 명령
#print(result)
for item in result:
    print(abspath(item))