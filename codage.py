from parametre import *
def codage():
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
        self.t0=time.clock()
