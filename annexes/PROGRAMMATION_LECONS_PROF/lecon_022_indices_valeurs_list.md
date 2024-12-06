# Plan de leçon : Indices et valeurs dans les listes

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Manipulation des indices et valeurs dans les listes
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'accès et la manipulation des éléments d'une liste

- Objectifs disciplinaires :
  - Comprendre l'indexation des listes
  - Maîtriser le slicing de listes
  - Manipuler les éléments et sous-listes
  - Comprendre les différences avec les chaînes

## Déroulement de la leçon

### 1. Indices de base (20 min)

#### A. Indexation positive
```python
# Les indices commencent à 0
nombres = [10, 20, 30, 40, 50]
print(nombres[0])    # 10 (premier élément)
print(nombres[2])    # 30 (troisième élément)
print(nombres[4])    # 50 (dernier élément)

# Modification par indice
nombres[0] = 15      # Modifie le premier élément
print(nombres)       # [15, 20, 30, 40, 50]

# Parcours avec indices
for i in range(len(nombres)):
    print(f"Index {i}: {nombres[i]}")
```

#### B. Indexation négative
```python
# Les indices négatifs commencent à -1
fruits = ["pomme", "banane", "orange", "kiwi"]
print(fruits[-1])    # "kiwi" (dernier)
print(fruits[-2])    # "orange" (avant-dernier)

# Table de correspondance
"""
+--------+---------+----------+--------+
| pomme  | banane  | orange   | kiwi   |
+--------+---------+----------+--------+
|   0    |    1    |    2     |   3    |
+--------+---------+----------+--------+
|  -4    |   -3    |   -2     |  -1    |
+--------+---------+----------+--------+
"""

# Modification avec indices négatifs
fruits[-1] = "fraise"  # Modifie le dernier élément
```

### 2. Slicing (découpage) (25 min)

#### A. Syntaxe de base
```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extraction de sous-listes
print(nombres[2:5])    # [2, 3, 4]
print(nombres[:4])     # [0, 1, 2, 3]
print(nombres[6:])     # [6, 7, 8, 9]
print(nombres[:])      # Crée une copie de la liste

# Avec pas (step)
print(nombres[::2])    # [0, 2, 4, 6, 8]
print(nombres[1::2])   # [1, 3, 5, 7, 9]

# Modification par slicing
nombres[2:5] = [20, 30, 40]
print(nombres)         # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]
```

#### B. Slicing avancé
```python
# Indices négatifs dans le slicing
liste = [10, 20, 30, 40, 50]
print(liste[-3:])      # [30, 40, 50]
print(liste[:-2])      # [10, 20, 30]
print(liste[-4:-1])    # [20, 30, 40]

# Pas négatif
print(liste[::-1])     # [50, 40, 30, 20, 10]
print(liste[4:1:-1])   # [50, 40, 30]

# Remplacement avec slicing
liste[1:4] = [200, 300, 400]
print(liste)           # [10, 200, 300, 400, 50]

# Suppression avec slicing
liste[1:4] = []        # Supprime les éléments 1 à 3
```

### 3. Méthodes et opérations courantes (25 min)

#### A. Recherche et comptage
```python
nombres = [1, 2, 3, 2, 4, 2, 5]

# Recherche d'index
premier_2 = nombres.index(2)      # 1
try:
    index_6 = nombres.index(6)    # ValueError
except ValueError:
    print("6 non trouvé")

# Comptage d'occurrences
nb_2 = nombres.count(2)           # 3

# Vérification d'existence
existe = 3 in nombres             # True
absent = 6 in nombres            # False

# Recherche avec condition
def trouver_indices(liste, valeur):
    return [i for i in range(len(liste)) if liste[i] == valeur]
```

#### B. Modification et manipulation
```python
liste = [1, 2, 3]

# Ajout d'éléments
liste.append(4)        # Ajoute à la fin
liste.insert(0, 0)     # Insère au début
liste.extend([5, 6])   # Ajoute plusieurs éléments

# Suppression d'éléments
liste.remove(3)        # Supprime la première occurrence de 3
element = liste.pop()  # Retire et retourne le dernier élément
element = liste.pop(0) # Retire et retourne l'élément d'index 0
del liste[1]          # Supprime l'élément d'index 1

# Tri et inversion
liste.sort()          # Tri en place
liste.reverse()       # Inverse en place
```

### 4. Listes imbriquées (20 min)

#### A. Accès aux éléments
```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accès aux éléments
element = matrice[1][2]    # 6
premiere_ligne = matrice[0] # [1, 2, 3]

# Modification d'éléments
matrice[0][1] = 20
print(matrice)  # [[1, 20, 3], [4, 5, 6], [7, 8, 9]]

# Parcours de matrice
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(f"matrice[{i}][{j}] = {matrice[i][j]}")
```

#### B. Manipulation de listes imbriquées
```python
# Copie de listes imbriquées
import copy
shallow_copy = matrice.copy()        # Copie superficielle
deep_copy = copy.deepcopy(matrice)   # Copie profonde

# Création de matrice
def creer_matrice(lignes, colonnes, valeur_defaut=0):
    return [[valeur_defaut for _ in range(colonnes)] 
            for _ in range(lignes)]

# Transposition de matrice
def transposer(matrice):
    return [[matrice[j][i] for j in range(len(matrice))]
            for i in range(len(matrice[0]))]
```

### 5. Bonnes pratiques et pièges courants (20 min)

#### A. Copie et référence
```python
# Piège de la référence
liste1 = [1, 2, 3]
liste2 = liste1           # Crée une référence
liste2[0] = 10           # Modifie aussi liste1

# Solutions
liste2 = liste1.copy()    # Copie superficielle
liste2 = list(liste1)     # Autre méthode de copie
liste2 = liste1[:]        # Copie par slicing

# Pour les listes imbriquées
import copy
liste2 = copy.deepcopy(liste1)  # Copie profonde
```

#### B. Bonnes pratiques
```python
# Vérification de l'index avant accès
def acceder_securise(liste, index):
    if 0 <= index < len(liste):
        return liste[index]
    return None

# Modification sécurisée
def modifier_securise(liste, index, valeur):
    if 0 <= index < len(liste):
        liste[index] = valeur
        return True
    return False

# Utilisation de enumerate
for i, valeur in enumerate(liste):
    print(f"Index {i}: {valeur}")
```

### Phase de pratique (15 min)

Exercices :

1. Manipulation de liste :
```python
def manipuler_liste(liste):
    """
    - Inverser les éléments
    - Remplacer les éléments pairs par leur carré
    - Supprimer les doublons
    - Retourner la nouvelle liste
    """
    # À compléter
```

2. Opérations sur matrice :
```python
def operations_matrice(matrice):
    """
    - Calculer la somme de chaque ligne
    - Trouver le maximum de chaque colonne
    - Calculer la diagonale principale
    """
    # À compléter
```

### Synthèse (5 min)
- Indexation et slicing
- Méthodes principales
- Gestion des listes imbriquées
- Points d'attention sur les références

## Points importants à retenir :

1. Indexation :
   - Commence à 0
   - Indices négatifs disponibles
   - Modification possible par index

2. Slicing :
   - [debut:fin:pas]
   - Crée une nouvelle liste
   - Peut être utilisé pour modifier

3. Bonnes pratiques :
   - Attention aux références
   - Utiliser les bonnes méthodes de copie
   - Vérifier les indices avant accès