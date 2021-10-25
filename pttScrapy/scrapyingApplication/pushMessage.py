from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot.models import TextSendMessage
import scrapying

CHANNEL_ACCESS_TOKEN = "tbLH9BRyZkcnXvQpCxgwpbpe6ddX3P3JcN5+rlE10hYSbzxuawmYjWKtYR45OYWJ/WT62cbmICSVI15Y8ZWkDymWul8lyDrGDYsRaTrtlw1/7v+MnNegL46mI0/UZcC7TN63/GoakCtQ04Mzuws4PgdB04t89/1O/w1cDnyilFU="

to = 'U5b46e8411c37e1529b3aa0698cdec353'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

try:
    line_bot_api.push_message(to, TextSendMessage(text=scrapying.six_Hour_A_ACIN()))
except LineBotApiError as e:
    #錯誤處理
    raise e