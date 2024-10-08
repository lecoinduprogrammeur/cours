from cartes_a_jouer import Cartes
from tkinter import *


class Jeu(object):

    def __init__(self):
        # objet classe et paquets de cartes
        self.cartes_objet=Cartes()
        self.cartes_objet.paquet_cartes()
        self.cartes_objet.melange_cartes()
        self.cartes_objet.distribution_cartes()
      
        # INTERFACE fenêtre principlale tkinter
        self.fenetre = Tk()
        self.fenetre.title("Bataille 6TT")
        self.fenetre.config(bg ='black', padx = 5, pady = 5)

    # METHODE JEU DEPART
    def jeu_depart (self):
        # cartes départ
        self.dos_carte_joueur = PhotoImage(file = "./cartes/1_dos_carte.png")
        self.dos_carte_ordinateur = PhotoImage(file = "./cartes/1_dos_carte.png")
        self.depart_carte_joueur = PhotoImage(file = "./cartes/1_depart_carte.png")
        self.depart_carte_ordinateur = PhotoImage(file = "./cartes/1_depart_carte.png")
        # fenetre dessus Frame
        self.fenetre_dessus = Frame(self.fenetre,borderwidth=2,relief=FLAT, bg="black")
        self.fenetre_dessus.pack(side=TOP,padx=5,pady=5)
        # fenetre dessus contenu
        self.paquet_joueur = Label (self.fenetre_dessus,bg="black",image=self.dos_carte_joueur)
        self.paquet_joueur.pack (side=LEFT, padx = 5, pady = 5)
        self.carte_joueur = Label (self.fenetre_dessus,bg="black",image=self.depart_carte_joueur)
        self.carte_joueur.pack (side=LEFT, padx = 10, pady = 5)
        self.carte_ordinateur = Label (self.fenetre_dessus,bg="black",image=self.depart_carte_ordinateur)
        self.carte_ordinateur.pack (side=LEFT, padx = 10, pady = 5)
        self.paquet_ordinateur = Label (self.fenetre_dessus,bg="black",image=self.dos_carte_ordinateur)
        self.paquet_ordinateur.pack (side=LEFT, padx = 5, pady = 5)
        # fenetre milieu Frame
        self.fenetre_milieu = Frame(self.fenetre,borderwidth=2,relief=GROOVE,bg="black")
        self.fenetre_milieu.pack(side=TOP,padx=30,pady=5)
        # fenetre milieu Frame -> Frame gauche
        self.fenetre_milieu_gauche = Frame(self.fenetre_milieu,borderwidth=2,relief=GROOVE,bg="white")
        self.fenetre_milieu_gauche.pack(side=LEFT,padx=5,pady=5)
        self.texte1b = Label(self.fenetre_milieu_gauche, text=str(len (self.cartes_objet.paquet_j1))+ " cartes à jouer" + "\n" +"NBRE"+ " cartes gagnées",fg = 'black',bg = 'white', font=('times', 15, 'bold'))
        self.texte1b.pack (side=LEFT, padx=60, pady=10)
        # fenetre milieu Frame -> Frame milieu
        self.fenetre_milieu_milieu = Frame(self.fenetre_milieu,borderwidth=2,relief=GROOVE,bg="white")
        self.fenetre_milieu_milieu.pack(side=LEFT,padx=5,pady=5)
        self.texte1a = Label(self.fenetre_milieu_milieu, text="POINTS : 000\nTOTAL : 000",fg = 'black',bg = 'white', font=('times', 15, 'bold'))
        self.texte1a.pack (side=LEFT, padx=40, pady=10)
        self.texte2a = Label(self.fenetre_milieu_milieu, text="POINTS : 000\nTOTAL : 000",fg = 'black',bg = 'white', font=('times', 15, 'bold'))
        self.texte2a.pack (side=LEFT, padx=40, pady=10)
        # fenetre milieu Frame -> Frame droite
        self.fenetre_milieu_droite = Frame(self.fenetre_milieu,borderwidth=2,relief=GROOVE,bg="white")
        self.fenetre_milieu_droite.pack(side=LEFT,padx=5,pady=5)
        self.texte2b = Label(self.fenetre_milieu_droite, text=str(len (self.cartes_objet.paquet_j2))+ " cartes à jouer" + "\n" +"NBRE"+ " cartes gagnées",fg = 'black',bg = 'white', font=('times', 15, 'bold'))
        self.texte2b.pack (side=LEFT, padx=60, pady=10)
        # fenetre dessous Frame
        self.fenetre_dessous = Frame(self.fenetre,borderwidth=2,relief=GROOVE,bg="white")
        self.fenetre_dessous.pack(side=BOTTOM,padx=5,pady=5)
        # fenetre dessous contenu
        self.texte1 = Label(self.fenetre_dessous, text="JOUEUR          ",fg = 'black',bg = 'white', font=('times', 20, 'bold'))
        self.texte1.pack (side=LEFT, padx=100, pady=10)
        self.bouton_jouer = Button(self.fenetre_dessous,text='jouer',command=None)# self.jeu_cartes_bataille
        self.bouton_jouer.pack(side=LEFT,padx=20,pady=10)
        self.bouton_rejouer = Button(self.fenetre_dessous,text='rejouer',command=None) # self.rejouer
        self.bouton_rejouer.pack(side=LEFT,padx=20,pady=10)
        self.bouton_destroy = Button(self.fenetre_dessous,text='quitter',command=None) # self.fenetre.destroy
        self.bouton_destroy.pack(side=LEFT,padx=20,pady=10)
        self.texte2 = Label(self.fenetre_dessous, text="          ORDINATEUR",fg = 'black',bg = 'white', font=('times', 20, 'bold'))
        self.texte2.pack (side=RIGHT, padx=60, pady=10)

if __name__ =='__main__':
    jeu_objet = Jeu()
    jeu_objet.jeu_depart()
    jeu_objet.fenetre.mainloop()

        
