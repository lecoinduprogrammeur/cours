# Plan de leçon : Indices et valeurs dans les chaînes de caractères

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Manipulation des indices et valeurs dans les chaînes
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'accès et la manipulation des caractères dans une chaîne

- Objectifs disciplinaires :
  - Comprendre l'indexation en Python
  - Maîtriser le slicing (découpage)
  - Utiliser les indices négatifs
  - Manipuler les caractères et sous-chaînes

## Déroulement de la leçon

### 1. Indices de base (20 min)

#### A. Indexation positive
```python
# Les indices commencent à 0
texte = "Python"
print(texte[0])    # 'P'
print(texte[1])    # 'y'
print(texte[5])    # 'n'

# Accès aux caractères
for i in range(len(texte)):
    print(f"Indice {i}: {texte[i]}")

# Erreur d'indice
try:
    print(texte[6])  # IndexError: string index out of range
except IndexError as e:
    print(f"Erreur: {e}")
```

#### B. Indexation négative
```python
# Les indices négatifs commencent à -1
texte = "Python"
print(texte[-1])   # 'n' (dernier caractère)
print(texte[-2])   # 'o' (avant-dernier)
print(texte[-6])   # 'P' (premier caractère)

# Équivalences
dernier = texte[-1]
dernier_bis = texte[len(texte)-1]  # Même résultat

# Table de correspondance
"""
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
| 0 | 1 | 2 | 3 | 4 | 5 |
+---+---+---+---+---+---+
|-6 |-5 |-4 |-3 |-2 |-1 |
+---+---+---+---+---+---+
"""
```

### 2. Slicing (découpage) (25 min)

#### A. Syntaxe de base
```python
# Syntaxe: chaine[debut:fin:pas]
texte = "Python Programming"

# Extraction de sous-chaînes
print(texte[0:6])     # "Python"
print(texte[7:])      # "Programming"
print(texte[:6])      # "Python"
print(texte[:])       # Copie complète

# Avec pas (step)
print(texte[::2])     # "Pto rgamn"
print(texte[::1])     # "Python Programming"

# Indices négatifs dans le slicing
print(texte[-11:])    # "Programming"
print(texte[:-7])     # "Python Pr"
```

#### B. Cas d'utilisation avancés
```python
# Inverser une chaîne
texte = "Python"
inverse = texte[::-1]  # "nohtyP"

# Extraire les caractères pairs/impairs
pairs = texte[::2]     # "Pto"
impairs = texte[1::2]  # "yhn"

# Extraction avec pas négatif
print(texte[5:0:-1])   # "nohty"
print(texte[-1::-2])   # "nhy"

# Slicing avec tous les paramètres
texte = "0123456789"
print(texte[2:8:2])    # "246"
```

### 3. Méthodes de recherche (20 min)

#### A. Recherche d'indices
```python
texte = "Python Programming"

# Trouver la première occurrence
index_p = texte.index('P')         # 0
index_prog = texte.index('Prog')   # 7

# Trouver la dernière occurrence
last_m = texte.rindex('m')         # 15

# Recherche avec find (plus sûr)
pos = texte.find('z')              # -1 si non trouvé
pos = texte.rfind('m')             # Comme rindex mais retourne -1

# Vérification d'existence
exists = 'Python' in texte          # True
not_exists = 'Java' in texte        # False
```

#### B. Applications pratiques
```python
def extraire_domaine(email):
    """Extrait le domaine d'une adresse email."""
    try:
        debut = email.index('@') + 1
        return email[debut:]
    except ValueError:
        return "Email invalide"

def trouver_mots(texte, debut_mot):
    """Trouve tous les mots commençant par une certaine chaîne."""
    mots = texte.split()
    return [mot for mot in mots if mot.startswith(debut_mot)]

def compter_occurrences(texte, caractere):
    """Compte les occurrences d'un caractère."""
    return sum(1 for i in range(len(texte)) if texte[i] == caractere)
```

### 4. Manipulation de caractères (20 min)

#### A. Conversion et vérification
```python
# Vérification de caractères
texte = "Python3.9"

for char in texte:
    print(f"'{char}' est un chiffre: {char.isdigit()}")
    print(f"'{char}' est une lettre: {char.isalpha()}")
    print(f"'{char}' est alphanumérique: {char.isalnum()}")

# Conversion de casse
for i, char in enumerate(texte):
    print(f"Original: {char}")
    print(f"Majuscule: {char.upper()}")
    print(f"Minuscule: {char.lower()}")
```

#### B. Manipulation avancée
```python
def remplacer_position(texte, position, nouveau_char):
    """Remplace un caractère à une position donnée."""
    if 0 <= position < len(texte):
        return texte[:position] + nouveau_char + texte[position+1:]
    return texte

def extraire_caracteres_type(texte, type_verif):
    """Extrait les caractères selon leur type."""
    verifications = {
        'alpha': str.isalpha,
        'digit': str.isdigit,
        'space': str.isspace
    }
    verif = verifications.get(type_verif, lambda x: True)
    return ''.join(char for char in texte if verif(char))
```

### 5. Bonnes pratiques (10 min)

```python
# Vérification de longueur avant accès
def acceder_securise(texte, index):
    if 0 <= index < len(texte):
        return texte[index]
    return None

# Utilisation de méthodes intégrées
def nettoyer_texte(texte):
    # Plutôt que de vérifier caractère par caractère
    return ''.join(char for char in texte if char.isalnum())

# Slicing sécurisé
def extraire_sous_chaine(texte, debut, fin):
    return texte[max(0, debut):min(len(texte), fin)]
```

### Phase de pratique (10 min)

Exercices :

1. Manipulation d'indices :
```python
def analyser_chaine(texte):
    """
    Retourner un dictionnaire contenant :
    - Premier caractère
    - Dernier caractère
    - Caractères aux positions paires
    - Caractères aux positions impaires
    """
    # À compléter
```

2. Extraction de sous-chaînes :
```python
def extraire_information(texte):
    """
    Extraire et retourner :
    - Les 3 premiers caractères
    - Les 3 derniers caractères
    - La chaîne inversée
    - Les caractères aux positions multiples de 3
    """
    # À compléter
```

### Synthèse (5 min)
- Indexation positive et négative
- Slicing et ses paramètres
- Méthodes de recherche
- Manipulation de caractères

## Points importants à retenir :

1. Indices :
   - Commencent à 0
   - Peuvent être négatifs
   - Doivent être dans les limites

2. Slicing :
   - [debut:fin:pas]
   - Flexible et puissant
   - Crée une nouvelle chaîne

3. Bonnes pratiques :
   - Vérifier les limites
   - Utiliser les méthodes intégrées
   - Préférer les méthodes sécurisées