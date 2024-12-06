# Plan de leçon : Les listes en Python

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Les listes : création, manipulation et méthodes
- Durée prévue : 2h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser la création et la manipulation des listes

- Objectifs disciplinaires :
  - Comprendre les différentes façons de créer des listes
  - Maîtriser les méthodes de manipulation
  - Savoir accéder et modifier les éléments
  - Utiliser efficacement les méthodes de liste

## Déroulement de la leçon

### 1. Création de listes (20 min)

#### A. Méthodes de base
```python
# Liste vide
liste1 = []
liste2 = list()

# Liste avec éléments
nombres = [1, 2, 3, 4, 5]
fruits = ["pomme", "banane", "orange"]

# Liste mixte
mixte = [1, "texte", 3.14, True]

# Liste par compréhension
carres = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
pairs = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Liste à partir d'autres séquences
liste_string = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
liste_tuple = list((1, 2, 3))  # [1, 2, 3]
```

#### B. Listes imbriquées
```python
# Matrice
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Liste de tuples
coordonnees = [(1, 2), (3, 4), (5, 6)]

# Création dynamique
taille = 3
tableau = [[0 for _ in range(taille)] for _ in range(taille)]
```

### 2. Accès aux éléments (25 min)

#### A. Indexation
```python
nombres = [10, 20, 30, 40, 50]

# Accès simple
premier = nombres[0]    # 10
dernier = nombres[-1]   # 50

# Slicing
sous_liste = nombres[1:4]    # [20, 30, 40]
premiers = nombres[:3]       # [10, 20, 30]
derniers = nombres[2:]       # [30, 40, 50]

# Pas
pairs = nombres[::2]         # [10, 30, 50]
inverse = nombres[::-1]      # [50, 40, 30, 20, 10]

# Listes imbriquées
matrice = [[1, 2, 3], [4, 5, 6]]
element = matrice[1][2]      # 6
```

#### B. Modification par index
```python
fruits = ["pomme", "banane", "orange"]

# Modification simple
fruits[0] = "kiwi"

# Modification par slice
fruits[1:] = ["poire", "fraise"]

# Insertion multiple
fruits[1:1] = ["ananas", "mangue"]  # Insertion au milieu

# Dans les listes imbriquées
matrice = [[1, 2], [3, 4]]
matrice[0][1] = 5
```

### 3. Méthodes de modification (30 min)

#### A. Ajout d'éléments
```python
liste = [1, 2, 3]

# Ajouter à la fin
liste.append(4)               # [1, 2, 3, 4]

# Insérer à une position
liste.insert(1, 5)           # [1, 5, 2, 3, 4]

# Étendre avec une autre liste
liste.extend([6, 7, 8])      # [1, 5, 2, 3, 4, 6, 7, 8]

# Alternative avec +=
liste += [9, 10]             # [1, 5, 2, 3, 4, 6, 7, 8, 9, 10]
```

#### B. Suppression d'éléments
```python
liste = [1, 2, 3, 2, 4, 2, 5]

# Supprimer par valeur (première occurrence)
liste.remove(2)               # [1, 3, 2, 4, 2, 5]

# Supprimer par index
del liste[2]                  # [1, 3, 4, 2, 5]

# Retirer et retourner le dernier élément
dernier = liste.pop()         # [1, 3, 4, 2]

# Retirer à un index spécifique
element = liste.pop(1)        # [1, 4, 2]

# Vider la liste
liste.clear()                 # []
```

### 4. Méthodes de recherche et tri (25 min)

#### A. Recherche
```python
nombres = [1, 2, 3, 2, 4, 2, 5]

# Compter les occurrences
compte = nombres.count(2)      # 3

# Trouver l'index (première occurrence)
index = nombres.index(2)       # 1

# Recherche avec gestion d'erreur
try:
    index = nombres.index(6)   # ValueError
except ValueError:
    print("Non trouvé")

# Vérification d'existence
existe = 3 in nombres         # True
```

#### B. Tri et réorganisation
```python
liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Tri en place
liste.sort()                  # Modifie la liste
liste.sort(reverse=True)      # Tri décroissant

# Créer une nouvelle liste triée
nouvelle = sorted(liste)      # Original non modifié

# Inverser l'ordre
liste.reverse()              # Inverse en place
inverse = liste[::-1]        # Nouvelle liste inversée

# Tri personnalisé
objets = [("a", 3), ("b", 1), ("c", 2)]
objets.sort(key=lambda x: x[1])  # Tri selon le second élément
```

### 5. Opérations avancées (25 min)

#### A. Copie de listes
```python
# Copie superficielle
liste1 = [1, [2, 3], 4]
copie1 = liste1.copy()        # ou liste1[:]
copie2 = list(liste1)

# Copie profonde
import copy
copie_profonde = copy.deepcopy(liste1)

# Démonstration de la différence
liste1[1][0] = 5
print(copie1[1][0])          # 5 (copie superficielle)
print(copie_profonde[1][0])  # 2 (copie profonde)
```

#### B. Compréhensions avancées
```python
# Compréhension avec conditions multiples
nombres = [x for x in range(20) if x % 2 == 0 if x % 4 == 0]

# Compréhension imbriquée
matrice = [[i+j for j in range(3)] for i in range(3)]

# Compréhension avec try-except
nombres = ["1", "2", "a", "3"]
valides = [int(x) for x in nombres if x.isdigit()]

# Aplatir une liste imbriquée
imbriquee = [[1, 2], [3, 4], [5, 6]]
aplatie = [x for sous_liste in imbriquee for x in sous_liste]
```

### 6. Méthodes utilitaires (20 min)

```python
# Longueur
liste = [1, 2, 3, 4, 5]
taille = len(liste)

# Min et Max
minimum = min(liste)
maximum = max(liste)

# Somme
total = sum(liste)

# Énumération
for index, valeur in enumerate(liste):
    print(f"Index {index}: {valeur}")

# Zip pour combiner des listes
noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for nom, age in zip(noms, ages):
    print(f"{nom} a {age} ans")
```

### 7. Applications pratiques (20 min)

```python
def filtrer_liste(liste, condition):
    """Filtre une liste selon une condition."""
    return [x for x in liste if condition(x)]

def transformer_liste(liste, transformation):
    """Applique une transformation à chaque élément."""
    return [transformation(x) for x in liste]

def grouper_elements(liste, taille):
    """Groupe les éléments par taille donnée."""
    return [liste[i:i+taille] for i in range(0, len(liste), taille)]

def eliminer_doublons(liste):
    """Élimine les doublons en préservant l'ordre."""
    return list(dict.fromkeys(liste))
```

### Phase de pratique (15 min)

Exercices :

1. Manipulation de liste :
```python
def manipuler_liste(liste):
    """
    - Trier la liste
    - Éliminer les doublons
    - Filtrer les nombres pairs
    - Calculer la moyenne
    """
    # À compléter
```

2. Traitement avancé :
```python
def traiter_matrice(matrice):
    """
    - Calculer la somme de chaque ligne
    - Trouver le maximum de chaque colonne
    - Transposer la matrice
    """
    # À compléter
```

### Synthèse (5 min)
- Création et initialisation
- Méthodes de modification
- Méthodes de recherche
- Applications pratiques

## Points importants à retenir :

1. Création et accès :
   - Différentes méthodes de création
   - Indexation et slicing
   - Modification par index

2. Méthodes principales :
   - append(), insert(), extend()
   - remove(), pop(), clear()
   - sort(), reverse()

3. Bonnes pratiques :
   - Attention aux copies
   - Utilisation appropriée des méthodes
   - Gestion efficace de la mémoire