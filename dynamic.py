import cv2
from os import system
scal = 4

pic = ""

x,y = 480 ,640

if scal == 1:
    sc = 8
elif scal == 2 :
    sc = 16
elif scal == 3 :
    sc = 32
elif scal == 4 :
    sc = 64
else :
    sc = 128
    
u , o= int(x/sc) , int(y/sc)
a , b , c = 0 ,0 ,0

vid = cv2.VideoCapture(0)
ret, frame = vid.read()

while(True):
    
    ret, frame = vid.read()
              
    for i in range(0,x,u):
        for j in range(0,y,o):
            for w in range(0,u):
                for r in range(0,o):
                    if i+w < x and j+r < y:
                        a1 , b1 , c1  = frame[i+w][j+r]
                        a = (a + a1)/2
                        b = (b + b1)/2
                        c = (c + c1)/2

            a = int(a+b+c/3)

            if a<85:
                pic +="$ "
            elif a<170:
                pic +="@ "
            elif a<255:
                pic +="# "
            elif a<340:
                pic +="/ "
            elif a<425:
                pic +=": "
            elif a<510:
                pic +=". "
            else:
                pic +="  "


        pic += "\n"
        
    system('cls')
    print(pic)