
from tkinter import *


global gagnant
gagnant=""


def saisir_nom(event):                          #event précise que la fonction sera utilisée après une action de l'utilisateur
    global gagnant
    gagnant=entr1.get()                         #affecte la saisie à la variable gagnant
    fen1.destroy()
    
    
fen1 = Tk()                                     #crée une fenetre graphique
fen1.title('Vous entrez dans le top 10')        #donne un nom à la fenetre
txt1 = Label(fen1, text = 'Entrez votre nom :') #crée un texte dans la fenetre
entr1 = Entry(fen1)                             #crée une zone dans laquelle l'utilisateur pourra saisir un nom
txt1.grid(row=0,)                               #place la zone de texte
entr1.grid(row=0,column=1)                      #place la zone de saisie
entr1.bind("<Return>",saisir_nom)               #relie la commande "Entrer" à la fonction "saisir_nom"


fen1.mainloop()                                 #lance la boucle d'attente d'événement    
obFichier = open('noms des joueurs','a')
obFichier.write(gagnant)
obFichier.write('\n')
obFichier.close()
of = open('noms des joueurs','r')
t = of.read()
print(t)





