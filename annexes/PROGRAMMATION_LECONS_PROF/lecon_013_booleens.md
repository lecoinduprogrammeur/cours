# Plan de leçon : Les booléens (True et False) en Python

## Informations générales

- Date : À définir
- Classe : Débutants en programmation
- Matière : Informatique - Programmation Python
- Thème : Les booléens et l'algèbre booléenne
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des booléens en Python

- Objectifs disciplinaires :
  - Comprendre les valeurs booléennes
  - Maîtriser les opérations logiques
  - Savoir évaluer les expressions booléennes
  - Utiliser les booléens dans les conditions

## Déroulement de la leçon

### 1. Introduction aux booléens (15 min)

#### A. Définition et valeurs
```python
# Les deux valeurs booléennes
vrai = True
faux = False

# Type booléen
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>

# Création de booléens
x = bool(1)    # True
y = bool(0)    # False
z = bool("")   # False
```

#### B. Comparaisons retournant des booléens
```python
# Opérateurs de comparaison
x = 5
y = 10

egal = x == y       # False
different = x != y  # True
plus_petit = x < y  # True
plus_grand = x > y  # False
petit_egal = x <= y # True
grand_egal = x >= y # False
```

### 2. Opérations logiques (20 min)

#### A. Opérateurs de base
```python
# AND (et)
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# OR (ou)
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# NOT (non)
print(not True)         # False
print(not False)        # True
```

#### B. Combinaisons complexes
```python
# Combinaisons d'opérateurs
a = True
b = False
c = True

resultat = (a and b) or (not b and c)  # True
print(not (a and b))    # True

# Priorité des opérateurs
# not > and > or
resultat = a or b and c  # Équivalent à: a or (b and c)
```

### 3. Évaluation booléenne des objets Python (25 min)

#### A. Valeurs considérées comme False
```python
# Valeurs "falsy"
print(bool(0))          # False (entier nul)
print(bool(0.0))        # False (flottant nul)
print(bool(""))         # False (chaîne vide)
print(bool([]))         # False (liste vide)
print(bool(()))         # False (tuple vide)
print(bool({}))         # False (dictionnaire vide)
print(bool(set()))      # False (ensemble vide)
print(bool(None))       # False (None)

# Dans les conditions
liste = []
if liste:
    print("Liste non vide")
else:
    print("Liste vide")
```

#### B. Valeurs considérées comme True
```python
# Valeurs "truthy"
print(bool(1))          # True (entiers non nuls)
print(bool(-1))         # True
print(bool(0.1))        # True (flottants non nuls)
print(bool("texte"))    # True (chaînes non vides)
print(bool([1, 2]))     # True (collections non vides)
print(bool({"a": 1}))   # True

# Utilisation pratique
texte = "Hello"
if texte:
    print("Texte non vide")
```

### 4. Applications pratiques (20 min)

#### A. Dans les conditions
```python
age = 18
permis = True

# Vérifications simples
if age >= 18 and permis:
    print("Peut conduire")

# Conditions multiples
est_etudiant = True
reduction = age < 25 and est_etudiant

# Simplification de conditions
# Au lieu de
if bool(age >= 18) == True:  # Redondant
    print("Majeur")

# Préférer
if age >= 18:
    print("Majeur")
```

#### B. Dans les fonctions
```python
def est_majeur(age):
    """Vérifie si une personne est majeure."""
    return age >= 18

def peut_voter(age, nationalite):
    """
    Vérifie si une personne peut voter.
    Retourne un booléen.
    """
    return est_majeur(age) and nationalite == "Française"

# Utilisation
age = 20
nationalite = "Française"
if peut_voter(age, nationalite):
    print("Peut voter")
```

### 5. Pièges et bonnes pratiques (15 min)

#### A. Pièges courants
```python
# Comparaison avec True/False
x = 5

# À éviter
if x == True:    # Incorrect
    print("x est vrai")

# Préférer
if x:            # Correct
    print("x est vrai")

# Comparaison avec None
variable = None

# Correct
if variable is None:
    print("Variable est None")

# Incorrect
if variable == None:
    print("Ne pas utiliser ==")
```

#### B. Bonnes pratiques
```python
# Expressions explicites
def est_valide(nombre):
    return 0 <= nombre <= 100

# Utilisation de fonctions booléennes
def a_age_legal(age):
    return age >= 18

# Nommage clair
est_actif = True
a_paye = False
peut_acceder = age >= 18 and est_abonne

# Simplification d'expressions
# Au lieu de
if len(liste) > 0:
    print("Liste non vide")

# Préférer
if liste:
    print("Liste non vide")
```

### Phase de pratique (10 min)

Exercices :

1. Évaluation d'expressions :
```python
# Prédire le résultat de ces expressions
resultat1 = True and (False or True)
resultat2 = not (True and True)
resultat3 = bool([]) or bool("texte")
```

2. Création de fonction :
```python
def peut_emprunter(age, revenu, historique_credit):
    """
    Déterminer si une personne peut emprunter
    selon plusieurs critères
    """
    # À compléter
```

### Synthèse (5 min)
- Valeurs True et False
- Opérations logiques fondamentales
- Évaluation booléenne des objets
- Bonnes pratiques d'utilisation

### Évaluation (5 min)
1. Quelles sont les principales valeurs considérées comme False ?
2. Comment simplifier une expression booléenne ?
3. Quelle est la différence entre == et is avec les booléens ?

## Points importants à retenir :

1. Fondamentaux :
   - True et False sont des mots-clés
   - bool est un type de données
   - Opérateurs logiques : and, or, not

2. Évaluation :
   - Valeurs "falsy" : 0, "", [], {}, None
   - Valeurs "truthy" : tout le reste
   - Priorité des opérateurs

3. Bonnes pratiques :
   - Expressions explicites
   - Simplification des conditions
   - Nommage clair des variables booléennes