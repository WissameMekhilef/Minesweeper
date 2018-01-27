from parametre import *
def sauver(self):
	f=open('./etat', 'wb')
	pickle.dump(self.jeu.etat, f)
	f.close()

	g=open('./code', 'wb')
	pickle.dump(self.jeu.code, g)
	g.close()
