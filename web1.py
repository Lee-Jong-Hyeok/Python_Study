# web1.py
# 웹크롤링(데이터 수집)
from bs4 import BeautifulStoneSoup

#메서드 체인:연속으로 함수나 메서드 호출
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulStoneSoup(page, "html.parse") # "html.parse" -> 정해진 규칙
# 문서 정렬
# print( soup.prettify() )
# <P>를 몽땅 검색  
# print( soup.find_all("P") )  
# 첫번째 <P>태그 
# print( soup.find("P") )
# 조건이 있는: <P class='outer-text'> 필터링
# 파이썬의 키워드 class --> class_
# print( soup.find_all("P", class_="outer-text") )

#내부 문자열 추출 
for item in soup.find_all("P"):
    #컨텐츠: ~.txt
    title = item.text.strip()
    title = title.replace("\n","")
    print(title)
