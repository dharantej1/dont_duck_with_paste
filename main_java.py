import pyautogui
import time

text=open("copy_text.txt")
print("Paste the copied text in 'copy_text.txt' file")
Enter=input("Then Press Enter button here and move to target Page Text Area within 6 seconds")
time.sleep(6)
count=0
for each_line in text:
    each_line=each_line.strip()
    if "{" in each_line:
        count+=1
        pyautogui.typewrite(each_line)
        pyautogui.press("Enter")
    elif "}" in each_line and count > 0:
        each_line.replace("}","")
        count-=1
        pyautogui.press("Down")
        pyautogui.press("Enter")
    else:
        pyautogui.typewrite(each_line)
        pyautogui.press("Enter")
