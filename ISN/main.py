from tkinter import * 
from classes import * 
from constantes import *

#fonctions de deplacement

def test_collision():
    POS_perso_X = canvas.coords(perso.perso)[0]
    POS_perso_Y = canvas.coords(perso.perso)[1]
    
    POS_ennemi_X = canvas.coords(ennemi.ennemi)[0]
    POS_ennemi_Y = canvas.coords(ennemi.ennemi)[1]
    print(POS_ennemi_X)
    print(POS_perso_X)
    
    if (POS_perso_X, POS_perso_Y) == (POS_ennemi_X, POS_ennemi_Y):
        print('collision')
        
        
def gauche(event):
    perso.deplacement("gauche")
    canvas.coords(perso.perso, perso.x, perso.y)
    test_collision()
    
def droite(event):
    perso.deplacement("droite")
    canvas.coords(perso.perso, perso.x, perso.y)
    test_collision()
    
def haut(event):
    perso.deplacement("haut")
    canvas.coords(perso.perso, perso.x, perso.y)
    test_collision()
    
def bas(event):
    perso.deplacement("bas")
    canvas.coords(perso.perso, perso.x, perso.y)
    test_collision()


    
#init varibales
largeur = 600 #20*30 (20sprites, 30leur taille)
hauteur = 600

fenetre = Tk()
fenetre.geometry("600x600")
fenetre.title("Labyrinthe")
canvas = Canvas(fenetre, width=largeur, height=hauteur, bg="grey")

#perso
img_perso = PhotoImage(file=img_perso)
#ennemi
img_ennemi = PhotoImage(file=img_ennemi)
#genere le terrain et affiche
lvl = Niveau(n1)
lvl.load_lvl()
lvl.afficher_lvl(canvas)

#creer objet personnage
perso = Perso(canvas, lvl, img_perso)
#creer objet ennemi
ennemi = Ennemi(canvas, lvl, img_ennemi, fenetre)
ennemi.deplacement_auto()

ennemi2 = Ennemi(canvas, lvl, img_ennemi, fenetre)
ennemi2.deplacement_auto()

canvas.pack()


#lie touche avec fonctions qui deplacent le personnage
fenetre.bind('<Left>', gauche)
fenetre.bind('<Right>', droite)
fenetre.bind('<Up>', haut)
fenetre.bind('<Down>', bas)


fenetre.mainloop()