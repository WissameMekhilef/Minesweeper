#!/usr/bin/env python
# coding: utf-8

from parametre import *
class Affichage(Frame):
	
# Ici on détermine les attributs de l'objet Affcihage
	def __init__(self, parent):
		Frame.__init__(self, parent)    
		self.parent = parent        
		self.initUI()
	# Ici on détermine la méthode qui va créer le canevas
	# et le remplir
	def initUI(self):
		self.pack()
		canvas = Canvas(self)
		canvas.create_text(0,20, anchor=W, font="Purisa",text="Le jeu tourne actuellement sous :")
		canvas.create_text(0,60, anchor=W, font="Purisa",text="Nombre de case a liberer")
##        canvas.create_text(0,60, anchor=W, font="Purisa",
##        text=jeu.NbCasesaLiberer)
##        print("Affichage: ",NbCasesaLiberer)
		canvas.create_text(0,100, anchor=W, font="Purisa",text="Nombre de mines restante(s)")
		canvas.pack(fill=BOTH, expand=1) 
