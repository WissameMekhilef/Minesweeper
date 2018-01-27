from parametre import *
def ouvrir(self):
	f=open('./etat', 'rb')
	self.jeu.etat = pickle.load(f)
	f.close()
        
	g=open('./code', 'rb')
	self.jeu.code = pickle.load(g)
	g.close()
        
	self.jeu.traceMaGrille()
