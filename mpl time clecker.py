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
    clp=0
    for i in range(200):
        if k==0:
            d=im.getpixel((618+i, 621))
            clp=618+i
        else:
            d=im.getpixel((818+i, 549))
            clp=818+i
        if ((d[0]>82 and d[0]<156 )and(d[1]>160 and d[1]<230 )and(d[2]>190 and d[2]<255 )):
            print('started',clp, 541)
            pyautogui.click(clp, 541)
            k+=1
            time.sleep(1)
            break

