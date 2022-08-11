# db1.py
import sqlite3

#연결객체 생성
con = sqlite3.connect(":memory:")

#커서객체 생성
cur = con.cursor()

#테이블 구조(테이블 스키마 생성)
cur.execute("create table phoneBook (Name text, phoneNum text);")

#입력 파라메터 처리 (웹페이지, 모바일앱)
name = "gildong"
phoneNumber = "001-222"
cur.execute( "insert into phoneBook values (?,?);", (name, phoneNumber) )
#1건 레코드(행)을 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")
#검색
cur.execute("select * from phoneBook;")
for row in cur:
    print(row)
