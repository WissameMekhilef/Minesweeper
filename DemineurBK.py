from tkinter import *
from random import *
import pickle
import platform
#import Winsound
#
class MenuBar(Frame):
    """Barre de menus déroulants"""
    def __init__(self, boss =None):
        Frame.__init__(self, borderwidth =2, relief =GROOVE)
        ##### Menu <Fichier> #####
        fileMenu = Menubutton(self, text ='Fichier')
        fileMenu.pack(side =LEFT, padx =5)
        me1 = Menu(fileMenu)
        me1.add_command(label ='Options', underline =0,command = boss.options)
        me1.add_command(label ='Restart', underline =0,command = boss.reset)
        me1.add_command(label ='Terminer', underline =0,command = boss.quit)
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


class Jeu(Frame):
    """Jeu de jeu (grille de n x m cases)"""
# _____________________________________________________________
    def __init__(self, boss =None):
        # Ce Jeu de jeu est constitué d'un cadre redimensionnable
        # contenant lui-même un canevas. A chaque redimensionnement du
        # cadre, on calcule la plus grande taille possible pour les
        # cases (carrées) de la grille, et on adapte les dimensions du
        # canevas en conséquence.
        Frame.__init__(self)
        
        self.nlig, self.ncol = 10, 10
        # Grille initiale = 10 x 10
        # Liaison de l'événement <resize> à un gestionnaire approprié :
        self.bind("<Configure>", self.redim)
        # Canevas :
        self.can =Canvas(self, bg ="white", borderwidth =0,highlightthickness =1, highlightbackground ="white")
        # Liaison de l'événement <clic de souris> à son gestionnaire :
        self.can.bind("<Button-1>", self.clicGauche)
        self.can.bind("<Button-3>",self.clicDroit)
        self.can.pack()
        # Initialistaion de la probabilité de base
        self.pmines = 0.2
        # Initialisation d'une variable gardant le nombres de mines
        self.nmines = 0
        # Dimensionnement des tableaux aux valeurs max
        self.code =[]
        for i in range(30):           
            self.code.append([0]*30)   
        self.etat =[]
        for i in range(30):           
            self.etat.append([0]*30)
        self.NbCasesaLiberer=0
        # Variable prennant en compte le mode de vue
        # Programmeur ou Joueur
        self.mode=1
        #
        self.gagnant=""
        
# _____________________________________________________________
    def redim(self, event):
        "Opérations effectuées à chaque redimensionnement"
        # Les propriétés associées à l'événement de reconfiguration
        # contiennent les nouvelles dimensions du cadre :
        self.width, self.height = event.width -4, event.height -4
        # La différence de 4 pixels sert à compenser l'épaisseur
        # de la 'highlightbordure" entourant le canevas
##        self.initGrille()
        self.traceMaGrille()

# _____________________________________________________________
    def initGrille(self):        
        # Remplir les cases avec ou sans une mine (le tout est visualisé)
        # etat=0 absence de mines -> vert
        # etat=1 mine -> rouge,
        # etat=2 case libérée par un clic -> bleu
        # etat=3 case entourée de mines -> jaune
        # etat=4 case minée et sur laquelle on a cliqué -> noir0
        # etat=5 case libérée par l'algorithme -> cyan
        # etat=6 case avec drapeau

        # remise a zero du compteur de mines
        self.nmines=0
        # Creation d'un tableau gardant le codage
        self.etat=[]
        for i in range(30):
            # On met 0 dans chacune des cases
            self.etat.append([0]*30)
            
        # On remplis ici le tableau de mines
        # On recupere self.nlig qui est le nombre de ligne
        for n in range(self.nlig):
            # et self.ncol, le nombres de colonne
            for m in range(self.ncol):
                difficulte=self.pmines
                p=random()
                #print(p)
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
        ########################################### CODAGE DES CASES DE LA GRILLE ###########################################
        ## Pour chaque grille proposée au joueur on va coder chacune des cases de la grille pour permettre un "éclatement"
        ## plus simple et une recupération d'un grille aussi plus simple
        # Création d'un tableau pour enregistrer le codage
        self.code =[]
        for i in range(30):           
            self.code.append([0]*30)       
            
        # PARCOURS DE LA GRILLE POUR CODER LES CASES
        ### code=9 la case est minée
        ### code=0 la case n'a aucun voisin miné
        ### code=1,2,3,4,5,6,7,8 indique le nombre de mines qui touchent la case
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
                          
