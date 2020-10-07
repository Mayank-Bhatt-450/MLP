import pyautogui
import time

'''
#it reaches to top in 0.4 second
'''
print('move value: ')
#m=int(input())
while True:
    im = pyautogui.screenshot()
    if (im.getpixel((718, 761))!=(174,21,39)):
        time.sleep(1)
        pyautogui.click(718, 761)
