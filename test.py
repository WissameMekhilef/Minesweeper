def options(selfXYZ):
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
  curM =Scale(opt, length =200, label ="Probabilitée de mines :",
      orient =HORIZONTAL,from_ =1, to =9, command =self.mines)
  curM.set(self.jeu.mines) # position initiale du curseur
  curM.pack()
