# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # THE HOUSE
# # # # # # # # # # # # # # # # # # # # # # # # FAZIL VINCENT ADBEL AMINE RAYAN
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  PROJET ISN
from tkinter import *
from tkinter.messagebox import *
import os

from random import randint  # importation de l'aleatoire dans le programme 
from random import choice

import turtle
import time
import random

import math

fen = Tk() # fenetre tk inter 
fen.title("T H E   H O U S E")
fen.geometry("1280x720")
fen.iconbitmap("images/mhico.ico") # petite icone de la page 

#################################################################################################################
balleL=10
balleC=10                           ### ### ### LABYRINTHE 50*30 ### ### ###
LC=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,1],
    [1,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,1,1,0,0,1,0,1,1,1],
    [1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1],
    [1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1],
    [1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,0,1,0,0,1,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1],
    [1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1],
    [1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1],
    [1,0,0,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,1],
    [1,0,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,9],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,5],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,5],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9]]

#################################################################################################################
flechedroite = PhotoImage(file="images/flechedroite.png")
flechegauche = PhotoImage(file="images/flechegauche.png")
tablette = PhotoImage(file="images/tablette.png")
################################# DEFINITIONS #################################

def videfen():   # effacer page precedente 
    global fen
    for C in fen.winfo_children():
        C.destroy()
        

        
def surdequit():
    rep = askokcancel ("ATTENTION !",\
                       "Vous allez quitter le jeu !\n"+\
                       "En êtes vous conscient ?")
    if rep:
        fen.destroy()
#module de Tkinter messagebox qui ouvre une petite fenetre
            #qui averti l'utiliateur

###      =======================================================================
        
################## COMPTEUR SALLE ##################
compteurentree = 0                                 #
compteurcuisine = 0                                #
compteurcouloir = 0                                #
compteurchambre = 0                                #
compteursalledufond = 0                            #
compteursalledebain = 0                            #
compteursortie = 0                                 #
compteursalleGsortie = 0                           #
compteurjardin = 0                                 #
compteurmagie = 0                                  #
                                                   #
################### COMPTEUR JEU ###################
compteursnake = 0                                  #
compteurlaby = 0                                   #
compteurpcf = 0                                    #
compteurgw = 0                                     #
####################################################
                                                   
# LABY ###########################################################################################
def laby():

    def KeyBoard (event):
        global balleL,balleC,LC   # balle ligne  ,balle colonne, LC = lignes/colonnes "en gros le labyrinthe"
        newL,NewC = balleL,balleC #nouvelle positions de la balle

        Key=event.keysym   # association des touches au clavier
    
        if Key == "Up":                         #
            newL,newC=balleL-1,balleC           # si la touche appuyée est "haut"
                                                # nouvelles coordonnées de la balle = y-1,x
        if Key == "Down":                       #
            newL,newC=balleL+1,balleC           #
                                                #
        if Key == "Right":                      #
            newL,newC=balleL,balleC+1

        if Key == "Left":
            newL,newC=balleL,balleC-1

        Verification(newL,newC)

    def Verification(newL,newC):
        global balleL,balleC,LC,compteurlaby,compteurentree

        if LC[newL][newC]==0:     # si on atterit sur une nouvelle case vide 
            LC[balleL][balleC]=0  # balleL et balleC gardent tjrs la val 0 donc c'est encore une case vide
            balleL,balleC = newL,newC # les anciennes coords valent les nouvelles
            LC[balleL][balleC]=2      # balleL et balleC prennent la val 2 (peut etre changé)
            canlaby.coords(balle, balleC*20,balleL*20 , balleC*20+20,balleL*20+20) # la balle se recrée a la nouvelle position

        if LC[newL][newC]==5:     # pour gagner il faut atteindre les cases où il y a des 5
            compteurlaby += 1       
            print("compteurlaby = ",compteurlaby)
            compteurentree += 1       
            print("compteurentree = ",compteurentree)
            cuisine()

    global Largeur, Hauteur, photolaby,mur
    Largeur = 1280
    Hauteur = 720
    videfen()
    photolaby = PhotoImage( file ="images/cuisine.png")
    canlaby = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)#création d'un canvas
    canlaby.create_image(Largeur/2, Hauteur/2, image=photolaby)# largeur/2 et hauteur/2 pour centrer image en haut à gauche sinon excentré
    #création de la balle à partir d'un carré qui contient la balle
    balle = canlaby.create_oval(balleL*20, balleC*20, balleL*20+20, balleC*20+20, width=2, outline="red",fill="black")
    canlaby.bind("<Key>",KeyBoard)#lie les touches au clavier
    canlaby.focus_set()#opération nécessaire à l 'encrage des touches du clavier
    fen.resizable(width = FALSE,  height=FALSE)#fen ne change pas de taille quand on l'étire avec la souris
    canlaby.pack(padx=140, pady=50)#permet de centrer le canvas

    
    LC[balleL][balleC]=2
#bloc du programme permettant de créer les murs
    print(LC)
    i=0
    j=0

    while j<31:
        while i<50:
            if LC[j][i]==1:
                canlaby.create_rectangle(i*20,j*20,i*20+20,j*20+20,outline="brown",fill="orange")
            i +=1
        i=0
        j =j+1

# SORTIE DU LABY
    i=0
    j=0    
    while j<31:
        while i<50:
            if LC[j][i]==9:
                canlaby.create_rectangle(i*20,j*20,i*20+20,j*20+20,outline="black",fill="red")
            i +=1
        i=0
        j =j+1

    

# SNAKE ##########################################################################################

