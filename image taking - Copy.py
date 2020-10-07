import pyautogui,time
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()
while True:
    img = pyautogui.screenshot()
    f=time.time()
    img.save("G:\Downloads\Compressed\scrcpy-win64-v1.8\MLP\data\\"+str(time.time()-k)+'.jpg')
    k=f
