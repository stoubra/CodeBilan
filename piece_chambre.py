from time import perf_counter
from mur import mur 
from personne import personne



class piece:
    def __init__(self,nomPiece,Glongeur,Plongeur,hauteur = 0.0,prixmur = 0.0, prixplafon = 0.0) :
        self.d_nomPiece = nomPiece
        self.d_Gmur = mur(Glongeur,hauteur)
        self.d_Pmur = mur(Plongeur,hauteur)
        self.d_prixmur = prixmur
        self.d_prixplafon = prixplafon
        self.d_descriptionP = " "
        self.d_descriptionM = " "
        

    def surfaceMur(self):
        """Calcul la surface des murs"""
        return (2*self.d_Gmur.d_hauteur*(self.d_Gmur.d_longuer + self.d_Pmur.d_longuer) )

    def surfacePlafon(self):
        """Calcul la surface du plafon"""
        return self.d_Gmur.d_longuer*self.d_Pmur.d_longuer

    def surfacePiece(self):
        """calcul la surface du piece"""
        return self.surfaceMur() + self.surfacePlafon()

    def prixMur(self):
        """Calcul le prix de mur"""
        return (self.surfaceMur()*self.d_prixmur)

    def prixPlafon(self):
        """Calcul le prix du plafon"""
        return self.surfacePlafon()*self.d_prixplafon
    
    def prixPiece(self):
        """calcul le prix du piece"""
        return self.prixMur() + self.prixPlafon()

    def reductionPrixMur(self):
        taux = float(input("taux de reduction mur, 20 pour 20% : "))
        self.d_prixmur *= (1 - taux/100)
        return self.prixMur()
    
    def reductionPrixPlafon(self):
        taux = float(input("taux de reduction Plafon, 20 pour 20% : "))
        self.d_prixplafon *= (1 - taux/100)
        return self.prixMur()

    def sesiePieceDansAppart(self):
        
        nomPiece = str(input("Nom de la piece : "))
        try:
            Glongeur = float(input("Longuer Grand Mur : "))
        except:
            print("Exeption donner un entier")
            Glongeur = float(input("Longuer Grand Mur : "))
        try:
            Plongeur = float(input("Longuer Petit Mur : "))
        except:
            print("Exeption donner un entier")
            Plongeur = float(input("Longuer Petit Mur : "))
        descriptionM = str(input("Desciption du travail à faire pour le mur : \n"))
        try:
            prixmur = float(input("Prix mur : "))
        except:
            print("Exeption donner un entier")
            prixmur = float(input("Prix mur : "))
        descriptionP = str(input("Desciption du travail à faire pour le plafon : \n"))
        try:
            prixplafon = float(input("Prix plafon : "))
        except:
            print("Exeption donner un entier")
            prixplafon = float(input("Prix plafon : "))
            
        self.d_nomPiece = nomPiece
        if(Glongeur < Plongeur):
            self.d_Gmur.d_longuer = Plongeur
            self.d_Pmur.d_longuer = Glongeur
        else:
            self.d_Gmur.d_longuer = Glongeur
            self.d_Pmur.d_longuer = Plongeur
        
        
        self.d_descriptionP = descriptionP
        self.d_descriptionM = descriptionM
        self.d_prixmur = prixmur
        self.d_prixplafon = prixplafon



    def sesiePieceUnique(self):
        nomPiece = str(input("Nom de la piece : "))
        try:
            Glongeur = float(input("Longuer Grand Mur : "))
        except:
            print("Exeption donner un entier")
            Glongeur = float(input("Longuer Grand Mur : "))
        try:
            Plongeur = float(input("Longuer Petit Mur : "))
        except:
            print("Exeption donner un entier")
            Plongeur = float(input("Longuer Petit Mur : "))
        try:
            hauteur = float(input("Hauteur Mur : "))
        except:
            print("Exeption donner un entier")
            hauteur = float(input("Hauteur Mur : "))
        
        descriptionM = str(input("Desciption du travail à faire pour le mur : \n"))
        try:
            prixmur = float(input("Prix mur : "))
        except:
            print("Exeption donner un entier")
            prixmur = float(input("Prix mur : "))
        descriptionP = str(input("Desciption du travail à faire pour le plafon : \n"))
        try:
            prixplafon = float(input("Prix plafon : "))
        except:
            print("Exeption donner un entier")
            prixplafon = float(input("Prix plafon : "))
        
        self.d_nomPiece = nomPiece
        if(Glongeur < Plongeur):
            self.d_Gmur.d_longuer = Plongeur
            self.d_Pmur.d_longuer = Glongeur
        else:
            self.d_Gmur.d_longuer = Glongeur
            self.d_Pmur.d_longuer = Plongeur
        self.d_Gmur.d_hauteur = hauteur
        self.d_descriptionP = descriptionP
        self.d_descriptionM = descriptionM
        self.d_prixmur = prixmur
        self.d_prixplafon = prixplafon
    

    def sesieMur(self):
        nomPiece = str(input("Nom de la piece : "))
        try:
            Glongeur = float(input("Longuer Grand Mur : "))
        except:
            print("Exeption donner un entier")
            Glongeur = float(input("Longuer Grand Mur : "))
        try:
            Plongeur = float(input("Longuer Petit Mur : "))
        except:
            print("Exeption donner un entier")
            Plongeur = float(input("Longuer Petit Mur : "))
        try:
            Hauteur = float(input("Hauteur Mur : "))
        except:
            print("Exeption donner un entier")
            Hauteur = float(input("Hauteur Mur : "))
        description = str(input("desciption du travail à faire : "))
        try:
            prixmur = float(input("Prix mur : "))
        except:
            print("Exeption donner un entier")
            prixmur = float(input("Prix mur : "))
        
        
        self.d_nomPiece = nomPiece
        self.d_Gmur.d_longuer = Glongeur
        self.d_Pmur.d_longuer = Plongeur
        self.d_Gmur.d_hauteur = Hauteur
        self.d_description = description
        self.d_prixmur = prixmur


    def sesiePlafon(self):
        nomPiece = str(input("Nom de la piece : "))
        try:
            Glongeur = float(input("Longuer Grand Mur : "))
        except:
            print("Exeption donner un entier")
            Glongeur = float(input("Longuer Grand Mur : "))
        try:
            Plongeur = float(input("Longuer Petit Mur : "))
        except:
            print("Exeption donner un entier")
            Plongeur = float(input("Longuer Petit Mur : "))
        description = str(input("desciption du travail à faire : "))
        try:
            prixPlafon = float(input("Prix plafon : "))
        except:
            print("Exeption donner un entier")
            prixPlafon = float(input("Prix plafon : "))
        self.d_nomPiece = nomPiece
        self.d_Gmur.d_longuer = Glongeur
        self.d_Pmur.d_longuer = Plongeur
        self.d_description = description
        self.d_prixplafon = prixPlafon

    
    def affichePlafon(self):
        """Affiche plafon seul"""
        print("Nom de la piece : ",self.d_nomPiece)
        print("Longuer Grand Mur : ",self.d_Gmur.d_longuer)
        print("Longuer Petit Mur : ",self.d_Pmur.d_longuer)
        print("Desciption du travail à faire : ",self.d_description)
        print("Surface plafon : ",self.d_nomPiece," ",self.surfacePlafon()," m2")
        print("Prix plafon : ",self.d_nomPiece," ",self.prixPlafon()," Euro")
        
    def fichierPlafon(self,persn):
    
        tabmur = [f"Nom de la piece : {self.d_nomPiece}",f"Longuer Grand Mur : {self.d_Gmur.d_longuer} m",
                    f"Longuer Petit Mur : {self.d_Pmur.d_longuer} m", f"Hauteur Mur : {self.d_Gmur.d_hauteur} m",
                    f"Desciption du travail à faire : {self.d_description}",
                    f"Surface plafon : {self.d_nomPiece} {self.surfacePlafon()} m2",
                    f"Prix plafon : {self.d_nomPiece} {self.prixPlafon()} Euro"]
        
        with open (persn, "a") as f :
            for res in tabmur:
                f.write(res +"\n")
        
    
    
    def fichierMur(self,persn):
    
        tabmur = [f"Nom de la piece : {self.d_nomPiece}",f"Longuer Grand Mur : {self.d_Gmur.d_longuer} m",
                      f"Longuer Petit Mur : {self.d_Pmur.d_longuer} m", f"Hauteur Mur : {self.d_Gmur.d_hauteur} m",
                      f"Desciption du travail à faire : {self.d_description}",
                      f"Surface mur {self.d_nomPiece} {self.surfaceMur()} m2",
                      f"Prix mur {self.d_nomPiece} {self.prixMur()} Euro"]
        
        with open (persn, "a") as f :
            for res in tabmur:
                f.write(res +"\n")


    def afficheMur(self):
        """Affiche mur seul"""
        print("Nom de la piece : ",self.d_nomPiece)
        print("Longuer Grand Mur : ",self.d_Gmur.d_longuer)
        print("Longuer Petit Mur : ",self.d_Pmur.d_longuer)
        print("Hauteur Mur : ",self.d_Gmur.d_hauteur)
        print("Desciption du travail à faire : ",self.d_description)
        print("Surface mur",self.d_nomPiece," ",self.surfaceMur()," m2")
        print("Prix mur",self.d_nomPiece," ",self.prixMur()," Euro")
     

    


    def affichePiece(self):
        """Affiche la piece"""
        print("Nom de la piece : ",self.d_nomPiece)
        print("Longuer Grand Mur : ",self.d_Gmur.d_longuer)
        print("Longuer Petit Mur : ",self.d_Pmur.d_longuer)
        print("Hauteur Mur : ",self.d_Gmur.d_hauteur)
        print("Desciption du travail à faire mur : ",self.d_descriptionM)
        print("Surface mur : ",self.surfaceMur()," m2")
        print("Prix mur : ",self.prixMur()," Euro")
        print("Desciption du travail à faire plafon : ",self.d_descriptionP)
        print("Surface plafon : ",self.surfacePlafon()," m2")
        print("Prix plafon : ",self.prixPlafon()," Euro")
        print("Prix total",self.d_nomPiece," ",self.prixPiece()," Euro")
        
    def fichierPiece(self,persn):
    
        tabmur = [f"Nom de la piece : {self.d_nomPiece}",f"Longuer Grand Mur : {self.d_Gmur.d_longuer} m",
                    f"Longuer Petit Mur : {self.d_Pmur.d_longuer} m", f"Hauteur Mur : {self.d_Gmur.d_hauteur} m",
                    f"Desciption du travail à faire mur : {self.d_descriptionM} ",
                    f"Surface mur {self.d_nomPiece} {self.surfaceMur()} m2",
                    f"Prix mur {self.d_nomPiece} {self.prixMur()} Euro",
                    f"Desciption du travail à faire plafon : {self.d_descriptionP} ",
                    f"Surface plafon : {self.d_nomPiece} {self.surfacePlafon()} m2",
                    f"Prix plafon : {self.d_nomPiece} {self.prixPlafon()} Euro",
                    f"Prix total {self.d_nomPiece} {self.prixPiece()} Euro \n"]
        
        with open (persn, "a") as f :
            for res in tabmur:
                f.write(res +"\n")
                