def snake():
    def ça_sert_a_R():
        showinfo ("RÈGLES DU JEU",\
                        "CE JEU SE JOUE AU CLAVIER \n"+\
                        "AVEC LES FLÈCHES DIRECTIONNELS ")
        
    delai = 0.1#délai de raffraichissement de la fenetre

    # Score
    score = 0

    # creation de l'ecran
    global compteursnake #annonce des variable utlise dans la fonction
    fensnake = turtle.Screen()#creations d'une fenetre turtle
    fensnake.title("SNAKE")#titre de la fenetre
    fensnake.bgcolor("green")# couleur de fond de la fentre 
    fensnake.setup(width=600, height=600)#taille de la fenetre
    fensnake.tracer(0) # arreter la mise à jour de l'ecran
    # Récupérer le toplevel (la fenêtre) du canvas de turtle :
    master = turtle.getcanvas().master
    # Ajouter un bouton à la fenêtre :
    instruction = Button(master, text ='instruction',fg = "purple", command = ça_sert_a_R)#creation boutton quitter
    instruction.pack()#verification de la fonctions ou varible #obligatoire pour que le programme marche


    # tete du snake
    tete = turtle.Turtle() #creation de la tete du snake
    tete.speed(0)          #vitesse de déplacement du snake
    tete.shape("square")   #forme de la tete
    tete.color("blue")     #couleur de la tete
    tete.penup()           #le crayon ne dessine pas
    tete.goto(0,0)         #et part à l'emplacement (0,0)
    tete.direction = "stop"#et la tete reste immobile

    # nourriture
    food = turtle.Turtle() #creation de la nourriture
    food.speed(0)          #vitesse de la nourriture
    food.shape("circle")   #forme de la nourriture
    food.color("yellow")   #couleur
    food.penup()           #le crayon ne dessine pas
    food.goto(0,100)       #et part à l'emplacement (0,100)

    segments = []  #liste vide des segments du corps du serpent

    # ecriture du score avec un crayon
    crayon = turtle.Turtle()#creation crayon
    crayon.speed(0)#delai de deplace du crayon (plus rapide possible)
    crayon.shape("square")#forme 
    crayon.color("white")#couleur 
    crayon.penup()#le crayon ne dessine pas
    crayon.hideturtle()  #cache le turtle crayon donc est invisible;
    crayon.goto(0, 260)  # permet juste d'avoir l'ecriture du score sans avoir un point blanc visible à lécran
    crayon.write("Score: 0", align="center", font=("Courier", 24, "normal"))# norme d'ecriture du crayon

    # fonctions qui permettent de ne pas faire de demi-tour subitement
    # et elles sont les fonctions qui permettra a serpent de bouger dans
    # les quatres directions
    def haut():
        if tete.direction != "down":#si la tete ne monte pas elle descends
            tete.direction = "up"

    def bas():
        if tete.direction != "up":#si la tete ne decnds pas elle monte
            tete.direction = "down"

    def gauche():
        if tete.direction != "right":#si la tete ne va pas a droite pas elle va a gauche
            tete.direction = "left"

    def droite():
        if tete.direction != "left":#si la tete ne vas pas a gauche pas elle va a droite
            tete.direction = "right"

    # déplacement de la tete 20 par 20 pixels
    def move(): 
        if tete.direction == "up": #si on appuie sur haut alors les coordoné en y=y+20
            y = tete.ycor()
            tete.sety(y + 20)

        if tete.direction == "down": #si on appuie sur bas alors les coordoné en y=y-20
            y = tete.ycor()
            tete.sety(y - 20)

        if tete.direction == "left":#si on appuie sur gauche alors les coordoné en x=x-20
            x = tete.xcor()
            tete.setx(x - 20)

        if tete.direction == "right":#si on appuie sur droite alors les coordoné en x=y+20
            x = tete.xcor()
            tete.setx(x + 20)

    # association des touche du clavier ======= FLECHES DIRECTIONELLES
    fensnake.listen()#commande qui permet de mettre en relation le programme et le clavier
    fensnake.onkeypress(haut, "Up")#associations up a haut
    fensnake.onkeypress(bas, "Down")#IDEM
    fensnake.onkeypress(gauche, "Left")#IDEM
    fensnake.onkeypress(droite, "Right")#IDEM

    # Main loop : boucle principale du snake
    while True:
        fensnake.update() #MAJ de la fenetre à chaque lancement du programme snake

        # Verification collision avec les bords
        if tete.xcor()>290 or tete.xcor()<-290 or tete.ycor()>290 or tete.ycor()<-290:
            #Si les coord en x et y sont sup ou inf a 290 alors 
            time.sleep(1)  #temps de chargement apres la défaite  
            tete.goto(0,0)#la tete se place très rapidement au 0,0
            tete.direction = "stop"#la tete ne bouge plus apres la défaite

            # cacher les segments
            for segment in segments:
                segment.goto(1000, 1000) # partent en dehors de l'écran défini
            
            # effacer la liste des segments
            segments.clear()

            # réinitialisation du score
            score = 0

            # réinitialisation du delai
            delai = 0.1

            crayon.clear() # le crayon efface le score et le réecrit. donc se réinitialise
            crayon.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal")) 


        # Verification collision avec la nourriture
        if tete.distance(food) < 20:
            # faire apparaire la nourriture à un endroit aléatoire
            x = random.randint(-290, 290)
            #affiche le score a des coord aleatoires entre -290 et 290 en x et en y
            y = random.randint(-290, 290)
            food.goto(x,y)#la nourriture va a cette endroit

            # ajouter un carré pour faire grandir le snake
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            segments.append(new_segment)

            # raccourcissement du délai donc le jeu s'accélère
            delai -= 0.001

            # le score augmente de 10 en 10
            score += 10

            crayon.clear()
            crayon.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal")) 

        # permet de faire suivre les segments (corps) par rapport à la tête
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = tete.xcor()
            y = tete.ycor()
            segments[0].goto(x,y)

        move()   #fonction déplacement     

        global compteursnake   ########################## WIN
        if score == 100:#si on arrive a 100 point le jeu s'arrete et la page se quitte
            compteursnake +=1
            print("compteursnake = ",compteursnake)
            fensnake.bye()#quitte la fenetre apres victoire
            salledufond()
            
        # Verification collision tete/segment du corps
        for segment in segments:
            if segment.distance(tete) < 20:#taille tete = 20 pixels
                time.sleep(1)
                tete.goto(0,0)
                tete.direction = "stop"
            
                # cacher les segments
                for segment in segments:
                    segment.goto(1000, 1000)
            
                # effacer la liste des segments
                segments.clear()

                # réinitialisation du score
                score = 0

                # Réinitialisation du delai
                delai = 0.1
            
                # MAJ score + RECORD
                crayon.clear()
                crayon.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        time.sleep(delai)
    #actionner le gestionaire d'évènement ou démmarer
    fensnake.mainloop()

