#!/usr/bin/env python
# coding: utf-8

from parametre import *
def principe(self):
	"Fenetre-message contenant la description sommaire du principe du jeu"
	# Ici on indique ou placer le texte
	msg =Toplevel(self)
	Message(msg, bg ="navy", fg ="ivory", width =400,
		font ="Helvetica 10 bold",
		# On insere dans la variable texte le texte que l'on souhaite afficher
		text ="""Chaque case de la grille peut soit cacher une mine, soit être vide. Le but du jeu est de découvrir toutes les cases libres sans faire exploser les mines, 
			c'est-à-dire sans cliquer sur les cases qui les dissimulent. Lorsque le joueur clique sur une case libre et que toutes les cases adjacentes le sont également, 
			une case vide est affichée. Si en revanche au moins l'une des cases avoisinantes contient une mine, un chiffre apparaît, indiquant le nombre de cases adjacentes 
			contenant une mine. 
			En comparant les différentes informations récoltées, vous avez ainsi la possibilité de progresser dans le déminage du terrain.
			Si vous vous trompez et que vous cliquiez sur une mine, vous avez perdu.""").pack(padx =10, pady =10)
