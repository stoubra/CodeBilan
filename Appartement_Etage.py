from piece_chambre import piece
from personne import personne
class appartement:
    def __init__(self,nbrpiece):
        self.d_nombrePiece = nbrpiece
        self.d_piece = []

    def pieces(self,i):
        """Envoi la piece du rang i"""
        return self.d_piece[i]
    
    def suprimePiece(self):
        """supirime la piece i"""
        i = int(input("Numero de la piece à supprimer : "))
        del self.d_piece[i - 1]
        self.d_nombrePiece -= 1
    
    def ajoutPiece(self):
        """Ajouter une piece """
        p = piece(None,None,None)
        self.d_nombrePiece+=1
        p.sesiePieceUnique()
        self.d_piece.append(p)

    def surfaceAppart(self):
        """Calcule la surface de l'appartement"""
        res  = 0
        for pieces in self.d_piece :
            res += pieces.surfacePiece()
        return res

    def prixAppart(self):
        """Calcule le prix de l'appartement"""
        res = 0
        for pieces in self.d_piece : 
            res += pieces.prixPiece()
        return res
    

    def sesieAppart(self):
        """sesir un appartement dont la hauteur des pieces est modifier"""
        try:
            nbpiece = int(input("nombre de piece : "))
        except:
            print("Exeption donner un entier ")
            nbpiece = int(input("nombre de piece : "))
        
        self.d_nombrePiece = nbpiece 
        try:
            hauteur = float(input("Hauteur de l'appartement : "))
        except:
            print("Exception donner un entier")
            hauteur = float(input("Hauteur de l'appartement : "))
        
        for i in range(self.d_nombrePiece):
            d = piece(None,None,None)
            d.d_Gmur.d_hauteur = hauteur
            d.sesiePieceDansAppart()
            self.d_piece.append(d)
        
        
        
    def afficheAppart(self):
        """affiche un appartement"""
        for i in range(self.d_nombrePiece):
            self.d_piece[i].affichePiece()

        print("Prix Total Appart = ",self.prixAppart()," Euro \n")
        
    def fichieAppart(self,pers):
        for i in range(self.d_nombrePiece):
            self.d_piece[i].fichierPiece(pers)
        with open (pers, "a") as f :
            f.write(f"Prix total appart = {self.prixAppart()} Euro \n")
            


def menuAppartement():
    def menup():
        print("[1] sesie Appartement")
        print("[2] affiche Appartement")
        print("[3] Supprime Piece")
        print("[4] Ajoute Piece")
        print("[5] Quiter")
    menup()
    choix = int(input("Entrer votre choix : "))
    a = appartement(None)
    p = personne(None,None,None,None,None)
    while choix != 5 :
        if choix == 1:
            p.sesiePresonne()
            a.sesieAppart()
            t = p.tabPersone()
            with open (f"{p.d_nom} {p.d_prenom}", "w") as f :
                for res in t:
                    f.write(res +"\n")
        elif choix == 2:
            p.affichePresonne()
            a.afficheAppart()
            a.fichieAppart(f"{p.d_nom} {p.d_prenom}")
        elif choix == 3:
            a.suprimePiece()
        elif choix == 4:
            a.ajoutPiece()
        elif choix == 5:
            break
        else:
            print("Erreur donner un otre nombre entre 1 et 5")
        
        print()
        menup()
        choix = int(input("Entrer votre choix : "))