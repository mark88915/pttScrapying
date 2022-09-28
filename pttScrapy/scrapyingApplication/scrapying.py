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

    #刪除已被刪除的文章
    delList = []

    for articleNo in range(len(title)):
        if("本文已被刪除" in title[articleNo].text):
            delList.append(articleNo)
    
    deleteCount = 0

    for delNo in delList:
        title.pop(delNo-deleteCount)
        date.pop(delNo-deleteCount)
        deleteCount+=1

    #今日時間
    toNow = datetime.datetime.now()
    month = str(toNow.month)
    day = str(toNow.day)
    today = month+'/'+day

    allIWant = ""

    #列出
    for i in range(len(title)):
        if(date[i].text.strip() == today and (title[i].text[1:5] == "[洽特]" or title[i].text == "今泉")):
            allIWant += title[i].text + date[i].text.strip() + ' www.ptt.cc' + link[i].get('href') + "\n"

    if(len(allIWant) == 0):
        allIWant = "今天還沒有新的洽特！"

    return allIWant
six_Hour_A_ACIN()