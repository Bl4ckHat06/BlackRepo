from constantes import *
from random import * 
from tkinter import *

class Ennemi:
    def __init__(self, ennemi, canvas, fenetre, rect_perso):
        self.dy = 0
        self.x = randint(50,450)
        self.y = 0
        self.canvas = canvas
        self.ennemi = self.canvas.create_image(self.x, self.y, anchor=NW, image=ennemi)
        self.fenetre= fenetre
        self.rect_perso = rect_perso
    
    def move_ennemi(self):
        self.dy+=10
        
        self.canvas.coords(self.ennemi, self.x, self.dy)
        
        self.x = self.canvas.coords(self.ennemi)[0]
        self.y = self.canvas.coords(self.ennemi)[1]
        
        if self.y  > self.canvas.coords(self.rect_perso)[1] and self.y < self.canvas.coords(self.rect_perso)[3] and self.x > self.canvas.coords(self.rect_perso)[0]-40 and self.x < self.canvas.coords(self.rect_perso)[2]:
            print("collision")
            
            
        self.fenetre.after(50, self.move_ennemi)
        