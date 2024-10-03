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