# GALAXY WARS #################################################################################
global bulletstate

def GALAXYWARS():
    global bulletstate

    def regles():
        rep = showinfo ("RÈGLES DU JEU",\
                              "CE JEU SE JOUE AU CLAVIER \n"+\
                              "AVEC LES FLÈCHES DIRECTIONNELS POUR SE DEPLACER\n"+\
                              "ET ESPACE POUR TIRER")
        if rep:
            gw.bye()
            
    #parametre de la fenêtre
    gw = turtle.Screen()
    gw.bgcolor("black")
    gw.title("GALAXY WARS")
    # Récupérer le toplevel (la fenêtre) du canvas de turtle : superposer tkinter et turtle
    master = turtle.getcanvas().master
    # Ajouter un bouton à la fenêtre :
    instruction = Button(master, text ='instruction',fg = "purple", command = regles)
    instruction.pack()


    #dessin des bords de la fentre 
    border_pen = turtle.Turtle() 
    border_pen.speed(10)  # la vitesse est ultra rapide donc toute les etapes a suivre ce font rapidement sans que cela se remarque 
    border_pen.color("white")
    border_pen.penup()        #ne dessine pas
    border_pen.setposition(-300,-300) # positon du pen pour dessiner les bors 
    border_pen.pendown()      #dessine
    border_pen.pensize(3)     #epaisseur ici 3
    for side in range(4):     # boucle pour dessiner les bords
        border_pen.fd(600)    # longueur tracé 600 pixel 
        border_pen.lt(90)  # angle entre les tracet 
    border_pen.hideturtle()  # le borderpen disparait lorsqu'il fini son travail 


    #mettre le score a 0
    score =0

    #dessiner le score
    score_pen = turtle.Turtle()  # cad un point 
    score_pen.speed(10) # vitesse que met le stylo a dessiner les contours unité en mili seconde 
    score_pen.color("white")
    score_pen.penup()       
    score_pen.setposition(-290, 280) # endroit de l'ecriture se fait a ces coordonées 
    scorestring = "Score: %s" %score  # le % correspond au score 
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))  # parametre de l'ecriture du score 
    score_pen.hideturtle()


    #creation du joueur
    player = turtle.Turtle() # c'est un point 
    player.color("blue")  # le joueur est bleu 
    player.shape("triangle") # la forme du joueur est triangulaire 
    player.penup()   # 
    player.speed(0)  # vitesse instantanné ultra rapide on ne voit pas l'action se derouler 
    player.setposition(0,-252) # position initial du joueur 
    player.setheading(90) # inclinaison du jouer toujours a 90 par rapport a l'axe des x donc regarde vers le haut

    playerspeed = 15 # vitesse du joueur 


    #choisir nbr d ennemis
    number_of_enemies = 5  # nombre d'enemie sur le front  peut etre changer 
    #creation d une liste vide d ennemis
    enemies = [] # 


    #ajouter ennemies a la liste
    for i in range(number_of_enemies):   # selectionne le nombre d ennemi ici 5
        #creation de l ennemi
        enemies.append(turtle.Turtle())  # creation d ennemi fois 5
        
    for enemy in enemies:       # pour un ennemi parmis les 5
        enemy.color("red")
        enemy.shape("circle")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)  # la postion x de l'enemmie va etre aleatoire  dans cette intervalle 
        y = random.randint(100, 260)   # idem axe Y 
        enemy.setposition(x, y)  # defini sa position grace au etape en amont 

    enemyspeed = 3


    #creation de projectils pour le joueur
    bullet = turtle.Turtle()# c'est un point 
    bullet.color("yellow")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()

    bulletspeed = 27


    #definition etat du bullet
    #pret - pret a tirer
    #tire - bullet est lancé
    bulletstate = "ready"


    # bouger le joueur a droite ou a gauche
    def move_left():
        x = player.xcor()
        if x < -270:
            x = -270
        x -=playerspeed
        player.setx(x)

    def move_right():
        x = player.xcor()
        if x > 270:
            x = 270
        x +=playerspeed
        player.setx(x)

    def fire_bullet():
        #déclarer bulletstate comme un global si besoin de changement
        global bulletstate
        if bulletstate == "ready":
            bulletstate = "fire" 
            #bouger the bullet juste au dessus du joueur
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x,y)
            bullet.showturtle()

    def isCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 15:
            return True
        else:
            return False
     

    #association des touches fleches
    turtle.listen()
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_right, "Right")    
    turtle.onkey(fire_bullet, "space")


    #BOUCLE PRINCIPALE
    while True:

        for enemy in enemies:
            #faire bouger l ennemi
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)

            #bouger l'ennemi vers le joueur et en bas
            if enemy.xcor() > 280:
                #deplace ennemis en bas
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                #change la direction    
                enemyspeed *= -1    # regle des signes (1*(-1))=-1 et ((-1)*(-1))=1
                                    # donc déplacement inverse
            if enemy.xcor() < -280:
                #deplace ennemis en bas
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                #change la direction     
                enemyspeed *= -1



             #cheker si collision entre bullet et l'ennemi
            if isCollision(bullet, enemy):
                #reset le bullet
                bullet.hideturtle()
                bulletstate= "ready"
                bullet.setposition(0, 400)
                #reset l ennemi
                x = random.randint(-200, 200)
                y = random.randint(100, 260)
                enemy.setposition(x, y)
                #Mise A Jour du score
                score += 10
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


            #checker collision sur joueur
            if isCollision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                print("GAME OVER")
                break
                gw.bye()
                jardin()

        #mettre en mouvement le bullet
        if bulletstate == "fire":    
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)
        
        #cheker si le bullet a touché en haut
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate= "ready"
            
        global compteurgw       ##########################         WIN
        if score == 100:
            compteurgw +=1
            print("compteurgw = ",compteurgw)
            gw.bye()
            jardin()


