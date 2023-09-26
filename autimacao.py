import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(5)

link = "192.168.0.141/frangolandia"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=970, y=562)
pyautogui.write("teste")
pyautogui.press("tab")

pyautogui.write("teste321")
pyautogui.press("tab")
pyautogui.press("enter")