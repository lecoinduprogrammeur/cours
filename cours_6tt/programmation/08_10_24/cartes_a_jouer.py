import random

class Cartes(object):

    def __init__(self):
        self.paquet_52=[]
        self.valeurs=["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","As"] 
        self.couleurs=["Coeur","Carreau","Pique","Trèfle"]
        
    def paquet_cartes(self):
        for val in self.valeurs :
            for coul in self.couleurs :
                self.paquet_52.append (val + " de " + coul)

    def melange_cartes(self):
        random.shuffle(self.paquet_52)

    def distribution_cartes(self):
        self.paquet_j1 = []
        self.paquet_j2 = []
        self.paquet_j1 = self.paquet_52[0:len(self.paquet_52)//2]
        self.paquet_j2 = self.paquet_52[len(self.paquet_52)//2:]

    def blabla(self):
        pass

if __name__ == "__main__":
    un_objet = Cartes()
    un_objet.paquet_cartes()
    un_objet.melange_cartes()
    un_objet.distribution_cartes()
    print(un_objet.paquet_j1)
    print(un_objet.paquet_j2)
