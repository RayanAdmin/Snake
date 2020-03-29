from turtle import*
import time
from random import randint



Nom = input("\nEntrez votre nom : ").upper()
if len(Nom) > 1:
    Nom = Nom[0] + Nom[1:].lower()



print("\nNiveau de difficulté possible :\n")

print("Facile")
print("Moyen")
print("Difficile")
print("Impossible")
print("")

Level = input("\nEntré votre niveau de difficulté : ").lower()

while Level not in ["facile", "moyen", "difficile", "impossible", " facile", " moyen", " difficile", " impossible"]:
    Level= input("\nRentrer un des niveaux proposés! : ")    
    


Partie = 1
print ("\nPartie N°1 : \n")


scene = Screen()
scene.bgpic("Fond.gif")
scene.setup(850, 600, 500, 50)

titre = "Snake de " + Nom
title(titre)


snake = [Turtle("square")]
snake[0].up()
snake[0].speed(0)

apple = Turtle("circle")
apple.speed(500)
apple.up()

bordure = Turtle("blank")
bordure.speed(0)
bordure.width(3)
bordure.up()

score = 0
rotation = snake[0].heading()

X = -280
Y = 255


for loop in range(15):

    bordure.goto(X,Y)
    bordure.down()
    bordure.setheading(0)
    bordure.forward(30)
    bordure.setheading(90)
    bordure.forward(30)
    bordure.setheading(180)
    bordure.forward(30)
    bordure.setheading(270)
    bordure.forward(30)
    bordure.up()
    X = X + 35

for loop in range(15):

    bordure.goto(X,Y)
    bordure.down()
    bordure.setheading(0)
    bordure.forward(30)
    bordure.setheading(90)
    bordure.forward(30)
    bordure.setheading(180)
    bordure.forward(30)
    bordure.setheading(270)
    bordure.forward(30)
    bordure.up()
    Y = Y - 35


for loop in range(15):

    bordure.goto(X,Y)
    bordure.down()
    bordure.setheading(0)
    bordure.forward(30)
    bordure.setheading(90)
    bordure.forward(30)
    bordure.setheading(180)
    bordure.forward(30)
    bordure.setheading(270)
    bordure.forward(30)
    bordure.up()
    X = X - 35

for loop in range(15):

    bordure.goto(X,Y)
    bordure.down()
    bordure.setheading(0)
    bordure.forward(30)
    bordure.setheading(90)
    bordure.forward(30)
    bordure.setheading(180)
    bordure.forward(30)
    bordure.setheading(270)
    bordure.forward(30)
    bordure.up()
    Y = Y + 35

bordure.up()


def Droite():
    global tour
    if tour == True:
        global rotation
        if rotation != 180:
            rotation = 0
            tour = False
    
def Gauche():
    global tour
    if tour == True:
        global rotation
        if rotation != 0:
            rotation = 180
            tour = False
def Haut():
    global tour
    if tour == True:
        global rotation
        if rotation != 270:
            rotation = 90
            tour = False
def Bas():
    global tour
    if tour == True:
        global rotation
        if rotation != 90:
            rotation = 270
            tour = False


Fichier = open("Couleurs.txt", "r")
print(Fichier.read())
Fichier.close()

C = input("\nRentrer la couleur choisie pour le serpent : ").lower()
while C not in ["blue", "red", "green", "yellow", "brown", "black", "pink", "orange", "purple", "grey"]:
    C = input("\nRentrer une couleur valable ! : ")

ecriture = Turtle("blank")
ecriture.speed(0)
ecriture.up()


ecriturescore = Turtle("blank")
ecriturescore.speed(0)
ecriturescore.up()
ecriturescore.goto(-420,260)
ecriturescore.write("Score : ", font = ("Arial", 20, "bold"))
ecriturescore.up()

scorejeu = Turtle("blank")
scorejeu.speed(0)
scorejeu.up()
scorejeu.goto(-315,259)
scorejeu.write("0", font = ("Arial", 20, "bold"))


