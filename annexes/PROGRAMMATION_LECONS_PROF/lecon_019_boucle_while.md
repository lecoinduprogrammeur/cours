# Plan de leçon : La boucle while

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Boucle while et ses utilisations
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation de la boucle while

- Objectifs disciplinaires :
  - Comprendre la structure et le fonctionnement
  - Maîtriser les conditions de sortie
  - Gérer les boucles infinies
  - Implémenter des cas d'utilisation courants

## Déroulement de la leçon

### 1. Structure de base (20 min)

#### A. Syntaxe fondamentale
```python
# Structure de base
while condition:
    # Instructions à répéter
    # Tant que la condition est True

# Exemple simple
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

# Avec une condition complexe
x = 0
y = 10
while x < 5 and y > 0:
    print(f"x={x}, y={y}")
    x += 1
    y -= 2
```

#### B. Fonctionnement
```python
# Processus d'évaluation
nombre = 1
while nombre <= 3:
    print(f"Étape {nombre}")
    nombre += 1
    # 1. Vérifie la condition
    # 2. Si True, exécute le bloc
    # 3. Retourne à l'étape 1

# Importance de l'indentation
while nombre > 0:
    print(nombre)  # Dans la boucle
    nombre -= 1
print("Fin")      # Hors de la boucle
```

### 2. Contrôle de boucle (25 min)

#### A. Instructions break et continue
```python
# Utilisation de break
while True:
    reponse = input("Continuer ? (o/n) : ")
    if reponse.lower() == 'n':
        break  # Sort immédiatement de la boucle

# Utilisation de continue
compteur = 0
while compteur < 5:
    compteur += 1
    if compteur == 3:
        continue  # Passe à l'itération suivante
    print(compteur)
```

#### B. Else avec while
```python
# While avec else
tentatives = 3
while tentatives > 0:
    reponse = input("Mot de passe : ")
    if reponse == "secret":
        print("Accès accordé")
        break
    tentatives -= 1
else:
    print("Trop de tentatives")  # Exécuté si pas de break
```

### 3. Cas d'utilisation courants (30 min)

#### A. Validation d'entrées
```python
def obtenir_age_valide():
    while True:
        try:
            age = int(input("Votre âge : "))
            if 0 <= age <= 150:
                return age
            print("Âge invalide")
        except ValueError:
            print("Veuillez entrer un nombre")

def obtenir_choix_menu():
    options = ['1', '2', '3', '4']
    while True:
        choix = input("Choix (1-4) : ")
        if choix in options:
            return choix
        print("Option invalide")
```

#### B. Traitement de données
```python
def rechercher_element(liste, cible):
    index = 0
    while index < len(liste):
        if liste[index] == cible:
            return index
        index += 1
    return -1

def diviser_jusqu_a_impair(nombre):
    while nombre % 2 == 0:
        nombre //= 2
    return nombre
```

#### C. Jeux et simulations
```python
def jeu_devinette():
    import random
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    
    while True:
        tentatives += 1
        essai = int(input("Devinez le nombre : "))
        
        if essai == nombre_secret:
            return f"Gagné en {tentatives} essais!"
        elif essai < nombre_secret:
            print("Plus grand")
        else:
            print("Plus petit")

def simulation_population(pop_initiale, taux_croissance):
    population = pop_initiale
    annees = 0
    while population < pop_initiale * 2:
        population *= (1 + taux_croissance)
        annees += 1
    return annees
```

### 4. Gestion des boucles infinies (20 min)

#### A. Causes et prévention
```python
# Boucle infinie par erreur
x = 1
while x > 0:
    print(x)
    x += 1  # x ne sera jamais <= 0

# Boucle infinie intentionnelle avec sortie
while True:
    commande = input("> ")
    if commande == "quit":
        break
    executer_commande(commande)
```

#### B. Sécurités et garde-fous
```python
def boucle_securisee():
    max_iterations = 1000
    compteur = 0
    
    while condition():
        if compteur >= max_iterations:
            raise Exception("Trop d'itérations")
        # Traitement
        compteur += 1

def traitement_avec_timeout():
    import time
    debut = time.time()
    timeout = 5  # secondes
    
    while traitement_necessaire():
        if time.time() - debut > timeout:
            return "Timeout"
        # Traitement
```

### 5. Optimisation et bonnes pratiques (15 min)

#### A. Simplicité et lisibilité
```python
# À éviter : conditions complexes
while a > 0 and b < 10 and c != 0 and d.is_valid():
    # Code

# Préférer : conditions décomposées
while condition_est_valide():  # Fonction séparée
    # Code

# À éviter : boucles imbriquées profondes
while condition1:
    while condition2:
        while condition3:
            # Code

# Préférer : extraire en fonctions
def traiter_niveau3():
    while condition3:
        # Code
```

#### B. Performance
```python
# Éviter les calculs répétés
# Mauvais
while calcul_complexe() > limite:
    # Code

# Bon
resultat = calcul_complexe()
while resultat > limite:
    # Code
    resultat = calcul_complexe()

# Utiliser des drapeaux pour les conditions complexes
recherche_active = True
while recherche_active:
    # Code
    if condition_arret():
        recherche_active = False
```

### Phase de pratique (15 min)

Exercices :

1. Validation d'entrées :
```python
def obtenir_email_valide():
    """
    Demander un email jusqu'à obtenir
    un format valide (contient @ et .)
    """
    # À compléter
```

2. Traitement de données :
```python
def compter_occurrences(texte, caractere):
    """
    Compter les occurrences d'un caractère
    dans un texte en utilisant while
    """
    # À compléter
```

### Synthèse (5 min)
- Structure et fonctionnement
- Contrôle de flux
- Cas d'utilisation
- Bonnes pratiques

### Évaluation (5 min)
1. Quand utiliser while plutôt que for ?
2. Comment éviter les boucles infinies ?
3. Comment optimiser une boucle while ?

## Points importants à retenir :

1. Structure :
   - Condition initiale
   - Corps de boucle
   - Condition de sortie

2. Contrôle :
   - break et continue
   - else avec while
   - Drapeaux de contrôle

3. Bonnes pratiques :
   - Conditions claires
   - Sortie garantie
   - Optimisation des calculs