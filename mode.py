#!/usr/bin/env python
# coding: utf-8

from parametre import *
# Ici définit la méthode qui va permettre la mise
# à jour du mode de visualisation de la grille
def mode(self,n):
	# On affecte à la variable mode de l'objet jeu
	# la valeur choisie avec le curseur
	self.jeu.mode = int(n)
	# Ici on a jsute besoin de reafficher la grille avec la
	# nouvelle vue. Il ne faut pas initialiser un nouveau jeu
	# au risque de ne pas pouvoir suivre la même partie 
	self.jeu.traceMaGrille()        
