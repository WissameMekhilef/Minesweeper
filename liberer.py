#!/usr/bin/env python
# coding: utf-8

from parametre import *
def liberer(self,li,co):
	# Cette fonction est appelée seulement pour liberer les cases
	# adjacentes dans le cas d'un espace
	limin=max(0,li-1)
	limax=min(self.nlig-1,li+1)
	comin=max(0,co-1)
	comax=min(self.ncol-1,co+1)
	self.etat[li][co]=2
	for i in range(limin,limax+1):
		for j in range(comin,comax+1):
			if (i!=li)|(j!=co):
				if (self.code[i][j]!=0) & (self.code[i][j]!=9):
					self.etat[i][j]=3
				elif (self.code[i][j]==0) & (self.etat[i][j]!=2):
					self.etat[i][j]=5
	self.traceMaGrille()


	for i in range(limin,limax+1):
		for j in range(comin,comax+1):
			if ((i!=li)|(j!=co))&(self.etat[i][j]==5)&(self.etat[i][j]!=2):
				self.etat[i][j]=2
				self.liberer(i,j)
	self.traceMaGrille()