# _____________________________________________________________
    def traceMaGrille(self):
        "Dessin de la grille, en fonction des options & dimensions"
        # largeur et hauteur maximales possibles pour les cases :
        lmax = self.width/self.ncol
        hmax = self.height/self.nlig
        # Le coté d'une case sera égal à la plus petite de ces dimensions :
        self.cote = min(lmax, hmax)
        # -> établissement de nouvelles dimensions pour le canevas :
        larg, haut = self.cote*self.ncol, self.cote*self.nlig
        self.can.configure(width =larg, height =haut)
        # Tracé de la grille :Jeu de Démineur
        self.can.delete(ALL)    # Effacement dessins antérieurs
        s =self.cote
        for l in range(self.nlig):   # lignes horizontales
            self.can.create_line(0, s, larg, s, fill="grey")
            s +=self.cote
        s =self.cote
        for c in range(self.ncol):   # lignes verticales
            self.can.create_line(s, 0, s, haut, fill ="grey")
            s +=self.cote
        #Dessign des ronds
        #print(self.nlig,self.ncol)
        for n in range(self.nlig):
            for m in range(self.ncol):
                x1 = m *self.cote +5        #  
                x2 = (m +1)*self.cote -5    # 
                y1 = n *self.cote +5        #
                y2 = (n +1)*self.cote -5    #
                if (self.etat[n][m]!=3) & (self.etat[n][m]!=6):
                    if self.mode==0:
                        # Mettre cette ligne pour pouvoir voir les mines
                        coul=["green","red","blue","yellow","black","cyan","purple"][self.etat[n][m]]
                    else :
                        # Mettre cette ligne pour pouvoir masquer les mines
                        coul =["white","white","blue","yellow","black","cyan","purple"][self.etat[n][m]]
                    self.can.create_oval(x1, y1, x2, y2, outline ="white",width =1, fill =coul)
                elif self.etat[n][m]==3:
                    coul =["white","blue","red","green","orange","purple","brown","black","magenta"][self.code[n][m]]
                    self.can.create_text(x1+self.cote/2, y1+self.cote/2, font="Purisa",fill = coul, text=self.code[n][m])
                elif self.etat[n][m]==6:
                    d=7
                    e=2*d
                    points = [x1+d,y1+self.cote-e,x1+d+(self.cote-e)/4,y1+d,x1+d+2*(self.cote-e)/3,y1+d,x1+self.cote-e,y1+d+(2*d),x1+self.cote-e,y1+d+(2*d)+self.cote/3,x1+d+2*(self.cote-e)/3,y1+d+self.cote/3,x1+3.225*d,y1+d+self.cote/3]
                    self.can.create_polygon(points, outline='black', fill='purple', width=2)    
            
# _____________________________________________________________
    def liberer(self,li,co):
        # Cette fonction est appelée seulement pour liberer les cases
        # adjacentes dans le cas d'un espace
        limin=max(0,li-1)
        limax=min(self.nlig-1,li+1)
        comin=max(0,co-1)
        comax=min(self.ncol-1,co+1)
        self.etat[li][co]=2
        #print(li,co,self.etat[li][co],sep="|")
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
        

# _____________________________________________________________
    def clicGauche(self, event):
        "Gestion du clic de souris"
        # On commence par déterminer la ligne et la colonne :
        lig, col = int(event.y/self.cote), int(event.x/self.cote)
        # On vérifie que l'on ne clique pas sur une case minée
        if self.code[lig][col]==9:              # SI on clique sur une case minée
            for m in range(0,self.ncol):
                for n in range(0,self.nlig):
                    self.etat[n][m]=4           # ALORS le jeu est perdu = noircie toutes les cases
        elif self.code[lig][col]==0:            # SINON SI on clique sur un espace (case libre de voisin minée)
            self.etat[lig][col]=2               # ALORS on libére la case et on appel la fonction libérer
            self.liberer(lig,col)
        else :                                  # SINON la case a un ou des voisins minée
            self.etat[lig][col]=3               # ALORS on jaunie la case
        self.gagne()
        self.traceMaGrille()

