def addition():
    a = int(input ("Premier nombre :"))
    b = int(input ("Second nombre :"))
    print("Le résultat de cette addition:")
    print(a,"+",b,"=",a+b)

def soustraction():
    a = int(input("Premier nombre : "))
    b = int(input("Second nombre : "))
    print("Le résultat de cette soustraction:")
    print(a,"-",b,"=",a-b)

def multiplication():
    a = int(input("Premier nombre : "))
    b = int(input("Second nombre : "))
    print("Le résultat de cette multiplication:")
    print(a,"X",b,"=",a*b)
    

def division():
    a = int(input("Premier nombre : "))
    b = int(input("Second nombre : "))
    print("Le résultat de cette division:")
    print(a,"/",b,"=",round(a/b,2))

def choisir_operation():
    global choix
    print("\nChoisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    choix = input("Votre choix 1-2-3-4-5 : ")
    

def calculatrice():
    while True:
        choisir_operation()
        if choix == "1":
            addition() 
        elif choix == "2":
            soustraction()
        elif choix == "3":
            multiplication()
        elif choix == "4":
            division()
        elif choix == "5":
            print("Salut !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Exécution du programme
calculatrice()
