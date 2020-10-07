from pynput.mouse import Listener
import logging
import pyautogui
import threading 
import ctypes 
import time
for i in range(10):
    print('time')
    time.sleep(1)
    pyautogui.press('h')
    #pyautogui.click(720+(i), 501)
