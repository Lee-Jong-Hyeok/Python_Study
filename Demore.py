# Demore.py
import re
#re.search 내용 중 값이 있으면 가져옴
result = re.search("[0-9]*th", "35th")
print( result )
print( result.group() ) # group 메서드 사용하면 보기가 편해짐
# 결과값
# print( result )로 출력된 값 : <re.Match object; span=(0, 4), match='35th'>
# 35th -> group()을 사용하면 위 값보다 깔끔하게 나옴

# re.match 정확히 일치하는 값만 가져옴
# result = re.match("[0-9]*th", "35th")
# print( result )
# print( result.group() )

print( bool(re.search("apple", "this is apple")) )
print( bool(re.match("apple", "this is apple")) )
print( bool(re.search("\d{4}", "올해는 2022년입니다.")) )
print( bool(re.search("\d{5}", "우리동네는 52300")) )

result = re.search("\d{5}", "우리동네는 52300")
print( result.group() )

#전화번호
print("---전화번호 확인---")
telChecker = re.compile("(\d{2,3})-(\d{3,4})-(\d{4})")
result = telChecker.match("02-3429-5000")
print(result.group())
print(result.group(1))
print(result.group(2))