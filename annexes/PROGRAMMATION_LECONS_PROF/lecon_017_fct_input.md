# Plan de leçon : La fonction input()

## Informations générales

- Date : À définir
- Classe : Débutants en programmation
- Matière : Informatique - Programmation Python
- Thème : Utilisation de la fonction input()
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation de la fonction input()

- Objectifs disciplinaires :
  - Comprendre le fonctionnement de input()
  - Savoir gérer les entrées utilisateur
  - Maîtriser la conversion des types
  - Gérer les erreurs d'entrée

## Déroulement de la leçon

### 1. Bases de input() (15 min)

#### A. Syntaxe de base
```python
# Entrée simple
nom = input("Entrez votre nom : ")
print(f"Bonjour {nom}!")

# Sans message
reponse = input()  # Attend une entrée utilisateur

# Le retour est toujours une chaîne
entree = input("Tapez quelque chose : ")
print(type(entree))  # <class 'str'>
```

#### B. Messages d'invite
```python
# Messages simples
age = input("Quel est votre âge ? ")

# Messages sur plusieurs lignes
description = input("""
Décrivez-vous en quelques mots
(appuyez sur Entrée quand vous avez terminé) :
""")

# Messages formatés
nom = "utilisateur"
question = input(f"Bonjour {nom}, comment allez-vous ? ")
```

### 2. Conversion des types (20 min)

#### A. Conversion numérique
```python
# Conversion en entier
age_str = input("Âge : ")
age = int(age_str)  # Conversion en entier

# Conversion en float
taille = float(input("Taille en mètres : "))

# Méthode combinée
prix = float(input("Prix : "))
```

#### B. Validation et conversion sécurisée
```python
# Vérification que l'entrée est un nombre
def lire_nombre():
    while True:
        try:
            return float(input("Entrez un nombre : "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide")

# Vérification avec plage de valeurs
def lire_age():
    while True:
        try:
            age = int(input("Âge : "))
            if 0 <= age <= 150:
                return age
            print("L'âge doit être entre 0 et 150")
        except ValueError:
            print("Veuillez entrer un nombre entier")
```

### 3. Applications pratiques (25 min)

#### A. Formulaire simple
```python
def saisir_informations():
    """Saisie d'informations personnelles."""
    infos = {}
    
    # Saisie avec validation
    infos["nom"] = input("Nom : ").strip()
    while not infos["nom"]:
        print("Le nom ne peut pas être vide")
        infos["nom"] = input("Nom : ").strip()
    
    # Saisie de l'âge avec validation
    while True:
        try:
            age = int(input("Âge : "))
            if 0 <= age <= 150:
                infos["age"] = age
                break
            print("Âge invalide")
        except ValueError:
            print("Veuillez entrer un nombre")
    
    return infos

# Utilisation
donnees = saisir_informations()
print(f"Bonjour {donnees['nom']}, vous avez {donnees['age']} ans")
```

#### B. Menu interactif
```python
def afficher_menu():
    print("""
    1. Nouveau jeu
    2. Charger partie
    3. Options
    4. Quitter
    """)

def menu_principal():
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()
        
        if choix == "1":
            print("Nouveau jeu...")
        elif choix == "2":
            print("Chargement...")
        elif choix == "3":
            print("Options...")
        elif choix == "4":
            print("Au revoir!")
            break
        else:
            print("Choix invalide")
```

### 4. Gestion des erreurs et validation (20 min)

#### A. Validation des entrées
```python
def valider_email():
    """Valide une adresse email basique."""
    while True:
        email = input("Email : ").strip().lower()
        if "@" in email and "." in email:
            return email
        print("Email invalide")

def valider_mot_de_passe():
    """Valide un mot de passe avec critères."""
    while True:
        mdp = input("Mot de passe : ")
        if len(mdp) < 8:
            print("Trop court (min 8 caractères)")
            continue
        if not any(c.isdigit() for c in mdp):
            print("Doit contenir au moins un chiffre")
            continue
        return mdp
```

#### B. Traitement des erreurs
```python
def saisir_date():
    """Saisie d'une date avec validation."""
    while True:
        try:
            jour = int(input("Jour : "))
            mois = int(input("Mois : "))
            annee = int(input("Année : "))
            
            # Validation simple
            if not (1 <= jour <= 31):
                print("Jour invalide")
                continue
            if not (1 <= mois <= 12):
                print("Mois invalide")
                continue
            if not (1900 <= annee <= 2100):
                print("Année invalide")
                continue
            
            return (jour, mois, annee)
            
        except ValueError:
            print("Veuillez entrer des nombres valides")
```

### 5. Bonnes pratiques (15 min)

#### A. Messages clairs
```python
# Bon : message explicite
age = input("Entrez votre âge (en années) : ")

# Bon : format attendu
date = input("Date (JJ/MM/AAAA) : ")

# Bon : plage de valeurs
note = input("Note (entre 0 et 20) : ")
```

#### B. Validation et nettoyage
```python
def nettoyer_entree(texte):
    """Nettoie une entrée utilisateur."""
    return texte.strip().lower()

def saisir_choix_multiple(options):
    """Saisie avec choix multiples."""
    while True:
        print("\nOptions disponibles :")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
            
        choix = input("\nVotre choix (numéro) : ")
        try:
            index = int(choix) - 1
            if 0 <= index < len(options):
                return options[index]
            print("Choix hors limites")
        except ValueError:
            print("Veuillez entrer un numéro")
```

### Phase de pratique (10 min)

Exercices :

1. Formulaire complet :
```python
def creer_compte():
    """
    Créer un formulaire d'inscription avec :
    - Nom (non vide)
    - Email (format valide)
    - Âge (nombre entre 0 et 150)
    - Mot de passe (critères de sécurité)
    """
    # À compléter
```

2. Calculatrice simple :
```python
def calculatrice():
    """
    Créer une calculatrice interactive qui :
    - Demande deux nombres
    - Demande l'opération (+, -, *, /)
    - Gère les erreurs
    - Affiche le résultat
    """
    # À compléter
```

### Synthèse (5 min)
- Utilisation basique de input()
- Conversion des types
- Validation des entrées
- Gestion des erreurs

### Évaluation (5 min)
1. Comment gérer une entrée numérique de façon sécurisée ?
2. Quelles sont les meilleures pratiques pour les messages ?
3. Comment valider une entrée utilisateur ?

## Points importants à retenir :

1. Bases :
   - input() retourne toujours une chaîne
   - Importance des messages clairs
   - Nettoyage des entrées

2. Conversion et validation :
   - Toujours gérer les erreurs de conversion
   - Valider avant d'utiliser
   - Donner un feedback clair

3. Bonnes pratiques :
   - Messages explicites
   - Validation robuste
   - Gestion des erreurs appropriée