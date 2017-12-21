from tkinter import * 
from random import*

list_rond = []
i = -1
dx= 0
dy= 0
anim = False

xr=200
yr=200
dxr=0
dyr=0

xi=20
yi=20
dxi = 0
dyi = 0

def move_rond(event):
    global xr, yr, dxr, dyr
    if event.keysym == "Right":
        dxr+=10
    elif event.keysym == "Left":
        dxr-=10
    elif event.keysym == "Up":
        dyr-=10
    elif event.keysym == "Down":
        dyr+=10
    else: pass
    
    canvas2.coords(rect_move, dxr+xr,dyr+yr,dxr+xr+50, dyr+yr+50)
    
def anim_rond():
    global xi, yi
    rond_anim = canvas2.create_oval(xi, yi, xi+50, yi+50, fill="blue")
    animer_rond(rond_anim)
def animer_rond(rondi):
    global xi, yi, dxi, dyi
    
    if canvas2.coords(rondi)[2]<400 and canvas2.coords(rondi)[1]<21:
        dxi+=10
    elif canvas2.coords(rondi)[2]==400 and canvas2.coords(rondi)[3]<390:
        dyi+=10
    elif canvas2.coords(rondi)[3]==390 and canvas2.coords(rondi)[0]>10:
        dxi-=10
    elif canvas2.coords(rondi)[0]==10 and canvas2.coords(rondi)[1]>20:
        dyi-=10
    canvas2.coords(rondi, xi+dxi, yi+dyi, xi+dxi+50, yi+dyi+50)
    
    fenetre.after(60, lambda: animer_rond(rondi))

def insert_objet():
    global list_rond, x,y 
    
    x = randint(0,400)
    y = randint(0,400)
    rond = canvas.create_oval(x,y,x+50,y+50, fill="#B42471", outline="#8928AC")
    list_rond.append(rond)
def change_color():
    global list_rond
    couleur = ["blue", "white", "pink", "purple", "black"]
    n_couleur = randint(0,4)
    for rond in list_rond:
        canvas.itemconfigure(rond, fill=couleur[n_couleur])
        
def erase():
    global list_rond, i
    canvas.delete(list_rond[i])
    i-=1
    
def Anim_1():
    global list_rond, couleur1, anim
    if anim == True:
        couleur1 = ["blue", "white", "pink", "purple", "black"]
        n_couleur = randint(0,4)
        for rond in list_rond:
            canvas.itemconfigure(rond, fill=couleur1[n_couleur])
        fenetre.after(150, Anim_1)
def anim():
    global anim
    anim = True
    Anim_1()
def stop_anim():
    global anim
    anim = False
    
fenetre= Tk()
fenetre.title("Tkinter")
fenetre.geometry("800x800")
canvas = Canvas(fenetre, width=400, height=400, bg="#C8C8C8")
canvas.grid(row=0, column=0)
canvas2 = Canvas(fenetre, width=400, height=400, bg="pink")
canvas2.grid(row=1, column=0)

frame= Frame(fenetre,bg="#c8c8c8")
frame.grid(row=0, column=1)
frame2 = Frame(fenetre)
frame2.grid(row=1, column=1)

B_Objet = Button(frame, text="Inserer un objet", command=insert_objet, height="2", width="22")
B_Objet.grid(row=0, column=0, padx=0, pady=0)
B_Color = Button(frame, text="Changer la couleur de l'objet", command=change_color, height="2")
B_Color.grid(row=1, column=0, pady=10)
B_Effacer = Button(frame, text="Effacer l'objet", command=erase)
B_Effacer.grid(row=0, column=2)
B_Anim = Button(frame, text="Animer !", command=anim)
B_Anim.grid(row=0, column=1)
B_AnimS = Button(frame, text="Arreter l'animation", command=stop_anim)
B_AnimS.grid(row=1, column=1, padx=15)

#PARTIE 2
rect_move = canvas2.create_rectangle(xr,yr,xr+50,yr+50, fill="grey")

B_Anim_rond = Button(frame2, text="Animer un rond!", command=anim_rond, width="25", height="2")
B_Anim_rond.grid(row=0, column=0)



Quitter = Button(fenetre, text="Quitter", command=exit)
Quitter.place(x=750, y=770)

fenetre.bind('<Up>', move_rond)
fenetre.bind('<Down>', move_rond)
fenetre.bind('<Right>', move_rond)
fenetre.bind('<Left>', move_rond)
fenetre.mainloop()