def menuPiece():
    def menup():
        print("[1] Juste le plafon")
        print("[2] juste les murs")
        print("[3] La piece entier")
        print("[4] affiche piece")
        print("[5] reduction prix plafon")
        print("[6] reduction prix mur")
        print("[7] Quiter")
    menup()
    choix = int(input("Entrer votre choix : "))
    p = piece(None,None,None)
    pr = personne(None,None,None,None,None)
    pr.sesiePresonne()
    t = pr.tabPersone()
    with open (pr.d_nom+" "+pr.d_prenom, "w") as f :
        for res in t:
            f.write(res +"\n")
    while choix != 7 :
        if choix == 1:
            res = 1
            p.sesiePlafon()
        elif choix == 2:
            res = 2
            p.sesieMur()
        elif choix == 3:
            res = 3
            p.sesiePieceUnique()
        elif choix == 4:
            pr.affichePresonne()
                  
            if res == 1:
                p.affichePlafon()
                p.fichierPlafon(pr.d_nom+" "+pr.d_prenom)
            elif res == 2:
                p.afficheMur()
                p.fichierMur(pr.d_nom+" "+pr.d_prenom)
            elif res == 3:
                p.affichePiece()
                p.fichierPiece(pr.d_nom+" "+pr.d_prenom)
        elif choix == 5:
            p.reductionPrixPlafon() 
        elif choix == 6:
            p.reductionPrixMur()
        elif choix == 7:
            break
        else:
            print("Erreur donner un otre nombre entre 1 et 7")
        
        print()
        menup()
        choix = int(input("Entrer votre choix : "))
#menuPiece()