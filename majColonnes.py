#!/usr/bin/env python
# coding: utf-8

from parametre import *
# Ici on va definir la méthode qui va permettre
# de mettre a jour le nombre de colonne pour la
# grille de jeu.
def majColonnes(self, n):
	# On affecte donc à la variable définie dans
	# l'objet Jeu prennant en compte le nombre de
	# colonne la valeur choisie avec le curseur
	self.jeu.ncol = int(n)
	# Ici on va procéder à l'initialisation d'une
	# noivelle grille de jeu puis à son affichage.
	self.jeu.traceGrille()
