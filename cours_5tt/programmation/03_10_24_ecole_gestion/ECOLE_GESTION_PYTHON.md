# ECOLE GESTION PYTHON

## Le code de départ

```python
classe6 = []
classe5 = []
classe4 = []
eleve = []
codes_postaux = [1070,1160,1082,1000,1040,1140,1190,1083,1050,1090,1081,1080,1060,1210,1030,1180,1170,1200,1150]
liste_age = [15,16,17]

reponse = "o"
reponse = input("Voulez-vous inscrire un élève ? o ou autre touche ")

while reponse == "o":
    

    question1 = input("Quel est ton nom de famille ? ").capitalize()
    eleve.append(question1)
    
    question2 = input("Quel est ton prénom ? ").capitalize()
    eleve.append(question2)
    
    compteur = 1
    for code in codes_postaux:
        print(compteur,code)
        compteur = compteur + 1
    question3 = int(input("Quelle est ta commune ? Choisissez 1 à 19 : "))
    eleve.append(codes_postaux[question3-1])
    
    compteur2 = 1
    for age in liste_age:
        print(compteur2,age)
        compteur2 = compteur2 + 1
    question4 = int(input("Quel est ton âge ? Choisissez 1 à 3 "))
    eleve.append(liste_age[question4-1])
    
    if eleve[3] == 17:
        classe6.append(eleve)
    elif eleve[3] == 16:
        classe5.append(eleve)
    elif eleve[3] == 15:
        classe4.append(eleve)
    else:
        print("Nous ne pouvons vous inscrire dans aucune de nos classes.")
    
    eleve = []
    reponse = input("Encore un élève à inscrire ? ")

print(classe4,classe5,classe6)

print("CLASSE DES 4EMES")
for item in classe4:
    print(item[0],item[1],item[2],item[3])
    
print("CLASSE DES 5EMES")
for item in classe5:
    print(item[0],item[1],item[2],item[3])

print("CLASSE DES 6EMES")
for item in classe6:
    print(item[0],item[1],item[2],item[3])
```

Nous avons mis un compteur à chaque question où s'imposait un choix entre plusieurs réponses possibles.

Pour les codes postaux et pour les âges

Il existe une autre façon d'envisager cela ! Avec la fonction enumerate () 

```python
liste_age = [15,16,17]
compteur = 1
for age in liste_age:
    print(compteur, age)
    compteur = compteur + 1


1 15
2 16
3 17
liste_age = [15,16,17]
for index,age in enumerate(liste_age):
    print(index, age)


0 15
1 16
2 17
liste_age = [15,16,17]
for index,age in enumerate(liste_age, start=1):
    print(index, age)


1 15
2 16
3 17
```



## Le code optimisé 

- fonction enumerate( )
- try et except -> gestion des erreurs

```python
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
    

print("CLASSE DES 4EMES")
for item in classe4:
    print(item[0],item[1],item[2],item[3])
    
print("CLASSE DES 5EMES")
for item in classe5:
    print(item[0],item[1],item[2],item[3])

print("CLASSE DES 6EMES")
for item in classe6:
    print(item[0],item[1],item[2],item[3])
```

