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

            
class Blocks(sprite.Sprite):
    def __init__(self, mur):
        super().__init__()
        self.image = image.load(mur)
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
    
