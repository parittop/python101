import pyautogui as pg
import time
import webbrowser as web


url = 'www.google.com'
web.open(url)
time.sleep(2)
print('Start Typing .....')
#pg.typewrite('Hello world!', interval=.25)
#pg.press('enter')
time.sleep(2)

keyword = 'Tottenham Hot spur'
for i in keyword:
    pg.press(i)

pg.press('enter')

time.sleep(2)
pg.screenshot('hello.jpg')

print('Complete.....')
