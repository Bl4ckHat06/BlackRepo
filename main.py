from pygame import *
from pygame.locals import *

from classes import * 
from constantes import *
from fonctions import *

init()
#chargement fenetre
fenetre = display.set_mode((cote_x, cote_y))
icone = image.load(image_icone)
display.set_icon(icone)
titre = display.set_caption(titre_fenetre)

#load les image
accueil = image.load(image_accueil)
image_fond = image.load(image_fond).convert()
dark = image.load(image_dark)
stars = image.load(image_stars)
didac = image.load(image_didact)
choix_img = image.load(image_choix)

#dans ces listes ce trouves toutes les images des sprites(une pour chaque etat qu'on defile une par une pour l'effet d'animé)
dark_list = []
star_list = []

#fonctions qui "coupe" les images avec la fonction subsurface parametre -> (taille_image_x, taille_image,y taille_sprite_x, taille_sprite_y, l'image en question, et la liste dans laquelle les decoupe vont ête mise)          
cut(960, 384, 192, 192, dark, dark_list)
cut(1775, 69, 71, 69, stars, star_list)

#initilisation des variables
continuer = 1
direction = 0 
i = 0
n_lvl = {1: n1, 2: n2}
b_anim = True
y_anim = True
time_frame = 30

#init des index pour les animations du perso, dark, et stars
index_img = 0
index_dark = 0
index_stars = 1
    
#le block anim dark
block_dark = Blocks(dark.subsurface(0,0,192,192), 1330, 640)

#les blocks stars sont ajouté comme sprites avec des indexs different (couleurs differentes)
block_stars_y = Blocks(star_list[index_stars], 500, 500) #etoile jaune
block_stars_b = Blocks(star_list[index_stars+6], 100, 400)#etoile bleu


