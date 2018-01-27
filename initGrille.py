#!/usr/bin/env python
# coding: utf-8

from parametre import *

def initGrille(self):        
	# remise a zero du compteur de mines
	self.nmines=0
            
	# On remplis ici le tableau de mines
	# On recupere self.nlig qui est le nombre de ligne
	for n in range(self.nlig):
		# et self.ncol, le nombres de colonne
		for m in range(self.ncol):
			difficulte=self.pmines
			p=random()
			if  p<difficulte :
				# il y a une mine
				self.etat[n][m]=1 
				# on incremente la variable nmines
				self.nmines = self.nmines+1 
			else:
				# il n'y a pas de mine
				self.etat[n][m]=0
	print("initGrile : Le jeu comporte :",self.nmines," mines")
	self.NbCasesaLiberer= (self.ncol*self.nlig)- self.nmines
	print("initGrille : Nombre de cases à libérer: ",self.NbCasesaLiberer)
	#### CODAGE DES CASES DE LA GRILLE ####
	# Pour chaque grille proposée au joueur on va coder
	# chacune des cases de la grille pour permettre un
	# "éclatement" plus simple et une recupération
	# d'un grille aussi plus simple.
	### Création d'un tableau pour enregistrer le codage ###
	self.code =[]
	for i in range(30):           
		self.code.append([0]*30)       
            
	# PARCOURS DE LA GRILLE POUR CODER LES CASES #
	# On parcourt toute la grille pour
	# traiter toute les cases
	for i in range(self.nlig):                              
		for j in range(self.ncol):                          
			# Si la case traitée ne comporte pas de mine
			if self.etat[i][j]==0:                              
				# On determine limin la borne inferieure en terme de ligne
				limin=max(0,i-1)
				# On determine limax la borne superieure en terme de ligne
				limax=min(self.nlig-1,i+1)
				# On determine comin la borne inferieure en terme de colonne
				comin=max(0,j-1)
				# On determine comax la borne superieure en terme de colonne
				comax=min(self.ncol-1,j+1)
				# On initialise une variable qui va être le nombre de mines adjacente a la case traité
				nbm=0      #Compteur local à la case (i,j)                                         
				# Traitement des 8 cases adjacentes pour determiner combien de mines touche la case
				for i1 in range (limin,limax+1):
					# On fais varier i1 de la borne inf à la borne sup
					for j1 in range (comin,comax+1):            
						# On fais varier j1 de la borne inf à la borne sup
						if self.etat[i1][j1]!=self.etat[i][j]:
							# Si la case traitée est différente de la case centrale
							if self.etat[i1][j1]==1:                
								# Et Si la case traitée est minée
								# Alors le compteur de mine est incrementé de 1
								nbm=nbm+1                               
				# Quand on a traité les 8 cases adjacentes, on met la valeur du compteur dans le tableau le nombre de mine qui touche la case
				self.code[i][j]= nbm
			else:
				# Sinon celà veut donc dire que la case traiter est miné :  On la code donc en tant que tel
				self.code[i][j]=9
	self.t0=datetime.now()
	print("initGrille : ", self.t0 ,", heure de début du jeu")
