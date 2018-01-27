#!/usr/bin/env python
# coding: utf-8

# Ici on importe la totalité avec * du code parametre.py.
from parametre import *
# _____________________________________________________________
# Ici on va importer tout les objets du programme pour faire
# tourner le jeu
from MenuBar import MenuBar
from Jeu import Jeu
from Affichage import Affichage
from Demineur import Demineur
# _____________________________________________________________
# Ici on céer un instance sans nom de l'objet Demineur



if __name__ == '__main__':
    Demineur().mainloop()
