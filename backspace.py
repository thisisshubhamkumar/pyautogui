  

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

#pyautogui.hotkey("command", "space") #change hotkey() accordingly 
#pyautogui.typewrite("Sublime Text.app") #change typewrite() accordingly 
#pyautogui.typewrite(["enter"])
sleep(5)  #change sleep time accordingly
pyautogui.hotkey("down", "right")
pyautogui.hotkey("backspace")
x = 1
while x < 300: # #change loop number accordingly 
    pyautogui.hotkey("down", "right")
    pyautogui.hotkey("backspace")
    x += 1
# -----------------------------------------------------------
# there r times when u need to press some key hundreds of time for some specific task like >> need to press (delete/backspace) key in my code to remove some error.
# i write this code to fix (IndentationError:) in python but it can be used anywhere.
# so i made this bot >> programmed it to run specific keystroke on loop.
# so whn u run the code >> "there’s sleep time of 5 sec">> manually open that specific file put the cursor form where wanna bot to work & then >> it automatically start pressing "down arrow key, right arrow key, backsapce.
# & then it will repeat same thing 300 times.
# -----------------------------------------------------------
