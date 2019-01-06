from tkinter import *
from random import *
import time


largeur = 500
hauteur = 500

#
dx,dy=1,0
#ball
x1 = 240
y1 = 240
x2 = 260
y2 = 260
y1_J1 = 200
y2_J1 = 300
y1_J2 = 200
y2_J2 = 300
a = True
score_J1 = 0
score_J2 = 0
nb_points = 0
last = None
J1 = None
J2 = None
#choix de la vitesse
vitesse = {0:'lent', 1:'normal', 2:'rapide'}
vitesse2 = {'lent':1, 'normal':2, 'rapide':5}
cle_vitesse = 1
#choix des couleurs
couleur = {0:'black', 1:'white', 2:'red', 3:'green', 4:'blue'}
cle_b = 0
cle_J1 = 4
cle_J2 = 4
cle_ball = 2
#temps
debut = 0
#bubulle
couleur_bulle = {0:'yellow', 1:'green', 2:'red'}
liste_bulle = []
liste_couleur = []
bulle = None
couleur2 = None

def menu_principale():
    menu_principale = Tk()
    #Ball
    canevas = Canvas(menu_principale, width=largeur, height=hauteur, bg='black')
    canevas.grid(row=0,rowspan=10, column=0,columnspan=10,pady=0)
    btn_Quitter = Button(menu_principale,text='Quitter', command=menu_principale.destroy).grid(row=9,column=9)
    btn_play = Button(menu_principale, text='Play', command=lambda: Play1()).grid(row=5, column=5)
    
    # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    def Play1():
        menu_principale.destroy()
        settings()
    menu_principale.mainloop()

def Play():
    global J1,J2, y2_J2, y2_J1, y1_J1, y1_J2
    play = Tk()
    play.focus_force()
    canevas = Canvas(play, width=largeur, height=hauteur, bg=couleur[cle_b%5])
    canevas.grid(row=0,rowspan=10, column=0,columnspan=10,pady=0)
    ball = canevas.create_oval(x1,y1,x2,y2, fill=couleur[cle_ball%5])
    J1 = canevas.create_rectangle(50,y1_J1,75,y2_J1,fill=couleur[cle_J1%5])
    J2 = canevas.create_rectangle(450,y1_J2,425,y2_J2,fill=couleur[cle_J2%5])
    global dx , dy, a, score_J1, score_J2, liste_bulle, liste_couleur
    dx = vitesse2[vitesse[cle_vitesse%3]]
    dy = 0
    liste_bulle = []
    liste_couleur = []
    def move_ball():
        global dx , dy, a, score_J1, score_J2, nb_points, liste_bulle, liste_couleur, bulle, last
        #Premiere Colision Raquette J2
        if ((canevas.coords(ball)[2]>=canevas.coords(J2)[0]) and (canevas.coords(ball)[2]<=canevas.coords(J2)[2]) and (canevas.coords(ball)[1]>=canevas.coords(J2)[1]) and (canevas.coords(ball)[3]<=canevas.coords(J2)[3])) and a == True:
            dx = -dx
            dy = 2
            last =  False
            a = False
        #Colision raquette J1
        elif ((canevas.coords(ball)[1]<=canevas.coords(J1)[3]) and (canevas.coords(ball)[1]>=canevas.coords(J1)[1]) and (canevas.coords(ball)[0]<=canevas.coords(J1)[2]) and (canevas.coords(ball)[0]>=canevas.coords(J1)[0])):
            dx = -dx
            last = True
        #Colision Raquette J2
        elif ((canevas.coords(ball)[2]>=canevas.coords(J2)[0]) and (canevas.coords(ball)[2]<=canevas.coords(J2)[2]) and (canevas.coords(ball)[1]>=canevas.coords(J2)[1]) and (canevas.coords(ball)[3]<=canevas.coords(J2)[3])):
            dx = -dx
            last = False
        #Rebond en haut et en bas
        if canevas.coords(ball)[1] <= 0 or canevas.coords(ball)[3] >= hauteur:
            dy = -dy
        #But du joueur 1
        if canevas.coords(ball)[0] <= 0:
            score_J2 += 1
            a = True
            bulle = None
            y1_J1 = 200
            y1_J2 = 200
            y2_J1 = 300
            y2_J2 = 300
            play.destroy()
            if score_J2 == nb_points:
                fin_partie()
            else : 
                Play()
        #But du joueur 2
        if canevas.coords(ball)[2] >= largeur:
            score_J1 += 1
            a = True
            bulle = None
            y1_J1 = 200
            y1_J2 = 200
            y2_J1 = 300
            y2_J2 = 300
            play.destroy()
            if score_J1 == nb_points:
                fin_partie()
            else:
                Play()

        canevas.move(ball, dx, dy)
        set_bubulle()
        canevas.after(10, move_ball)




    def move_J1_up(event):
        canevas.move(J1, 0, -20)

    def move_J1_down(event):
        canevas.move(J1, 0, 20)

    def move_J2_up(event):
        canevas.move(J2, 0, -20)

    def move_J2_down(event):
        canevas.move(J2, 0, 20)

    play.bind('z', move_J1_up)
    play.bind('s', move_J1_down)
    play.bind('i', move_J2_up)
    play.bind('k', move_J2_down)

    def set_bubulle():
        global bulle, couleur2, dx, J1, J2
        if bulle == None:
            if randrange(0,1000) == randrange(0,1000):
                center_x = randrange(100,400)
                center_y = randrange(100,400)
                couleur2 = couleur_bulle[randrange(0,3)]
                bulle = canevas.create_oval(center_x+10,center_y+10,center_x-10,center_y-10, fill=couleur2)
        elif (canevas.coords(ball)[1]<=canevas.coords(bulle)[3]) and (canevas.coords(ball)[3]>=canevas.coords(bulle)[1]) and (canevas.coords(ball)[2]>=canevas.coords(bulle)[0]) and (canevas.coords(ball)[0]<=canevas.coords(bulle)[2]):
            if couleur2 == 'yellow':
                dx *= 2
            if couleur2 == 'green':
                if last == True:
                    canevas.delete(J1)
                    J1 = canevas.create_rectangle(50,y1_J1-50,75,y2_J1+50,fill=couleur[cle_J1%5])
                if last == False:
                    canevas.delete(J2)
                    J2 = canevas.create_rectangle(450,y1_J2+20,425,y2_J2-20,fill=couleur[cle_J2%5])
            if couleur2 == 'red':
                if last == True:
                    canevas.delete(J2)
                    J2 = canevas.create_rectangle(450,y1_J2+20,425,y2_J2-20,fill=couleur[cle_J2%5])
                if last == False:
                    canevas.delete(J1)
                    J1 = canevas.create_rectangle(50,y1_J1+20,75,y2_J1-20,fill=couleur[cle_J1%5])
            canevas.delete(bulle)
            bulle = None
        canevas.after(1000,set_bubulle)
    
    move_ball()
    play.mainloop()

