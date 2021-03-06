from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from . import searchAndScrapy

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if(event.message.text == "檢查看板"):
                    line_bot_api.reply_message(  
                        event.reply_token,
                        TextSendMessage(text=searchAndScrapy.checkBoardList())
                    )
                elif(event.message.text == "說明"):
                    line_bot_api.reply_message(  
                        event.reply_token,
                        TextSendMessage(text="1.輸入'檢查看板'可以查看所有熱門看板名稱\n\n2.輸入欲查詢的看板名稱可查詢該看板的文章\n\n※ 為防止接收過多的內容(較熱門的看板一天會有超過10頁的文章)，將爬取範圍限定在第一頁。")
                    )
                else:
                    line_bot_api.reply_message(  
                        event.reply_token,
                        TextSendMessage(text=searchAndScrapy.showTheSearchBoard(event.message.text))
                    )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
