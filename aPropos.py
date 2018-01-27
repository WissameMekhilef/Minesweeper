from parametre import *
def aPropos(self):
	"Fenetre-message indiquant l'auteur et le type de licence"
	msg =Toplevel(self)
	Message(msg, width =200, aspect =100, justify =CENTER,
	text ="Jeu de Demineur\n\n(C) MEKHILEF Wissame, Fevrier 2013.\n").pack(padx =10, pady =10)
