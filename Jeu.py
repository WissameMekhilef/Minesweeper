#!/usr/bin/env python
# coding: utf-8


from parametre import *
class Jeu(Frame):
    """Jeu de jeu (grille de n x m cases)"""
# _____________________________________________________________
# Ici on détermine les attributs de l'objet Jeu
    def __init__(self, boss =None):
        # Ce Jeu de jeu est constitué d'un cadre redimensionnable
        # contenant lui-même un canevas. A chaque redimensionnement du
        # cadre, on calcule la plus grande taille possible pour les
        # cases (carrées) de la grille, et on adapte les dimensions du
        # canevas en conséquence.
        Frame.__init__(self)
        
        self.nlig, self.ncol = 10, 10
        # Grille initiale = 10 x 10
        # Liaison de l'événement <resize> à un gestionnaire approprié :
        self.bind("<Configure>", self.redim)
        # Canevas :
        self.can =Canvas(self, bg ="white", borderwidth =0,highlightthickness =1,
			highlightbackground ="white")
        # Liaison de l'événement <clic de souris> à son gestionnaire :
        self.can.bind("<Button-1>", self.clicGauche)
        self.can.bind("<Button-3>",self.clicDroit)
        self.can.pack()
        # Initialistaion de la probabilité de base
        self.pmines = 0.2
        # Initialisation d'une variable gardant le nombres de mines
        self.nmines = 0
        # Dimensionnement des tableaux aux valeurs max
        self.code =[]
        for i in range(30):           
            self.code.append([0]*30)   
        self.etat =[]
        for i in range(30):           
            self.etat.append([0]*30)
        self.NbCasesaLiberer=0
        # Variable prennant en compte le mode de vue
        # Programmeur ou Joueur
        self.mode=1
        # variable pour le nom du joueur
        self.gagnant=""
        # On met en place des variables qui vont
        # enregistrer l'heure de début et l'heure de fin
        self.t0=0
        self.t1=0
        
# _____________________________________________________________
# Ici on importe toutes les méthodes de l'objet Jeu
    from redim import redim
    from initGrille import initGrille
    from traceMaGrille import traceMaGrille
    from liberer import liberer
    from clicGauche import clicGauche
    from clicDroit import clicDroit
    from gagne import gagne
    from traceGrille import traceGrille
