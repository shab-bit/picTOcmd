from PIL import Image
def cmder(fname , scal):
    m = []
    im = Image.open('E:\programs\pythone\programs\snak and stairs\snake.jpg')
    
    pix = im.load()
    x,y = im.size
    
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
    
    for j in range(0,y,o):
        for i in range(0,x,u):
            for w in range(0,u):
                for r in range(0,o):
                    if i+w < x and j+r < y:
                        a1 , b1 , c1  = pix[i+w,j+r]
                        a = (a + a1)/2
                        b = (b + b1)/2
                        c = (c + c1)/2
            
            a = int(a+b+c/3)
            
            if not(a in m) :
                m.append(a)
                
                
            if a<85:
                print("$" , end="")
            elif a<170:
                print("@" , end="")
            elif a<255:
                print("#" , end="")
            elif a<340:
                print("/" , end="")
            elif a<425:
                print(":" , end="")
            elif a<510:
                print("." , end="")
            else:
                print(" " , end="")
            
            
        print("")
            
        
            # b = int(a)
            # c = int(a)
            
            
            # for w in range(0,4):
            #     for r in range(0,4):
            #         pix[i+w,j+r] = (a,b,c,d)
    # im.save('E:\programs\pythone\programs\picTOcmd\++.png')

        
# scale and addres
scal = 4
cmder("E:\programs\pythone\programs\picTOcmd\+.png" , scal)