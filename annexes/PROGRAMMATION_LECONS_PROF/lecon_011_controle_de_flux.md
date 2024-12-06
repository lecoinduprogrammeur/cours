# Plan de leçon : Contrôle de flux - Conditions et blocs d'instructions

## Informations générales

- Date : À définir
- Classe : Débutants en programmation
- Matière : Informatique - Programmation Python
- Thème : Structures de contrôle et conditions
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les structures de contrôle en Python

- Objectifs disciplinaires :
  - Comprendre la syntaxe des conditions
  - Maîtriser l'indentation et les blocs
  - Utiliser les opérateurs de comparaison
  - Implémenter des conditions complexes

## Déroulement de la leçon

### 1. Structure conditionnelle simple (if) (20 min)

#### A. Syntaxe de base
```python
# Structure if simple
age = 18
if age >= 18:
    print("Majeur")
    print("Peut voter")  # Même bloc car même indentation

print("Hors du bloc if")  # Exécuté dans tous les cas

# Indentation : 4 espaces ou 1 tabulation
if age > 0:
    print("Âge valide")  # Indentation correcte
```

#### B. Opérateurs de comparaison
```python
# Opérateurs disponibles
x = 5
y = 10

if x == y:    # Égalité
    print("Égaux")
if x != y:    # Différence
    print("Différents")
if x < y:     # Inférieur
    print("x plus petit")
if x <= y:    # Inférieur ou égal
    print("x plus petit ou égal")
if x > y:     # Supérieur
    print("x plus grand")
if x >= y:    # Supérieur ou égal
    print("x plus grand ou égal")
```

### 2. Structure if-else (20 min)

#### A. Syntaxe if-else
```python
age = 15

if age >= 18:
    print("Majeur")
    print("Peut voter")
else:
    print("Mineur")
    print("Ne peut pas voter")

# Version compacte (ternaire)
statut = "Majeur" if age >= 18 else "Mineur"
```

#### B. Structure if-elif-else
```python
note = 75

if note >= 90:
    print("Excellent")
elif note >= 80:
    print("Très bien")
elif note >= 70:
    print("Bien")
elif note >= 60:
    print("Passable")
else:
    print("À améliorer")
```

### 3. Conditions composées (25 min)

#### A. Opérateurs logiques
```python
age = 25
permis = True

# Opérateur and
if age >= 18 and permis:
    print("Peut conduire")

# Opérateur or
if age < 5 or age > 65:
    print("Tarif réduit")

# Opérateur not
if not permis:
    print("Doit passer le permis")

# Combinaisons complexes
if (age >= 18 and permis) or (age >= 16 and permis_accompagne):
    print("Peut conduire sous conditions")
```

#### B. Conditions imbriquées
```python
age = 20
etudiant = True
revenu = 15000

if age >= 18:
    if etudiant:
        if revenu < 20000:
            print("Éligible à l'aide")
        else:
            print("Revenu trop élevé")
    else:
        print("Non étudiant")
else:
    print("Trop jeune")

# Version améliorée (éviter trop d'imbrication)
if age >= 18 and etudiant and revenu < 20000:
    print("Éligible à l'aide")
```

### 4. Tests de valeurs spéciales (20 min)

#### A. Test de None
```python
valeur = None

# Bonne pratique
if valeur is None:
    print("Valeur non définie")

# Mauvaise pratique
if valeur == None:
    print("Ne pas utiliser ==")
```

#### B. Tests de vérité
```python
# Valeurs considérées comme False
if not '':          # Chaîne vide
    print("Chaîne vide")
if not []:          # Liste vide
    print("Liste vide")
if not 0:           # Zéro
    print("Zéro")
if not None:        # None
    print("None")

# Tests d'existence
liste = [1, 2, 3]
if liste:           # Liste non vide
    print("Liste contient des éléments")

# Test d'appartenance
if 2 in liste:
    print("2 est dans la liste")
```

### 5. Bonnes pratiques et pièges courants (20 min)

#### A. Indentation et lisibilité
```python
# Bon : alignement clair
if condition1:
    instruction1()
    instruction2()
elif condition2:
    instruction3()
else:
    instruction4()

# Mauvais : indentation inconsistante
if condition1:
  instruction1()
    instruction2()  # Indentation incorrecte
```

#### B. Simplification des conditions
```python
# À éviter
if bool(x) == True:
    print("x est vrai")

# Préférer
if x:
    print("x est vrai")

# À éviter
if len(liste) != 0:
    print("Liste non vide")

# Préférer
if liste:
    print("Liste non vide")
```

### Phase de pratique (10 min)

Exercices :

1. Structure simple :
```python
def verifier_age(age):
    """
    Vérifier si une personne est majeure
    et retourner un message approprié
    """
    # À compléter
```

2. Conditions composées :
```python
def eligibilite_pret(age, salaire, historique_credit):
    """
    Déterminer si une personne est éligible à un prêt
    selon plusieurs critères
    """
    # À compléter
```

### Synthèse (5 min)
- Importance de l'indentation
- Choix des bonnes structures
- Simplification des conditions

### Évaluation (5 min)
1. Quelle est la différence entre == et is ?
2. Comment simplifier des conditions imbriquées ?
3. Quand utiliser elif vs conditions imbriquées ?

## Points importants à retenir :

1. Structure des conditions :
   - if, elif, else
   - Indentation obligatoire
   - Blocs d'instructions

2. Opérateurs :
   - Comparaison (==, !=, <, >, <=, >=)
   - Logiques (and, or, not)
   - Appartenance (in)

3. Bonnes pratiques :
   - Indentation cohérente
   - Conditions simplifiées
   - Éviter l'imbrication excessive

4. Pièges à éviter :
   - Confusion entre == et is
   - Indentation incorrecte
   - Conditions trop complexes