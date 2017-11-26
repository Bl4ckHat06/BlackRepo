from constantes import *
from pygame import *
from pygame.locals import *

class Niveau:
    
    def __init__(self, niveau):
        self.niveau = niveau
        self.structure = 0
        
    def load_lvl(self):
    
        with open(self.niveau, "r") as fichier:
            
            structure_niveau = []
            
            for lignes in fichier:
                listes_niveau= []
                for sprites in lignes:
                    if sprites != "\n":
                        listes_niveau.append(sprites)
                structure_niveau.append(listes_niveau)
            self.structure = structure_niveau
            
    def afficher_lvl(self, fenetre):
        mur = image.load(image_mur).convert_alpha()
        depart= image.load(image_depart).convert()
        #coffres = pygame.image.load(image_coffre).convert_alpha()
        
        num_ligne = 0
        for listes in self.structure:
            num_case = 0
            
            for sprites in listes:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprites == "m":
                    fenetre.blit(mur, (x, y))
                if sprites == "a":
                    fenetre.blit(depart, (x, y))
                if sprites == "d":
                    fenetre.blit(depart, (x,y))
                num_case +=1
            num_ligne +=1




class Perso():
    def __init__(self, perso):
        self.x = 200
        self.y = 200
        self.image = []
        self.perso = perso

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
    