# _____________________________________________________________
    def clicDroit(self,event):
        "Gestion du clic gauche de la souris"
        # On commence par determiner la ligne et la colonne :
        lig, col = int(event.y/self.cote), int(event.x/self.cote)
        #On change l'etat de la case en case avec drapeau
        #On verifie que la case est soit libre soit miné 
        if (self.etat[lig][col]==0) | (self.etat[lig][col]==1):
            self.etat[lig][col]=6
        
        self.gagne()
        self.traceMaGrille()
        
# _____________________________________________________________
    def gagne(self):
        compteurp=0
        NbLibres=0
        for n in range(self.nlig):
            for m in range(self.ncol):
                if self.etat[n][m]==4:
                    compteurp=compteurp+1
                    #print("gagne : compteurp =",compteurp)
                if ( (self.etat[n][m]==2) | (self.etat[n][m]==3) | (self.etat[n][m]==5)):
                    NbLibres=NbLibres+1
        print("gagne : Nombre de cases restantes à libérer: ",self.NbCasesaLiberer-NbLibres,NbLibres)
        if(NbLibres==self.NbCasesaLiberer):
            self.saisirNom()
            print("gagne : tu as gagné")
        elif compteurp==self.NbCasesaLiberer+self.nmines:
            print("gagne : tu as perdu")
# _____________________________________________________________
    def traceGrille(self):
        self.initGrille()
        self.traceMaGrille()

# _____________________________________________________________
    def saisirNom(self):
        self.gagnant=entr1.get()                         #affecte la saisie à la variable gagnant
        fen1.destroy()

        fen1 = Tk()                                     #crée une fenetre graphique
        fen1.title('Vous entrez dans le top 10')        #donne un nom à la fenetre
        txt1 = Label(fen1, text = 'Entrez votre nom :') #crée un texte dans la fenetre
        entr1 = Entry(fen1)                             #crée une zone dans laquelle l'utilisateur pourra saisir un nom
        txt1.grid(row=0,)                               #place la zone de texte
        entr1.grid(row=0,column=1)                      #place la zone de saisie
        entr1.bind("<Return>",saisir_nom)               #relie la commande "Entrer" à la fonction "saisir_nom"


        fen1.mainloop()                                 #lance la boucle d'attente d'événement    
        obFichier = open('noms des joueurs','a')
        obFichier.write(self.gagnant)
        obFichier.write('\n')
        obFichier.close()
        of = open('noms des joueurs','r')
        t = of.read()
        print(t)


# _____________________________________________________________
class affichage(Jeu):
#    def __init__(self, parent):
    def __init__(self, boss =None):
#        Frame.__init__(self, parent)   
        Frame.__init__(self)   
         
#        self.parent = parent        
        self.initUI()
        
    def initUI(self):
        self.pack()

        canvas = Canvas(self)


        canvas.create_text(0,20, anchor=W, font="Purisa",
            text="Le jeu tourne actuellement sous :")
        canvas.create_text(0,60, anchor=W, font="Purisa",
            text="Nombre de case a liberer")
##        canvas.create_text(0,60, anchor=W, font="Purisa",
##            text=jeu.NbCasesaLiberer)
        print("Affichage: ",boss.NbCasesaLiberer)
        canvas.create_text(0,100, anchor=W, font="Purisa",
            text="Nombre de mines restante(s)")
        canvas.pack(fill=BOTH, expand=1) 
    
class Demineur(Frame):
    """corps principal du programme"""
