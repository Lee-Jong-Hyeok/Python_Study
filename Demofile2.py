# Demofile2.py
# 파일쓰기
#f = open("c:\\work\\demo.txt", "wt", encoding="utf-8") # utf-8 유니코드 읽기쓰기 사용 정의, \t -> Tab 인식하기 때문에 \\붙여줌
#raw string notation(r)
# f = open(r"c:\work\test1.txt", "wt", encoding="utf-8")
#linux, unix
# f = open("c:/work/test2.txt", "wt", encoding="utf-8")
# f = open("c:\\work\\test1.txt", "rt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close

#파일읽기 
f = open("c:\\work\\test1.txt", "rt", encoding="utf-8")
print( f.read() )
print( f.tell() )
#다시 처음으로 돌아가기
f.seek(0)
# lst = f.readlines()
# print(lst)

print("---한줄씩---")
print( f.readline(), end="")
print( f.readline(), end="")
f.close