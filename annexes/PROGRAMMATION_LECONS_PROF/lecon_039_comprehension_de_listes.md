# Plan de leçon : Les compréhensions de listes

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Compréhensions de listes
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les compréhensions de listes

- Objectifs disciplinaires :
  - Comprendre la syntaxe des compréhensions
  - Savoir créer des compréhensions simples et complexes
  - Maîtriser les conditions dans les compréhensions
  - Optimiser l'utilisation des compréhensions

## Déroulement de la leçon

### 1. Syntaxe de base (25 min)

#### A. Structure simple
```python
# Forme basique
# [expression for élément in itérable]

# Exemple simple
carres = [x**2 for x in range(5)]
print(carres)  # [0, 1, 4, 9, 16]

# Équivalent avec boucle for
carres_classique = []
for x in range(5):
    carres_classique.append(x**2)

# Transformation de chaînes
mots = ["python", "java", "javascript"]
majuscules = [mot.upper() for mot in mots]
print(majuscules)  # ['PYTHON', 'JAVA', 'JAVASCRIPT']

# Opérations sur des nombres
nombres = [1, 2, 3, 4, 5]
doubles = [n * 2 for n in nombres]
```

#### B. Expressions plus complexes
```python
# Utilisation de méthodes
phrases = ["  hello  ", "  python  ", "  world  "]
nettoyees = [phrase.strip() for phrase in phrases]

# Opérations arithmétiques
points = [(1, 2), (3, 4), (5, 6)]
sommes = [x + y for x, y in points]

# Création de tuples
coords = [(x, y) for x in range(2) for y in range(2)]
print(coords)  # [(0, 0), (0, 1), (1, 0), (1, 1)]
```

### 2. Compréhensions avec conditions (25 min)

#### A. Filtrage avec if
```python
# Syntaxe avec condition
# [expression for élément in itérable if condition]

# Filtrer les nombres pairs
nombres = range(10)
pairs = [n for n in nombres if n % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8]

# Filtrer les chaînes non vides
textes = ["", "hello", "", "world", "  "]
non_vides = [t for t in textes if t.strip()]

# Filtrer sur plusieurs conditions
nombres = range(20)
multiples_3_5 = [n for n in nombres if n % 3 == 0 and n % 5 == 0]
```

#### B. Structure if-else
```python
# Syntaxe avec if-else
# [expression_if if condition else expression_else for élément in itérable]

# Exemple basique
nombres = range(10)
parite = ['pair' if n % 2 == 0 else 'impair' for n in nombres]

# Classification plus complexe
notes = [12, 15, 8, 19, 7, 16]
resultats = ['excellent' if n >= 16 
            else 'bien' if n >= 12 
            else 'insuffisant' 
            for n in notes]

# Transformation conditionnelle
valeurs = [1, -2, 3, -4, 5]
absolus = [n if n > 0 else -n for n in valeurs]
```

### 3. Compréhensions imbriquées (25 min)

#### A. Boucles multiples
```python
# Syntaxe avec boucles imbriquées
# [expression for x in itérable1 for y in itérable2]

# Création de paires
lignes = range(2)
colonnes = range(3)
coords = [(x, y) for x in lignes for y in colonnes]
print(coords)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

# Produit cartésien
lettres = ['a', 'b']
nombres = [1, 2]
combinaisons = [l + str(n) for l in lettres for n in nombres]
print(combinaisons)  # ['a1', 'a2', 'b1', 'b2']
```

#### B. Matrices et listes imbriquées
```python
# Création de matrice
matrice = [[i + j for j in range(3)] for i in range(3)]
print(matrice)  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Aplatir une matrice
matrice = [[1, 2], [3, 4], [5, 6]]
aplatie = [x for ligne in matrice for x in ligne]
print(aplatie)  # [1, 2, 3, 4, 5, 6]

# Transformation de matrice
matrice = [[1, 2], [3, 4]]
carres = [[x**2 for x in ligne] for ligne in matrice]
```

### 4. Applications pratiques (25 min)

#### A. Traitement de données
```python
# Filtrage et transformation de dictionnaires
personnes = [
    {"nom": "Alice", "age": 25},
    {"nom": "Bob", "age": 17},
    {"nom": "Charlie", "age": 30}
]

majeurs = [p["nom"] for p in personnes if p["age"] >= 18]
print(majeurs)  # ['Alice', 'Charlie']

# Extraction de données
fichiers = ["doc1.txt", "image.jpg", "doc2.txt", "video.mp4"]
txt_files = [f for f in fichiers if f.endswith('.txt')]

# Traitement de chaînes
phrases = ["Hello World", "Python Programming", "Data Science"]
mots = [mot for phrase in phrases 
        for mot in phrase.split()]
```

#### B. Manipulation de données structurées
```python
# Transformation de structures imbriquées
data = [
    ("Groupe A", [85, 90, 78]),
    ("Groupe B", [92, 87, 95]),
    ("Groupe C", [79, 88, 92])
]

moyennes = [(groupe, sum(notes)/len(notes)) 
            for groupe, notes in data]

# Création de lookup tables
codes = ["USD", "EUR", "GBP"]
taux = [1.0, 0.85, 0.73]
conversion = {code: taux for code, taux in zip(codes, taux)}

# Filtrage complexe
transactions = [
    {"id": 1, "montant": 100, "valide": True},
    {"id": 2, "montant": -50, "valide": False},
    {"id": 3, "montant": 75, "valide": True}
]

valides = [t["montant"] for t in transactions 
          if t["valide"] and t["montant"] > 0]
```

### 5. Optimisation et bonnes pratiques (15 min)

#### A. Lisibilité vs Complexité
```python
# Trop complexe - À éviter
resultat = [x*y for x in range(5) 
           for y in range(5) 
           if x % 2 == 0 
           if y % 2 == 0 
           if x*y > 5]

# Mieux - Plus lisible
resultat = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 0 and x*y > 5:
                resultat.append(x*y)

# Équilibre - Complexité modérée
nombres = range(10)
filtres = [n for n in nombres 
          if n % 2 == 0 and n > 0]
```

#### B. Performance
```python
# Éviter les opérations coûteuses
# Mauvais
resultat = [fonction_couteuse(x) for x in grande_liste]

# Meilleur
resultats_intermediaires = [x for x in grande_liste if condition_simple(x)]
resultat = [fonction_couteuse(x) for x in resultats_intermediaires]

# Utilisation de générateurs pour les grandes listes
grand_resultat = list(x for x in range(1000000) if x % 2 == 0)
```

### Phase de pratique (15 min)

Exercices :

1. Traitement de données :
```python
def analyser_donnees(donnees):
    """
    Créer des compréhensions pour :
    - Filtrer les données valides
    - Transformer les données
    - Calculer des statistiques
    """
    # À compléter
```

2. Manipulation de texte :
```python
def traiter_texte(texte):
    """
    Utiliser des compréhensions pour :
    - Extraire des mots
    - Filtrer selon certains critères
    - Transformer le texte
    """
    # À compléter
```

### Synthèse (5 min)
- Syntaxe de base
- Conditions et filtrage
- Imbrication
- Bonnes pratiques

## Points importants à retenir :

1. Syntaxe :
   - Structure de base
   - Conditions if/else
   - Boucles imbriquées

2. Applications :
   - Transformation de données
   - Filtrage
   - Création de structures

3. Bonnes pratiques :
   - Lisibilité
   - Performance
   - Complexité appropriée