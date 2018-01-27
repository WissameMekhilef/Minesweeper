#!/usr/bin/env python
# coding: utf-8

# On importe les paramètres
from parametre import *
# Mais on aussi besoin de tous les objets pour pouvoir
# les instanciers
from MenuBar import MenuBar
from Jeu import Jeu
from Affichage import Affichage
# On définie la classe Demineur
class Demineur(Frame):
	"corps principal du programme"
# _____________________________________________________________
# Ici on détermine les attributs de l'objet Demineur
	def __init__(self):
		# On définie la fenetre de jeu
		Frame.__init__(self)
		# Et on lui donne les dimensions initiale
		self.master.geometry("900x600")
		# On donne ensuite un titre à cette fenêtre
		self.master.title(" Jeu de Demineur")
        
		# On créer une instance mbar de MenuBar
		# C'est la barre qui se situe en haut de la fenêtre et
		# qui permet de paramètrer le jeu.
		self.mbar = MenuBar(self)
		# On place ceci en indiquant quelques paramètres.
		self.mbar.pack(side =TOP, expand =NO, fill =X)
        
		# De même on créer une instance jeu de Jeu.
		# C'est le cadre de jeu , celui sur lequel la grille
		# est dessinée.
		self.jeu =Jeu(self)
		# On place ceci en indiquant quelques paramètres
		# notemment celui expand qui permet au cadre de prendre
		# le maximum de place
		self.jeu.pack(side= LEFT, expand =YES, fill=BOTH,)

		# De même on créer une instance affichage d'Afficahge
		# C'est le cadre situé à droite de la fenêtre de jeu
		# il permet un affichage de l'évolution de la partie.
		self.affichage = Affichage(self)
		# On place ceci en indiquant quelques paramètres
		self.affichage.pack(side=RIGHT, expand = NO, fill=BOTH)
        
		# Ici on utilise la fonction pack du module tkinter.
		self.pack()

		# Pour lancer la musique pendant le jeu on a besoin de
		# lancer une fonction particulière en fonction du système
		# d'exploitation sur lequel le programme tourne et donc
		# d'enregistrer le nom du système dans une variable global
		# Ici on va determiner sur quelle systeme le jeu tourne
		global operatingSystem
		# On initialise une variable qui va enregistrer le nom du 
		# systeme
		operatingSystem = 'none'
		# On attribut a cette variable le nom du system grace a la
		# librairie platform
		operatingSystem = platform.system()
		print('Demineur : Le jeu tourne actuellement sous :',operatingSystem)

# Ici on importe les méthodes de l'objet Demineur
	from options import options
	from pmines import pmines
	from majColonnes import majColonnes
	from majLignes import majLignes
	from reset import reset
	from couleur import couleur
	from fond import fond
	from principe import principe
	from aPropos import aPropos
	from mode import mode
	from sauver import sauver
	from ouvrir import ouvrir
    

    
