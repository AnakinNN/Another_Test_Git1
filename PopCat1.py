"""
This is test fot auto click with the popcat.click.
Note! Just test fot auto click
In this state I do not know how to handle haha.
"""

import pyautogui as pg
import time

loop = 10
clicks = 120

t1 = time.time()
for i in range (loop):
    pg.click(x=305, y=289, clicks=clicks)
    time.sleep(0.01)

t2 = time.time()
total_using_time = t2 - t1
total_click = (loop * clicks) - 1
click_per_sec = total_click/total_using_time
print('Total clicks :', total_click)
print('Total click per sec :', click_per_sec)
print('Time :', t2-t1)