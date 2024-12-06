# Plan de leçon : Les fonctions lambda (anonymes)

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Fonctions lambda
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser la création et l'utilisation des fonctions lambda

- Objectifs disciplinaires :
  - Comprendre la syntaxe des lambdas
  - Savoir quand utiliser les lambdas
  - Maîtriser les cas d'utilisation courants
  - Connaître les limitations des lambdas

## Déroulement de la leçon

### 1. Introduction aux lambdas (20 min)

#### A. Syntaxe de base
```python
# Fonction lambda simple
carre = lambda x: x**2
print(carre(4))  # 16

# Comparaison avec fonction classique
def carre_classique(x):
    return x**2

# Lambda avec plusieurs arguments
somme = lambda a, b: a + b
print(somme(3, 4))  # 7

# Lambda avec condition
est_pair = lambda x: x % 2 == 0
print(est_pair(4))  # True
print(est_pair(5))  # False
```

#### B. Limitations
```python
# Une seule expression
# IMPOSSIBLE:
# lambda x: 
#     if x > 0:
#         return x
#     else:
#         return -x

# Solution avec opérateur ternaire
valeur_absolue = lambda x: x if x >= 0 else -x

# Pas de docstring possible
# Pas d'instructions multiples
# Pas de boucles directes
```

### 2. Cas d'utilisation courants (25 min)

#### A. Avec les fonctions de tri
```python
# Tri de liste avec lambda
nombres = [5, 2, 8, 1, 9]
tries = sorted(nombres, key=lambda x: x)  # Tri croissant
tries_desc = sorted(nombres, key=lambda x: -x)  # Tri décroissant

# Tri de dictionnaires
personnes = [
    {"nom": "Alice", "age": 25},
    {"nom": "Bob", "age": 20},
    {"nom": "Charlie", "age": 30}
]

# Tri par âge
tries_age = sorted(personnes, key=lambda p: p["age"])

# Tri par nom
tries_nom = sorted(personnes, key=lambda p: p["nom"])

# Tri complexe
tries_multiple = sorted(personnes, 
                      key=lambda p: (p["age"], p["nom"]))
```

#### B. Avec map, filter, reduce
```python
from functools import reduce

# Utilisation avec map
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))
print(carres)  # [1, 4, 9, 16, 25]

# Utilisation avec filter
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)  # [2, 4]

# Utilisation avec reduce
somme = reduce(lambda x, y: x + y, nombres)
print(somme)  # 15

# Combinaisons
resultat = reduce(lambda x, y: x + y,
                 filter(lambda x: x % 2 == 0,
                       map(lambda x: x**2, nombres)))
```

### 3. Applications pratiques (25 min)

#### A. Dans les fonctions de traitement de données
```python
# Transformation de données
donnees = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

# Conversion en dictionnaire
dict_donnees = list(map(
    lambda x: {"nom": x[0], "age": x[1]},
    donnees
))

# Filtrage avec conditions multiples
def filtrer_donnees(liste, **conditions):
    return list(filter(
        lambda x: all(
            getattr(x, attr) == val 
            for attr, val in conditions.items()
        ),
        liste
    ))

# Calculs avec lambda
calculs = {
    'somme': lambda x, y: x + y,
    'difference': lambda x, y: x - y,
    'produit': lambda x, y: x * y,
    'division': lambda x, y: x / y if y != 0 else None
}
```

#### B. Dans les interfaces graphiques (callbacks)
```python
import tkinter as tk

# Création de boutons avec lambdas
fenetre = tk.Tk()
bouton1 = tk.Button(
    fenetre,
    text="Cliquez",
    command=lambda: print("Bouton cliqué!")
)

# Gestionnaire d'événements
entry = tk.Entry(fenetre)
entry.bind('<Return>', 
          lambda event: print(f"Entrée: {entry.get()}"))
```

### 4. Lambda dans des fonctions de plus haut niveau (20 min)

```python
def creer_multiplicateur(n):
    """Crée une fonction qui multiplie par n."""
    return lambda x: x * n

doubler = creer_multiplicateur(2)
tripler = creer_multiplicateur(3)

print(doubler(5))  # 10
print(tripler(5))  # 15

def appliquer_operations(valeur, operations):
    """Applique une série d'opérations à une valeur."""
    return [op(valeur) for op in operations]

operations = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]

resultat = appliquer_operations(3, operations)
print(resultat)  # [4, 6, 9]

# Création de fonctions de validation
def creer_validateur(min_val, max_val):
    return lambda x: min_val <= x <= max_val

valider_age = creer_validateur(0, 150)
valider_pourcentage = creer_validateur(0, 100)
```

### 5. Bonnes pratiques et alternatives (15 min)

#### A. Quand utiliser les lambdas
```python
# BON : Lambda pour opérations simples
nombres = [1, 2, 3, 4, 5]
carres = map(lambda x: x**2, nombres)

# MAUVAIS : Lambda pour opérations complexes
# Préférer une fonction normale
def traitement_complexe(x):
    resultat = x * 2
    if resultat > 10:
        return resultat + 5
    return resultat - 3

# Au lieu de:
# lambda x: x * 2 + 5 if x * 2 > 10 else x * 2 - 3
```

#### B. Alternatives aux lambdas
```python
from operator import itemgetter, attrgetter

# Au lieu de lambda pour accéder aux dictionnaires
personnes = [{'nom': 'Alice'}, {'nom': 'Bob'}]
# Avec lambda
tries_lambda = sorted(personnes, key=lambda p: p['nom'])
# Avec itemgetter
tries_getter = sorted(personnes, key=itemgetter('nom'))

# Pour les objets
class Personne:
    def __init__(self, nom):
        self.nom = nom

personnes = [Personne('Alice'), Personne('Bob')]
# Avec attrgetter au lieu de lambda
tries = sorted(personnes, key=attrgetter('nom'))
```

### Phase de pratique (15 min)

Exercices :

1. Traitement de données :
```python
def creer_pipeline_traitement():
    """
    Créer un pipeline de traitement qui :
    - Filtre des données
    - Transforme les résultats
    - Agrège les résultats
    En utilisant des lambdas
    """
    # À compléter
```

2. Système de callbacks :
```python
def creer_gestionnaire_evenements():
    """
    Créer un système qui :
    - Enregistre des callbacks lambda
    - Les exécute selon les événements
    - Gère différents types d'événements
    """
    # À compléter
```

### Synthèse (5 min)
- Syntaxe et limitations
- Cas d'utilisation appropriés
- Alternatives aux lambdas
- Bonnes pratiques

## Points importants à retenir :

1. Syntaxe :
   - Expression unique
   - Arguments -> résultat
   - Pas de statements

2. Utilisation :
   - Fonctions simples
   - Callbacks
   - Tris et filtres

3. Bonnes pratiques :
   - Garder simple
   - Préférer les fonctions normales pour la complexité
   - Utiliser les alternatives quand approprié