# PIERRE FEUILLE CISEAU ##########################################################################


   # variables globales
ton_score = 0
ordi_score = 0

def pcf():#création fonction pierre feuille ciseaux
    global Largeur, Hauteur#annonce des variables utilisées dans la définition
    Largeur = 1280
    Hauteur = 720
    videfen()#application fonction videfen
    cangon = Canvas(fen, bg ='black', bd=0, highlightthickness=0)#création d'un canvas
    fen.resizable(width = FALSE,  height=FALSE)#la fenêtre ne change pas de taille
    cangon.pack() # ancre le canevas a la fenetre
    quitter = Button(fen, text ='Quitter',fg = "purple", command = salleGsortie).place(x="1150", y="650")

    
    def scorepcf(ordi,ton_coup):       #1= pierre  2= feuille  3=ciseaux
        global ordi_score, ton_score
        if ordi == 1 and ton_coup == 2:#si je joue "pierre" et l'ordinateur "feuille" alors l'ordinateur gagne 1 point
            ton_score += 1
        elif ordi == 2 and ton_coup == 1:#idem
            ordi_score += 1
        elif ordi == 1 and ton_coup == 3:#idem
            ordi_score += 1
        elif ordi == 3 and ton_coup == 1:#idem
            ordi_score += 1
        elif ordi == 3 and ton_coup == 2:#idem
            ordi_score += 1
        elif ordi == 2 and ton_coup == 3:#idem
            ton_score += 1        

    def jouer(ton_coup):
        global ordi_score, ton_score, score1, score2,compteurpcf
        ordi = randint(1,3)#l'ordinateur choisit une valeur entre 1,2 et 3
        if ordi==1:#si l'ordinateur choisit pierre
            lab2.configure(image=pierre)#le label de l'ennemi num2 prend l'image "pierre"
        elif ordi==2:
            lab2.configure(image=papier)
        else:
            lab2.configure(image=ciseaux)
        scorepcf(ordi,ton_coup)
        if ton_score == 3:
            compteurpcf += 1
            print("compteurpcf = ",compteurpcf)
            salleGsortie()

        
    def jouer_pierre():
        jouer(1)
        lab1.configure(image=pierre)

    def jouer_papier():
        jouer(2)
        lab1.configure(image=papier)

    def jouer_ciseaux():
        jouer(3)
        lab1.configure(image=ciseaux)

    
    
    #images
    rien = PhotoImage(file ='images/rien.gif')
    pierre = PhotoImage(file ='images/pierre1.png')
    papier = PhotoImage(file ='images/feuille1.png')
    ciseaux = PhotoImage(file ='images/ciseaux1.png')

    # Label
    texte1 = Label(cangon, text="Vous :", font=("Helvetica", 16))
    texte1.grid(row=0,column=0)#placement du label dans le canvas ligne=0 colonne=0

    texte2 = Label(cangon, text="Machine :", font=("Helvetica", 16))
    texte2.grid(row=0,column=2)#placement du label dans le canvas ligne=0 colonne=2

    lab1 = Label(cangon, image=rien)
    lab1.grid(row =4, column =0)#placement du label dans le canvas ligne=4 colonne=0

    lab2 = Label(cangon, image=rien)
    lab2.grid(row =4, column =2)#placement du label dans le canvas ligne=4 colonne=2

    # boutons
    bouton1 = Button(cangon,command=jouer_pierre)#création du bouton permettant au joueur de jouer pierre
    bouton1.configure(image=pierre)
    bouton1.grid(row =2, column =0)

    bouton2 = Button(cangon,command=jouer_papier)#création du bouton permettant au joueur de jouer feuille
    bouton2.configure(image=papier)
    bouton2.grid(row =2, column =1,)

    bouton3 = Button(cangon,command=jouer_ciseaux)#création du bouton permettant au joueur de jouer ciseaux
    bouton3.configure(image=ciseaux)
    bouton3.grid(row =2, column =2)

    bouton5 = Button(cangon,text='Quitter',command= salleGsortie)
    bouton5.grid(row =5, column =2, pady =10, sticky=W)
#création du bouton permettant au joueur de quitter le jeu pierre feuille ciseaux

######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES######
    
#############################

def entree(): #def de la def entree
    global Largeur,Hauteur,photo2,compteurentree,photodial1_4,photodial2_4,photodial3_4,photodial4_4,compteurcuisine
    Largeur = 1280
    Hauteur = 720
    videfen()

    # importation des photos
    photodial1entree = PhotoImage( file ="images/entreedial1.png")# photo avec les dialogues 
    photodial2entree = PhotoImage( file ="images/entreedial2.png")
    photodial3entree = PhotoImage( file ="images/entreedial3.png")
    photodial4entree = PhotoImage( file ="images/entreedial4.png")
    
    photo2 = PhotoImage( file ="images/entree.png")
    # creation d'un canevas sans image pour l'instant
    can2 = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)
    
    fen.resizable(width = FALSE,  height=FALSE) # fenetre non redimentionable
    can2.pack(expand=YES) # le canevas s'affiche par dessus l'ancien canevas
    menu() # le menu est present pour la fenetre