# _____________________________________________________________
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("900x600")
        self.master.title(" Jeu de Demineur")
        
        self.mbar = MenuBar(self)
        self.mbar.pack(side =TOP, expand =NO, fill =X)
        
        self.jeu =Jeu(self)
        self.jeu.pack(side= LEFT, expand =YES, fill=BOTH,)

        self.affichage = affichage(self)
        self.affichage.pack(side=RIGHT, expand = NO, fill=BOTH)
        
        self.pack()

        # Ici on va determiner sur quelle systeme le jeu tourne
        global operatingSystem
        # On initialise une variable qui va enregistrer le nom du systeme
        operatingSystem = 'none'
        # On attribut a cette variable le nom du system grace a la librairie
        # platform
        operatingSystem = platform.system()
        print('Demineur : Le jeu tourne actuellement sous :',operatingSystem)
            
# _____________________________________________________________
    def options(self):
        "Choix du nombre de lignes et de colonnes pour la grille"
        opt =Toplevel(self)
        curL =Scale(opt, length =200, label ="Nombre de lignes :",
            orient =HORIZONTAL,from_ =1, to =30, command =self.majLignes)
        curL.set(self.jeu.nlig) # position initiale du curseur
        curL.pack()
        curH =Scale(opt, length =200, label ="Nombre de colonnes :",
            orient =HORIZONTAL,from_ =1, to =30, command =self.majColonnes)
        curH.set(self.jeu.ncol) # position initiale du curseur
        curH.pack()
        curM =Scale(opt, length =200, label ="Probabilitee de mines :",
            orient =HORIZONTAL,from_ =1, to =9, command =self.pmines)
        curM.set(self.jeu.pmines) # position initiale du curseur
        curM.pack()

# _____________________________________________________________
    def pmines(self,n):
        self.jeu.pmines = (int (n))/10
        print("pmines: pmines= ",self.jeu.pmines)
        self.jeu.traceGrille()

# _____________________________________________________________
    def majColonnes(self, n):
        self.jeu.ncol = int(n)
        self.jeu.traceGrille()

# _____________________________________________________________
    def majLignes(self, n):
        self.jeu.nlig = int(n)
        self.jeu.traceGrille()

# _____________________________________________________________
    def reset(self):
        self.jeu.traceGrille()

# _____________________________________________________________
    def principe(self):
        "Fenetre-message contenant la description sommaire du principe du jeu"
        msg =Toplevel(self)
        Message(msg, bg ="navy", fg ="ivory", width =400,
            font ="Helvetica 10 bold",
            text ="").pack(padx =10, pady =10)

# _____________________________________________________________
    def aPropos(self):
        "Fenetre-message indiquant l'auteur et le type de licence"
        msg =Toplevel(self)
        Message(msg, width =200, aspect =100, justify =CENTER,
            text ="Jeu de Demineur\n\n(C) MEKHILEF Wissame, Fevrier 2013.\n").pack(padx =10, pady =10)

# _____________________________________________________________
    def couleur(self):
        msg =Toplevel(self)
        curM =Scale(msg, length =250, label ="Choisir developpeur ou joueur",
            orient =HORIZONTAL,from_ =0, to =1, command =self.mode)
        curM.set(self.jeu.mode) # position initiale du curseur
        curM.pack()

# _____________________________________________________________
    def mode(self,n):
        self.jeu.mode = int(n)
        self.jeu.traceMaGrille()        

# _____________________________________________________________
    def fond(self):
        msg =Toplevel(self)
        Message(msg, width =200, aspect =100, justify =CENTER,
            text ="Choisir la couleur du fond du jeux\n").pack(padx =10, pady =10)

# _____________________________________________________________
    def sauver(self):
        f=open('./etat', 'wb')
        pickle.dump(self.jeu.etat, f)
        f.close()

        g=open('./code', 'wb')
        pickle.dump(self.jeu.code, g)
        g.close()

# _____________________________________________________________
    def ouvrir(self):
        f=open('./etat', 'rb')
        self.jeu.etat = pickle.load(f)
        f.close()
        
        g=open('./code', 'rb')
        self.jeu.code = pickle.load(g)
        g.close()
        
        self.jeu.traceMaGrille()

# _____________________________________________________________
# _____________________________________________________________
# _____________________________________________________________

if __name__ == '__main__':
    Demineur().mainloop()
