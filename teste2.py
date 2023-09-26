import random
import pyautogui as pg
import time

words = ('','Voce Mamou!' )
time.sleep(3)


for i in range(500):
    a = random.choice(words)
    pg.write(' ' + a)
    pg.press('enter')