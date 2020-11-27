
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
# ChromeDriverManager must be installed on the system
# To install type "pip install webdriver_manager"
# R0cK & R0oL !!
# -----------------------------------------------------------

import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Point(x=998, y=60) >search bar postion >ctrl + shift + r
#ctrl + s > save
#ctrl + shift + r  >run

print(pyautogui.position()) 
pyautogui.click(998, 60)                   #search bar postion
pyautogui.typewrite("spyboy.blog")
pyautogui.typewrite(["enter"])
