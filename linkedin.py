import pyautogui
import time

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('msedge')
pyautogui.press('enter')

time.sleep(1)
# Focus on the address bar
pyautogui.hotkey('alt', 'd')
pyautogui.typewrite('https://www.linkedin.com/',interval=0.05)
pyautogui.typewrite(["enter"]) # pressing the Enter key


time.sleep(2)
#typing name in linkedin search bar
pyautogui.moveTo(381,117,duration=1)
pyautogui.click()
pyautogui.typewrite("Ashutosh Kumar",interval=0.05)

#Going to the specific search 

pyautogui.hotkey('alt', 'd')
pyautogui.typewrite('https://www.linkedin.com/in/ashutoshpw/')
pyautogui.typewrite(["enter"])

time.sleep(2)

#For Follow the Person
pyautogui.moveTo(470,659,duration=1)
pyautogui.click()

time.sleep(1)

#For MORE option
pyautogui.moveTo(606,667,duration=0.1)
pyautogui.click()

time.sleep(1)

#For Connect 
pyautogui.moveTo(665,848,duration=0.05)
pyautogui.click()