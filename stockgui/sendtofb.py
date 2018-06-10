# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *
import stockchecker

stockname,stockprice = stockchecker.checkprice('SCB')
#print(stockname,stockprice)

client = Client('parit.top@gmail.com', 'pottirap')

print('Own id: {}'.format(client.uid))
#user = client.searchForUsers('noonoon.settaumnuay')[0]

client.send(Message(text='ราคาหุ้น:'+stockname+'\nล่าสุด: '+ stockprice), thread_id=client.uid, thread_type=ThreadType.USER)
#client.send(Message(text='ปล. จากสามี 55'), thread_id=user.uid, thread_type=ThreadType.USER)

client.logout()
