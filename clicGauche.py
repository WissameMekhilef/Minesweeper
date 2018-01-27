#!/usr/bin/env python
# coding: utf-8

from parametre import *
def clicGauche(self, event):
	"Gestion du clic de souris gauche"
	# On commence par déterminer la ligne et la colonne :
	lig, col = int(event.y/self.cote), int(event.x/self.cote)
	# On vérifie sur quel type de case on a cliqué
	# Si on a cliqué sur une case miné
	if self.code[lig][col]==9:
		# Alors on va parcourir la grille pour coder toutes
		# les cases en état 4
		for m in range(0,self.ncol):
			for n in range(0,self.nlig):
				# Ici code pour chaque case l'état 4
				self.etat[n][m]=4
	# Sinon si on clique sur une case codé 0
	elif self.code[lig][col]==0:
		# Alors on libére la case et on appel la fonction
		# libérer pour procéder à la libération des cases voisines
		self.etat[lig][col]=2
		# Ici on stipule que l'on souahite libérer
		# uniquement la case codé 0 sur laquel on a cliqué
		self.liberer(lig,col)
	# Sinon celà veut dire que la case a un ou des
	# voisins possédant des mines
	else :
		# Dans ce cas on passe dans la case dans l'état 3
		# qui va permettre lors du passage de la fonction
		# traceMaGrille de voir combien de mine touchent
		# cette case
		self.etat[lig][col]=3
	# Ici comme pour le clic Droit on teste si le jeu est
	# gagné
	self.gagne
	# et on lance cette fonction pour rafraichir la grille
	self.traceMaGrille()
