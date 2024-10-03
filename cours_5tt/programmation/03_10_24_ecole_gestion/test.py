reponse = "o"
reponse = input("Veux-tu ajouter un nombre ?")
liste = []
while reponse == "o":
    nombre = int(input("Nombre : "))
    liste.append(nombre)
    reponse = input("Veux-tu encore ajouter un nombre ?")

