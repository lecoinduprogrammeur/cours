# Plan de leçon : Variables de type liste (list)

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Manipulation des listes
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation et la manipulation des listes

- Objectifs disciplinaires :
  - Comprendre la création et l'accès aux listes
  - Maîtriser les méthodes de liste
  - Savoir modifier les listes
  - Gérer les cas complexes

## Déroulement de la leçon

### 1. Création et accès aux listes (20 min)

#### A. Création de listes
```python
# Liste vide
liste1 = []
liste2 = list()

# Liste avec éléments
nombres = [1, 2, 3, 4, 5]
texte = ["a", "b", "c"]
mixte = [1, "texte", 3.14, True]

# Liste par compréhension
carres = [x**2 for x in range(5)]
pairs = [x for x in range(10) if x % 2 == 0]

# Liste à partir d'autres séquences
liste_str = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
tuple_list = list((1, 2, 3))  # [1, 2, 3]
```

#### B. Accès aux éléments
```python
# Accès par index
nombres = [10, 20, 30, 40, 50]
premier = nombres[0]     # 10
dernier = nombres[-1]    # 50

# Slicing
partie = nombres[1:4]    # [20, 30, 40]
debut = nombres[:3]      # [10, 20, 30]
fin = nombres[2:]        # [30, 40, 50]
pas = nombres[::2]       # [10, 30, 50]
inverse = nombres[::-1]  # [50, 40, 30, 20, 10]

# Vérification d'existence
existe = 30 in nombres   # True
```

### 2. Méthodes de modification (25 min)

#### A. Ajout d'éléments
```python
liste = [1, 2, 3]

# Ajouter à la fin
liste.append(4)          # [1, 2, 3, 4]

# Insérer à une position
liste.insert(1, 5)       # [1, 5, 2, 3, 4]

# Étendre avec une autre liste
liste.extend([6, 7])     # [1, 5, 2, 3, 4, 6, 7]

# Concaténation avec +
nouvelle = liste + [8, 9]
```

#### B. Suppression d'éléments
```python
# Supprimer par valeur
liste.remove(5)          # Première occurrence

# Supprimer par index
del liste[0]             # Supprime premier élément

# Retirer et retourner le dernier élément
dernier = liste.pop()    # Retire et retourne le dernier

# Retirer à un index spécifique
element = liste.pop(1)   # Retire et retourne l'élément à l'index 1

# Vider la liste
liste.clear()            # []
```

### 3. Méthodes de tri et recherche (25 min)

```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Tri en place
nombres.sort()           # Modifie la liste
nombres.sort(reverse=True)  # Tri décroissant

# Créer une nouvelle liste triée
triee = sorted(nombres)  # Original non modifié
triee_desc = sorted(nombres, reverse=True)

# Inverser l'ordre
nombres.reverse()        # Inverse en place
inverse = list(reversed(nombres))  # Nouvelle liste

# Recherche
index = nombres.index(5)   # Premier index de 5
compte = nombres.count(3)  # Nombre d'occurrences de 3

# Tri personnalisé
personnes = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
personnes.sort(key=lambda x: x[1])  # Tri par âge
```

### 4. Listes imbriquées (20 min)

```python
# Matrice
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accès aux éléments
element = matrice[1][2]  # 6

# Modification
matrice[0][1] = 10

# Parcours de matrice
for ligne in matrice:
    for element in ligne:
        print(element, end=' ')
    print()

# Création de matrice par compréhension
taille = 3
matrice = [[0 for _ in range(taille)] for _ in range(taille)]

# Aplatir une liste imbriquée
aplatie = [x for ligne in matrice for x in ligne]
```

### 5. Opérations avancées (25 min)

#### A. Copie de listes
```python
# Copie superficielle
liste1 = [1, [2, 3], 4]
copie1 = liste1.copy()     # ou liste1[:]
copie2 = list(liste1)

# Copie profonde
import copy
copie_profonde = copy.deepcopy(liste1)

# Démonstration de la différence
liste1[1][0] = 5
print(copie1[1][0])        # 5 (copie superficielle)
print(copie_profonde[1][0])  # 2 (copie profonde)
```

#### B. Manipulation avancée
```python
def filtrer_liste(liste, condition):
    """Filtre les éléments selon une condition."""
    return [x for x in liste if condition(x)]

def transformer_liste(liste, transformation):
    """Applique une transformation à chaque élément."""
    return [transformation(x) for x in liste]

def grouper_elements(liste, taille):
    """Groupe les éléments par taille."""
    return [liste[i:i + taille] for i in range(0, len(liste), taille)]

def eliminer_doublons(liste):
    """Élimine les doublons en préservant l'ordre."""
    return list(dict.fromkeys(liste))
```

### 6. Applications pratiques (15 min)

```python
def calculer_statistiques(nombres):
    """Calcule diverses statistiques."""
    if not nombres:
        return None
    
    return {
        'minimum': min(nombres),
        'maximum': max(nombres),
        'moyenne': sum(nombres) / len(nombres),
        'médiane': sorted(nombres)[len(nombres)//2],
        'unique': len(set(nombres))
    }

def rotation_liste(liste, n):
    """Effectue une rotation de n positions."""
    if not liste:
        return liste
    n = n % len(liste)
    return liste[n:] + liste[:n]

def fusionner_listes_triees(liste1, liste2):
    """Fusionne deux listes triées."""
    resultat = []
    i = j = 0
    
    while i < len(liste1) and j < len(liste2):
        if liste1[i] <= liste2[j]:
            resultat.append(liste1[i])
            i += 1
        else:
            resultat.append(liste2[j])
            j += 1
    
    resultat.extend(liste1[i:])
    resultat.extend(liste2[j:])
    return resultat
```

### Phase de pratique (15 min)

Exercices :

1. Gestionnaire de liste :
```python
def creer_gestionnaire():
    """
    Créer un gestionnaire qui :
    - Ajoute/supprime des éléments
    - Trie et filtre
    - Maintient des statistiques
    """
    # À compléter
```

2. Manipulation avancée :
```python
def manipuler_matrice():
    """
    Créer des fonctions pour :
    - Rotation de matrice
    - Transposition
    - Opérations par ligne/colonne
    """
    # À compléter
```

## Points importants à retenir :

1. Création et accès :
   - Différentes méthodes de création
   - Indexation et slicing
   - Copie de listes

2. Modification :
   - Ajout et suppression
   - Tri et recherche
   - Modifications en place vs nouvelles listes

3. Cas avancés :
   - Listes imbriquées
   - Compréhensions de liste
   - Manipulations complexes