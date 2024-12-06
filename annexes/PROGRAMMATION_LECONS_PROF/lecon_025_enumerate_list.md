# Plan de leçon : Parcours de listes avec enumerate()

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Parcours de listes avec enumerate()
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation de enumerate() avec les listes

- Objectifs disciplinaires :
  - Comprendre l'intérêt de enumerate() pour les listes
  - Savoir manipuler indices et valeurs simultanément
  - Maîtriser les différents cas d'utilisation
  - Optimiser le parcours de listes

## Déroulement de la leçon

### 1. Bases de enumerate() avec les listes (20 min)

#### A. Syntaxe de base
```python
# Structure de base
nombres = [10, 20, 30, 40, 50]
for index, nombre in enumerate(nombres):
    print(f"Index {index}: {nombre}")

# Avec index de départ personnalisé
fruits = ["pomme", "banane", "orange"]
for index, fruit in enumerate(fruits, start=1):
    print(f"Fruit #{index}: {fruit}")

# Conversion en liste de tuples
liste = ["a", "b", "c"]
enumere = list(enumerate(liste))
print(enumere)  # [(0, 'a'), (1, 'b'), (2, 'c')]
```

#### B. Comparaison avec autres méthodes
```python
nombres = [1, 2, 3, 4, 5]

# Avec range (moins élégant)
for i in range(len(nombres)):
    print(f"{i}: {nombres[i]}")

# Avec enumerate (plus pythonique)
for i, nombre in enumerate(nombres):
    print(f"{i}: {nombre}")

# Avantage de enumerate pour modifications
for i, valeur in enumerate(nombres):
    nombres[i] = valeur * 2  # Modification de la liste
```

### 2. Applications pratiques (25 min)

#### A. Manipulation de listes
```python
def modifier_elements_pairs(liste):
    """Double les éléments aux indices pairs."""
    for i, valeur in enumerate(liste):
        if i % 2 == 0:
            liste[i] = valeur * 2
    return liste

def remplacer_valeurs(liste, ancien, nouveau):
    """Remplace toutes les occurrences d'une valeur."""
    for i, valeur in enumerate(liste):
        if valeur == ancien:
            liste[i] = nouveau
    return liste

def filtrer_avec_positions(liste, condition):
    """Retourne les éléments et leurs positions qui satisfont une condition."""
    return [(i, val) for i, val in enumerate(liste) if condition(val)]
```

#### B. Analyses et transformations
```python
def analyser_liste(liste):
    """Analyse chaque élément avec sa position."""
    analyse = {}
    for i, valeur in enumerate(liste):
        analyse[i] = {
            'valeur': valeur,
            'type': type(valeur).__name__,
            'position': i,
            'est_pair': i % 2 == 0
        }
    return analyse

def transformer_avec_index(liste):
    """Transforme chaque élément en fonction de sa position."""
    return [
        f"{val}_{i}" if isinstance(val, str) else val * i
        for i, val in enumerate(liste, 1)
    ]

def trouver_sequences(liste, taille):
    """Trouve toutes les séquences de taille donnée."""
    sequences = {}
    for i, _ in enumerate(liste):
        if i + taille <= len(liste):
            seq = tuple(liste[i:i+taille])
            if seq in sequences:
                sequences[seq].append(i)
            else:
                sequences[seq] = [i]
    return sequences
```

### 3. Cas d'utilisation avancés (20 min)

#### A. Traitement de listes imbriquées
```python
def parcourir_matrice(matrice):
    """Parcourt une matrice avec indices de ligne et colonne."""
    for i, ligne in enumerate(matrice):
        for j, valeur in enumerate(ligne):
            print(f"Position [{i}][{j}]: {valeur}")

def transformer_matrice(matrice):
    """Transforme une matrice selon les positions."""
    return [
        [valeur * (i + j) for j, valeur in enumerate(ligne)]
        for i, ligne in enumerate(matrice)
    ]

def trouver_elements(matrice, cible):
    """Trouve toutes les positions d'un élément dans une matrice."""
    positions = []
    for i, ligne in enumerate(matrice):
        for j, valeur in enumerate(ligne):
            if valeur == cible:
                positions.append((i, j))
    return positions
```

#### B. Manipulations complexes
```python
def comparer_listes(liste1, liste2):
    """Compare deux listes élément par élément."""
    differences = []
    min_len = min(len(liste1), len(liste2))
    
    for i, (val1, val2) in enumerate(zip(liste1[:min_len], liste2[:min_len])):
        if val1 != val2:
            differences.append({
                'position': i,
                'valeur1': val1,
                'valeur2': val2
            })
    
    # Gestion des longueurs différentes
    if len(liste1) != len(liste2):
        differences.append({
            'type': 'longueur',
            'liste1': len(liste1),
            'liste2': len(liste2)
        })
    
    return differences

def reorganiser_liste(liste):
    """Réorganise une liste selon des critères de position."""
    modifications = []
    for i, valeur in enumerate(liste):
        if i > 0 and valeur < liste[i-1]:
            # Enregistre les modifications nécessaires
            modifications.append((i-1, i))
    
    # Applique les modifications
    for pos1, pos2 in modifications:
        liste[pos1], liste[pos2] = liste[pos2], liste[pos1]
    
    return liste, modifications
```

### 4. Optimisation et bonnes pratiques (15 min)

#### A. Performance
```python
# Éviter la création de listes temporaires inutiles
def mauvaise_approche(liste):
    positions = list(enumerate(liste))  # Inutile
    for pos in positions:
        # traitement

def bonne_approche(liste):
    for i, val in enumerate(liste):
        # traitement directement

# Utilisation efficace avec compréhension de liste
def filtrer_efficacement(liste):
    return [
        val for i, val in enumerate(liste)
        if condition(i, val)
    ]
```

#### B. Lisibilité et maintenance
```python
def traiter_liste(liste, debut=0):
    """Exemple de bonnes pratiques."""
    # Documentation claire
    # Paramètres flexibles
    # Gestion des cas spéciaux
    if not liste:
        return []
    
    resultats = []
    for i, valeur in enumerate(liste, start=debut):
        try:
            resultat = traiter_element(i, valeur)
            resultats.append(resultat)
        except Exception as e:
            print(f"Erreur à l'index {i}: {e}")
    
    return resultats
```

### Phase de pratique (15 min)

Exercices :

1. Manipulation de liste :
```python
def traiter_liste_nombres(nombres):
    """
    - Multiplier par 2 les nombres aux positions paires
    - Ajouter l'index aux nombres aux positions impaires
    - Retourner la nouvelle liste
    """
    # À compléter
```

2. Analyse de liste :
```python
def analyser_elements(liste):
    """
    Pour chaque élément, créer un dictionnaire avec :
    - Sa position
    - Sa valeur
    - Son type
    - Sa relation avec les éléments voisins
    """
    # À compléter
```

### Synthèse (5 min)
- Avantages de enumerate() pour les listes
- Cas d'utilisation appropriés
- Bonnes pratiques
- Points d'optimisation

## Points importants à retenir :

1. Utilisation :
   - Accès simultané aux indices et valeurs
   - Paramètre start pour index personnalisé
   - Plus pythonique que range(len())

2. Applications :
   - Modification de listes
   - Analyse de données
   - Traitement conditionnel

3. Bonnes pratiques :
   - Éviter les conversions inutiles
   - Utiliser des noms explicites
   - Gérer les cas spéciaux