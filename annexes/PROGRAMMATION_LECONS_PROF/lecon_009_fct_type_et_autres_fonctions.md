# Plan de leçon : Fonction type() et fonctions intégrées Python

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Fonctions intégrées (Built-in functions)
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser la fonction type() et les principales fonctions intégrées

- Objectifs disciplinaires :
  - Comprendre l'utilisation de type()
  - Connaître les fonctions intégrées essentielles
  - Savoir quand utiliser chaque fonction
  - Maîtriser les conversions de types

## Déroulement de la leçon

### 1. La fonction type() (20 min)

#### A. Utilisation basique
```python
# Vérification du type d'une variable
x = 42
print(type(x))        # <class 'int'>
y = "Hello"
print(type(y))        # <class 'str'>
z = [1, 2, 3]
print(type(z))        # <class 'list'>

# Comparaison de types
type(x) is int        # True
type(y) is str        # True
isinstance(x, int)    # True (méthode préférée)
```

#### B. Cas d'utilisation avancés
```python
# Vérification dynamique de types
def traiter_donnee(x):
    if type(x) is str:
        return len(x)
    elif type(x) is int:
        return x * 2
    else:
        raise TypeError("Type non supporté")

# Création de types dynamiques
MonType = type('MonType', (), {'attribut': 42})
instance = MonType()
print(type(instance))  # <class '__main__.MonType'>
```

### 2. Fonctions de conversion de types (20 min)

```python
# Conversion en entier
int("42")          # 42
int(3.14)          # 3
int("2A", 16)      # 42 (base 16)

# Conversion en flottant
float("3.14")      # 3.14
float("1e-3")      # 0.001

# Conversion en chaîne
str(42)            # "42"
str([1, 2, 3])     # "[1, 2, 3]"

# Conversion en booléen
bool(0)            # False
bool([])           # False
bool("False")      # True (chaîne non vide)

# Conversion en liste, tuple, set
list("abc")        # ['a', 'b', 'c']
tuple([1, 2, 3])   # (1, 2, 3)
set([1, 2, 2, 3])  # {1, 2, 3}
```

### 3. Fonctions mathématiques intégrées (15 min)

```python
# Valeur absolue
abs(-42)           # 42
abs(3.14)          # 3.14

# Arrondis
round(3.14159, 2)  # 3.14
round(3.5)         # 4
round(4.5)         # 4 (arrondi aux pairs)

# Min et Max
min(1, 2, 3)       # 1
max([4, 5, 6])     # 6

# Somme
sum([1, 2, 3])     # 6
sum([[1], [2]], [])  # [1, 2] (avec valeur initiale)

# Puissance
pow(2, 3)          # 8
pow(2, 3, 5)       # 3 (2³ modulo 5)
```

### 4. Fonctions de séquence (20 min)

```python
# Longueur
len("Python")      # 6
len([1, 2, 3])     # 3

# Énumération
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)  # 0 a, 1 b, 2 c

# Tri
sorted([3, 1, 2])  # [1, 2, 3]
sorted("bac")      # ['a', 'b', 'c']

# Inversion
reversed([1, 2, 3])  # itérateur inversé

# Zip
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# Range
list(range(5))     # [0, 1, 2, 3, 4]
list(range(1, 6, 2))  # [1, 3, 5]
```

### 5. Fonctions d'itération (20 min)

```python
# Map
list(map(str, [1, 2, 3]))  # ['1', '2', '3']
list(map(len, ['a', 'ab', 'abc']))  # [1, 2, 3]

# Filter
list(filter(bool, [0, 1, '', 'a']))  # [1, 'a']
list(filter(lambda x: x > 0, [-1, 0, 1, 2]))  # [1, 2]

# Reduce (de functools)
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3])  # 6

# Any et All
any([True, False, False])  # True
all([True, True, False])   # False
```

### 6. Fonctions d'entrée/sortie (15 min)

```python
# Affichage
print("Hello", "World", sep=", ")
print("Pas de retour", end="")

# Entrée utilisateur
nom = input("Votre nom : ")

# Représentation
repr("Hello")      # "'Hello'"

# Format
format(3.14159, '.2f')  # '3.14'
```

### 7. Fonctions d'aide et d'information (10 min)

```python
# Aide
help(len)          # Affiche la documentation
dir([])           # Liste les méthodes disponibles

# Variables globales
globals()         # Dictionnaire des variables globales
locals()          # Dictionnaire des variables locales

# Identifiant
id(42)            # Identifiant unique de l'objet

# Hash
hash("hello")     # Valeur de hachage
```

### Tableau récapitulatif des fonctions intégrées principales

| Catégorie  | Fonctions                                                    | Description               |
| ---------- | ------------------------------------------------------------ | ------------------------- |
| Types      | type(), isinstance()                                         | Vérification de types     |
| Conversion | int(), float(), str(), bool(), list(), tuple(), set(), dict() | Conversion entre types    |
| Math       | abs(), round(), min(), max(), sum(), pow()                   | Opérations mathématiques  |
| Séquences  | len(), enumerate(), sorted(), reversed(), zip(), range()     | Manipulation de séquences |
| Itération  | map(), filter(), any(), all()                                | Opérations sur itérables  |
| E/S        | print(), input(), repr(), format()                           | Entrées/Sorties           |
| Système    | help(), dir(), globals(), locals(), id()                     | Information système       |

### Phase de pratique (15 min)

Exercices :

1. Manipulation de types :
```python
def verifier_et_convertir(valeur):
    """
    Vérifie le type de la valeur et la convertit si nécessaire
    en entier ou flottant
    """
    # À compléter
```

2. Utilisation de fonctions d'itération :
```python
def filtrer_et_transformer(liste):
    """
    Filtre les nombres positifs et les double
    """
    # À compléter
```

### Synthèse (5 min)
- Importance de la vérification des types
- Choix des bonnes fonctions selon le contexte
- Bonnes pratiques d'utilisation

### Évaluation (5 min)
1. Quelle est la différence entre type() et isinstance() ?
2. Comment convertir efficacement une liste de nombres en chaînes ?
3. Quand utiliser map() vs. une compréhension de liste ?

## Points importants à retenir :

1. La fonction type() :
   - Retourne le type d'un objet
   - Utile pour le débogage
   - Préférer isinstance() pour les vérifications de type

2. Conversion de types :
   - Toujours vérifier la possibilité de conversion
   - Gérer les exceptions possibles
   - Choisir la méthode appropriée

3. Fonctions d'itération :
   - Préférer les compréhensions pour les cas simples
   - Utiliser map()/filter() pour les opérations complexes
   - Penser à la lisibilité du code