Rejouer = "oui"
while Rejouer.lower() == "oui" or Rejouer.lower() == "ou" or Rejouer.lower() == "o" :
    
    if Level == "facile" or " facile":
        vitesse = 5

    if Level == "moyen" or " moyen" :
        vitesse = 20

    if Level == "difficile" or " difficile":
        vitesse = 100

    if Level == "impossible" or " impossible":
        vitesse = 50000

    snake[0].up()
    snake[0].goto(0,0)
    snake[0].color(C)
    
    if Partie > 1 :

        print ("\nPartie N°" + str(Partie) + " :" + "\n")
        print("")

    A = randint(-11,11)
    O = randint(-11,11)
    while A == 0 and O == 0:
        A = randint(-11,11)
        O = randint(-11,11)
    apple.goto(A*20, O*20)

    score = 0
    c = 1

    sortie = False 
    
    print("Appuyer 1 fois sur la fenétre Turtle pour commencer")
    print("")

    while c != 4 :
        ecriture.up()
        ecriture.speed(0)
        ecriture.goto(-20,100)
        ecriture.down()
        ecriture.write(c, font = ("Arial", 50, "bold"))
        c = c + 1
        time.sleep(1)
        ecriture.reset()
        ecriture.up()
        
    ecriture.speed(0)
    ecriture.goto(-80,100)
    ecriture.down()
    ecriture.write("Go !!!", font = ("Arial", 50, "bold"))
    time.sleep(1)
    ecriture.reset()
        

    while sortie == False:
        
        tour = True
        onkey(Droite, "Right")
        onkey(Gauche, "Left")
        onkey(Haut, "Up")
        onkey(Bas, "Down")
        scene.listen()
        
        snake.insert(0, Turtle("square", visible=False))
        snake[0].color(C)
        snake[0].speed(0)
        snake[0].setheading(rotation)
        rotation = snake[0].heading()
        snake[0].up()
        snake[0].goto(snake[1].pos())
        snake[0].forward(20)
        snake[0].st()


        if snake[0].xcor() > apple.xcor() - 5 and snake[0].xcor() < apple.xcor() + 5 and snake[0].ycor() > apple.ycor() - 5 and snake[0].ycor() < apple.ycor() + 5:
            for i in range (len(snake)):
                if snake[i].xcor() <= A*20 + 5 and snake[i].xcor() >= A*20 - 5 and snake[i].ycor() <= O*20 + 5 and snake[i].ycor() >= O*20 - 5:
                    A = randint(-11,11)
                    O = randint(-11,11)
            apple.goto(A*20, O*20)
            score = score + 1
            vitesse = vitesse + 10
            
            scorejeu.reset()
            scorejeu.speed(0)
            scorejeu.up()
            if score < 10 :    
                scorejeu.goto(-315,259)
            else :
                scorejeu.goto(-320,259)
                

            scorejeu.write(score, font = ("Arial", 20, "bold"))
        else:
            
            snake[-1].ht()
            snake.pop(-1)


        if snake[0].xcor() < -240 or snake[0].xcor() > 235 or snake[0].ycor() < -232 or snake[0].ycor() > 248 : 
             sortie = True
             print("Fin du Jeu : vous êtes sortie du terrain")


             
	     
        for i in range(1, len(snake)):
            if snake[0].pos() == snake[i].pos():
                sortie = True
                print("Fin du Jeu : vous vous etes mordu la queue")
    
        time.sleep(1/vitesse)
        
    print("\nVotre score est de",score,"\n") 
    Rejouer = input("Voulez-vous rejouer ? (oui/non) : ")

    print("")
    Partie = Partie + 1

    for k in range(len(snake)):
        snake[k].shape("blank")
    snake = [Turtle("square")]
    snake[0].color(C)

    scorejeu.reset()
    scorejeu.speed(0) 
    scorejeu.up()
    scorejeu.goto(-315,259)
    scorejeu.write("0", font = ("Arial", 20, "bold"))
        
    

time.sleep(1)
scene.bye()  
