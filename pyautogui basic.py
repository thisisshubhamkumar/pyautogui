import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Point(x=998, y=60) >ctrl + shift + r
#ctrl + s > save
#ctrl + shift + r  >run

print(pyautogui.position())
pyautogui.click(998, 60)
#pyautogui.typewrite("spyboy blog")
#pyautogui.typewrite(["enter"])
pyautogui.hotkey("command", "c")
pyautogui.hotkey("command", "space")
sleep(3.5)
pyautogui.hotkey("command", "v")