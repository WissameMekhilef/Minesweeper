#!/usr/bin/env python
# coding: utf-8

from parametre import *
def clicDroit(self,event):
	"Gestion du clic droit de la souris"
	# On commence par determiner la ligne et la colonne :
	lig, col = int(event.y/self.cote), int(event.x/self.cote)
	### On change l'etat de la case en case avec drapeau ##
	# On verifie que la case est soit libre soit miné 
	if (self.etat[lig][col]==0) | (self.etat[lig][col]==1):
		# Si c'est le cas alors on change l'état de la case
		# pour quelle apparaisse avec drapeau lors du 
		# rafraichissement
		self.etat[lig][col]=6
	# On lance la fonction gagne pour tester si le jeu est
	# gagné ou pas
	self.gagne()
	# Et on lance la fonction traceMaGrille pour rafraichir
	# la grille de jeu
	self.traceMaGrille()
