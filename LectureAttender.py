# Google meet lecture attend

import time
import pyautogui
import webbrowser
import datetime

url=input('Enter meeting url :')
def join():
    webbrowser.open(url)
    time.sleep(20)
    pyautogui.click(488, 577)
    pyautogui.click(409, 577)
    pyautogui.click(993, 416)

hr = int(datetime.datetime.now().hour)

while True:
    if hr == 23:
        join()
        break
