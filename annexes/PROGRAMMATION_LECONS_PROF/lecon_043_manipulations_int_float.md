# Plan de leçon : Variables numériques (int et float)

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Manipulation des variables numériques
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des variables numériques

- Objectifs disciplinaires :
  - Comprendre la différence entre int et float
  - Maîtriser les opérations numériques
  - Savoir convertir entre types numériques
  - Gérer les cas particuliers

## Déroulement de la leçon

### 1. Types numériques de base (20 min)

#### A. Entiers (int)
```python
# Déclaration d'entiers
a = 42
b = -17
c = 1_000_000  # Notation avec underscore pour lisibilité

# Vérification du type
print(type(a))  # <class 'int'>

# Limites des entiers
import sys
max_int = sys.maxsize
print(f"Plus grand entier: {max_int}")
# Python 3 n'a pas de limite réelle pour les entiers

# Bases numériques
binaire = 0b1010  # Base 2 (10 en décimal)
octal = 0o12     # Base 8 (10 en décimal)
hexa = 0x0A      # Base 16 (10 en décimal)
```

#### B. Nombres à virgule flottante (float)
```python
# Déclaration de flottants
x = 3.14
y = -0.001
z = 2.0

# Notation scientifique
grand = 1e6      # 1 million
petit = 1e-6     # 0.000001

# Vérification du type
print(type(x))  # <class 'float'>

# Précision et limites
import sys
print(sys.float_info.max)  # Plus grand float
print(sys.float_info.min)  # Plus petit float non nul

# Cas spéciaux
inf = float('inf')  # Infini
nan = float('nan')  # Not a Number
```

### 2. Opérations arithmétiques (25 min)

#### A. Opérations de base
```python
# Addition
somme = 5 + 3        # 8
somme_float = 5.0 + 3  # 8.0

# Soustraction
difference = 10 - 4   # 6
diff_neg = 4 - 10    # -6

# Multiplication
produit = 6 * 7      # 42
prod_float = 6 * 7.0  # 42.0

# Division
division = 15 / 3    # 5.0 (toujours un float)
div_float = 10 / 3   # 3.3333...

# Division entière
div_entiere = 15 // 3  # 5
div_ent_neg = -15 // 4  # -4 (arrondi vers -∞)

# Modulo (reste)
reste = 17 % 5       # 2
reste_neg = -17 % 5  # 3

# Puissance
puissance = 2 ** 3   # 8
puis_float = 2 ** 0.5  # 1.4142...
```

#### B. Opérations combinées
```python
# Priorité des opérations
resultat = 2 + 3 * 4    # 14 (multiplication avant addition)
avec_parent = (2 + 3) * 4  # 20

# Opérations multiples
calcul = 2 + 3 * 4 / 2 - 1  # 7.0

# Opérations avec assignation
x = 5
x += 3   # x = x + 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4
x //= 2  # x = x // 2
x %= 3   # x = x % 3
x **= 2  # x = x ** 2
```

### 3. Conversions entre types (20 min)

```python
# Int vers float
x = float(42)      # 42.0
y = float(-17)     # -17.0

# Float vers int
a = int(3.14)      # 3 (troncature)
b = int(-3.14)     # -3 (troncature)
c = int(3.9)       # 3 (pas d'arrondi)

# Arrondis
import math
arrondi = round(3.7)    # 4
plancher = math.floor(3.7)  # 3
plafond = math.ceil(3.7)    # 4

# Conversions chaîne vers nombre
str_int = int("42")     # 42
str_float = float("3.14")  # 3.14
str_sci = float("1e-3")   # 0.001

# Gérer les erreurs de conversion
try:
    nombre = float("abc")
except ValueError as e:
    print(f"Erreur de conversion: {e}")
```

### 4. Fonctions mathématiques (25 min)

```python
import math

# Fonctions de base
absolu = abs(-5)             # 5
maximum = max(2, 3, 4)       # 4
minimum = min(2, 3, 4)       # 2

# Fonctions trigonométriques
sin = math.sin(math.pi/2)    # 1.0
cos = math.cos(math.pi)      # -1.0
tan = math.tan(math.pi/4)    # 1.0

# Fonctions exponentielles et logarithmes
exp = math.exp(1)            # e
log = math.log(10)           # ln(10)
log10 = math.log10(100)      # 2.0

# Racines et puissances
racine = math.sqrt(16)       # 4.0
puis = math.pow(2, 3)        # 8.0

# Constantes mathématiques
pi = math.pi                 # 3.141592...
e = math.e                   # 2.718281...

# Fonctions de manipulation de nombres
trunc = math.trunc(3.7)      # 3
floor = math.floor(3.7)      # 3
ceil = math.ceil(3.7)        # 4
```

### 5. Cas pratiques (25 min)

#### A. Calculs financiers
```python
def calculer_interet_compose(principal, taux, annees):
    """Calcule l'intérêt composé."""
    return principal * (1 + taux) ** annees

def arrondir_monnaie(montant):
    """Arrondit à 2 décimales."""
    return round(montant, 2)

# Exemple d'utilisation
principal = 1000
taux = 0.05  # 5%
annees = 5

montant_final = calculer_interet_compose(principal, taux, annees)
montant_arrondi = arrondir_monnaie(montant_final)
print(f"Montant final: {montant_arrondi}€")
```

#### B. Calculs scientifiques
```python
def calculer_distance(x1, y1, x2, y2):
    """Calcule la distance euclidienne entre deux points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def convertir_celsius_fahrenheit(celsius):
    """Convertit Celsius en Fahrenheit."""
    return celsius * 9/5 + 32

# Exemples d'utilisation
distance = calculer_distance(0, 0, 3, 4)
temperature_f = convertir_celsius_fahrenheit(20)
```

### 6. Tests et validation (15 min)

```python
def est_presque_egal(a, b, tolerance=1e-9):
    """Compare deux flottants avec tolérance."""
    return abs(a - b) < tolerance

def valider_nombre(valeur):
    """Valide une entrée numérique."""
    if isinstance(valeur, (int, float)):
        if math.isnan(float(valeur)):
            return False
        if math.isinf(float(valeur)):
            return False
        return True
    return False

# Tests
assert est_presque_egal(0.1 + 0.2, 0.3)
assert valider_nombre(42)
assert valider_nombre(3.14)
assert not valider_nombre(float('inf'))
```

### Phase de pratique (15 min)

Exercices :

1. Calculateur scientifique :
```python
def creer_calculateur():
    """
    Créer une calculatrice qui :
    - Gère les opérations de base
    - Inclut des fonctions scientifiques
    - Valide les entrées
    """
    # À compléter
```

2. Gestionnaire financier :
```python
def creer_gestionnaire_financier():
    """
    Créer un gestionnaire qui :
    - Calcule les intérêts
    - Gère les arrondis monétaires
    - Valide les montants
    """
    # À compléter
```

## Points importants à retenir :

1. Types numériques :
   - int pour les entiers
   - float pour les décimaux
   - Conversion entre types

2. Opérations :
   - Opérateurs de base
   - Fonctions mathématiques
   - Précision et limites

3. Bonnes pratiques :
   - Validation des entrées
   - Gestion des erreurs
   - Tests appropriés