#debute la boucle prinicpal
while continuer:
    
    fenetre.blit(accueil, (0,0))
    choix = 0
    continuer_accueil = 1
    continuer_jeu = 1
    continuer_didact = 1
    choix_lvl = 1
    
    display.flip()
    while continuer_accueil:
        for ev in event.get():
            if ev.type == QUIT:
                continuer_accueil =0
                continuer_jeu = 0
                continuer = 0
                continuer_didact = 0
                choix_lvl = 0
                
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    continuer_accueil = 0
                    continuer_jeu = 0
                    continuer = 0
                    continuer_didact = 0
                    choix_lvl = 0
            
                if ev.key == K_F1:
                    continuer_accueil = 0
                    continuer_didact = 0
                if ev.key == K_F2:
                    continuer_accueil = 0
                  
    while continuer_didact: #boucle du didactitiel
        fenetre.blit(didac, (0,0))
        display.flip()
        for ev in event.get():
            if ev.type == QUIT:
                continuer_didact = 0
                continuer_jeu = 0
                continuer = 0
                choix_lvl = 0
            if ev.type == KEYDOWN and ev.key == K_ESCAPE:
                continuer_didact = 0
                choix_lvl = 0
                continuer_jeu =0
                
             
    while choix_lvl:
        fenetre.blit(choix_img, (0,0))
        display.flip()
        for ev in event.get():
            if ev.type == QUIT:
                choix_lvl = 0
                continuer_jeu = 0
                continuer = 0
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    choix_lvl = 0
                    continuer_jeu = 0
                if ev.key == K_F1:
                    choix = 1
                    choix_lvl = 0

                if ev.key == K_F2:
                    choix = 2
                    choix_lvl = 0
                    
    #si on quitte et que la bucle continuer_accueil s'arrete ce code va être pris en compte la condition if choix != 0, permet de ne pas charger cette partie tant qu'aaucune action (F1, F2) n'a été faite        
    if choix != 0:
        #charge niveau
        lvl = Niveau(n_lvl[choix])
        lvl.load_lvl()
        #creation d'une liste qui collete les blocks de la partie
        block_list = sprite.Group()
        afficher_lvl(fenetre, block_list, lvl)
        
        #rempli la liste image des image(subsurface) du perso, et charge les images
        perso = image.load(image_perso)
        perso = Perso(perso)
        perso.cut_img()
        
    while continuer_jeu:
        #enregistre action utilisateur a chaque tour de boucle (get a single event from the queue) -> permet d'initiliaser la variable "key", pour key.pressed() quand on appui sur une touche (une key)
        ev = event.poll()

        if ev.type == QUIT:
            continuer = 0
            continuer_jeu = 0
        if ev.type == KEYDOWN:
            if ev.key == K_ESCAPE:
                continuer_jeu = 0
        #la varible k renvoie True si une touche est pressé (get_pressed) (guette l'état de chaquet ouche en envoyant une liste de booleen) -> verifie si une touche est maintenue enfoncée
        k = key.get_pressed()
        #la variable touche qui comprend(fleche bas, haut, gauche, droite)
        for touche in (K_DOWN ,K_UP,K_LEFT, K_RIGHT):
            if k[touche]: #la liste si la variable k de la touche selectionné vaut True
                #direction = touche (ex : direction = 274) car les touches valent un numero
                direction = touche
                if direction == 274: #BAS
                    direction = 0 #on met un index pour que cela corresponde aux listes creer dans la Perso methode -> cut_img()
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

                #on vérifie si les sprites dans la block_list(mur, stations, etc..) rentrent en collision avec le personnage dans ce cas la liste col vas se remplir
                col = sprite.spritecollide(perso, block_list, False)
                #gestion sorti de maap
                if perso.y < 0 or perso.y > cote_y-64:
                    perso.y = old_y
                elif perso.x < 0 or perso.x > cote_x-64:
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

        #gestion animation dark
        if sprite.collide_rect(perso, block_dark):
            if i < 10:
                index_dark = (index_dark+1)%10
                i+=1
            else:
                #on recharge TOUT pour reintialiser toutes les positions, le lvl,  etc... (a perfectionner)
                lvl = Niveau(n2)
                lvl.load_lvl()
                block_list = sprite.Group()
                afficher_lvl(fenetre, block_list, lvl)
                perso.x = 0
                perso.y = 0
                perso.rect.x = perso.x
                perso.rect.y = perso.y
                block_stars_y = Blocks(star_list[index_stars], 500, 500) #etoile jaune
                block_stars_b = Blocks(star_list[index_stars+6], 100, 400)#etoile bleu
                i=0

        #algorithme a perfectionner poru le placement des étoiles quand le personnage rentre en collisiona avec... peut être adaptere ça en avec une Class (class Anim_Stars:)
        if sprite.collide_rect(perso, block_stars_b):
            b_anim = False
            block_stars_b.rect.x = 1410
            block_stars_b.rect.y = 0
            if sprite.collide_rect(block_stars_y, block_stars_b):
                block_stars_b.rect.x = 1410-75
                block_stars_b.rect.y = 0
        if sprite.collide_rect(perso, block_stars_y):
            y_anim= False
            block_stars_y.rect.x = 1410
            block_stars_y.rect.y = 0
            if sprite.collide_rect(block_stars_y, block_stars_b):
                block_stars_y.rect.x = 1410-75
                block_stars_y.rect.y = 0
                
        if y_anim == True or b_anim == True:
            time_frame = time_frame - 10
            if time_frame < 0:
                time_frame = time_frame+30
                index_stars = ((index_stars+1)%5)+1
        else: index_stars = 1
            
        #on affiche l'image de fond
        fenetre.blit(image_fond, (0,0))
        #on draw les sprites qui sont dans la block_list -> sprites -> Rect(x, y, width, height) -> les murs
        block_list.draw(fenetre)


        fenetre.blit(star_list[index_stars], (block_stars_y.rect.x, block_stars_y.rect.y)) #affiche etoile jaune
        fenetre.blit(star_list[index_stars+6], (block_stars_b.rect.x, block_stars_b.rect.y))#affiche etoile bleu
        
        fenetre.blit(dark_list[index_dark], (block_dark.rect.x, block_dark.rect.y))#affiche le trou noir
        
        fenetre.blit(perso.image[direction][index_img],(perso.x,perso.y))#on affiche le personnage avec sa direction associée, et son image 
        
        display.flip()#on raffraichit l'écran
        
        #pause pendant 30ms avant de refaire un tour de boucle(pygame.time.wait(30ms))
        time.wait(35)
