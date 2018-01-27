#!/usr/bin/env python
# coding: utf-8

from parametre import *
# Ici on va définir la méthode qui va permettre de changer
# le mode de jeu, entre dévelopeur et joueur.
def couleur(self):
	# On indique où placer le texte du curseur.
	msg =Toplevel(self)
	# On met un curseur qui va permettre de choisir entre la
	# valeur 1 ou 0, ce curseur renvoie à la methode mode de
	# Demineur.
	curM =Scale(msg, length =250, label ="Choisir developpeur ou joueur",
	orient =HORIZONTAL,from_ =0, to =1, command =self.mode)
	# On met comme valeur initiale pour le curseur la valeur
	# qui est inscrite dans la variable mode de Jeu
	curM.set(self.jeu.mode)
	curM.pack()
