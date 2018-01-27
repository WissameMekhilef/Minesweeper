#!/usr/bin/env python
# coding: utf-8

from parametre import *
# On définie ici la fonction pmines qui va mettre a jour
# la variable pmines de l'objet Jeu
def pmines(self,n):
	# On affecte à la variable pmines de l'objet Jeu 
	# la valeur choisie par le joueur par le biais du
	# curseur en la divisant par 10.
	# On obtient donc une probabilité comprise entre
	# 0.1 et 0.9
	self.jeu.pmines = (int (n))/10
	# On affiche sur la fenêtre de commande la nouvelle
	# valeur de la probabiltée de mines
	print("pmines: pmines= ",self.jeu.pmines)
	# On relance une initialisation de la grille suivie
	# de son affichage.
	self.jeu.traceGrille()
