# Plan de leçon : Fonctions de conversion

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Fonctions de conversion de types
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les différentes fonctions de conversion

- Objectifs disciplinaires :
  - Comprendre les conversions entre types de base
  - Maîtriser la gestion des erreurs de conversion
  - Appliquer les conversions dans des cas pratiques
  - Optimiser l'utilisation des conversions

## Déroulement de la leçon

### 1. Conversions numériques (30 min)

#### A. int() - Conversion en entier
```python
# Depuis une chaîne
nombre = int("42")     # 42
negatif = int("-42")   # -42
hex_num = int("2A", 16)  # 42 (conversion depuis hexadécimal)

# Depuis un flottant
arrondi = int(3.14)    # 3 (tronque la partie décimale)
negatif = int(-3.14)   # -3

# Gestion des erreurs
try:
    int("3.14")  # ValueError
except ValueError as e:
    print(f"Erreur: {e}")

# Avec différentes bases
binaire = int("1010", 2)   # 10
octal = int("52", 8)       # 42
hexa = int("2a", 16)       # 42
```

#### B. float() - Conversion en flottant
```python
# Depuis une chaîne
nombre = float("3.14")   # 3.14
scientifique = float("1e-3")  # 0.001

# Depuis un entier
entier = float(42)       # 42.0

# Depuis une notation scientifique
grand = float("1e10")    # 10000000000.0

# Gestion des erreurs
try:
    float("3,14")  # ValueError (utilise le point, pas la virgule)
except ValueError as e:
    print(f"Erreur: {e}")
```

### 2. Conversions en chaînes (25 min)

#### A. str() - Conversion en chaîne
```python
# Depuis des nombres
entier_str = str(42)       # "42"
float_str = str(3.14)      # "3.14"
scientifique = str(1e-3)   # "0.001"

# Depuis des conteneurs
liste_str = str([1, 2, 3])  # "[1, 2, 3]"
dict_str = str({"a": 1})    # "{'a': 1}"

# Depuis des booléens
bool_str = str(True)        # "True"

# Formatage personnalisé
nombre = 42
format_perso = f"{nombre:05d}"  # "00042"
```

#### B. repr() - Représentation formelle
```python
# Différence avec str()
texte = "Hello"
print(str(texte))   # Hello
print(repr(texte))  # 'Hello'

# Pour les objets personnalisés
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(1, 2)
print(str(p))   # "Point(1, 2)"
print(repr(p))  # "Point(x=1, y=2)"
```

### 3. Conversions de conteneurs (25 min)

#### A. list(), tuple(), set()
```python
# Conversion en liste
chaine_liste = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
tuple_liste = list((1, 2, 3))  # [1, 2, 3]
set_liste = list({1, 2, 3})    # [1, 2, 3]

# Conversion en tuple
liste_tuple = tuple([1, 2, 3])  # (1, 2, 3)
set_tuple = tuple({1, 2, 3})    # (1, 2, 3)

# Conversion en set
liste_set = set([1, 2, 2, 3])  # {1, 2, 3}
tuple_set = set((1, 2, 2, 3))  # {1, 2, 3}
chaine_set = set("hello")      # {'h', 'e', 'l', 'o'}
```

#### B. dict() - Conversion en dictionnaire
```python
# Depuis une liste de tuples
liste_dict = dict([('a', 1), ('b', 2)])  # {'a': 1, 'b': 2}

# Depuis deux listes
cles = ['a', 'b']
valeurs = [1, 2]
zip_dict = dict(zip(cles, valeurs))       # {'a': 1, 'b': 2}

# Depuis des arguments nommés
params_dict = dict(nom='Alice', age=25)   # {'nom': 'Alice', 'age': 25}
```

### 4. Conversions booléennes (20 min)

#### A. bool() - Conversion en booléen
```python
# Valeurs considérées comme False
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(None))     # False

# Valeurs considérées comme True
print(bool(42))       # True
print(bool("texte"))  # True
print(bool([1, 2]))   # True

# Utilisation dans les conditions
def est_valide(valeur):
    return bool(valeur)

# Objets personnalisés
class Validation:
    def __init__(self, valeur):
        self.valeur = valeur
    
    def __bool__(self):
        return self.valeur > 0
```

### 5. Conversions spéciales et avancées (25 min)

#### A. ord() et chr()
```python
# Conversion caractère -> code ASCII
code = ord('A')     # 65
code_euro = ord('€')  # 8364

# Conversion code ASCII -> caractère
char = chr(65)      # 'A'
euro = chr(8364)    # '€'

def analyser_texte(texte):
    """Analyse les codes ASCII d'un texte."""
    return [(char, ord(char)) for char in texte]
```

#### B. Conversions personnalisées
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

# Utilisation
temp = Temperature.from_fahrenheit(98.6)
print(temp.celsius)  # ~37.0
```

### 6. Gestion des erreurs de conversion (15 min)

```python
def conversion_securisee(valeur, type_cible):
    """Effectue une conversion sécurisée avec gestion d'erreurs."""
    convertisseurs = {
        'int': int,
        'float': float,
        'str': str,
        'bool': bool,
        'list': list,
        'tuple': tuple,
        'set': set,
        'dict': dict
    }
    
    try:
        convertisseur = convertisseurs.get(type_cible)
        if not convertisseur:
            raise ValueError(f"Type de conversion inconnu: {type_cible}")
        return convertisseur(valeur)
    except (ValueError, TypeError) as e:
        print(f"Erreur de conversion: {e}")
        return None

def parser_nombre(chaine):
    """Parse une chaîne en nombre avec gestion des formats."""
    try:
        # Essaie d'abord en entier
        return int(chaine)
    except ValueError:
        try:
            # Essaie ensuite en flottant
            return float(chaine)
        except ValueError:
            raise ValueError(f"Impossible de convertir '{chaine}' en nombre")
```

### Phase de pratique (15 min)

Exercices :

1. Convertisseur universel :
```python
def convertisseur_universel(valeur, type_source, type_cible):
    """
    Implémenter un convertisseur qui peut :
    - Détecter le type source
    - Convertir vers le type cible
    - Gérer les erreurs
    """
    # À compléter
```

2. Parseur de données :
```python
def parser_donnees(donnees_brutes):
    """
    Parser des données brutes en :
    - Nombres (int ou float selon le cas)
    - Listes
    - Dictionnaires
    Selon le format détecté
    """
    # À compléter
```

### Synthèse (5 min)
- Fonctions de conversion principales
- Gestion des erreurs
- Cas particuliers
- Bonnes pratiques

## Points importants à retenir :

1. Conversions de base :
   - int(), float() pour les nombres
   - str() pour les chaînes
   - list(), tuple(), set(), dict() pour les conteneurs

2. Gestion des erreurs :
   - Toujours prévoir les cas d'erreur
   - Utiliser try/except
   - Valider les données avant conversion

3. Bonnes pratiques :
   - Vérifier le type source
   - Documenter les conversions complexes
   - Prévoir des valeurs par défaut