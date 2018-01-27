#!/usr/bin/env python
# coding: utf-8

from parametre import *
# Cette méthode est resté au stade de test elle n'est pas 
# utilisable en l'état
def fond(self):
	# On indique où placer le message
	msg =Toplevel(self)
	# On choisit içi les paramètre du message : taille,
	# aspect, position et le texte à afficher.
	Message(msg, width =200, aspect =100, justify =CENTER,
	text ="Choisir la couleur du fond du jeux\n").pack(padx =10, pady =10)
