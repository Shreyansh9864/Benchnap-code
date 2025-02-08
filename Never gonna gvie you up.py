# Today i will Tell you best way to rick roll somone without a link just using pythoon let us start the video
# 1. Import PYautogui
import time

import pyautogui
pyautogui.moveTo(488,  1050)
pyautogui.click()
#To find the x,y codinates you have to create a prog for x,y code in description
pyautogui.moveTo( 1078,  978)
pyautogui.click()
#Now file name
file = open("Better than you","r")
content = file.read()
pyautogui.typewrite(content)
pyautogui.press('enter')
