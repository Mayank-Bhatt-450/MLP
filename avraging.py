import pyautogui,time
from PIL import Image
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''

img = Image.open("Untitled11.jpg")
k=109
t1=508
k1=[0,0,0]
for t in range(3):#row
    for r in range(3):#column
        d=img.getpixel((k+r,t1+t))
        k1[0]+=d[0]
        k1[1]+=d[1]
        k1[2]+=d[2]
k1[0]=k1[0]/9
k1[1]=k1[1]/9
k1[2]=k1[2]/9
print(k1)
'''
#print(img.getpixel((409 ,407)))
for i in range(811):
    for k in range(406):
        t1=(i)#+k
        for t in range(3):#row
            for r in range(3):#column
                try:
                    #print(((t1+r,i+t)))
                    img.getpixel((k+r,t1+t))
                    #print(img.getpixel((t1+r,t1+t)))
                except:
                    print('t1=',t1,'\n',k+r,t1+t)
'''
print('done')

