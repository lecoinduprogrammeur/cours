# Plan de leçon : L'indentation en Python

## Informations générales

- Date : À définir
- Classe : Débutants en programmation
- Matière : Informatique - Programmation Python
- Thème : L'indentation et la structuration du code
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'indentation en Python

- Objectifs disciplinaires :
  - Comprendre l'importance de l'indentation
  - Maîtriser les règles d'indentation
  - Savoir structurer son code correctement
  - Éviter les erreurs courantes d'indentation

## Déroulement de la leçon

### 1. Principes fondamentaux (20 min)

#### A. Définition et importance
```python
# L'indentation définit les blocs de code
# Mauvaise indentation = erreur de syntaxe

# Correct
if True:
    print("Bloc correctement indenté")
    print("Toujours dans le même bloc")
print("Hors du bloc")

# Incorrect - provoque une erreur
if True:
print("Pas d'indentation")  # IndentationError
```

#### B. Règles de base
```python
# 1. Standard PEP 8 : 4 espaces par niveau
if True:
    # Un niveau = 4 espaces
    if True:
        # Deux niveaux = 8 espaces
        print("Double indentation")

# 2. Cohérence dans tout le fichier
# Ne pas mélanger espaces et tabulations
```

### 2. Structures nécessitant l'indentation (25 min)

#### A. Conditions
```python
age = 18
if age >= 18:
    print("Majeur")
    if age < 21:
        print("Entre 18 et 21 ans")
        print("Encore dans le bloc interne")
    print("Retour au premier niveau")
print("Hors des conditions")
```

#### B. Boucles
```python
# Boucle for
for i in range(3):
    print("Niveau 1")
    for j in range(2):
        print("Niveau 2")
        print("Toujours niveau 2")
    print("Retour niveau 1")

# Boucle while
while True:
    print("Dans la boucle")
    if condition:
        break  # Aligné avec le print
```

#### C. Fonctions
```python
def ma_fonction():
    # Tout le corps de la fonction est indenté
    x = 1
    if x == 1:
        print("x est 1")
        return True
    return False

# Classes et méthodes
class MaClasse:
    def __init__(self):  # Premier niveau
        self.x = 0       # Second niveau
        
    def methode(self):   # Premier niveau
        if self.x == 0:  # Second niveau
            return True  # Troisième niveau
```

### 3. Cas particuliers et exceptions (20 min)

#### A. Lignes longues et continuations
```python
# Continuation implicite dans les parenthèses
ma_liste = [
    1, 2,
    3, 4
]  # L'indentation dans les listes est flexible

# Continuation explicite avec \
texte = "Ceci est une très longue " \
        "chaîne de caractères"  # Aligné avec les guillemets

# Opérations longues
resultat = (premier_nombre +
            deuxieme_nombre +
            troisieme_nombre)  # Aligné après l'opérateur
```

#### B. Multi-lignes avec délimiteurs
```python
# Les listes, tuples, dictionnaires peuvent être sur plusieurs lignes
liste = [
    "premier",
    "deuxième",
    "troisième"
]

dictionnaire = {
    "clé1": "valeur1",
    "clé2": "valeur2",
    "clé3": {
        "sous_clé": "valeur"  # Indentation supplémentaire pour la clarté
    }
}
```

### 4. Erreurs courantes et débogage (15 min)

#### A. Erreurs typiques
```python
# 1. Mélange d'espaces et de tabulations
if True:
    print("Espacés")
	print("Tabulé")  # Erreur!

# 2. Indentation incorrecte après les deux points
if True:
print("Erreur")  # IndentationError

# 3. Désalignement dans un bloc
if True:
    print("Ligne 1")
   print("Ligne 2")  # IndentationError (3 espaces au lieu de 4)
```

#### B. Comment déboguer
```python
# 1. Activer l'affichage des espaces dans l'éditeur

# 2. Utiliser des outils de formatage
# - autopep8
# - black
# - yapf

# 3. Vérifier visuellement l'alignement vertical
def fonction():
    if condition:
        faire_quelque_chose()
        faire_autre_chose()
    retour()  # Vérifie l'alignement avec 'if'
```

### 5. Bonnes pratiques (15 min)

#### A. Recommandations PEP 8
```python
# 1. Utiliser 4 espaces par niveau d'indentation
if True:
    print("4 espaces")
    
# 2. Limiter l'imbrication à 4 niveaux maximum
def fonction():
    if condition1:
        if condition2:
            if condition3:
                if condition4:
                    print("Trop profond!")  # Éviter
                    
# 3. Aligner les éléments de manière logique
elements = [
    1, 2,
    3, 4
    ]  # Fermeture alignée avec 'elements'
```

#### B. Organisation du code
```python
# 1. Grouper les blocs logiques
def traitement():
    # Initialisation
    x = 0
    y = 0
    
    # Traitement principal
    if x == 0:
        y = 1
    
    # Retour
    return y

# 2. Éviter les blocs trop profonds
# Au lieu de:
if a:
    if b:
        if c:
            faire()

# Préférer:
if not (a and b and c):
    return
faire()
```

### Phase de pratique (10 min)

Exercices :

1. Correction d'indentation :
```python
# Corriger l'indentation de ce code
def fonction():
if True:
print("Hello")
    print("World")
  return True
```

2. Restructuration :
```python
# Améliorer la structure de ce code
def calcul(x):
    if x > 0:
        if x < 10:
            if x % 2 == 0:
                return x * 2
            else:
                return x * 3
        else:
            return x
    else:
        return 0
```

### Synthèse (5 min)
- Importance de la cohérence
- Règles principales à retenir
- Outils de formatage disponibles

### Évaluation (5 min)
1. Pourquoi l'indentation est-elle cruciale en Python ?
2. Quelles sont les règles d'indentation principales ?
3. Comment éviter les erreurs d'indentation courantes ?

## Points importants à retenir :

1. Fondamentaux :
   - 4 espaces par niveau
   - Cohérence dans tout le fichier
   - L'indentation définit la structure

2. Règles pratiques :
   - Éviter les imbrications profondes
   - Utiliser des outils de formatage
   - Maintenir une structure claire

3. Bonnes pratiques :
   - Suivre PEP 8
   - Grouper les blocs logiques
   - Limiter la profondeur d'imbrication