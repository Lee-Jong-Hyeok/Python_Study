# Form2.py
# Form2.ui(화면단) + Form1.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹서버에 요청
import urllib.request
from bs4 import BeautifulSoup


form_class = uic.loadUiType("Form2.ui")[0]

#화면 클래스 정의 (QMainWindows)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt화면")
    # 슬롯 메서드
    def firstClick(self):
        #파일에 저장 web2.py 소스 가져옴
        f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
        for i in range(1,6):
            #웹서버에 요청해서 실행결과 받기(문자열)
            # \ 는 아래 주소가 길어질때 잇는 다는 문자
            url = \
            "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i) #해당주소의 page= str(i)
            print(url)
            data = urllib.request.urlopen(url)
            #검색에 용이한 객체
            soup = BeautifulSoup(data,"html.parser")
            cartoons = soup.find_all("td", class_="title")
        for item in cartoons:
            title = item.find("a").text.strip()
            print(title)
            f.write(title + "\n")
        f.close()
        self.label.setText("웹 크롤링 작업 완료") 

    def secondClick(self):
        self.label.setText("두번째 작업~~")
    def thirdClick(self):
        self.label.setText("세번째 작업~~")


#직접 모듈을 수행한 경우만 실행(진입점, 엔트리 포인트)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindows = DemoForm()
    demoWindows.show()
    app.exec_() # App.대기
