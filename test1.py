class Tableau_jeu(object):
    "Definition d'un tableau de jeu"
    largeur = int
    longueur = int
    def Nb_cases(self,largeur,longueur):
        n=largeur*longueur
        print("le nombres de case de la grille vaut : ", n)
        return n

tab = Tableau_jeu()
tab.largeur = 6
tab.longeur = 5
x = tab.Nb_cases(largeur,longueur)