### DIALOGUE ###
    def dialentree1():
        can2.create_image(Largeur/2, Hauteur/2, image=photodial1entree)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialentree2).place(x="1027", y="576")
        # bouton suite pour faire defiler les images avec le dialogue
    def dialentree2():
        can2.create_image(Largeur/2, Hauteur/2, image=photodial2entree)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialentree3).place(x="1027", y="576")

    def dialentree3():
        can2.create_image(Largeur/2, Hauteur/2, image=photodial3entree)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialentree4).place(x="1027", y="576")

    def dialentree4():
        can2.create_image(Largeur/2, Hauteur/2, image=photodial4entree)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = entree).place(x="1027", y="576")    

    if compteurentree == 0: # si compteur egale à 0 : le canevas affiche juste une image et un bouton
        can2.create_image(Largeur/2, Hauteur/2, image=photo2)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialentree1).place(x="1027", y="576")
        # ce bouton affiche ici dialentree1 qui et definit au dessus
# =================
                
    if compteurentree >=1: 
        if compteurcuisine <=2 :  # si condition respectée , cree les widget suivants:
            can2.create_image(Largeur/2, Hauteur/2, image=photo2)#fonction pour importer la photo
            # Création d'un widget Button (bouton Quitter)
            quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
            retour = Button(fen, width=200, height=2,text='RETOUR AU MENU PRINCIPALE',bg="black",fg = "red", command=ini).place(x="0", y="665")
            droite = Button(fen, image = flechedroite, command = cuisine).place(x="1000", y="500")
            
    if compteurentree >=3:        # si condition respectée , cree les widget suivants: 
        can2.create_image(Largeur/2, Hauteur/2, image=photo2)#fonction pour importer la photo
        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        monter = Button(fen, text ='MONTER', bg="Black", fg = "red", command = couloir).place(x="370", y="200")
        retour = Button(fen, width=200, height=2,text='RETOUR AU MENU PRINCIPALE',bg="white",fg = "red", command=ini).place(x="0", y="665")
        
    compteurentree += 1 # à la fin du processus avec les conditions achevées, le compteur prend plus 1 "a chaque fois que entree est activé "
    print ("compteurentree = ",compteurentree)


    
################################ 
def cuisine():
    global Largeur,Hauteur,photok,compteurcuisine
    Largeur = 1280
    Hauteur = 720
    videfen()
    cank = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)

    photok = PhotoImage( file ="images/cuisine.png")
    photodial1_2cuisine = PhotoImage( file ="images/cuisinedial1.png") 
    photodial2_2cuisine = PhotoImage( file ="images/cuisinedial2.png")

    photodial5entree = PhotoImage( file ="images/entreedial5.png")
    photodial6entree = PhotoImage( file ="images/entreedial6.png")
    
    souris =  PhotoImage( file ="images/souris1.png")
    
    fen.resizable(width = FALSE,  height=FALSE)
    cank.pack(expand=YES)
    menu()

    
### DIALOGUE ###
    def dialcuisine1():
        cank.create_image(Largeur/2, Hauteur/2, image = photodial1_2cuisine)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialcuisine2).place(x="1027", y="576") 

    def dialcuisine2():
        cank.create_image(Largeur/2, Hauteur/2, image = photodial2_2cuisine)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = cuisine).place(x="1027", y="576")
        
    if compteurcuisine == 0:
        cank.create_image(Largeur/2, Hauteur/2, image = photok)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialcuisine1).place(x="1027", y="576")


#================

    if compteurcuisine >=1:
        if compteurcuisine <=2:
            cank.create_image(Largeur/2, Hauteur/2, image=photok)#fonction pour importer la photo
            # Création d'un widget Button (bouton Quitter)
            quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")

            if compteurlaby == 0:
                droite = Button(fen, image = flechedroite, command = laby).place(x="1100", y="350")

    if compteurcuisine >=2:       
        cank.create_image(Largeur/2, Hauteur/2, image=photok)#fonction pour importer la photo
        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")

    if compteurlaby ==1:
        cank.create_image(Largeur/2, Hauteur/2, image=photok)#fonction pour importer la photo
        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        retour = Button(fen, width=11, height=1, bg="Black", fg = "red",text='RETOUR', command=entree).place(x="640", y="665")

    compteurcuisine += 1
    print ("compteurcuisine = ",compteurcuisine)

    

##################
def couloir():
    global Largeur,Hauteur,photo3,compteurcouloir,photodialcouloir1,photodialcouloir2,photodialcouloir3
    Largeur = 1280
    Hauteur = 720
    videfen()
    photo3 = PhotoImage( file ="images/couloir.png") 
    can3 = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)

    photodialcouloir1 = PhotoImage( file ="images/couloirdial1.png")
    photodialcouloir2 = PhotoImage( file ="images/couloirdial2.png")
    photodialcouloir3 = PhotoImage( file ="images/couloirdial3.png")

    fen.resizable(width = FALSE,  height=FALSE)
    can3.pack(expand=YES)
    menu()

 ### DIALOGUE ###
    def dialcouloir1():
        can3.create_image(Largeur/2, Hauteur/2, image = photodialcouloir1)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialcouloir3).place(x="1027", y="576") 


    def dialcouloir3():
        can3.create_image(Largeur/2, Hauteur/2, image = photodialcouloir3)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = couloir).place(x="1027", y="576")
        
    if compteurcouloir == 0:
        can3.create_image(Largeur/2, Hauteur/2, image = photo3)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialcouloir1).place(x="1027", y="576")


