#A SUIVRE
import random
from pygame import *
init()
perso = image.load('D:\\Desktop\\Projet_ISN_Fini\\Jeux\\RPG_ISN\\data\\perso.png')
fenetre = display.set_mode((500,500))
BLACK = (1,1,1)
class Block(sprite.Sprite):
    def __init__(self, color, width, height):
        
        #appelle la class parrent sprite (constructeur)
        super().__init__()
        #creer une image du block and rempli avec une couleur
        #ca peut tres bien être une image load
        self.image = Surface([width, height])
        self.image.fill(color)
        
        
        #cherche l'obet rectangle qui a les dimensins de l'image self.image
        #update la position de l'objet en lui attribuant une valuer
        #rect.x et rect.y
        self.rect = self.image.get_rect()

class Perso(sprite.Sprite):
    def __init__(self, perso):
        super().__init__()
        self.x = 200
        self.y = 200
        self.image = []
        self.perso = perso
        self.rect = perso.get_rect()

    def deplacement(self):

        K_DOWN = []
        K_UP = []
        K_LEFT = []
        K_RIGHT = []
        for x in range (0,256,64):
            K_DOWN.append(self.perso.subsurface(x,0,64,64))
        for x in range (0,256,64):
            K_UP.append(self.perso.subsurface(x, 64,64,64))
        for x in range(0,256,64):
            K_LEFT.append(self.perso.subsurface(x,128,64,64))
        for x in range(0,256,64):
            K_RIGHT.append(self.perso.subsurface(x, 192, 64, 64))


        self.image.append(K_DOWN)
        self.image.append(K_UP)
        self.image.append(K_LEFT)
        self.image.append(K_RIGHT)
    
    
#c'est une liste de psrites, tous les murs de ce programme sont ajoutés à cette liste. Cette liste est gerere par une classe appellé Group
block_list = sprite.Group()
#c'est une liste dez tous les sprites
#tous les blocks et le block "joueur" aussi

for i in range(50):
    #le block
    block = Block(BLACK, 20,15)
    #postiion du block
    block.rect.x = random.randrange(500)
    block.rect.y = random.randrange(500)
    print(block.rect.x)
    print(block.rect.y)
    #on ajoute chaque blocks a la  block_list et a all_sprite
    block_list.add(block)
#le perso est déjà creer et gerer



continuer = 1
direction = 0 
index_img = 0
  
    
perso = Perso(perso)
perso.deplacement()
#affiche perso dans la fenetre
fenetre.blit(perso.image[0][index_img],(202,202))
display.flip()

while continuer:
    ev = event.poll()
    if ev.type == QUIT: 
        continuer = 0
        
    k = key.get_pressed()
    
    perso.rect.x = perso.x
    perso.rect.y = perso.y
    perso.rect.height = 64
    perso.rect.width = 64
    print(perso.rect)
    blocks_hit_list = sprite.spritecollide(perso, block_list, True)
    
    for collide in blocks_hit_list:
        print("collision")

    
    for touche in (K_DOWN ,K_UP,K_LEFT, K_RIGHT):
        if k[touche]:
            direction = touche
            if direction == 274: #BAS
                direction = 0
            elif direction == 273:#HAUT
                direction = 3
            elif direction == 276:#left
                direction = 1
            elif direction == 275: #right
                direction = 2
            index_img = (index_img+1)%4

            
            if k[K_LEFT]:
                perso.x -= 8
            elif k[K_RIGHT]:
                perso.x += 8
            elif k[K_UP]:
                perso.y -= 8
            elif k[K_DOWN]:
                perso.y += 8
            break
    else:
        index_img = 0
      

    fenetre.fill((255,255,255))
    fenetre.blit(perso.image[direction][index_img],(perso.x,perso.y))
    block_list.draw(fenetre)

    display.flip()
    time.wait(60)