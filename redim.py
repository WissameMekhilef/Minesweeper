#!/usr/bin/env python
# coding: utf-8

from parametre import *
def redim(self, event):
    "Opérations effectuées à chaque redimensionnement"
    # Les propriétés associées à l'événement de reconfiguration
    # contiennent les nouvelles dimensions du cadre :
    self.width, self.height = event.width -4, event.height -4
    # La différence de 4 pixels sert à compenser l'épaisseur
    # de la 'highlightbordure" entourant le canevas
    self.traceMaGrille()