#ecran settings
def settings():
    settings = Tk()
    canevas = Canvas(settings, width=largeur, height=hauteur, bg='black')
    canevas.grid(row=0,rowspan=10, column=0,columnspan=10,pady=0)
    canevas.create_text(250,100, text='nombre de point gagnant', fill='white',font="Arial")
    gauche = Button(settings, text='<', font='Arial', command=lambda: nb_points_gagnant_plus()).grid(row=3, column=2)
    droite = Button(settings, text='>', font='Arial', command=lambda: nb_points_gagnant_moins()).grid(row=3, column=8)
    suivant = Button(settings, text='suivant', command=lambda: suivant()).grid(row=8, column=8)
    canevas.create_text(250,150, text=str(nb_points), fill='white',font="Arial")
    def nb_points_gagnant_plus():
        global nb_points
        nb_points += 1
        canevas.create_rectangle(225,110,275,175,fill='black')
        canevas.create_text(250,150, text=str(nb_points), fill='white',font="Arial")
    def nb_points_gagnant_moins():
        global nb_points
        if nb_points < 2:
            canevas.create_rectangle(225,110,275,175,fill='black')
            canevas.create_text(250,150, text="infini", fill='white',font="Arial")
        else:
            nb_points -= 1
            canevas.create_rectangle(225,110,275,175,fill='black')
            canevas.create_text(250,150, text=str(nb_points), fill='white',font="Arial")

    #choix vitesse de la balle
    canevas.create_text(250,275, text='vitesse de la balle', fill='white',font="Arial")
    gauche = Button(settings, text='<', font='Arial', command=lambda: vitesse_plus()).grid(row=6, column=2)
    droite = Button(settings, text='>', font='Arial', command=lambda: vitesse_moins()).grid(row=6, column=8)
    def vitesse_plus():
        global cle_vitesse
        cle_vitesse += 1
        canevas.create_rectangle(225,300,275,350,fill='black')
        canevas.create_text(250,325, text=vitesse[cle_vitesse%3], fill='white',font="Arial")
    def vitesse_moins():
        global cle_vitesse
        cle_vitesse -= 1
        canevas.create_rectangle(225,300,275,350,fill='black')
        canevas.create_text(250,325, text=vitesse[cle_vitesse%3], fill='white',font="Arial")


    def suivant():
        settings.destroy()
        settings2()

    settings.mainloop()

