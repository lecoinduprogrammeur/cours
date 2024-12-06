# Plan de leçon : Variables de type set (ensemble)

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Manipulation des ensembles
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des ensembles en Python

- Objectifs disciplinaires :
  - Comprendre le concept d'ensemble
  - Maîtriser les opérations sur les ensembles
  - Savoir utiliser les méthodes d'ensemble
  - Appliquer les ensembles dans des cas pratiques

## Déroulement de la leçon

### 1. Introduction aux ensembles (20 min)

#### A. Création d'ensembles
```python
# Ensemble vide
ensemble1 = set()
ensemble2 = set([])

# Ensemble avec éléments
nombres = {1, 2, 3, 4, 5}
lettres = {'a', 'b', 'c'}

# Conversion depuis d'autres types
liste_vers_set = set([1, 2, 2, 3])  # {1, 2, 3}
string_vers_set = set("hello")      # {'h', 'e', 'l', 'o'}

# Caractéristiques principales
# - Pas de doublons
# - Non ordonné
# - Elements immutables uniquement
ensemble = {1, 2, 2, 3}  # {1, 2, 3}
```

#### B. Propriétés fondamentales
```python
# Vérification d'appartenance
ensemble = {1, 2, 3}
print(1 in ensemble)      # True
print(4 not in ensemble)  # True

# Taille
taille = len(ensemble)    # 3

# Éléments uniques
liste = [1, 2, 2, 3, 3, 3]
uniques = set(liste)      # {1, 2, 3}

# Types autorisés/non autorisés
valide = {1, "texte", (1, 2)}  # OK
# invalide = {[1, 2], {3, 4}}  # TypeError: unhashable type
```

### 2. Opérations sur les ensembles (25 min)

#### A. Opérations de base
```python
# Ajout d'éléments
ensemble = {1, 2}
ensemble.add(3)           # {1, 2, 3}
ensemble.update([4, 5])   # {1, 2, 3, 4, 5}

# Suppression d'éléments
ensemble.remove(3)        # Lève KeyError si absent
ensemble.discard(3)       # Ne lève pas d'erreur si absent
element = ensemble.pop()  # Retire et retourne un élément arbitraire
ensemble.clear()          # Vide l'ensemble

# Copie
copie = ensemble.copy()
```

#### B. Opérations mathématiques
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
union = A | B            # ou A.union(B)
# {1, 2, 3, 4, 5, 6}

# Intersection
intersection = A & B     # ou A.intersection(B)
# {3, 4}

# Différence
difference = A - B       # ou A.difference(B)
# {1, 2}

# Différence symétrique
sym_diff = A ^ B        # ou A.symmetric_difference(B)
# {1, 2, 5, 6}
```

### 3. Relations entre ensembles (25 min)

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7}

# Sous-ensemble
est_sous_ensemble = A <= B  # True
est_strict = A < B         # True (strict sous-ensemble)

# Sur-ensemble
est_sur_ensemble = B >= A  # True
est_strict_sur = B > A     # True (strict sur-ensemble)

# Disjonction
sont_disjoints = A.isdisjoint(C)  # True

# Tests d'égalité
sont_egaux = A == B        # False
```

### 4. Applications pratiques (25 min)

#### A. Élimination des doublons
```python
def obtenir_elements_uniques(sequence):
    """Retourne les éléments uniques en préservant l'ordre."""
    return list(dict.fromkeys(sequence))

def compter_elements_uniques(sequence):
    """Compte le nombre d'éléments uniques."""
    return len(set(sequence))

def trouver_doublons(sequence):
    """Trouve les éléments qui apparaissent plus d'une fois."""
    vus = set()
    doublons = set()
    for element in sequence:
        if element in vus:
            doublons.add(element)
        vus.add(element)
    return doublons
```

#### B. Analyse de données
```python
def analyser_texte(texte):
    """Analyse les caractères uniques dans un texte."""
    caracteres = set(texte.lower())
    return {
        'lettres': {c for c in caracteres if c.isalpha()},
        'chiffres': {c for c in caracteres if c.isdigit()},
        'ponctuation': caracteres - {c for c in caracteres 
                                   if c.isalnum() or c.isspace()}
    }

def comparer_sequences(seq1, seq2):
    """Compare deux séquences."""
    set1, set2 = set(seq1), set(seq2)
    return {
        'communs': set1 & set2,
        'uniques_seq1': set1 - set2,
        'uniques_seq2': set2 - set1
    }
```

### 5. Cas d'utilisation avancés (20 min)

```python
def verifier_permissions(utilisateur, permissions_requises):
    """Vérifie si un utilisateur a toutes les permissions requises."""
    permissions_user = set(utilisateur['permissions'])
    return permissions_requises <= permissions_user

def trouver_intersections_multiples(*sequences):
    """Trouve les éléments communs à toutes les séquences."""
    if not sequences:
        return set()
    resultat = set(sequences[0])
    for seq in sequences[1:]:
        resultat &= set(seq)
    return resultat

def grouper_par_caracteristique(elements, key_func):
    """Groupe les éléments par caractéristique commune."""
    groupes = {}
    for elem in elements:
        key = key_func(elem)
        if key not in groupes:
            groupes[key] = set()
        groupes[key].add(elem)
    return groupes
```

### 6. Performance et optimisation (15 min)

```python
# Comparaison avec les listes
def recherche_efficace():
    # Avec liste (lent pour les grandes collections)
    liste = list(range(10000))
    element = 9999
    existe_liste = element in liste  # O(n)
    
    # Avec ensemble (rapide)
    ensemble = set(range(10000))
    existe_set = element in ensemble  # O(1)

# Élimination efficace des doublons
def optimiser_recherche_doublons(sequence):
    """Optimise la recherche de doublons avec un set."""
    vus = set()
    doublons = set()
    ajouter_vu = vus.add
    ajouter_doublon = doublons.add
    
    for element in sequence:
        if element in vus:
            ajouter_doublon(element)
        else:
            ajouter_vu(element)
    return doublons
```

### Phase de pratique (15 min)

Exercices :

1. Système de gestion de droits :
```python
def creer_systeme_permissions():
    """
    Créer un système qui :
    - Gère les permissions utilisateur
    - Vérifie les accès
    - Compare les niveaux de permission
    """
    # À compléter
```

2. Analyse de données :
```python
def analyser_donnees():
    """
    Créer un système qui :
    - Trouve les éléments communs
    - Identifie les différences
    - Génère des statistiques
    """
    # À compléter
```

## Points importants à retenir :

1. Caractéristiques :
   - Pas de doublons
   - Non ordonné
   - Éléments hashables uniquement

2. Opérations :
   - Union, intersection, différence
   - Ajout, suppression
   - Tests d'appartenance

3. Avantages :
   - Recherche rapide
   - Élimination des doublons
   - Opérations mathématiques