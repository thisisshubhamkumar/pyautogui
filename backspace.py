import pyautogui
from time import sleep

pyautogui.hotkey("command", "space")
pyautogui.typewrite("Sublime Text.app")
pyautogui.typewrite(["enter"])
sleep(1.5)
pyautogui.hotkey("down", "right")
pyautogui.hotkey("backspace")
x = 1
while x < 161:
    pyautogui.hotkey("down", "right")
    pyautogui.hotkey("backspace")
    x += 1