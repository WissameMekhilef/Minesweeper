#!/usr/bin/env python
# coding: utf-8

from parametre import *

def saisir_nom(self,event):                          #event précise que la fonction sera utilisée après une action de l'utilisateur

    gagnant=entr1.get()                         #affecte la saisie à la variable gagnant
    fen1.destroy()
    self.affichageNom(gagnant)

def affichageNom(self):
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

def gagne(self):
	# Cette fonction sert a tester le jeu pour savoir si il est
	# gagné ou pas et dans le cas contraire d'afficher des
	# information concernant le déroulement de la partie
	## On initialise quelques variables ##
	# La première compte le nombre de case qui sont dans l'état 4
	compteurp=0
	# La deuxième compte le nombre de case qui sont libérer,
	# c-à-d soit dans l'état 2 , 3 ou 5
	NbLibres=0
	# On créer une boucle qui parcourt la grille
	for n in range(self.nlig):
		for m in range(self.ncol):
			# Si la case rencontrée est dans l'état 4
			if self.etat[n][m]==4:
				# Alors on incrémente le compteurp de 1
				# Etape longue certe car on sais dejà que si la
				# première case rencontrée est dans l'état 4 alors
				# toutes les autres case seront dans cette état
				compteurp=compteurp+1
			# Mais si la case a était libérée, état 2 , 3 ou 5
			if ( (self.etat[n][m]==2) | (self.etat[n][m]==3) | (self.etat[n][m]==5)):
				# Alors on Incrémente le compteur de case libre
				# de 1
				NbLibres=NbLibres+1
	# Ici on imprime sur la fenêtre de commande le nombre de case
	# restantes à libérer
	print("gagne : Nombre de cases restantes à libérer: ",self.NbCasesaLiberer-NbLibres,NbLibres)
	# Si le nombre de cases libérées est égal au nombre de case
	# à libérer alors le jeu est gagné
	if(NbLibres==self.NbCasesaLiberer):
		# On imprime sur la fenêtre de commande l'heure de fin
		print("gagne : heure de fin", self.t1)
		# On enregistre l'heure de fin de la partie
		self.t1=datetime.now()
		# On imprime sur la fenêtre de commande que la partie est
		# gagné et on indique aussi en combien de temps
		print("gagne : tu as gagné en ",self.t1-self.t0,"secondes")
		#self.saisir_nom()
	# Sinon si le compeurp est égale au nombre de cases à libérer
	# ajouté du nombre de mines que comporte le jeu. Alors celà
	# veut dire que la partie est perdu	
	elif compteurp==self.NbCasesaLiberer+self.nmines:
                print("gagne : tu as perdu")

