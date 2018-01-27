#!/usr/bin/env python
# coding: utf-8

from parametre import *
# Ici on va définir la méthode qui va mettre à jour le nombre
# de ligne de la grille de jeu
def majLignes(self, n):
	# On affecte donc à la variable nlig de l'instance jeu la 
	# valeur prise par le curseur. 
	self.jeu.nlig = int(n)
	# On va donc comme pour la mise à jour du nombre de colonne
	# initiaiser une nouvelle grille et procéder à son affichage.
	self.jeu.traceGrille()
