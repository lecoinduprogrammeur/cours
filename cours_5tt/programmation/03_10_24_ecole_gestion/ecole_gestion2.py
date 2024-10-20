classe6 = []
classe5 = []
classe4 = []
eleve = []
codes_postaux = [1070,1160,1082,1000,1040,1140,1190,1083,1050,1090,1081,1080,1060,1210,1030,1180,1170,1200,1150]
liste_age = [15,16,17]

reponse = "o"
#reponse = input("Voulez-vous inscrire un élève ? o ou autre touche ")

while reponse.lower() == "o":
    eleve = []  # Réinitialiser l'élève à chaque itératio ou tour de boucle

    # Nom de famille et prénom
    nom_famille = input("Quel est ton nom de famille ? ").capitalize()
    eleve.append(nom_famille)
    
    prenom = input("Quel est ton prénom ? ").capitalize()
    eleve.append(prenom)

    # Choix de la commune avec validation
    while True:
        print("\nVeuillez choisir votre commune :")
        for i, code in enumerate(codes_postaux, start=1):
            print(f"{i}. {code}")
        
        try:
            choix_commune = int(input("Choisissez un numéro entre 1 et 19 : "))
            if 1 <= choix_commune <= 19:
                eleve.append(codes_postaux[choix_commune - 1])
                break
            else:
                print("Erreur: Veuillez entrer un nombre entre 1 et 19.")
        except ValueError:
            print("Erreur: Veuillez entrer un nombre valide.")

    # Choix de l'âge avec validation
    while True:
        print("\nVeuillez choisir votre âge :")
        for i, age in enumerate(liste_age, start=1):
            print(f"{i}. {age} ans")
        
        try:
            choix_age = int(input("Choisissez un numéro entre 1 et 3 : "))
            if 1 <= choix_age <= 3:
                eleve.append(liste_age[choix_age - 1])
                break
            else:
                print("Erreur: Veuillez entrer un nombre entre 1 et 3.")
        except ValueError:
            print("Erreur: Veuillez entrer un nombre valide.")

    # Attribution des élèves dans la classe correspondante
    if eleve[3] == 17:
        classe6.append(eleve)
    elif eleve[3] == 16:
        classe5.append(eleve)
    elif eleve[3] == 15:
        classe4.append(eleve)
    else:
        print("Nous ne pouvons vous inscrire dans aucune de nos classes.")

    # Nouvelle inscription
    reponse = input("Encore un élève à inscrire ? (o pour continuer, autre pour arrêter) ").lower()
    while reponse not in ["o","n"]:
        reponse = input("Veuillez entrer seulement 'o' pour continuer ou 'n' pour arrêter : ").lower()
    else:
        if reponse == "o":
            continue
        elif reponse == "n":
            break



print("CLASSE DES 4EMES")
for item in classe4:
    print(item[0],item[1],item[2],item[3])
    
print("CLASSE DES 5EMES")
for item in classe5:
    print(item[0],item[1],item[2],item[3])

print("CLASSE DES 6EMES")
for item in classe6:
    print(item[0],item[1],item[2],item[3])
