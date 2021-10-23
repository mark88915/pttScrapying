import requests
import datetime
import re
from bs4 import BeautifulSoup

def six_Hour_A_ACIN():
    #取得網頁內容
    my_headers = {'cookie': 'over18=1;'} #通過18禁按鈕驗證
    request = requests.get("https://www.ptt.cc/bbs/AC_In/index.html", headers=my_headers)
    soup = BeautifulSoup(request.content, 'html.parser')

    #取得文章列表標題、時間
    title = soup.find_all('div', class_ = "title")
    date = soup.find_all('div', class_ = "date")
    link = soup.find_all('a', href = re.compile("^/bbs/AC_In/M"))

    #今日時間
    toNow = datetime.datetime.now()
    month = str(toNow.month)
    day = str(toNow.day)
    today = month+'/'+day

    allIWant = ""

    for i in range(len(title)):
        if(date[i].text == today and title[i].text[1:5] == "[洽特]"):
            allIWant += title[i].text + date[i].text + ' www.ptt.cc' + link[i].get('href') + "\n"
            #print(title[i].text + date[i].text + ' www.ptt.cc' + link[i].get('href'))

    return allIWant
six_Hour_A_ACIN()

'''
def search():
    #取得網頁內容
    request = requests.get("https://www.ptt.cc/bbs/index.html")
    soup = BeautifulSoup(request.content, 'html.parser')

    board = soup.find_all('div', class_ = "board-name")
'''