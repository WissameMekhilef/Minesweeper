#!/usr/bin/env python
# coding: utf-8

from parametre import *
class MenuBar(Frame):
    """Barre de menus déroulants"""
    def __init__(self, boss =None):
        Frame.__init__(self, borderwidth =2, relief =GROOVE)
        ##### Menu <Fichier> #####
        fileMenu = Menubutton(self, text ='Fichier')
        fileMenu.pack(side =LEFT, padx =5)
        me1 = Menu(fileMenu)
        me1.add_command(label ='Options',
            underline =0,command = boss.options)
        me1.add_command(label ='Restart', 
            underline =0,command = boss.reset)
        me1.add_command(label ='Terminer', 
            underline =0,command = boss.quit)
        fileMenu.configure(menu = me1)

        ##### Menu <gestion> #####
        JeuMenu = Menubutton(self, text ='Gestion')
        JeuMenu.pack(side =LEFT, padx =5)
        me1 = Menu(JeuMenu)
        me1.add_command(label ='Sauver', underline =0,
            command = boss.sauver)
        me1.add_command(label ='Ouvrir', underline =0,
            command = boss.ouvrir)
        JeuMenu.configure(menu = me1)
        
        ##### Menu <Aide> #####
        helpMenu = Menubutton(self, text ='Aide')
        helpMenu.pack(side =LEFT, padx =5)
        me1 = Menu(helpMenu)
        me1.add_command(label ='Principe du jeu', underline =0,
            command = boss.principe)
        me1.add_command(label ='A propos ...', underline =0,
            command = boss.aPropos)
        helpMenu.configure(menu = me1)

        ##### Menu <Configuration> #####
        confMenu = Menubutton(self, text ='Configuration')
        confMenu.pack(side =LEFT, padx =5)
        me1 = Menu(confMenu)
        me1.add_command(label ='Couleurs', underline =0,
            command = boss.couleur)
        me1.add_command(label ='Image de fond', underline =0,
            command = boss.fond)
        confMenu.configure(menu = me1)        
