# Plan de leçon : Variables booléennes (bool)

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Manipulation des variables booléennes
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des variables booléennes

- Objectifs disciplinaires :
  - Comprendre le type bool
  - Maîtriser les opérations logiques
  - Savoir utiliser les expressions booléennes
  - Gérer les conversions avec bool

## Déroulement de la leçon

### 1. Les bases du type bool (20 min)

#### A. Valeurs de base
```python
# Les deux valeurs booléennes
vrai = True
faux = False

# Vérification du type
print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>

# Comparaison
print(True == True)   # True
print(True == False)  # False
print(True != False)  # True

# Conversion en chaîne
str_true = str(True)   # "True"
str_false = str(False) # "False"
```

#### B. Opérateurs de comparaison
```python
# Égalité et différence
x = 5
y = 10
egal = x == y      # False
different = x != y # True

# Comparaisons numériques
plus_grand = x > y       # False
plus_petit = x < y      # True
plus_grand_egal = x >= y # False
plus_petit_egal = x <= y # True

# Comparaisons chaînes
texte1 = "abc"
texte2 = "def"
ordre = texte1 < texte2  # True (ordre alphabétique)
```

### 2. Opérateurs logiques (25 min)

#### A. Opérateurs de base
```python
# Opérateur AND
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Opérateur OR
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Opérateur NOT
print(not True)         # False
print(not False)        # True

# Combinaisons
resultat = (True and False) or (not False)  # True
```

#### B. Expressions complexes
```python
# Expressions composées
age = 25
majeur = age >= 18
permis = True
peut_conduire = majeur and permis

# Priorités des opérateurs
x = 5
y = 10
z = 15
resultat = x < y and y < z  # True
resultat = (x < y) and (y < z)  # Équivalent, plus lisible

# Court-circuit
def fonction():
    print("Fonction exécutée")
    return False

# Court-circuit avec and
resultat = False and fonction()  # fonction n'est pas appelée
# Court-circuit avec or
resultat = True or fonction()    # fonction n'est pas appelée
```

### 3. Conversion en bool (20 min)

#### A. Valeurs considérées comme False
```python
# Valeurs "falsy"
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(""))        # False
print(bool([]))        # False
print(bool(()))        # False
print(bool({}))        # False
print(bool(None))      # False
print(bool(set()))     # False

# Utilisation pratique
liste = []
if not liste:
    print("Liste vide")
```

#### B. Valeurs considérées comme True
```python
# Valeurs "truthy"
print(bool(1))         # True
print(bool(-1))        # True
print(bool(0.1))       # True
print(bool("texte"))   # True
print(bool([1, 2]))    # True
print(bool((1,)))      # True
print(bool({'a': 1}))  # True
print(bool({1, 2}))    # True

# Utilisation pratique
texte = "Hello"
if texte:
    print("Texte non vide")
```

### 4. Applications pratiques (20 min)

#### A. Validation de données
```python
def valider_utilisateur(age, email, mot_de_passe):
    """Valide les données d'un utilisateur."""
    age_valide = 13 <= age <= 120
    email_valide = "@" in email and "." in email
    mdp_valide = len(mot_de_passe) >= 8
    
    return age_valide and email_valide and mdp_valide

def verifier_access(utilisateur):
    """Vérifie les droits d'accès."""
    est_admin = utilisateur.get('role') == 'admin'
    est_actif = utilisateur.get('actif', False)
    est_verifie = utilisateur.get('verifie', False)
    
    return est_admin and est_actif and est_verifie
```

#### B. Contrôle de flux
```python
def traiter_donnees(donnees):
    """Traite des données avec validation."""
    if not donnees:
        return "Aucune donnée"
        
    est_valide = all(isinstance(x, (int, float)) for x in donnees)
    if not est_valide:
        return "Données invalides"
        
    sont_positifs = all(x > 0 for x in donnees)
    return "OK" if sont_positifs else "Valeurs négatives"

def verifier_conditions(*conditions):
    """Vérifie une série de conditions."""
    return all(conditions)
```

### 5. Bonnes pratiques (15 min)

```python
# Comparaison explicite
def mauvais_style(valeur):
    if valeur == True:  # Ne pas faire
        return True

def bon_style(valeur):
    if valeur:  # Meilleur
        return True

# Simplification d'expressions
def simplifier_conditions(a, b, c):
    # Au lieu de
    if a == True and b == True and c == True:
        return True
    
    # Préférer
    return all([a, b, c])

# Nommage explicite
est_valide = True  # Bon nom pour un booléen
peut_modifier = False  # Bon nom pour un booléen
```

### Phase de pratique (15 min)

Exercices :

1. Système de validation :
```python
def creer_validateur():
    """
    Créer un système qui :
    - Valide plusieurs conditions
    - Combine les résultats
    - Retourne un rapport détaillé
    """
    # À compléter
```

2. Contrôle d'accès :
```python
def creer_controleur_acces():
    """
    Créer un système qui :
    - Vérifie les permissions
    - Combine plusieurs conditions
    - Gère différents niveaux d'accès
    """
    # À compléter
```

### Synthèse (5 min)
- Valeurs booléennes de base
- Opérations logiques
- Conversions
- Bonnes pratiques

## Points importants à retenir :

1. Fondamentaux :
   - True et False
   - Opérateurs logiques
   - Conversions implicites

2. Opérations :
   - and, or, not
   - Comparaisons
   - Court-circuit

3. Bonnes pratiques :
   - Nommage explicite
   - Simplification des expressions
   - Tests appropriés