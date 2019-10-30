import pyautogui as pag
import random as rd
import time

def automouse(duration1, duration2, x1, x2, y1, y2, time1, time2):
    duration = rd.uniform(duration1, duration2)
    pag.moveTo(
        x = rd.uniform(x1, x2),
        y = rd.uniform(y1, y2),
        duration = duration
    )
    pag.mouseDown()
    time.sleep(rd.uniform(time1, time2))
    pag.mouseUp()

while (True):

    automouse(0.5, 1.0, 631, 430, 618, 583, 0.0000005, 0.00007)