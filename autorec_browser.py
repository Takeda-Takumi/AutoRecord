from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.alert import Alert

import os
import pathlib
from time import sleep

directory_name = "private"  # fix 何のディレクトリの名前かを詳しく
os.makedirs(directory_name, exist_ok=True)

setting_path = pathlib.Path(
    directory_name + "/AutorecBrowserSetting.txt"
)  # fix setting.txtを自動生成するようにする

with setting_path.open(mode="r") as f: #fix 順番に依存しないで読み込む
    chromedriver_path = f.readline().rstrip()
    meeting_url = f.readline().rstrip()
    student_number = f.readline().rstrip()
    student_passward = f.readline().rstrip()

options = webdriver.ChromeOptions()
options.add_argument('--disable-popup-blocking')
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-desktop-notifications")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

driver.get(meeting_url)

#統合認証ID入力
student_number_bar = driver.find_element_by_xpath("//*[@id=\"username_input\"]")
student_number_bar.send_keys(student_number)

#パスワード入力
student_passward_bar = driver.find_element_by_xpath("//*[@id=\"password_input\"]")
student_passward_bar.send_keys(student_passward)

#loginボタンをクリック
driver.find_element_by_xpath("//*[@id=\"login_button_area\"]/input").click()

sleep(5) # fix 時間以外で同期を取る

#遷移画面
#フレーム操作に変更
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_xpath("/html/body/div/a").click()

#フレーム操作から戻る
driver.switch_to_default_content()

sleep(10)

print()
driver.switch_to.window(driver.window_handles[1])
print()
print(driver.current_url)
print()

#アプリで参加
#フレーム操作に変更
print("browser")
print(driver.find_element_by_xpath("//*[@id=\"push_download_detect_link\"]"))
print(driver.find_element_by_id("push_download_detect_link"))
print(driver.find_element_by_link_text("ブラウザから参加してください。"))
driver.find_element_by_link_text("ブラウザから参加してください。").click()

element = driver.find_element_by_xpath("//*[@id=\"push_download_detect_link\"]")
onclick = element.get_attribute("onlclick")
driver.execute_script(onclick)


#//*[@id="push_download_detect_link"]
#/html/body/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/a
#id="push_download_detect_link


