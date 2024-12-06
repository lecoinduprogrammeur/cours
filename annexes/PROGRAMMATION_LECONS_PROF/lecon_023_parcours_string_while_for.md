# Plan de leçon : Parcours de chaînes avec les boucles for et while

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Parcours des chaînes de caractères
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les différentes méthodes de parcours des chaînes

- Objectifs disciplinaires :
  - Comprendre les différentes approches de parcours
  - Maîtriser les boucles for et while avec les chaînes
  - Savoir choisir la bonne méthode selon le besoin
  - Optimiser les parcours de chaînes

## Déroulement de la leçon

### 1. Parcours avec for (25 min)

#### A. Parcours caractère par caractère
```python
# Parcours simple
texte = "Python"
for caractere in texte:
    print(caractere)

# Avec énumération
for index, caractere in enumerate(texte):
    print(f"Position {index}: {caractere}")

# Avec traitement
def compter_voyelles(texte):
    voyelles = 'aeiouAEIOU'
    count = 0
    for caractere in texte:
        if caractere in voyelles:
            count += 1
    return count
```

#### B. Parcours avec range
```python
# Utilisation des indices
texte = "Python"
for i in range(len(texte)):
    print(f"texte[{i}] = {texte[i]}")

# Parcours inversé
for i in range(len(texte) - 1, -1, -1):
    print(texte[i])

# Parcours par pas
for i in range(0, len(texte), 2):
    print(f"Caractère pair: {texte[i]}")
```

### 2. Parcours avec while (25 min)

#### A. Parcours avec index
```python
# Parcours simple
texte = "Python"
i = 0
while i < len(texte):
    print(texte[i])
    i += 1

# Parcours jusqu'à condition
def trouver_caractere(texte, cible):
    i = 0
    while i < len(texte):
        if texte[i] == cible:
            return i
        i += 1
    return -1

# Parcours avec plusieurs conditions
def valider_chaine(texte):
    i = 0
    has_upper = has_digit = False
    while i < len(texte) and not (has_upper and has_digit):
        if texte[i].isupper():
            has_upper = True
        if texte[i].isdigit():
            has_digit = True
        i += 1
    return has_upper and has_digit
```

#### B. Parcours avec slicing
```python
# Parcours avec fenêtre glissante
def trouver_motif(texte, taille_fenetre):
    i = 0
    while i <= len(texte) - taille_fenetre:
        print(texte[i:i+taille_fenetre])
        i += 1

# Recherche de sous-chaîne
def compter_occurrences(texte, motif):
    count = 0
    i = 0
    while i < len(texte):
        if texte[i:i+len(motif)] == motif:
            count += 1
            i += len(motif)
        else:
            i += 1
    return count
```

### 3. Cas d'utilisation spécifiques (20 min)

#### A. Traitement par blocs
```python
def traiter_par_blocs(texte, taille_bloc):
    """Traite le texte par blocs de taille donnée."""
    for i in range(0, len(texte), taille_bloc):
        bloc = texte[i:i+taille_bloc]
        print(f"Bloc {i//taille_bloc + 1}: {bloc}")

def trouver_repetitions(texte, taille):
    """Trouve les séquences qui se répètent."""
    sequences = {}
    for i in range(len(texte) - taille + 1):
        seq = texte[i:i+taille]
        sequences[seq] = sequences.get(seq, 0) + 1
    return {s: c for s, c in sequences.items() if c > 1}
```

#### B. Analyse de texte
```python
def analyser_texte(texte):
    """Analyse statistique d'un texte."""
    stats = {
        'majuscules': 0,
        'minuscules': 0,
        'chiffres': 0,
        'espaces': 0,
        'ponctuation': 0
    }
    
    for caractere in texte:
        if caractere.isupper():
            stats['majuscules'] += 1
        elif caractere.islower():
            stats['minuscules'] += 1
        elif caractere.isdigit():
            stats['chiffres'] += 1
        elif caractere.isspace():
            stats['espaces'] += 1
        elif caractere in ',.;:!?':
            stats['ponctuation'] += 1
            
    return stats
```

### 4. Optimisation et cas particuliers (15 min)

#### A. Optimisation des parcours
```python
# Éviter les concaténations répétées
def mauvais_exemple(texte):
    resultat = ""
    for c in texte:
        resultat += c.upper()  # Inefficace
    return resultat

def bon_exemple(texte):
    return ''.join(c.upper() for c in texte)  # Efficace

# Utilisation de générateurs pour les grands textes
def parcours_efficace(texte):
    return (c for c in texte if c.isalnum())
```

#### B. Traitement des caractères spéciaux
```python
def nettoyer_texte(texte):
    """Nettoie un texte des caractères spéciaux."""
    caracteres_valides = []
    for c in texte:
        if c.isalnum() or c.isspace():
            caracteres_valides.append(c)
    return ''.join(caracteres_valides)

def normaliser_texte(texte):
    """Normalise un texte (supprime accents, etc.)."""
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFKD', texte)
                  if not unicodedata.combining(c))
```

### 5. Comparaison for vs while (10 min)

```python
# Quand utiliser for
def exemple_for(texte):
    # Parcours simple, complet
    for c in texte:
        print(c)
    
    # Avec indices connus
    for i in range(len(texte)):
        print(texte[i])

# Quand utiliser while
def exemple_while(texte):
    # Condition de sortie complexe
    i = 0
    while i < len(texte) and texte[i] != ' ':
        i += 1
    
    # Parcours avec sauts variables
    i = 0
    while i < len(texte):
        if texte[i].isdigit():
            i += 2
        else:
            i += 1
```

### Phase de pratique (10 min)

Exercices :

1. Analyse de texte :
```python
def analyser_mot(mot):
    """
    Analyser un mot et retourner :
    - Nombre de voyelles
    - Nombre de consonnes
    - Est palindrome ou non
    """
    # À compléter
```

2. Recherche de motifs :
```python
def trouver_sequences(texte, longueur):
    """
    Trouver toutes les séquences de longueur donnée
    qui apparaissent plus d'une fois
    """
    # À compléter
```

### Synthèse (5 min)
- Avantages et inconvénients de chaque méthode
- Choix de la bonne approche selon le cas
- Points d'attention pour l'optimisation

## Points importants à retenir :

1. For :
   - Idéal pour parcours simple
   - Plus lisible pour parcours complet
   - Meilleur pour indices réguliers

2. While :
   - Flexible pour conditions complexes
   - Contrôle précis de l'itération
   - Utile pour parcours irrégulier

3. Optimisation :
   - Éviter les concaténations dans les boucles
   - Utiliser les bonnes méthodes de chaînes
   - Considérer les cas spéciaux