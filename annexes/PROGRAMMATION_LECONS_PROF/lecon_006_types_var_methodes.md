# Plan de leçon : Types de données en Python et leurs méthodes

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Types de données et méthodes associées
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les différents types de données en Python

- Objectifs disciplinaires :
  - Connaître tous les types de données de base
  - Comprendre les méthodes associées à chaque type
  - Savoir convertir entre les différents types
  - Maîtriser les opérations de base sur chaque type

- Objectifs transversaux :
  - Développer la logique de programmation
  - Comprendre la manipulation de données
  - Acquérir les bonnes pratiques d'utilisation

## Prérequis
- Notions de base en Python
- Connaissance des variables
- Compréhension des opérateurs de base

## Matériel et ressources
- Ordinateurs avec Python installé
- Documentation Python
- Exemples de code
- Exercices pratiques

## Déroulement de la leçon

### 1. Types Numériques (25 min)

#### A. Entiers (int)
```python
# Création et opérations de base
x = 42
y = -17
grand_nombre = 1_000_000  # Notation avec underscore pour lisibilité

# Méthodes et fonctions utiles
abs(-42)      # Valeur absolue : 42
pow(2, 3)     # Puissance : 8
divmod(10, 3) # Division et modulo : (3, 1)

# Conversion
int("42")     # Depuis string : 42
int(3.14)     # Depuis float : 3
```

#### B. Nombres à virgule flottante (float)
```python
# Création
x = 3.14
y = 2.0
z = 1e-3      # Notation scientifique

# Méthodes utiles
x.is_integer()  # Vérifie si c'est un entier
round(3.14159, 2)  # Arrondi : 3.14

# Conversion
float("3.14")  # Depuis string
float(42)      # Depuis int
```

#### C. Nombres complexes (complex)
```python
# Création
z = 3 + 4j
w = complex(3, 4)

# Attributs et méthodes
z.real        # Partie réelle : 3.0
z.imag        # Partie imaginaire : 4.0
abs(z)        # Module : 5.0
z.conjugate() # Conjugué : 3 - 4j
```

### 2. Séquences (35 min)

#### A. Chaînes de caractères (str)
```python
# Création
texte = "Hello, World!"
multi_ligne = """Ligne 1
Ligne 2"""

# Méthodes principales
texte.upper()      # Majuscules : "HELLO, WORLD!"
texte.lower()      # Minuscules : "hello, world!"
texte.strip()      # Supprime espaces : "Hello, World!"
texte.split(",")   # Découpage : ["Hello", " World!"]
",".join(["a", "b"])  # Jointure : "a,b"

# Formatage
f"Valeur: {42}"    # f-string
"Valeur: {}".format(42)
"Valeur: %d" % 42

# Accès et slicing
texte[0]      # Premier caractère : "H"
texte[-1]     # Dernier caractère : "!"
texte[1:5]    # Sous-chaîne : "ello"
```

#### B. Listes (list)
```python
# Création
liste = [1, 2, 3]
liste2 = list("abc")  # Depuis itérable

# Méthodes principales
liste.append(4)    # Ajoute à la fin
liste.insert(0, 0) # Insère au début
liste.pop()        # Retire et retourne le dernier élément
liste.remove(2)    # Retire la première occurrence de 2
liste.sort()       # Trie la liste
liste.reverse()    # Inverse la liste

# Slicing
liste[1:3]        # Sous-liste
liste[::-1]       # Liste inversée
```

#### C. Tuples (tuple)
```python
# Création
tuple_simple = (1, 2, 3)
tuple_un_element = (1,)  # Virgule nécessaire
tuple2 = tuple([1, 2, 3])  # Depuis itérable

# Méthodes
tuple_simple.count(1)  # Compte les occurrences
tuple_simple.index(2)  # Trouve l'index

# Unpacking
x, y, z = tuple_simple
```

### 3. Collections (25 min)

#### A. Dictionnaires (dict)
```python
# Création
dico = {"clé": "valeur", "nombre": 42}
dico2 = dict(a=1, b=2)

# Méthodes principales
dico.keys()       # Liste des clés
dico.values()     # Liste des valeurs
dico.items()      # Liste des paires (clé, valeur)
dico.get("clé", "défaut")  # Valeur avec défaut
dico.update({"nouvelle_clé": "valeur"})  # Mise à jour
```

#### B. Ensembles (set)
```python
# Création
ensemble = {1, 2, 3}
ensemble2 = set([1, 2, 2, 3])  # Doublons éliminés

# Méthodes principales
ensemble.add(4)        # Ajoute un élément
ensemble.remove(1)     # Retire un élément
ensemble.discard(5)    # Retire si présent
ensemble.union(ensemble2)        # Union
ensemble.intersection(ensemble2)  # Intersection
ensemble.difference(ensemble2)    # Différence
```

### 4. Types Booléens et None (15 min)

#### A. Booléens (bool)
```python
# Création
vrai = True
faux = False
bool(1)      # Conversion : True
bool("")     # Conversion : False

# Opérations
not True     # False
True and False  # False
True or False   # True
```

#### B. None
```python
# Utilisation
valeur = None
valeur is None  # Test d'identité
valeur == None  # Déconseillé
```

### 5. Conversions entre types (10 min)

```python
# Conversions courantes
str(42)       # Entier vers string
int("42")     # String vers entier
list("abc")   # String vers liste
tuple([1,2])  # Liste vers tuple
set([1,2,2])  # Liste vers ensemble
dict([("a",1),("b",2)])  # Liste de tuples vers dictionnaire
```

### Phase de pratique (15 min)

Exercices :

1. Manipulation de strings :
```python
# Créer une fonction qui inverse les mots d'une phrase
```

2. Opérations sur listes :
```python
# Créer une fonction qui élimine les doublons tout en gardant l'ordre
```

3. Utilisation de dictionnaires :
```python
# Créer un mini-système de comptage de mots
```

### Synthèse et récapitulation (5 min)
- Types mutables vs immutables
- Choix du type selon le besoin
- Méthodes essentielles à retenir

### Évaluation formative (5 min)
1. Quels types sont mutables/immutables ?
2. Comment convertir efficacement entre types ?
3. Quelles méthodes sont les plus utilisées ?

## Devoirs et prolongements

Devoirs :
1. Créer des fonctions utilisant différents types
2. Expérimenter avec les conversions
3. Implémenter un mini-projet utilisant tous les types

Prolongements :
- Collections spécialisées (deque, Counter, etc.)
- Types personnalisés avec classes
- Gestion d'erreurs lors des conversions

## Points importants à retenir :

1. Types de base :
   - Numériques : int, float, complex
   - Séquences : str, list, tuple
   - Collections : dict, set
   - Autres : bool, None

2. Caractéristiques :
   - Mutables : list, dict, set
   - Immutables : int, float, complex, str, tuple, bool

3. Opérations communes :
   - Conversion entre types
   - Méthodes de manipulation
   - Tests et comparaisons