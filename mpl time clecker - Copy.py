import pyautogui
import time

'''
#it reaches to top in 0.4 second
'''
print('move value: ')
#m=int(input())
k=0
while True:#157 562(589)
    im = pyautogui.screenshot()
    d=im.getpixel((392, 667))
    if ((d[0]>157 and d[0]<243 )and(d[1]>6 and d[1]<82 )and(d[2]>25 and d[2]<93 ))!= True:
        print('started')
        if k == 1:
            time.sleep(0.7)
        else:
            time.sleep(2)
        pyautogui.click(392, 667)
        k+=1

