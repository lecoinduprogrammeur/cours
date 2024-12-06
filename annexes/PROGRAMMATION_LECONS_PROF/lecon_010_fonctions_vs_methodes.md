# Plan de leçon : Fonctions intégrées vs Méthodes en Python

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Distinction entre fonctions intégrées et méthodes
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Comprendre la différence entre fonctions intégrées et méthodes

- Objectifs disciplinaires :
  - Maîtriser l'utilisation des fonctions intégrées
  - Comprendre les méthodes spécifiques aux types
  - Savoir quand utiliser l'une ou l'autre
  - Identifier les avantages et limitations de chaque approche

## Déroulement de la leçon

### 1. Définitions et différences principales (20 min)

#### A. Fonctions intégrées
```python
# Fonctions intégrées : disponibles globalement, s'appliquent à différents types
len([1, 2, 3])     # Fonction intégrée
print("Hello")      # Fonction intégrée
type(42)           # Fonction intégrée

# S'utilisent en passant l'objet en paramètre
str(123)           # Conversion en chaîne
```

#### B. Méthodes
```python
# Méthodes : liées à un type spécifique, s'appellent avec la notation point
texte = "hello"
texte.upper()      # Méthode de string
liste = [1, 2, 3]
liste.append(4)    # Méthode de list

# S'utilisent après l'objet avec un point
"hello".capitalize()  # Méthode de string
```

### 2. Comparaison par type (30 min)

#### A. Chaînes de caractères (str)
```python
# Fonctions intégrées pour str
texte = "hello world"
len(texte)         # 11
str(123)           # "123"

# Méthodes de str
texte.upper()      # "HELLO WORLD"
texte.split()      # ["hello", "world"]
texte.replace("hello", "hi")  # "hi world"
texte.strip()      # Retire les espaces
texte.isdigit()    # Vérifie si numérique
```

#### B. Listes
```python
# Fonctions intégrées pour list
ma_liste = [3, 1, 2]
len(ma_liste)      # 3
list("abc")        # ['a', 'b', 'c']
sorted(ma_liste)   # [1, 2, 3] (nouvelle liste)

# Méthodes de list
ma_liste.append(4)  # Ajoute à la fin
ma_liste.sort()     # Trie la liste en place
ma_liste.pop()      # Retire et retourne le dernier élément
ma_liste.reverse()  # Inverse la liste en place
ma_liste.count(1)   # Compte les occurrences
```

#### C. Dictionnaires
```python
# Fonctions intégrées pour dict
mon_dict = {'a': 1, 'b': 2}
len(mon_dict)      # 2
dict([('a', 1)])   # Crée un dictionnaire

# Méthodes de dict
mon_dict.keys()     # Retourne les clés
mon_dict.values()   # Retourne les valeurs
mon_dict.items()    # Retourne paires clé-valeur
mon_dict.get('a')   # Accès sécurisé
mon_dict.update({'c': 3})  # Mise à jour
```

### 3. Cas pratiques de comparaison (30 min)

#### A. Manipulation de texte
```python
# Approche avec fonctions intégrées
texte = "hello world"
mots = len(texte.split())  # Combine fonction et méthode
est_chaine = isinstance(texte, str)  # Vérifie le type

# Approche avec méthodes
nombre_mots = texte.count(' ') + 1
est_alpha = texte.isalpha()  # Vérifie si alphabétique
```

#### B. Manipulation de collections
```python
# Approche avec fonctions intégrées
nombres = [1, 2, 3, 4, 5]
total = sum(nombres)    # Fonction intégrée
maximum = max(nombres)  # Fonction intégrée
tries = sorted(nombres) # Nouvelle liste triée

# Approche avec méthodes
nombres.reverse()       # Modifie en place
nombres.sort()         # Modifie en place
nombres.extend([6, 7]) # Ajoute plusieurs éléments
```

### 4. Différences clés et choix d'utilisation (20 min)

#### A. Principales différences
```python
# 1. Portée
len([1, 2, 3])        # Fonctionne sur plusieurs types
[1, 2, 3].append(4)   # Spécifique aux listes

# 2. Modification
sorted([3, 1, 2])     # Crée une nouvelle liste
[3, 1, 2].sort()      # Modifie en place

# 3. Retour
str(123)              # Retourne toujours une nouvelle chaîne
liste.append(4)       # Modifie l'objet, retourne None
```

#### B. Quand utiliser quoi ?
```python
# Fonctions intégrées pour :
# - Opérations génériques
len(sequence)         # Marche sur str, list, tuple, etc.
# - Conversions de type
int("123")           # Conversion explicite
# - Opérations qui retournent de nouvelles valeurs
sorted(liste)        # Nouvelle liste triée

# Méthodes pour :
# - Opérations spécifiques au type
texte.upper()        # Spécifique aux chaînes
# - Modifications en place
liste.sort()         # Modifie la liste existante
# - Comportements spécialisés
dict.get("clé", "défaut")  # Accès sécurisé aux dictionnaires
```

### 5. Tableaux comparatifs (15 min)

#### A. Opérations courantes
| Opération  | Fonction intégrée | Méthode         |
| ---------- | ----------------- | --------------- |
| Longueur   | len(obj)          | N/A             |
| Tri        | sorted(obj)       | obj.sort()      |
| Conversion | str(obj)          | obj.\_\_str__() |
| Maximum    | max(obj)          | N/A             |
| Comptage   | N/A               | obj.count()     |

#### B. Caractéristiques
| Aspect       | Fonctions intégrées | Méthodes           |
| ------------ | ------------------- | ------------------ |
| Portée       | Générale            | Spécifique au type |
| Modification | Non                 | Possible           |
| Retour       | Toujours une valeur | Peut être None     |
| Flexibilité  | Multiple types      | Un seul type       |

### Phase de pratique (15 min)

Exercices :

1. Choix d'approche :
```python
def traiter_donnees(donnees):
    """
    Choisir entre fonctions et méthodes pour :
    - Compter les éléments
    - Trier les données
    - Convertir en autre type
    """
    # À compléter
```

2. Optimisation :
```python
def optimiser_code(texte):
    """
    Réécrire en utilisant l'approche la plus appropriée
    """
    # Version à optimiser
    mots = str(texte).split(' ')
    mots = sorted(mots)
    longueur = len(mots)
    return longueur
```

### Synthèse (5 min)
- Différences fondamentales
- Cas d'utilisation appropriés
- Bonnes pratiques

### Évaluation (5 min)
1. Quand préférer une fonction intégrée à une méthode ?
2. Pourquoi certaines opérations n'existent que comme méthodes ?
3. Comment choisir entre sorted() et sort() ?

## Points importants à retenir :

1. Fonctions intégrées :
   - Génériques et versatiles
   - Disponibles globalement
   - Ne modifient pas les objets originaux
   - Retournent toujours une valeur

2. Méthodes :
   - Spécifiques à un type
   - Peuvent modifier l'objet
   - Parfois plus efficaces
   - Offrent des fonctionnalités spécialisées

3. Choix d'utilisation :
   - Basé sur le besoin de modification
   - Dépend du contexte d'utilisation
   - Considère la lisibilité du code
   - Tient compte des performances