import pyautogui, time  

time.sleep(5)    
for word in open("script.txt", "r"):  
    pyautogui.typewrite(word) 
    pyautogui.press("enter") 




