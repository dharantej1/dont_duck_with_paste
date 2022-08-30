import pyautogui
import time

text=open("copy_text.txt")
print("Paste the copied text in 'copy_text.txt' file")
Enter=input("Then Press Enter button here and move to target Page Text Area within 6 seconds")
time.sleep(6)
for each_line in text:
    each_line=each_line.strip()
    pyautogui.typewrite(each_line)
    pyautogui.press("Enter")
    
