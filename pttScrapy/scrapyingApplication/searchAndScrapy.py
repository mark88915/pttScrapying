import requests
import re
from bs4 import BeautifulSoup

def checkBoardList():
    #取得網頁內容
    my_header = {'cookie': 'over18=1;'} #通過18禁按鈕驗證
    request = requests.get('https://www.ptt.cc/bbs/hotboards.html',headers=my_header)
    soup = BeautifulSoup(request.content, 'html.parser')

    boardName = soup.find_all('div', class_ = "board-name")

    allIWant = ""

    #列出
    for i in range(len(boardName)):
        allIWant += str(i+1) + "." +boardName[i].text + "\n"
    
    allIWant += "---熱門看板---"
    
    return allIWant

def showTheSearchBoard(boardName):

    #取得網頁內容
    my_header = {'cookie': 'over18=1;'} #通過18禁按鈕驗證
    request = requests.get('https://www.ptt.cc/bbs/' + boardName + '/index.html',headers=my_header)
    soup = BeautifulSoup(request.content, 'html.parser')

    #取得文章列表標題、時間
    title = soup.find_all('div', class_ = "title")
    date = soup.find_all('div', class_ = "date")
    link = soup.find_all('a', href = re.compile("^/bbs/" + boardName + "/M"))

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
    
    allIWant = ""

    #列出
    for i in range(len(title)):
        allIWant += title[i].text + date[i].text + ' www.ptt.cc' + link[i].get('href') + "\n"

    #檢查是否有此看板
    if(len(allIWant) == 0):
        allIWant = "※ 不存在此看板或看板名稱大小寫有誤！"

    return allIWant