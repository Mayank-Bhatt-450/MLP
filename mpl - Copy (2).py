from pynput.mouse import Listener
import logging
import pyautogui
import threading 
import ctypes 
import time 
print('move value: ')
#m=int(input())
class thread_with_exception(threading.Thread): 
    def __init__(self, name): 
        threading.Thread.__init__(self) 
        self.name = name 
              
    def run(self): 

        # target function of the thread class 
        try: 
            while True:
                time.sleep(1)
                pyautogui.click(723, 488)
                print('lol')#'''
        finally: 
            print('ended') 
           
    def get_id(self): 

        # returns id of the respective thread 
        if hasattr(self, '_thread_id'): 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                return id

    def raise_exception(self): 
        thread_id = self.get_id() 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure') 
t1 = 0
def reset():
    global t1
    t1 = thread_with_exception('Thread 1')
def on_press(x, y, button,pressed):
    print('in')
    global t1,reset
    if pressed:
        reset()
        #t1 = thread_with_exception('Thread 1') 
        print('pressed')
        t1.start()
    else:
        pass
        #t1.raise_exception() 
        #t1.join() 
    

with Listener( on_click=on_press) as listener:
    listener.join()
