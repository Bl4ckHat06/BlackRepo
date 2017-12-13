from tkinter import *
from constantes import *
from random import *
from classes import *

direction = ""

def droite(event):
    global direction
    direction = "droite"
def gauche(event):
    global direction
    direction = "gauche"
    
def move_perso():
    global direction, dx, dy
    if direction == "droite":
        dx+=30
        canvas.coords(perso)[0]+=dx
        if canvas.coords(perso)[0]>=450:
            dx-=30
    elif direction == "gauche":
        dx-=30
        canvas.coords(perso)[0]+=dx
        if canvas.coords(perso)[0]<=0:
            dx+=30
        

    canvas.coords(perso, dx, dy)
    canvas.coords(rect_perso, dx+10, 550, dx+40,590)
    direction = ""
    fenetre.after(60, move_perso)

    
def move_ennemi():
    global list_img, enmi
    enmi.move_ennemi()
    
    new_ennemi()
def new_ennemi():
    global enmi
    if enmi.y > 200:
        index = randint(0,1)
        enmi = Ennemi(list_img[index], canvas, fenetre, rect_perso)
        move_ennemi()
    fenetre.after(60, new_ennemi)

       
dye = 0
dx = 100
dy = 550
largeur = 500
hauteur = 600
x = 100



fenetre = Tk()
fenetre.geometry("500x600")
canvas = Canvas(fenetre, width = largeur, height=hauteur, bg="black")

img_perso = PhotoImage(file=perso_img)
img_ennemi = PhotoImage(file=ennemi)

list_img = [img_perso, img_ennemi]

rect_perso = canvas.create_rectangle(110,550, 140, 590, fill="black")
perso = canvas.create_image(100, 550, anchor=NW, image=img_perso)

enmi = Ennemi(list_img[1], canvas, fenetre, rect_perso)

move_perso()
move_ennemi()

fenetre.bind('<Right>', droite)
fenetre.bind('<Left>', gauche)

canvas.pack()
fenetre.mainloop()