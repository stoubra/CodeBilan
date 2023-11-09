from piece_chambre import menuPiece
from Appartement_Etage import menuAppartement 
from immeuble_maison import menuImmeuble
def menuBilan():
    def menup():
        print("[1] Chambre (Piece)")
        print("[2] Appartement (Etage)")
        print("[3] Immeuble (Maison)")
        print("[4] Quiter")
    menup()
    choix = int(input("Entrer votre choix : "))
    while choix != 4 :
        if choix == 1:
            menuPiece()
        elif choix == 2:
            menuAppartement()
        elif choix == 3:
            menuImmeuble()
        elif choix == 4:
            break
        else:
            print("Erreur donner un autre nombre entre 1 et 4 inclu")
        
        print()
        menup()
        choix = int(input("Entrer votre choix : "))
    
menuBilan()