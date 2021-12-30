import sys
import pyautogui
import time
import os
import pathlib

# 画面左半分の場合を想定して作る

directory_name = "private"  # fix 何のディレクトリの名前かを詳しく
os.makedirs(directory_name, exist_ok=True)

setting_path = pathlib.Path(
    directory_name + "/setting.txt"
)  # fix setting.txtを自動生成するようにする

with setting_path.open(mode="r") as f:
    app_path = f.readline().rstrip()
    meeting_number = f.readline().rstrip()
    password = f.readline().rstrip()

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# アプリを起動
os.startfile(app_path)
print("アプリを起動しています")

# 起動を待つ
time.sleep(5)

# ミーティングを入力して参加
pyautogui.moveTo(1729, 250)
pyautogui.press("backspace")
pyautogui.typewrite(meeting_number)
pyautogui.click(1846, 252)
time.sleep(3)

# パスワード入力して決定
pyautogui.click(483, 425)
pyautogui.typewrite(password)
pyautogui.click(483, 482)
time.sleep(3)

# ミーティングに参加
pyautogui.click(632, 978)
time.sleep(3)

# 録画開始
pyautogui.hotkey("winleft", "altleft", "r")

# 100分待つ
# time.sleep(10)
time.sleep(6180)

# 録画終了
pyautogui.hotkey("winleft", "altleft", "r")
time.sleep(3)

# 退出
# 退出ボタンを画像認識によって見つけてクリックする処理だが
# 面倒くさいので一旦コメントアウトします
# position = pyautogui.locateCenterOnScreen(, confidence = 0.8)
# if position == None:
#     print("見つけられなかった")
#     pyautogui.click(595, 1000)
# else:
#     pyautogui.click(position)

pyautogui.click(595, 1000)

time.sleep(3)

pyautogui.click(842, 494)
time.sleep(3)

# アプリ閉じる
pyautogui.click(1885, 36)
