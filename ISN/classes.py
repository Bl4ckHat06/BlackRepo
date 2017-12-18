from tkinter import * 
from random import *

class Niveau:
    
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0
        
        
    def load_lvl(self):
        structure_niveau = []
        
        with open(self.fichier, 'r') as fichier:
            #parcours les lignes du fichier
            for lignes in fichier:
                liste_niveau = [] #creer une liste a chaque lignes
                for sprites in lignes:
                    liste_niveau.append(sprites) #ajoute les elements de la ligne a la liste
                structure_niveau.append(liste_niveau) #ajoute la liste a la liste principale
            self.structure = structure_niveau
    def afficher_lvl(self, canvas):
        num_ligne = 0
        for listes in self.structure: #parcours les listes creer dans load dans la lsite principal
            num_case = 0
            for sprites in listes: #parcours les elements de chaque listes
                x = 30*num_case
                y = 30*num_ligne
                if sprites == "1":
                    canvas.create_rectangle(x, y, x+30, y+30, fill="white", outline="#C8C8C8")
                if sprites == "v":
                    canvas.create_rectangle(x, y, x+30, y+30, fill="green", outline="#C8C8C8")
                if sprites == "r":
                    canvas.create_rectangle(x, y, x+30, y+30, fill="red", outline="#C8C8C8")
                
                num_case+=1
            num_ligne +=1
  
            
class Perso:
    def __init__(self, canvas, niveau, perso):
        self.canvas = canvas
        self.niveau = niveau
        
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        
        self.perso = self.canvas.create_image(self.x, self.y, anchor=NW, image=perso)
        
    def deplacement(self, direction):
        if direction == "gauche":
            if self.case_x>0: #verifie si on est en ehors de l'écran
                if self.niveau.structure[self.case_y][self.case_x-1] != "0": #verifie si il ya un muir
                    self.case_x -= 1 #dimie la case de 1
                    self.x = 30*self.case_x #la position reel prend en comtpe alt aille de l'objet
        elif direction == "droite":
            if self.case_x < 20-1:
                if self.niveau.structure[self.case_y][self.case_x+1] != "0":
                    self.case_x += 1
                    self.x = 30*self.case_x
        elif direction == "haut":
            if self.case_y > 0:
                if self.niveau.structure[self.case_y-1][self.case_x] != "0":
                    self.case_y -=1
                    self.y = 30*self.case_y
        elif direction == "bas":
            if self.case_y < 20-1:
                if self.niveau.structure[self.case_y+1][self.case_x] != "0":
                    self.case_y += 1
                    self.y = 30*self.case_y
        else: pass
        
        
        
        
class Ennemi(Perso):
    def __init__(self, canvas, niveau, ennemi, fenetre):
        
        self.canvas = canvas
        self.niveau = niveau
        self.fenetre = fenetre
        
        self.case_y = 5
        self.case_x = 0
        self.x = self.case_x*30
        self.y = self.case_y*30
        
        self.ennemi = self.canvas.create_image(self.x, self.y, anchor=NW, image = ennemi)
        
    def deplacement_auto(self):
        hasard = randint(0,3)
        if hasard == 0:
            self.deplacement("haut")
            self.canvas.coords(self.ennemi, self.x, self.y)
        elif hasard == 1:
            self.deplacement("bas")
            self.canvas.coords(self.ennemi, self.x, self.y)
        elif hasard == 2:
            self.deplacement("gauche")
            self.canvas.coords(self.ennemi, self.x, self.y)
        elif hasard == 3:
            self.deplacement("droite")
            self.canvas.coords(self.ennemi, self.x, self.y)
        self.fenetre.after(350, self.deplacement_auto)
    
        
        
        
        
        
                    
                    
            