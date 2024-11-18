def addition():
    a = int(input("Premier nombre : "))
    b = int(input("Second nombre : "))
    return a + b

def soustraction():
    a = int(input("Premier nombre : "))
    b = int(input("Second nombre : "))
    return a - b

def multiplication():
    a = int(input("Premier nombre : "))
    b = int(input("Second nombre : "))
    return a * b

def division():
    a = int(input("Premier nombre : "))
    b = int(input("Second nombre : "))
    if b != 0:
        return a / b
    else:
        print("Erreur : Division par zéro")
        return None

def choisir_operation():
    print("\nChoisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    choix = input("Votre choix : ")
    return choix

def calculatrice():
    while True:
        choix = choisir_operation()
        if choix == "1":
            resultat = addition()
            print("Résultat :", resultat)
        elif choix == "2":
            resultat = soustraction()
            print("Résultat :", resultat)
        elif choix == "3":
            resultat = multiplication()
            print("Résultat :", resultat)
        elif choix == "4":
            resultat = division()
            if resultat is not None:
                print("Résultat :", resultat)
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Exécution du programme
calculatrice()
