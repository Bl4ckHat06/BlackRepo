from pygame import *
perso = image.load('D:\\Desktop\\Projet_ISN_Fini\\Jeux\\RPG_ISN\\data\\perso.png')
scr = display.set_mode((500,500))


class Perso:
    image = []
    
    K_DOWN = []
    K_UP = []
    K_LEFT = []
    K_RIGHT = []
    
    
    #image = dict( [(direction,[perso.subsurface(x,y,64,64)for x in range(0,256,64)]) for direction,y in zip( (K_DOWN,K_LEFT,K_RIGHT,K_UP),range(0,256,64) )] )
    
    for x in range (0,256,64):
        K_DOWN.append(perso.subsurface(x,0,64,64))
    for x in range (0,256,64):
        K_UP.append(perso.subsurface(x, 64,64,64))
    for x in range(0,256,64):
        K_LEFT.append(perso.subsurface(x,128,64,64))
    for x in range(0,256,64):
        K_RIGHT.append(perso.subsurface(x, 192, 64, 64))
        
        
    image.append(K_DOWN)
    image.append(K_UP)
    image.append(K_LEFT)
    image.append(K_RIGHT)
    print(K_DOWN)
    print(image)
    
    
    x,y = 200, 200
    
direction = 0 
index_img = 0

scr.blit(Perso.image[0][index_img],(202,202))
display.flip()
continuer = 1
while continuer:
    
    ev = event.poll()
    if ev.type == QUIT: 
        continuer = 0
        
    k = key.get_pressed()

    for touche in (K_DOWN,K_UP,K_LEFT, K_RIGHT):
        if (k[K_LEFT] and k[K_UP]) or (k[K_RIGHT] and k[K_UP]) or (k[K_DOWN] and k[K_UP]) or (k[K_LEFT] and k[K_DOWN]) or (k[K_DOWN] and k[K_RIGHT]):
                break
        elif k[touche] == True:
            direction = touche
            if direction == 274:
                direction = 0
            if direction == 273:
                direction = 3
            if direction == 276:#left
                direction = 1
            if direction == 275: #right
                direction = 2
            print(direction)
            index_img = (index_img+1)%4
            

            if k[K_LEFT] or k[K_RIGHT]:
                Perso.x += (-k[K_LEFT]+k[K_RIGHT])*8
            elif k[K_UP] or k[K_DOWN]:
                Perso.y += (-k[K_UP]+k[K_DOWN])*8
            
    scr.fill(0) # ajoute un effet de trainée, sinon mettre scr.fill(0)
    scr.blit(Perso.image[direction][index_img],(Perso.x,Perso.y))

    display.flip()
    time.wait(60)