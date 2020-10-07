from pynput.mouse import Button, Controller
import time
mouse = Controller()
for i in range(10):
    print(i)
    time.sleep(1)
    mouse.click(Button.left, 1)
