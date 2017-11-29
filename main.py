from pygame import *
from pygame.locals import *
from classes import * 
from constantes import *
  

init()
#chargement fenetre
fenetre = display.set_mode((915, 469))
icone = image.load(image_icone)
display.set_icon(icone)
titre = display.set_caption(titre_fenetre)

#load les image
perso = image.load('D:\\Desktop\\Projet_ISN_Fini\\Jeux\\RPG_ISN\\data\\perso.png')
image_fond = image.load(image_fond).convert()
station = image.load(image_station).convert()

#initilisation des variables
continuer = 1
direction = 0 
index_img = 0

#charge niveau
lvl = Niveau(n2)
lvl.load_lvl()
fenetre.fill((255,255,255))

#creation d'une liste qui collete les blocks de la partie
block_list = sprite.Group()

#fonctions quia ffiche le niveau, et mets les blocs selectionner dans la liste avec un pour m->Rect(x, y 20,20) et a->Rect(x,y, 200,300)
def afficher_lvl(fenetre, block_list): 
    num_ligne = 0
    #on parcours la liste qui depend du fichier de l'objet lvl (class Niveau)
    for listes in lvl.structure:
        num_case = 0
        for sprites in listes:
            x = num_case * taille_sprite
            y = num_ligne * taille_sprite
            if sprites == "m" or sprites == "a":
                #on creeer un objet block -> mur devient sprite
                if sprites == "m":
                    block = Blocks(image_mur)
                elif sprites == "a":
                    block = Blocks(image_station)
                #rect x
                block.rect.x = x
                #rect y
                block.rect.y = y
                
                if sprites == "a":
                    block.rect.width = 300
                    block.rect.height = 200
                elif sprites == "m":
                    #rect height
                    block.rect.height = 20
                    #rect width 
                    block.rect.width = 20
                #on ajoute le Rect(x, y, width ,height) dans la liste de sprites block_list 
                block_list.add(block)
            num_case +=1
        num_ligne +=1 
        
#charge la fonction
afficher_lvl(fenetre, block_list)
#affiche_perso
perso = Perso(perso)
perso.deplacement()

#affiche perso dans la fenetre
continuer_acceuil = 0
#debute la boucle prinicpal
while continuer:
    #enregistre action utilisateur a chaque tour de boucle
    ev = event.poll()
    
    if ev.type == QUIT: 
        continuer = 0
    
    #la varible k renvoie True si une touche est pressé (get_pressed)
    k = key.get_pressed()
    

    #la variable touche qui comprend(fleche bas, haut, gauche, droite)
    for touche in (K_DOWN ,K_UP,K_LEFT, K_RIGHT):
        if k[touche]: #la liste si la variable k de la touche selectionné vaut True
            #direction = touche (ex : direction = 274) car les touches valent un numero
            direction = touche
            if direction == 274: #BAS
                direction = 0 #on met un index pour que cela corresponde aux listes creer dans la Perso methode -> deplacement()
            elif direction == 273:#HAUT
                direction = 3
            elif direction == 276:#left
                direction = 1
            elif direction == 275: #right
                direction = 2
            index_img = (index_img+1)%4 #l'image augement a chaque tour de boucle (effet d'animation) -> on applique le modulo, si index_img = 4 elle est égale à 0 la variable va donc de 0 à 3 (au final 4 images)
            
            old_x = perso.x#on enregistre l'ancienne valeur de (x) pour les collisions !
            old_y = perso.y
            #dans le cas normal si le personnage appui sur une touche il est dirigé vers sa direction
            if k[K_LEFT]: #si le boolen k[K_LEFT] vaut vrai alors le personnage se deplcaament de 8 pixel vers la gouche
                perso.x -= 8
            elif k[K_RIGHT]:
                perso.x += 8
            elif k[K_UP]:
                perso.y -= 8
            elif k[K_DOWN]:
                perso.y += 8
                
            #le personnage est un sprite donc un rectangle ->  Rect(perso.x, perso.y, 60,40) avec les nouvelles valeurs de x
            perso.rect.x = perso.x
            perso.rect.y = perso.y
            perso.rect.height = 60
            perso.rect.width = 40
            
            #on vérifie si les sprites dans la block_list(mur, stations, etc..) rentrent en collision avec le personnage dans ce cas la liste col vas se remplir
            col = sprite.spritecollide(perso, block_list, False)
            #gestion sorti de maap
            if perso.y < 0 or perso.y > 400:
                perso.y = old_y
            elif perso.x < 0 or perso.x > 860:
                perso.x = old_x 
                
            #si col est une liste remplie (donc qu'il y a collision)  on la parcours
            for listes in col:
                #perso.x ne change pas de position (idem pour perso.y)
                perso.x = old_x
                perso.y = old_y
            #on case la boucle for et on affiche l'image, la fenetre, le personnage avec ses coordonnées
            break
    #si on appui sur aucune touche l'image du personnage est l'image de base (pour pas qu'il se fige alors qu'il est en  mouvement)
    else:
        index_img = 0
        
    #on affiche l'image de fond
    fenetre.blit(image_fond, (0,0))
    #on draw les sprites qui sont dans la block_list -> sprites -> Rect(x, y, width, height)
    block_list.draw(fenetre)
    #on affiche le personnage avec sa direction associée, et son image 
    fenetre.blit(perso.image[direction][index_img],(perso.x,perso.y))
    #on raffraichit l'écran
    display.flip()
    
    #changement de niveau(en developpement....)
    if perso.x < 10:
        #on recreer un objet lvl avec le niveau n1
        lvl = Niveau(n1)
        #on load le lvl
        lvl.load_lvl()
        #on vide la block_list
        block_list = sprite.Group()
        #on y ajoute les sprites et ton recommence la boucle en afficahtn la nvouelle block_list 
        afficher_lvl(fenetre, block_list)
    #la boucle fait 60 tour par secondes
    time.wait(60)
