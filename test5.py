class Case(object):
    "Une case de notre super jeu"
    meteo=None
    def AfficheToi(self):
        "Methode d’affichage universelle"
        raise NotImplementedError()

class CaseMer(Case):
    "Case maritime avec un courant et tout"
    courant=None
    # TODO : surcharger AfficheToi()
