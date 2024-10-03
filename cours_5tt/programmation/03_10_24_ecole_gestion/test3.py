# Vérification initiale pour s'assurer que l'utilisateur entre bien "o" ou "n"
while True:
    reponse = input("Veux-tu ajouter un nombre ? (o pour continuer, n pour arrêter) ").lower()
    if reponse in ["o", "n"]:
        break
    else:
        print("Erreur : veuillez entrer 'o' pour continuer ou 'n' pour arrêter.")

liste = []

while reponse == "o":
    nombre = int(input("Nombre : "))
    liste.append(nombre)
    
    # Boucle pour s'assurer que l'utilisateur entre seulement "o" ou "n" pour continuer
    while True:
        reponse = input("Veux-tu encore ajouter un nombre ? (o pour continuer, n pour arrêter) ").lower()
        if reponse in ["o", "n"]:
            break
        else:
            print("Erreur : veuillez entrer 'o' pour continuer ou 'n' pour arrêter.")

print("Liste des nombres ajoutés :", liste)
