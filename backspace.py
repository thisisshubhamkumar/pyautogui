  

"""
                  _                 
                 | |                
  ___ ____  _   _| |__   ___  _   _ 
 /___)  _ \| | | |  _ \ / _ \| | | |
|___ | |_| | |_| | |_) ) |_| | |_| |
(___/|  __/ \__  |____/ \___/ \__  |
     |_|   (____/            (____/   
"""
# -----------------------------------------------------------
# Python3 or above must be installed on your System.
# Install pyautogui
# To install type "pip install pyautogui"
# pip install pyobjc (only for mac)
# pip install pyobjc-core (only for mac)
# R0cK & R0oL !!
# -----------------------------------------------------------
import pyautogui
from time import sleep

pyautogui.hotkey("command", "space") #change hotkey() accordingly 
pyautogui.typewrite("Sublime Text.app") #change typewrite() accordingly 
pyautogui.typewrite(["enter"])
sleep(1.5)
pyautogui.hotkey("down", "right")
pyautogui.hotkey("backspace")
x = 1
while x < 161:
    pyautogui.hotkey("down", "right")
    pyautogui.hotkey("backspace")
    x += 1
