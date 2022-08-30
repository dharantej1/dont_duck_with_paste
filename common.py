import pyperclip as pc
import pyautogui
import time

text=pc.paste()
print("Copy the required text to the ClipBoard!")
Enter=input("Then Press Enter button here and move to target Page Text Area within 6 seconds")
time.sleep(6)
pyautogui.typewrite(text)