def settings2():
    settings2 = Tk()
    canevas = Canvas(settings2, width=largeur, height=hauteur, bg='black')
    canevas.grid(row=0,rowspan=10, column=0,columnspan=10,pady=0)
    
    #choix de la couleur du fond
    gauche = Button(settings2, text='<', font='Arial', command=lambda: background_gauche()).grid(row=0, column=2)
    droite = Button(settings2, text='>', font='Arial', command=lambda: background_droite()).grid(row=0, column=7)
    def background_gauche():
        global cle_b
        cle_b += 1
        couleur[cle_b%5]
        canevas.create_rectangle(0,0,500,500,fill=couleur[cle_b%5])
    def background_droite():
        global cle_b
        cle_b -= 1
        couleur[cle_b%5]
        canevas.create_rectangle(0,0,500,500,fill=couleur[cle_b%5])

    #choix de la couleur de la balle
    gauche = Button(settings2, text='<', font='Arial', command=lambda: couleur_ball_gauche()).grid(row=4, column=3)
    canevas.create_oval(x1,y1,x2,y2, fill='red')
    droite = Button(settings2, text='>', font='Arial', command=lambda: couleur_ball_droite()).grid(row=4, column=6)
    def couleur_ball_gauche():
        global cle_ball
        cle_ball += 1
        canevas.create_oval(240,240,260,260, fill=couleur[cle_ball%5])
    def couleur_ball_droite():
        global cle_ball
        cle_ball -= 1
        canevas.create_oval(240,240,260,260, fill=couleur[cle_ball%5])

    gauche = Button(settings2, text='<', font='Arial', command=lambda: couleur_J1_gauche()).grid(row=4, column=0)
    canevas.create_rectangle(50,200,75,300,fill='blue')
    droite = Button(settings2, text='>', font='Arial', command=lambda: couleur_J1_droite()).grid(row=4, column=2)
    def couleur_J1_gauche():
        global cle_J1
        cle_J1 += 1
        canevas.create_rectangle(50,200,75,300,fill=couleur[cle_J1%5])
    def couleur_J1_droite():
        global cle_J1
        cle_J1 -= 1
        canevas.create_rectangle(50,200,75,300,fill=couleur[cle_J1%5])
    
    gauche = Button(settings2, text='<', font='Arial', command=lambda: couleur_J2_gauche()).grid(row=4, column=7)
    canevas.create_rectangle(450,200,425,300,fill='blue')
    droite = Button(settings2, text='>', font='Arial', command=lambda: couleur_J2_droite()).grid(row=4, column=9)
    def couleur_J2_gauche():
        global cle_J2
        cle_J2 += 1
        canevas.create_rectangle(450,200,425,300,fill=couleur[cle_J2%5])
    def couleur_J2_droite():
        global cle_J2
        cle_J2 -= 1
        canevas.create_rectangle(450,200,425,300,fill=couleur[cle_J2%5])


    suivant = Button(settings2, text='suivant', command=lambda: suivant2()).grid(row=10, column=10)
    def suivant2():
        global debut
        debut = recup_time()
        settings2.destroy()
        Play()


    settings2.mainloop()


#ecran fin de partie
def fin_partie():
    global score_J1, score_J2, debut, bulle
    ecran_fin_partie = Tk()
    canevas = Canvas(ecran_fin_partie, width=largeur, height=hauteur, bg='black')
    canevas.grid(row=0,rowspan=10, column=0,columnspan=10,pady=0)
    canevas.create_text(100,50, text=str(score_J1), fill='white',font="Arial")
    canevas.create_text(400,50, text=str(score_J2), fill='white',font="Arial")
    btn_replay = Button(ecran_fin_partie, text='replay', command=lambda: replay()).grid(row=5, column=6)
    btn_menu = Button(ecran_fin_partie, text='Menu', command=lambda: menu_principale1()).grid(row=5, column=4)
    btn_Quitter = Button(ecran_fin_partie,text='Quitter', command=ecran_fin_partie.destroy).grid(row=9,column=9)
    temps = int(recup_time()-debut)
    minute = int(temps/60)
    seconde = int(temps%60)
    canevas.create_text(245,50, text=str(minute), fill='white',font="Arial")
    canevas.create_text(253,50, text=':', fill='white',font="Arial")
    canevas.create_text(265,50, text=str(seconde), fill='white',font="Arial")
    #reinitialisation des variables score_J1 score_J2
    score_J1, score_J2=0,0
    debut = recup_time()
    bulle = None
    def menu_principale1():
        ecran_fin_partie.destroy()
        menu_principale()
    def replay():
        ecran_fin_partie.destroy()
        Play()

    ecran_fin_partie.mainloop()

def recup_time():
    return time.time()

menu_principale()