#================   
    if compteurcouloir >= 0:
            if compteurcouloir <= 1:
                can3.create_image(Largeur/2, Hauteur/2, image=photo3)#fonction pour importer la photo
                # Création d'un widget Button (bouton Quitter)
                quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
                
    if compteurcouloir == 1:
        can3.create_image(Largeur/2, Hauteur/2, image=photo3)#fonction pour importer la photo
        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        gauche = Button(fen, image = flechegauche, command = chambre).place(x="200", y="350")
   
    if compteurcouloir >= 2:
        can3.create_image(Largeur/2, Hauteur/2, image=photo3)#fonction pour importer la photo
        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        retour = Button(fen, width=11, bg="Black", fg = "red", height=1,text='RETOUR', command=entree).place(x="640", y="665")
        devant = Button(fen, text ='Î'  , bg="Black", fg = "red", command = sortie).place(x="640", y="400")
        

    compteurcouloir += 1
    print("compteurcouloir =",compteurcouloir)
##################
def chambre():
    global Largeur,Hauteur,photo4,compteurchambre,photodialchambre1
    Largeur = 1280
    Hauteur = 720
    videfen()
    photo4 = PhotoImage( file ="images/chambre1.png") 
    can4 = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)

    photodialchambre1 = PhotoImage( file ="images/chambredial1.png")

    fen.resizable(width = FALSE,  height=FALSE)
    can4.pack(expand=YES)
    menu()

   
 ### DIALOGUE ###
    def dialchambre1():
        can4.create_image(Largeur/2, Hauteur/2, image = photodialchambre1)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = chambre).place(x="1027", y="576") 
       
    if compteurchambre == 0:
        can4.create_image(Largeur/2, Hauteur/2, image = photo4)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialchambre1).place(x="1027", y="576")

#================   

    if compteurchambre >= 1:
        can4.create_image(Largeur/2, Hauteur/2, image=photo4)#fonction pour importer la photo
        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        retour = Button(fen, width=11, height=1, bg="Black", fg = "red",text='RETOUR', command= couloir).place(x="640", y="665")
        devant = Button(fen, text ='Î'  , bg="Black", fg = "red", command = salledufond).place(x="640", y="400")

    compteurchambre += 1
    print("compteurchambre = ",compteurchambre )

##################
def salledufond():
    global Largeur,Hauteur,photoch,compteursalledufond
    Largeur = 1280
    Hauteur = 720
    videfen()
    photoch = PhotoImage( file ="images/salledufond.png") 
    canch = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)
    fen.resizable(width = FALSE,  height=FALSE)
    canch.pack(expand=YES)
    menu()

    photodialsalledufond1 = PhotoImage( file ="images/salledufonddial1.png")
    photodialsalledufond2 = PhotoImage( file ="images/salledufonddial2.png")
    
### DIALOGUE ###
    def dialsalledufond1():
        canch.create_image(Largeur/2, Hauteur/2, image = photodialsalledufond1)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialsalledufond2).place(x="1027", y="576") 

    def dialsalledufond2():
        canch.create_image(Largeur/2, Hauteur/2, image = photodialsalledufond2)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = snake).place(x="1027", y="576")
        
    if compteursalledufond == 0:
        canch.create_image(Largeur/2, Hauteur/2, image = photoch)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialsalledufond1).place(x="1027", y="576")

#================

    if compteursalledufond >= 1:
        canch.create_image(Largeur/2, Hauteur/2, image=photoch)#fonction pour importer la photo

        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        retour = Button(fen, width=11, height=1,bg="Black", fg = "red",text='RETOUR', command=chambre).place(x="640", y="665")

    compteursalledufond += 1
    print ("compteursalledufond = ",compteursalledufond)
    
##################
def salledebain():
    global Largeur,Hauteur,photo5,compteursalledebain
    Largeur = 1280
    Hauteur = 720
    videfen()
    photo5 = PhotoImage( file ="images/salledebain.png") 
    can5 = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)
    fen.resizable(width = FALSE,  height=FALSE)
    can5.pack(expand=YES)
    menu()

    photodialsalledebain1 = PhotoImage( file ="images/salledebaindial1.png")
    photodialsalledebain2 = PhotoImage( file ="images/salledebaindial2.png")
    
### DIALOGUE ###
    def dialsalledebain1():
        can5.create_image(Largeur/2, Hauteur/2, image = photodialsalledebain1)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialsalledebain2).place(x="1027", y="576") 

    def dialsalledebain2():
        can5.create_image(Largeur/2, Hauteur/2, image = photodialsalledebain2)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = salledebain).place(x="1027", y="576")
        
    if compteursalledebain == 0:
        can5.create_image(Largeur/2, Hauteur/2, image = photo5)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialsalledebain1).place(x="1027", y="576")

#================
    if compteursalledebain >= 1:

        can5.create_image(Largeur/2, Hauteur/2, image=photo5)#fonction pour importer la photo
        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        retour = Button(fen, width=11, height=1,bg="Black", fg = "red",text='RETOUR', command=couloir).place(x="640", y="665")
        droite = Button(fen, image = flechedroite, command = salledebain).place(x="1100", y="350")

    compteursalledebain += 1
    print("compteursalledebain = ",compteursalledebain)


##################
def sortie():
    global Largeur,Hauteur,photo6,compteursortie,photodialsortie
    Largeur = 1280
    Hauteur = 720
    videfen()
    photo6 = PhotoImage( file ="images/sortie.png") 
    can6 = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)
    fen.resizable(width = FALSE,  height=FALSE)
    can6.pack(expand=YES)
    menu()
    photodialsortie = PhotoImage( file ="images/sortiedial.png")

