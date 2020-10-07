import pyautogui,time
from pynput.mouse import Listener
k=time.time()
s=0
def fun():
    print ('in fun')
    #'''
    while True:
        time.sleep(1)
        pyautogui.click(723, 488)
        print('lol')#'''
def on_press(x, y, button,pressed):
    print('call fun')
    #global fun
    fun()

with Listener( on_click=on_press) as listener:
    listener.join()
