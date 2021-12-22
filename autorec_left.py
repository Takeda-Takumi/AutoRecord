import sys
import pyautogui
import time
import os

#画面左半分の場合を想定して作る

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

#起動を待つ
time.sleep(300)


os.chdir("")
os.startfile("")
time.sleep(5)

#ミーティングを入力して参加
pyautogui.moveTo(1729,250)
pyautogui.press('backspace')
pyautogui.typewrite()
pyautogui.click(1846, 252)
time.sleep(3)

#パスワード入力して決定
pyautogui.click(483, 425)
pyautogui.typewrite()
pyautogui.click(483, 482)
time.sleep(3)

#ミーティングに参加
pyautogui.click(632, 978)
time.sleep(3)


#録画開始
pyautogui.hotkey('winleft', 'altleft', 'r')

#100分待つ
#time.sleep(10)
time.sleep(6180)

#録画終了
pyautogui.hotkey('winleft', 'altleft', 'r')
time.sleep(3)

#退出
position = pyautogui.locateCenterOnScreen(, confidence = 0.8)
if position == None:
    print("見つけられなかった")
    pyautogui.click(595, 1000)    
else:
    pyautogui.click(position)


time.sleep(3)

pyautogui.click(842, 494)
time.sleep(3)

#アプリ閉じる
pyautogui.click(1885, 36)