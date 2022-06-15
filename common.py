import pyperclip as pc
import pyautogui
import time

text=pc.paste()
time.sleep(6)
pyautogui.typewrite(text)
