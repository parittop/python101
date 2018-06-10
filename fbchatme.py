from fbchat import Client
from fbchat.models import *

import pyautogui as pg
import time
import webbrowser as web

'''
url = 'www.google.com'
web.open(url)
time.sleep(2)
print('Start Typing .....')
pg.typewrite('Hello world!', interval=.25)
pg.press('enter')
time.sleep(2)

keyword = 'Tottenham Hot spur'
for i in keyword:
    pg.press(i)

pg.press('enter')

time.sleep(2)
pg.screenshot('hello.jpg')

print('Complete.....')
'''

client = Client('parit.top@gmail.com', 'pottirap')
print('Own id: {}'.format(client.uid))

user = client.searchForUsers('noonoon.settaumnuay')[0]
#print('User id: {}'.format(user.uid))
'''
users = client.fetchAllUsers()
for user in users:
    print('user list: ', user.name)
'''

#client.send(Message(text='Hi Noonoonnn my wife!'), thread_id=user.uid, thread_type=ThreadType.USER)
client.sendLocalImage('hello.jpg', message=Message(text='เทสส่งรูป'), thread_id=user.uid, thread_type=ThreadType.USER)

client.logout()

print('Logout: ')
