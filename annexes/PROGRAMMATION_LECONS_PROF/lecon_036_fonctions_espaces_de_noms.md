# Plan de leçon : Fonctions sans paramètres et espaces de noms

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Création de fonctions simples et espaces de noms
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser la création de fonctions simples et comprendre les espaces de noms

- Objectifs disciplinaires :
  - Savoir créer des fonctions sans paramètres
  - Comprendre les espaces de noms global et local
  - Maîtriser la portée des variables
  - Gérer correctement les variables globales et locales

## Déroulement de la leçon

### 1. Création de fonctions simples (25 min)

#### A. Syntaxe de base
```python
# Fonction simple sans paramètre
def dire_bonjour():
    print("Bonjour!")

# Appel de la fonction
dire_bonjour()  # Affiche: Bonjour!

# Fonction avec valeur de retour
def obtenir_pi():
    return 3.14159

# Utilisation de la valeur retournée
pi = obtenir_pi()
print(f"La valeur de pi est {pi}")
```

#### B. Fonctions avec documentation
```python
def afficher_menu():
    """
    Affiche le menu principal de l'application.
    Cette fonction ne prend pas de paramètres.
    """
    print("1. Nouvelle partie")
    print("2. Charger partie")
    print("3. Options")
    print("4. Quitter")

# Accès à la documentation
help(afficher_menu)

def obtenir_version():
    """
    Retourne la version actuelle du programme.
    
    Returns:
        str: Numéro de version au format 'X.Y.Z'
    """
    return "1.0.0"
```

### 2. Espaces de noms locaux (30 min)

#### A. Variables locales
```python
def fonction_locale():
    # Variable locale
    x = 10
    print(f"Variable locale x = {x}")

# La variable x n'existe pas ici
# print(x)  # Génère une erreur

def exemple_portee():
    message = "Hello"  # Variable locale
    print(message)
    
    if True:
        autre_message = "World"  # Aussi locale à la fonction
        print(autre_message)
    
    print(autre_message)  # Accessible car dans la même fonction
```

#### B. Isolation des variables locales
```python
def fonction_1():
    x = 10
    print(f"x dans fonction_1: {x}")

def fonction_2():
    x = 20  # Différente variable x
    print(f"x dans fonction_2: {x}")

# Les deux fonctions ont leur propre 'x'
fonction_1()  # x dans fonction_1: 10
fonction_2()  # x dans fonction_2: 20

def demonstrer_isolation():
    compteur = 0
    def incrementer():
        compteur = 1  # Nouvelle variable locale
        print(f"Compteur local: {compteur}")
    
    incrementer()
    print(f"Compteur externe: {compteur}")  # Toujours 0
```

### 3. Espace de noms global (30 min)

#### A. Variables globales
```python
# Variable globale
PI = 3.14159

def utiliser_pi():
    print(f"La valeur de PI est {PI}")  # Accès en lecture

# Modification de variables globales
compteur_global = 0

def incrementer_compteur():
    global compteur_global
    compteur_global += 1
    print(f"Compteur: {compteur_global}")

def reinitialiser_compteur():
    global compteur_global
    compteur_global = 0
```

#### B. Bonnes pratiques avec les globales
```python
# Configuration globale
CONFIG = {
    "debug": True,
    "version": "1.0.0",
    "langue": "FR"
}

def obtenir_config():
    """Meilleure pratique que d'utiliser global."""
    return CONFIG

def modifier_config(cle, valeur):
    """Modification contrôlée de la configuration."""
    if cle in CONFIG:
        CONFIG[cle] = valeur
    else:
        raise KeyError(f"Configuration inconnue: {cle}")
```

### 4. Interaction entre espaces de noms (25 min)

#### A. Accès aux variables globales
```python
VERSION = "1.0"
DEBUG = True

def afficher_info():
    # Lecture des globales (pas besoin de 'global')
    print(f"Version: {VERSION}")
    if DEBUG:
        print("Mode debug activé")

def modifier_debug():
    global DEBUG  # Nécessaire pour modification
    DEBUG = not DEBUG
    print(f"Debug maintenant: {DEBUG}")
```

#### B. Imbrication d'espaces de noms
```python
message = "Global"

def fonction_externe():
    message = "Externe"
    
    def fonction_interne():
        message = "Interne"
        print(f"Interne: {message}")
    
    print(f"Externe: {message}")
    fonction_interne()
    print(f"Après interne: {message}")

print(f"Global: {message}")
fonction_externe()
```

### 5. Gestion avancée des espaces de noms (20 min)

#### A. Utilisation de nonlocal
```python
def compteur():
    count = 0
    
    def incrementer():
        nonlocal count
        count += 1
        return count
    
    def obtenir():
        return count
    
    return incrementer, obtenir

inc, get = compteur()
print(inc())  # 1
print(inc())  # 2
print(get())  # 2
```

#### B. Encapsulation avec fermetures
```python
def creer_compte(solde_initial):
    solde = solde_initial
    
    def depot(montant):
        nonlocal solde
        solde += montant
        return solde
    
    def retrait(montant):
        nonlocal solde
        if montant <= solde:
            solde -= montant
            return True
        return False
    
    def consulter():
        return solde
    
    return {
        "depot": depot,
        "retrait": retrait,
        "consulter": consulter
    }
```

### Phase de pratique (15 min)

Exercices :

1. Création de fonctions :
```python
def creer_jeu_simple():
    """
    Créer un petit jeu avec :
    - Un score global
    - Des fonctions pour jouer
    - Une fonction pour réinitialiser
    """
    # À compléter
```

2. Gestion d'état :
```python
def creer_gestionnaire_etat():
    """
    Créer un gestionnaire qui :
    - Maintient un état interne
    - Fournit des méthodes de modification
    - Protège les données
    """
    # À compléter
```

### Synthèse (5 min)
- Création de fonctions simples
- Espaces de noms local et global
- Utilisation appropriée des variables
- Encapsulation et protection des données

## Points importants à retenir :

1. Fonctions simples :
   - Définition avec def
   - Documentation avec docstrings
   - Return optionnel

2. Espaces de noms :
   - Local à chaque fonction
   - Global pour le module
   - Imbrication possible

3. Bonnes pratiques :
   - Limiter l'usage des variables globales
   - Préférer le passage de paramètres
   - Documenter les fonctions
   - Encapsuler les données sensibles