### DIALOGUE ###
    def dialsortie():
        can6.create_image(Largeur/2, Hauteur/2, image = photodialsortie)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = sortie).place(x="1027", y="576") 
        
    if compteursortie == 0:
        can6.create_image(Largeur/2, Hauteur/2, image = photo6)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialsortie).place(x="1027", y="576")

#================   
    if compteursortie >= 1:

        can6.create_image(Largeur/2, Hauteur/2, image=photo6)#fonction pour importer la photo


        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        retour = Button(fen, width=11, height=1,bg="Black", fg = "red",text='RETOUR', command=couloir).place(x="640", y="665")
        sortir = Button(fen, text ='sortir', bg="Black", fg = "red", command = jardin).place(x="650", y="390")
        gauche = Button(fen, image = flechegauche, command = salleGsortie).place(x="200", y="350")
        if compteurentree >=1 and compteurcuisine >= 1 and compteurlaby >= 1 and compteurcouloir >= 1 and compteurchambre >= 1:
            if compteursalledufond >= 1 and compteursnake >= 1 and compteursortie >= 1:
                if compteursalleGsortie >= 1 and compteurpcf >= 1 and compteurjardin >= 1:
                    droite = Button(fen, image = flechedroite, command = MAGIE).place(x="1100", y="350")
        # si toutes les salles et tout les jeu sont parcourus, cela fait apparaitre un bouton pour la fin
    compteursortie  += 1
    print("compteursortie= ",compteursortie)

##################
def salleGsortie():
    global Largeur,Hauteur,photo7,compteursalleGsortie
    Largeur = 1280
    Hauteur = 720
    videfen()
    photo7 = PhotoImage( file ="images/Gsortie.png") 
    can7 = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)
    fen.resizable(width = FALSE,  height=FALSE)
    can7.pack(expand=YES)
    menu()
    photodialsalleGsortie1 = PhotoImage( file ="images/Gsortiedial1.png")
    photodialsalleGsortie2 = PhotoImage( file ="images/Gsortiedial2.png")
    
### DIALOGUE ###
    def dialsalleGsortie1():
        can7.create_image(Largeur/2, Hauteur/2, image = photodialsalleGsortie1)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialsalleGsortie2).place(x="1027", y="576") 

    def dialsalleGsortie2():
        can7.create_image(Largeur/2, Hauteur/2, image = photodialsalleGsortie2)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = pcf).place(x="1027", y="576")
        
    if compteursalleGsortie == 0:
        can7.create_image(Largeur/2, Hauteur/2, image = photo7)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialsalleGsortie1).place(x="1027", y="576")

#================
    if compteursalleGsortie >= 1:
        can7.create_image(Largeur/2, Hauteur/2, image=photo7)#fonction pour importer la photo
        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        retour = Button(fen, width=11, height=1,bg="Black", fg = "red",text='RETOUR', command= sortie).place(x="640", y="665")

    compteursalleGsortie += 1
    print ("compteursalleGsortie = ",compteursalleGsortie)

##################
def jardin():
    global Largeur,Hauteur,photo8,compteurjardin
    Largeur = 1280
    Hauteur = 720
    videfen()
    photo8 = PhotoImage( file ="images/eljard.png") 
    can8 = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)

    fen.resizable(width = FALSE,  height=FALSE)
    can8.pack(expand=YES)
    menu()

    photodialjardin = PhotoImage( file ="images/eljarddial.png")

### DIALOGUE ###
    def dialjardin():
        can8.create_image(Largeur/2, Hauteur/2, image = photodialjardin)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = jardin).place(x="1027", y="576") 
    
    if compteurjardin == 0:
        can8.create_image(Largeur/2, Hauteur/2, image = photo8)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialjardin).place(x="1027", y="576")

#================
    if compteurjardin >= 1:
        if compteurgw == 0:
            can8.create_image(Largeur/2, Hauteur/2, image=photo8)#fonction pour importer la photo

            # Création d'un widget Button (bouton Quitter)
            quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
            retour = Button(fen, width=11, height=1,bg="Black", fg = "red",text='RETOUR', command = sortie).place(x="640", y="665")
            Gw = Button(fen, image = tablette, command = GALAXYWARS).place(x="355", y="610")
        if compteurgw >= 1:
            can8.create_image(Largeur/2, Hauteur/2, image=photo8)#fonction pour importer la photo

            # Création d'un widget Button (bouton Quitter)
            quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
            retour = Button(fen, width=11, height=1,bg="Black", fg = "red",text='RETOUR', command = sortie).place(x="640", y="665")

    compteurjardin += 1
    print("compteurjardin = ",compteurjardin)
##################
def MAGIE():
    global Largeur,Hauteur,photom,compteurmagie
    Largeur = 1280
    Hauteur = 720
    videfen()
    photom = PhotoImage( file ="images/OR.png")


    canm = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)

    fen.resizable(width = FALSE,  height=FALSE)
    canm.pack(expand=YES)
    menu()

    photodialor = PhotoImage( file ="images/ORdial1.png")

### DIALOGUE ###
    def dialor():
        canm.create_image(Largeur/2, Hauteur/2, image = photodialor)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = MAGIE).place(x="1027", y="576") 
    
    if compteurmagie == 0:
        canm.create_image(Largeur/2, Hauteur/2, image = photom)#fonction pour importer la photo
        suite = Button(fen, text ='suite',fg = "purple", command = dialor).place(x="1027", y="576")

    def milion():
        global Largeur,Hauteur,photomilion
        Largeur = 1280
        Hauteur = 720
        videfen()
        photomilion = PhotoImage( file ="images/milion.png")
        canmilion = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)
        canmilion.create_image(Largeur/2, Hauteur/2, image=photomilion)#fonction pour importer la photo
        fen.resizable(width = FALSE,  height=FALSE)
        canmilion.pack(expand=YES)
        menu()
        suite = Button(fen, text ='FIN',fg = "purple", command = ini).place(x="1027", y="576")

    def pluie():
        global Largeur,Hauteur,photopluie
        Largeur = 1280
        Hauteur = 720
        videfen()
        photopluie = PhotoImage( file ="images/pluie.png") 
        canpluie = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)
        canpluie.create_image(Largeur/2, Hauteur/2, image=photopluie)#fonction pour importer la photo
        fen.resizable(width = FALSE,  height=FALSE)
        canpluie.pack(expand=YES)
        menu()
        suite = Button(fen, text ='FIN',fg = "purple", command = ini).place(x="1027", y="576")

