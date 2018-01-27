#!/usr/bin/env python
# coding: utf-8

from parametre import *
def traceMaGrille(self):
        "Dessin de la grille en fonction des options & dimensions"
        # On doit determiner la taille maximal que pour nos cases
        # et celà en fonction de la taille de la fenêtre et du
        # nombre de colonnes ainsi que le nombre de lignes.
        # lmax=largeur et hmax=hauteur maximales possibles pour 
        # les cases :
        lmax = self.width/self.ncol
        hmax = self.height/self.nlig
        # Pour que la case reste un carré on donne comme coté à
        # à la case le plus petit coté entre lmax et hmax.
        self.cote = min(lmax, hmax)
        # Maintenant il est nécessaire de redessiner le canevas
        # pour l'adapter aux nombres de cases et à la taille 
        # de la fenêtre de jeu
        # établissement de nouvelles dimensions pour le canevas :
        larg, haut = self.cote*self.ncol, self.cote*self.nlig
        # On reconfigure le canevas avec les nouvelles dimensions
        self.can.configure(width =larg, height =haut)
        #### Tracé de la grille :Jeu de Démineur ####
        # Effacement dessins antérieurs
        self.can.delete(ALL)
        ### Determinantion du mode de jeu ###
        
        ### Tracé des lignes pour le cadrillage ###
        # On initialise une variable
        s =self.cote
        # On commence par les lignes horizontales.
        # On fais donc varier l en fonction  du nombre de lignes
        # pour pouvoir tracer autant de trait que l'utilisateur
        # a souahité
        for l in range(self.nlig):
			# A chaque ligne on utilise la fonction create_line
			# du module tkinter pour tracer la ligne.
			# On donne comme argument a fill black pour permettre
			# de tracer les traits en noir
            self.can.create_line(0, s, larg, s, fill="black")
            # Ici on ajoute self.cote pour pouvoir passer a la
            # ligne suivante
            s +=self.cote
        # On réinitialise cette variable pour pouvoir la
        # réutiliser.
        s =self.cote
        # On recommence comme pour la boucle précédentes sauf
        # qu'ici on va traiter les lignes verticales
        for c in range(self.ncol):
            self.can.create_line(s, 0, s, haut, fill ="black")
            s +=self.cote
        ### Dessin des ronds ###
        # Ici on va procéder au tracé des ronds qui matérialise
        # les mines.
        # On créer une boucle qui va traiter toute les cases du
        # tableau de jeu.
        # On fais varier n jusqu'au nombre de ligne max
        for n in range(self.nlig):
			# On fais varier m jusqu'au nombre de colonne max
            for m in range(self.ncol):
				# On établit des variables
                x1 = m *self.cote +5        #  
                x2 = (m +1)*self.cote -5    # 
                y1 = n *self.cote +5        #
                y2 = (n +1)*self.cote -5    #
                # Maintenant si la case voisine n'est pas miné et
                # qu'elle n'est pas non plus mise en drapeu
                if (self.etat[n][m]!=3) & (self.etat[n][m]!=6):
					# Ici on va profiter de la boucle pour gagner
					# tu temps de calcul.
					# Si l'etat de la variable est a 0 c'est à
					# dire que l'utilisateur est en mode 
					# développeur
                    if self.mode==0:
                        # On attribut à la variable coul une 
                        # matrice qui permet de distinguer 
                        # les cases minées
                        coul=["green","red","blue","yellow","black","cyan","purple"][self.etat[n][m]]
                    # Sinon alors l'utilisateur est en mode jeu
                    else :
                        # Alors on attribut à la variable coul
                        # une matrice ne permettant pas de 
                        # distinguer miné ou libre
                        coul =["white","white","blue","yellow","black","cyan","purple"][self.etat[n][m]]
                    # Connaissant le mode de jeu on peut tracer
                    # les cercles en conséquences
                    # Et donc si la case voisines n'est pas minée
                    # ou mise en drapeau
                    self.can.create_oval(x1, y1, x2, y2, outline ="white",width =1, fill =coul)
                elif self.etat[n][m]==3:
                    coul =["white","blue","red","green","orange","purple","brown","black","magenta"][self.code[n][m]]
                    self.can.create_text(x1+self.cote/2, y1+self.cote/2, font="Purisa",fill = coul, text=self.code[n][m])
                # Sinon si la case est en état 6
                elif self.etat[n][m]==6:
                    d=7
                    e=2*d
                    # On créer une matrice de point qui vont 
                    # servir pour construire le drapeau
                    points = [x1+d,y1+self.cote-e,x1+d+(self.cote-e)/4,y1+d,x1+d+2*(self.cote-e)/3,y1+d,x1+self.cote-e,y1+d+(2*d),x1+self.cote-e,y1+d+(2*d)+self.cote/3,x1+d+2*(self.cote-e)/3,y1+d+self.cote/3,x1+3.225*d,y1+d+self.cote/3]
                    # On se sert de la fonction creat_polygon pour
                    # dessiner le drapeau
                    self.can.create_polygon(points, outline='black', fill='purple', width=2)    
