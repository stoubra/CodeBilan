
from ExceptionNombre import exceptionInt 
class personne:
    def __init__(self,nom,prenom,adresse,codePostal,Ville) :
        self.d_nom = nom
        self.d_prenom = prenom
        self.d_adresse  = adresse
        self.d_codePostal = codePostal
        self.d_ville = Ville

    def sesiePresonne(self):
        nom = str(input("Nom client : "))
        prenom = str(input("Prenom client : "))
        adresse = str(input("Adresse client : "))
        try:
            code = int(input("Code Postale client : "))
        except:
            print("Exception donner un entier ")
            code = int(input("Code Postale client : "))
        ville = str(input("Ville client : "))
        self.d_nom = nom
        self.d_prenom = prenom
        self.d_adresse  = adresse
        self.d_codePostal = code
        self.d_ville = ville
    
    def affichePresonne(self):
        print(self.d_nom)
        print(self.d_prenom)
        print(self.d_adresse)
        print(self.d_codePostal," ",self.d_ville)
        
    def tabPersone(self):
        tabpr = [f"{self.d_nom}",f"{self.d_prenom}",f"{self.d_adresse}",f"{self.d_codePostal} {self.d_ville} \n"]
        return tabpr
   
    



  
    
    

    
    
         