#================
    if compteurmagie >= 1:
        canm.create_image(Largeur/2, Hauteur/2, image=photom)#fonction pour importer la photo

        # Création d'un widget Button (bouton Quitter)
        quitter = Button(fen, text ='Quitter',fg = "purple", command = surdequit).place(x="1227", y="676")
        choix1 = Button(fen, width=20, height=1,bg="Black", fg = "red",text="PRENDRE VOTRE FRÈRE", command = pluie).place(x="440", y="565")
        choix2 = Button(fen, width=20, height=1,bg="Black", fg = "red",text="PRENDRE L'OR", command = milion).place(x="640", y="565")

    compteurmagie += 1
    print("compteurmagie = ",compteurmagie)
######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES######SALLES###

   #####################
   ### BARRE DE MENU ###
   

def apropos():
    showinfo("À PROPOS ...", "Jeu fait par FAZIL ,VINCENT, ABDEL, AMINE, RAYAN .")

def aide():
    showinfo("AIDE", "Ce jeu se joue avec la souris et avec les touches directionnels.")

def regle():
    showinfo("REGLES DU JEU", "Votre frère est entrer dans une maison !"
             "Allez de le retrouver...")


######################################## CODE ORINCIPAL ########################################

## CREATION BARRE DE MENU

def menu():    
    menubar = Menu(fen)

    menu1 = Menu(menubar, tearoff=0)  
    menu1.add_command(label="Quitter", command=surdequit)
    menubar.add_cascade(label="Commande", menu=menu1) #menu en cascade

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Règles du jeu", command=regle)
    menubar.add_cascade(label="Histoire", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos", command=apropos)
    menu3.add_separator()                                
    menu3.add_command(label="Aide", command=aide)
    menubar.add_cascade(label="Aide", menu=menu3)

    # configurer notre fenetre pour ajouter cette menu bar
    fen.config(menu=menubar)



############################ CREATION FENETRE TK
####################### creation 1 ere fentre 
# Création d'un widget Canvas (cadre) 720p

def ini():
    global Largeur,Hauteur,photo
    videfen()
    Largeur = 1280
    Hauteur = 720
    photo = PhotoImage( file ="images/maisonhante.png")
    can1 = Canvas(fen, width = Largeur, height=Hauteur, bg ='black', bd=0, highlightthickness=0)
    can1.create_image(Largeur/2, Hauteur/2, image=photo)#fonction pour importer la photo
    fen.resizable(width = FALSE,  height=FALSE)
    can1.pack(expand=YES)
    menu()

    def opt():
        showinfo ("TOUCHES",\
                  "LABYRINTHE: TOUCHES DIRECTIONNELS \n"+\
                  "  SNAKE   : TOUCHES DIRECTIONNELS\n"+\
                  "PIERRE FEUILLE CISEAU : TOUCHER LES CASES\n"+\
                  "GALAXIE WARS: TOUCHES DROITE ET GAUCHE PUIS ESPACE POUR TIRER")
    def game():
        showinfo ("REGLES DU JEU",\
                  "VOTRE FRÈRE S'EST ENFUIT DANS CETTE MAISON! \n"+\
                  "TENTEZ DE LE RETROUVER POUR NE PAS AVOIR D'ENNUIS ...")
        
    # Création d'un widget Button (bouton jouer)
    jouer = Button(fen,width=30, height=2, text ='JOUER', bg="black", fg = "red", command = entree, font=("Courier", 10, "normal") ).place(x="1000", y="550")
    # le bouton jouer active la fonction entree
    opt = Button(fen,width=30, height=2, text ='TOUCHES', bg="black", fg = "red", command = opt, font=("Courier", 10, "normal") ).place(x="1000", y="500")
    game = Button(fen,width=30, height=2, text ='HISTORE', bg="black", fg = "red", command = game, font=("Courier", 10, "normal") ).place(x="1000", y="450")
    # Création d'un widget Button (bouton Quitter)
    quitter = Button(fen,width=30, height=2, text ='QUITTER',bg='black',fg = "red", command = surdequit,font=("Courier",10, "normal")).place(x="1000", y="600")

    jouer = Button(fen,width=30, height=2, text ='LABYRINTHE', bg="black", fg = "red", command = laby, font=("Courier", 10, "normal") ).place(x="100", y="450")
    jouer = Button(fen,width=30, height=2, text ='SNAKE', bg="black", fg = "red", command = snake, font=("Courier", 10, "normal") ).place(x="100", y="500")
    jouer = Button(fen,width=30, height=2, text ='PIERRE FEUILLE CISEAU', bg="black", fg = "red", command = pcf, font=("Courier", 10, "normal") ).place(x="100", y="550")
    jouer = Button(fen,width=30, height=2, text ='GALAXY WARS', bg="black", fg = "red", command = GALAXYWARS, font=("Courier", 10, "normal") ).place(x="100", y="600")
    jouer = Button(fen,width=30, height=2, text ='FIN', bg="black", fg = "red", command = MAGIE, font=("Courier", 10, "normal") ).place(x="100", y="650")


#################################### MAIN LOOP
# On appele la premiere fenetre afin de lancer le programme
ini()
fen.mainloop() # fait fonctionner le programme

######################## 
### FIN DU PROGRAMME ###
########################
