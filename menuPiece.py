from piece_chambre import *
from tkinter import *
p = piece(None, None,None)
def sesie():   
    p.sesiePieceUnique()
def affiche():
    p.affichePiece()

MenuPiece = Tk()
MenuPiece.title("Piece")
MenuPiece.minsize(850,550) 
menuPrincipale = Menu(MenuPiece)
menupiece = Menu(menuPrincipale,tearoff=0)
menuPrincipale.add_cascade(label="Menu Piece",menu=menupiece) 
menupiece.add_command(label="La piece entier",command= sesie)
menupiece.add_command(label="affiche piece",command= affiche)
menupiece.add_command(label="reduction prix plafon")
menupiece.add_command(label="reduction prix mur")
#menupiece.add_command(label="Quitter",command=quit) 
MenuPiece.config(menu=menuPrincipale)
MenuPiece.mainloop()
