from classes import *
from pygame import * 

init()
station = image.load(image_station)
mur = image.load(image_mur)


#fonctions quia ffiche le niveau, et mets les blocs selectionner dans la liste avec un pour m->Rect(x, y 20,20) et a->Rect(x,y, 200,300)
def afficher_lvl(fenetre, block_list, lvl): 
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
                    block = Blocks(mur,x , y)
                elif sprites == "a":
                    block = Blocks(station, x, y)
                
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
        
def cut(x_range, y_range, x_taille, y_taille, img, img_list):
    for y in range(0, y_range, y_taille):
        for x in range(0, x_range, x_taille):
            img_list.append(img.subsurface(x, y, x_taille, y_taille))