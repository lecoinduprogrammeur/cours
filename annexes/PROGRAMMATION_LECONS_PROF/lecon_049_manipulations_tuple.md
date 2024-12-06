# Plan de leçon : Les tuples

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Manipulation des tuples
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des tuples

- Objectifs disciplinaires :
  - Comprendre l'immutabilité des tuples
  - Maîtriser la création et l'accès aux tuples
  - Savoir utiliser les tuples efficacement
  - Comprendre les différences avec les listes

## Déroulement de la leçon

### 1. Création de tuples (20 min)

#### A. Syntaxe de base
```python
# Tuple vide
tuple_vide1 = ()
tuple_vide2 = tuple()

# Tuple avec un élément
tuple_simple = (1,)  # La virgule est nécessaire !
pas_un_tuple = (1)  # Ceci est un int !

# Tuples simples
nombres = (1, 2, 3)
mixte = (1, "texte", 3.14, True)

# Création à partir d'autres séquences
liste_vers_tuple = tuple([1, 2, 3])
chaine_vers_tuple = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')

# Tuple packing
coordonnees = 3, 4  # Création implicite d'un tuple
```

#### B. Tuple unpacking
```python
# Unpacking basique
x, y = (1, 2)
print(x)  # 1
print(y)  # 2

# Unpacking avec *
premier, *milieu, dernier = (1, 2, 3, 4, 5)
print(premier)  # 1
print(milieu)   # [2, 3, 4]
print(dernier)  # 5

# Échange de variables
a, b = 1, 2
a, b = b, a  # Échange élégant avec tuple
```

### 2. Accès aux éléments (25 min)

#### A. Indexation
```python
# Accès par index
tuple_exemple = (10, 20, 30, 40, 50)
premier = tuple_exemple[0]     # 10
dernier = tuple_exemple[-1]    # 50

# Slicing
partie = tuple_exemple[1:4]    # (20, 30, 40)
debut = tuple_exemple[:3]      # (10, 20, 30)
fin = tuple_exemple[2:]        # (30, 40, 50)
pas = tuple_exemple[::2]       # (10, 30, 50)
inverse = tuple_exemple[::-1]  # (50, 40, 30, 20, 10)

# Vérification d'appartenance
existe = 30 in tuple_exemple   # True
```

#### B. Méthodes de tuple
```python
# Méthode index
position = tuple_exemple.index(30)  # 2

# Méthode count
occurrences = (1, 2, 2, 3, 2).count(2)  # 3

# Conversion
liste = list(tuple_exemple)    # Conversion en liste
nouveau_tuple = tuple(liste)   # Reconversion en tuple

# Longueur
longueur = len(tuple_exemple)  # 5
```

### 3. Tuples imbriqués (25 min)

```python
# Création de tuples imbriqués
matrice = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Accès aux éléments imbriqués
element = matrice[1][2]  # 6

# Unpacking de tuples imbriqués
(x1, y1), (x2, y2) = ((1, 2), (3, 4))
print(x1, y1)  # 1 2
print(x2, y2)  # 3 4

# Manipulation de tuples imbriqués
def transposer_matrice(matrice_tuple):
    """Transpose une matrice représentée par des tuples."""
    return tuple(zip(*matrice_tuple))

# Utilisation avec zip
coords = ((1, 2), (3, 4), (5, 6))
x, y = zip(*coords)  # x = (1, 3, 5), y = (2, 4, 6)
```

### 4. Applications pratiques (25 min)

#### A. Retours multiples de fonction
```python
def calculer_stats(nombres):
    """Calcule plusieurs statistiques."""
    minimum = min(nombres)
    maximum = max(nombres)
    moyenne = sum(nombres) / len(nombres)
    return minimum, maximum, moyenne  # Retourne un tuple

# Utilisation
nombres = [1, 2, 3, 4, 5]
min_val, max_val, moy = calculer_stats(nombres)

def divmod_extended(a, b):
    """Version étendue de divmod."""
    quotient = a // b
    reste = a % b
    est_divisible = reste == 0
    return quotient, reste, est_divisible
```

#### B. Structures de données légères
```python
# Point en 2D
Point = tuple[float, float]  # Type hint Python 3.9+

def distance(p1: Point, p2: Point) -> float:
    """Calcule la distance entre deux points."""
    import math
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Représentation d'enregistrements
Personne = tuple[str, int, str]  # nom, age, ville

def creer_personne(nom: str, age: int, ville: str) -> Personne:
    return nom, age, ville

def afficher_personne(personne: Personne) -> None:
    nom, age, ville = personne
    print(f"{nom}, {age} ans, habite à {ville}")
```

### 5. Tuples vs Listes (20 min)

#### A. Comparaison
```python
# Performance
import sys
liste = [1, 2, 3, 4, 5]
tuple_equiv = (1, 2, 3, 4, 5)
print(sys.getsizeof(liste))    # Plus grand
print(sys.getsizeof(tuple_equiv))  # Plus petit

# Immutabilité
liste[0] = 10  # OK
# tuple_equiv[0] = 10  # TypeError

# Utilisation comme clés de dictionnaire
dict_ok = {(1, 2): "valeur"}    # OK
# dict_erreur = {[1, 2]: "valeur"}  # TypeError
```

#### B. Cas d'utilisation appropriés
```python
# Tuples pour les données immuables
CONFIGURATION = ('localhost', 8080, False)

# Listes pour les données modifiables
utilisateurs = ['Alice', 'Bob', 'Charlie']

# Tuples pour les retours multiples
def get_dimensions():
    return 1920, 1080  # Plus clair que [1920, 1080]

# Tuples pour les clés composées
cache = {
    ('utilisateur', 123): {'nom': 'Alice'},
    ('produit', 456): {'prix': 99.99}
}
```

### 6. Bonnes pratiques (15 min)

```python
# Nommage des tuples avec namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # Plus lisible que p[0], p[1]

# Documentation des tuples
def traiter_donnees(config: tuple[str, int, bool]) -> tuple[int, str]:
    """
    Traite des données selon une configuration.
    
    Args:
        config: Tuple (host, port, debug)
    
    Returns:
        Tuple (code_statut, message)
    """
    host, port, debug = config
    # Traitement...
    return 200, "Succès"

# Validation de tuples
def valider_point(point: tuple) -> bool:
    """Valide un point 2D."""
    return (
        isinstance(point, tuple) and
        len(point) == 2 and
        all(isinstance(x, (int, float)) for x in point)
    )
```

### Phase de pratique (15 min)

Exercices :

1. Gestionnaire de coordonnées :
```python
def creer_gestionnaire_coords():
    """
    Créer un système qui :
    - Gère des points en 2D/3D
    - Calcule des distances
    - Valide les coordonnées
    """
    # À compléter
```

2. Système de configuration :
```python
def creer_systeme_config():
    """
    Créer un système qui :
    - Utilise des tuples immuables
    - Gère différents types de config
    - Valide les données
    """
    # À compléter
```

## Points importants à retenir :

1. Caractéristiques :
   - Immutable
   - Ordonné
   - Peut contenir différents types

2. Utilisation :
   - Retours multiples
   - Données immuables
   - Clés de dictionnaire

3. Avantages :
   - Performance
   - Sécurité (immutabilité)
   - Clarté du code