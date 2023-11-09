from Appartement_Etage import appartement
from personne import personne
class immeuble:
    def __init__(self,nbrappart) :
        self.d_nombreAppart = nbrappart
        self.d_apptart = []

    def surfaceImmeuble(self):
        res = 0
        for appart in self.d_apptart :
            res += appart.surfaceAppart()
        return res

    def prixImmeuble(self):
        res = 0
        for appartements in self.d_apptart:
            res += appartements.prixAppart()
        return res
    
    def suprimerAppart(self):
        """supirime l'appartement i"""
        i = int(input("Numero de l'appartement à supprimer : "))
        del self.d_apptart[i-1]
        self.d_nombreAppart-=1


    def ajoutAppart(self):
        """Ajoute un appartement"""
        a = appartement(None)
        self.d_nombreAppart+=1
        a.sesieAppart()
        self.d_apptart.append(a)

        
    def sesieImmeuble(self):
        """sesir un Immeuble"""
        try:
            nbrAppart = int(input("Nombre Appartement : "))
        except:
            print("Exeption donner un entier ")
            nbrAppart = int(input("Nombre Appartement : "))
        
        self.d_nombreAppart = nbrAppart
        for i in range(self.d_nombreAppart):
            print("Appartement "+ str(i + 1))
            d = appartement(None)
            d.sesieAppart()
            self.d_apptart.append(d)
            
    def afficheImmeuble(self):
        i = 1
        for appartements in self.d_apptart:
            print("Appartement "+ str(i))
            appartements.afficheAppart()
            i+=1
        print("Prix Total = ",self.prixImmeuble()," Euro")
    
    def fichieImmeuble(self,pers):
        i = 1
        for appartements in self.d_apptart:
            with open (pers, "a") as f :
                f.write(f"Appartement {i} \n")
            appartements.fichieAppart(pers)
            i+=1
        with open (pers, "a") as f :
            f.write(f"Prix total immeuble = {self.prixImmeuble()} Euro \n")




def menuImmeuble():
    def menup():
        print("[1] sesie Immeuble")
        print("[2] affiche Immeuble")
        print("[3] Supprime Appartement i")
        print("[4] Ajoute Appartement")
        print("[5] Quiter")
    menup()
    choix = int(input("Entrer votre choix : "))
    i = immeuble(None)
    p = personne(None,None,None,None,None)
    while choix != 5 :
        if choix == 1:
            p.sesiePresonne()
            i.sesieImmeuble()
            t = p.tabPersone()
            with open (f"{p.d_nom} {p.d_prenom}", "w") as f :
                for res in t:
                    f.write(res + "\n")
        elif choix == 2:
            p.affichePresonne()
            i.afficheImmeuble()
            i.fichieImmeuble(f"{p.d_nom} {p.d_prenom}")
        elif choix == 3:
            i.suprimerAppart()
        elif choix == 4:
            i.ajoutAppart()
        elif choix == 5:
            break
        else:
            print("Erreur donner un otre nombre entre 1 et 5")
        
        print()
        menup()
        choix = int(input("Entrer votre choix : "))
        
        