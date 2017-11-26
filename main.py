from pygame import *
from pygame.locals import *
from classes import * 
from constantes import *


init()

fenetre = display.set_mode((cote_fenetre, cote_fenetre))
icone = image.load(image_icone)
display.set_icon(icone)

titre = display.set_caption(titre_fenetre)

perso = image.load('D:\\Desktop\\Projet_ISN_Fini\\Jeux\\RPG_ISN\\data\\perso.png')

continuer = 1
direction = 0 
index_img = 0

lvl = Niveau(n2)
lvl.load_lvl()
lvl.afficher_lvl(fenetre)
perso = Perso(perso)
perso.deplacement()
fenetre.blit(perso.image[0][index_img],(202,202))
display.flip()
continuer = 1
while continuer:
    
    ev = event.poll()
    if ev.type == QUIT: 
        continuer = 0
        
    k = key.get_pressed()

    for touche in (K_DOWN ,K_UP,K_LEFT, K_RIGHT):
        if (k[K_LEFT] and k[K_UP]) or (k[K_RIGHT] and k[K_UP]) or (k[K_DOWN] and k[K_UP]) or (k[K_LEFT] and k[K_DOWN]) or (k[K_DOWN] and k[K_RIGHT]) or (k[K_RIGHT] and k[K_LEFT]):
                break
        elif k[touche] == True:
            direction = touche
            if direction == 274: #BAS
                direction = 0
            if direction == 273:#HAUT
                direction = 3
            if direction == 276:#left
                direction = 1
            if direction == 275: #right
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
            
            fenetre.fill((255,255,255))
            lvl.afficher_lvl(fenetre) # ajoute un effet de trainée, sinon mettre scr.fill(0)
            fenetre.blit(perso.image[direction][index_img],(perso.x,perso.y))

    display.flip()
    time.wait(60)