#!/usr/bin/env python
# coding: utf-8

from parametre import *
# On définie la fonction options 
def options(self):
        "Choix du nombre de lignes et de colonnes pour la grille"
        # on indique où placer ceci
        opt =Toplevel(self)
        
        # On définie un curseur long de 200 ayant pour titre
        # "Nombre de lignes" et qui va permettre de choisir le
        # nombre de ligne. On fais varier ce curseur de 1 à 30
        # en lui faisant prendre des valeurs entière. On associe
        # à ce curseur la commande majLignes de l'objet Demineur
        # On précise aussi que le curseur est horizontal
        curL =Scale(opt, length =200, label ="Nombre de lignes :",
            orient =HORIZONTAL,from_ =1, to =30, command =self.majLignes)
        # On détermine la position initiale du curseur, en lui
        # affectant la valeur de la variable correspondant dans
        # l'objet Jeu : nlig
        curL.set(self.jeu.nlig) 
        curL.pack()
        
        # On définie un curseur long de 200 ayant pour titre
        # "Nombre de colonnes" et qui va permettre de choisir le
        # nombre de ligne. On fais varier ce curseur de 1 à 30
        # en lui faisant prendre des valeurs entière. On associe
        # à ce curseur la commande majColonnes de l'objet Demineur.
        # On précise aussi que le curseur est horizontal
        curH =Scale(opt, length =200, label ="Nombre de colonnes :",
            orient =HORIZONTAL,from_ =1, to =30, command =self.majColonnes)
        # On détermine la position initiale du curseur, en lui
        # affectant la valeur de la variable correspondant dans
        # l'objet Jeu : ncol
        curH.set(self.jeu.ncol)
        curH.pack()
        
        # On définie un curseur long de 200 ayant pour titre
        # "Probabilitee de mines" et qui va permettre de choisir
        # le nombre de ligne. On fais varier ce curseur de 1 à 9
        # en lui faisant prendre des valeurs entière. On associe
        # à ce curseur la commande pmines de l'objet Demineur
        # On précise aussi que le curseur est horizontal
        curM =Scale(opt, length =200, label ="Probabilitee de mines :",
            orient =HORIZONTAL,from_ =1, to =9, command =self.pmines)
        # On détermine la position initiale du curseur, en lui
        # affectant la valeur de la variable correspondant dans
        # l'objet Jeu : pmines
        curM.set(self.jeu.pmines)
        curM.pack()
