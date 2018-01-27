from math import sqrt

class Point(object):
    "Définition d'un point géométrique"
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def affiche_point(self,p):
        print("coord. horizontale =", p.x, "coord. verticale =", p.y)
    def distance(self,p1, p2):
        # On applique le théorème de Pythagore :
        dx =abs(p1.x - p2.x)
        # abs() => valeur absolue
        dy =abs(p1.y - p2.y)
        return sqrt(dx*dx + dy*dy)
    
class Rectangle(object):
    "définition d'une classe de rectangles"
    def __init__(self,largeur,longueur,coin):
        self.la = largeur
        self.lo = longueur
        self.coin = Point(coin.x,coin.y)
    def calculSurface(self):
        print ("surface = %.2f m2" %(self.la * self.lo))
    def trouveCentre(self):
        p = Point(x = 0,y =0)
        p.x = self.coin.x + self.la/2.0
        p.y = self.coin.y + self.lo/2.0
        print(p)

