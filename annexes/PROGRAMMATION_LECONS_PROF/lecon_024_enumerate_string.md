# Plan de leçon : Utilisation de enumerate() pour le parcours de chaînes

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Parcours de chaînes avec enumerate()
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation de la fonction enumerate()

- Objectifs disciplinaires :
  - Comprendre le fonctionnement de enumerate()
  - Savoir accéder aux indices et valeurs simultanément
  - Utiliser enumerate() efficacement dans les boucles
  - Maîtriser les options de enumerate()

## Déroulement de la leçon

### 1. Bases de enumerate() (20 min)

#### A. Syntaxe de base
```python
# Structure de base
texte = "Python"
for index, caractere in enumerate(texte):
    print(f"Index {index}: {caractere}")

# Résultat:
# Index 0: P
# Index 1: y
# Index 2: t
# Index 3: h
# Index 4: o
# Index 5: n

# Avec index de départ personnalisé
for index, caractere in enumerate(texte, start=1):
    print(f"Position {index}: {caractere}")

# Résultat:
# Position 1: P
# Position 2: y
# Position 3: t
# Position 4: h
# Position 5: o
# Position 6: n
```

#### B. Conversion et utilisation
```python
# Conversion en liste de tuples
indices_caracteres = list(enumerate(texte))
print(indices_caracteres)  # [(0, 'P'), (1, 'y'), (2, 't')...]

# Conversion avec index de départ
indices_caracteres = list(enumerate(texte, 1))
print(indices_caracteres)  # [(1, 'P'), (2, 'y'), (3, 't')...]

# Déballage de tuples
for tuple_index_char in enumerate(texte):
    index, caractere = tuple_index_char
    print(f"{index} -> {caractere}")
```

### 2. Applications pratiques (25 min)

#### A. Recherche et analyse
```python
def trouver_positions(texte, caractere_recherche):
    """Trouve toutes les positions d'un caractère."""
    positions = []
    for i, c in enumerate(texte):
        if c == caractere_recherche:
            positions.append(i)
    return positions

def analyser_caracteres(texte):
    """Analyse chaque caractère avec sa position."""
    analyse = {}
    for i, c in enumerate(texte):
        analyse[i] = {
            'caractere': c,
            'est_majuscule': c.isupper(),
            'est_chiffre': c.isdigit(),
            'position': i
        }
    return analyse

def trouver_sequence(texte, sequence):
    """Trouve les positions de début d'une séquence."""
    positions = []
    for i, c in enumerate(texte):
        if texte[i:i+len(sequence)] == sequence:
            positions.append(i)
    return positions
```

#### B. Modification et transformation
```python
def alterner_casse(texte):
    """Alterne majuscules et minuscules selon la position."""
    return ''.join(
        c.upper() if i % 2 == 0 else c.lower()
        for i, c in enumerate(texte)
    )

def inserer_position(texte):
    """Insère le numéro de position après chaque caractère."""
    return ''.join(
        f"{c}[{i}]"
        for i, c in enumerate(texte)
    )

def formater_texte(texte, separateur='-'):
    """Formate le texte avec des séparateurs numérotés."""
    return ''.join(
        f"{c}{separateur}{i}"
        for i, c in enumerate(texte, 1)
    )
```

### 3. Cas d'utilisation avancés (20 min)

#### A. Traitement conditionnel
```python
def traiter_positions_specifiques(texte, positions_cibles):
    """Traite uniquement les caractères à certaines positions."""
    resultat = []
    for i, c in enumerate(texte):
        if i in positions_cibles:
            resultat.append(c.upper())
        else:
            resultat.append(c)
    return ''.join(resultat)

def remplacer_motif(texte, ancien, nouveau):
    """Remplace un motif en gardant la trace des positions."""
    resultats = []
    for i, c in enumerate(texte):
        if texte[i:i+len(ancien)] == ancien:
            resultats.append((i, nouveau))
    return resultats
```

#### B. Analyse complexe
```python
def analyser_structure(texte):
    """Analyse la structure d'une chaîne avec positions."""
    structure = {
        'majuscules': [],
        'minuscules': [],
        'chiffres': [],
        'espaces': [],
        'speciaux': []
    }
    
    for i, c in enumerate(texte):
        if c.isupper():
            structure['majuscules'].append(i)
        elif c.islower():
            structure['minuscules'].append(i)
        elif c.isdigit():
            structure['chiffres'].append(i)
        elif c.isspace():
            structure['espaces'].append(i)
        else:
            structure['speciaux'].append(i)
    
    return structure

def comparer_positions(texte1, texte2):
    """Compare les caractères aux mêmes positions."""
    differences = []
    min_len = min(len(texte1), len(texte2))
    
    for i, (c1, c2) in enumerate(zip(texte1[:min_len], texte2[:min_len])):
        if c1 != c2:
            differences.append({
                'position': i,
                'texte1': c1,
                'texte2': c2
            })
    
    return differences
```

### 4. Bonnes pratiques et optimisation (15 min)

#### A. Performance et lisibilité
```python
# Éviter la création de listes inutiles
def mauvaise_approche(texte):
    # Ne pas faire ça
    positions = list(enumerate(texte))
    for pos in positions:
        # traitement

def bonne_approche(texte):
    # Utiliser directement enumerate
    for i, c in enumerate(texte):
        # traitement

# Utilisation avec compréhension de liste
def filtrer_positions(texte, condition):
    return [
        (i, c) 
        for i, c in enumerate(texte) 
        if condition(c)
    ]
```

#### B. Gestion des cas particuliers
```python
def parcours_securise(texte):
    """Gestion des cas particuliers dans le parcours."""
    if not texte:
        return []
    
    resultats = []
    for i, c in enumerate(texte):
        try:
            # Traitement qui pourrait échouer
            resultat = traiter_caractere(c)
            resultats.append((i, resultat))
        except Exception as e:
            print(f"Erreur à la position {i}: {e}")
    
    return resultats
```

### Phase de pratique (15 min)

Exercices :

1. Analyse de texte :
```python
def analyser_mots(texte):
    """
    Pour chaque mot du texte, retourner :
    - Sa position de début
    - Sa longueur
    - S'il commence par une majuscule
    """
    # À compléter
```

2. Transformation de texte :
```python
def transformer_texte(texte):
    """
    Transformer un texte en :
    - Majuscules pour les positions paires
    - Minuscules pour les positions impaires
    - Ajouter le numéro de position entre crochets
    """
    # À compléter
```

### Synthèse (5 min)
- Utilisation basique et avancée de enumerate()
- Cas d'utilisation appropriés
- Bonnes pratiques et optimisations

## Points importants à retenir :

1. Enumerate() :
   - Fournit indices et valeurs simultanément
   - Peut commencer à n'importe quel index
   - Plus efficace que la gestion manuelle des indices

2. Bonnes pratiques :
   - Utiliser le déballage de tuples
   - Éviter les conversions inutiles en liste
   - Gérer les cas particuliers

3. Applications :
   - Analyse de texte
   - Transformation basée sur la position
   - Comparaison de chaînes