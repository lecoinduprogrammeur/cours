# Plan de leçon : Modification de chaînes via conversion en liste

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Conversion et modification de chaînes via des listes
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Comprendre et maîtriser la modification de chaînes via conversion en liste

- Objectifs disciplinaires :
  - Comprendre l'immuabilité des chaînes
  - Maîtriser les méthodes split() et join()
  - Savoir modifier des chaînes via des listes
  - Apprendre les bonnes pratiques de conversion

## Déroulement de la leçon

### 1. Immuabilité des chaînes vs Mutabilité des listes (20 min)

#### A. Démonstration de l'immuabilité
```python
# Les chaînes sont immuables
texte = "Hello World"
try:
    texte[0] = 'h'  # Génère une erreur
except TypeError as e:
    print(f"Erreur: {e}")  # TypeError: 'str' object does not support item assignment

# Seule solution : créer une nouvelle chaîne
nouveau_texte = 'h' + texte[1:]
print(nouveau_texte)  # "hello World"
```

#### B. Démonstration de la mutabilité des listes
```python
# Les listes sont mutables
liste = ['H', 'e', 'l', 'l', 'o']
liste[0] = 'h'  # Modification possible
print(liste)  # ['h', 'e', 'l', 'l', 'o']

# Modifications multiples
liste.append('!')
liste.insert(0, '*')
liste.remove('l')
print(liste)
```

### 2. Utilisation de split() (25 min)

#### A. Bases de split()
```python
# Split basique (espace par défaut)
phrase = "Python est génial"
mots = phrase.split()
print(mots)  # ['Python', 'est', 'génial']

# Split avec séparateur spécifique
date = "2024-03-15"
elements = date.split('-')
print(elements)  # ['2024', '03', '15']

# Split avec limite
texte = "a,b,c,d,e"
parties = texte.split(',', 2)
print(parties)  # ['a', 'b', 'c,d,e']
```

#### B. Cas d'utilisation avancés
```python
def extraire_informations(ligne_csv):
    """Extrait les informations d'une ligne CSV."""
    return ligne_csv.split(',')

def separer_phrases(texte):
    """Sépare un texte en phrases."""
    return [p.strip() for p in texte.split('.') if p.strip()]

def analyser_log(ligne_log):
    """Analyse une ligne de log avec plusieurs délimiteurs."""
    date, reste = ligne_log.split(' - ', 1)
    type_log, message = reste.split(': ', 1)
    return {
        'date': date,
        'type': type_log,
        'message': message
    }
```

### 3. Modification des éléments (25 min)

#### A. Opérations sur liste
```python
def mettre_en_majuscule(phrase):
    """Met en majuscule le premier mot de chaque phrase."""
    mots = phrase.split()
    mots[0] = mots[0].capitalize()
    return ' '.join(mots)

def remplacer_mot(phrase, ancien, nouveau):
    """Remplace toutes les occurrences d'un mot."""
    mots = phrase.split()
    for i, mot in enumerate(mots):
        if mot == ancien:
            mots[i] = nouveau
    return ' '.join(mots)

def inverser_ordre_mots(phrase):
    """Inverse l'ordre des mots dans une phrase."""
    mots = phrase.split()
    mots.reverse()  # ou mots = mots[::-1]
    return ' '.join(mots)
```

#### B. Transformations complexes
```python
def formater_phrase(phrase):
    """Applique plusieurs transformations à une phrase."""
    mots = phrase.split()
    
    # Capitalize premier mot
    mots[0] = mots[0].capitalize()
    
    # Met en majuscules les mots de plus de 5 lettres
    for i, mot in enumerate(mots):
        if len(mot) > 5:
            mots[i] = mot.upper()
    
    # Ajoute numérotation
    mots = [f"{i+1}.{mot}" for i, mot in enumerate(mots)]
    
    return ' '.join(mots)
```

### 4. Utilisation de join() (25 min)

#### A. Bases de join()
```python
# Join basique
mots = ['Python', 'est', 'génial']
phrase = ' '.join(mots)
print(phrase)  # "Python est génial"

# Join avec différents séparateurs
fruits = ['pomme', 'banane', 'orange']
liste = ', '.join(fruits)  # "pomme, banane, orange"
chemin = '/'.join(['dossier', 'sous-dossier', 'fichier.txt'])

# Join avec conversion automatique
nombres = [1, 2, 3, 4, 5]
texte = '-'.join(str(n) for n in nombres)  # "1-2-3-4-5"
```

#### B. Applications avancées
```python
def creer_ligne_csv(donnees):
    """Crée une ligne CSV à partir d'une liste."""
    return ','.join(str(d) for d in donnees)

def assembler_paragraphes(paragraphes):
    """Assemble des paragraphes avec deux sauts de ligne."""
    return '\n\n'.join(paragraphes)

def formater_table(lignes):
    """Crée une table formatée."""
    return '\n'.join(
        '|' + '|'.join(str(cell).center(10) for cell in ligne) + '|'
        for ligne in lignes
    )
```

### 5. Exemples complets de workflow (20 min)

#### A. Traitement de texte
```python
def formater_texte(texte):
    """Exemple complet de traitement de texte."""
    # 1. Split en phrases
    phrases = [p.strip() for p in texte.split('.') if p.strip()]
    
    # 2. Traitement de chaque phrase
    phrases_traitees = []
    for phrase in phrases:
        # Split en mots
        mots = phrase.split()
        
        # Capitalize premier mot
        mots[0] = mots[0].capitalize()
        
        # Traitement des autres mots
        for i in range(1, len(mots)):
            # Mettre en minuscules sauf noms propres
            if not mots[i].istitle():
                mots[i] = mots[i].lower()
        
        # Rejoindre les mots
        phrases_traitees.append(' '.join(mots))
    
    # 3. Rejoindre les phrases
    return '. '.join(phrases_traitees) + '.'
```

#### B. Manipulation de données
```python
def traiter_donnees(texte_donnees):
    """Traitement complet de données textuelles."""
    # 1. Split en lignes
    lignes = texte_donnees.split('\n')
    
    # 2. Traitement de chaque ligne
    donnees_traitees = []
    for ligne in lignes:
        # Split en champs
        champs = ligne.split(',')
        
        # Nettoyage et validation
        champs = [c.strip() for c in champs]
        if all(champs):  # Vérifie que tous les champs sont non vides
            # Transformation des données
            champs[0] = champs[0].upper()  # ID en majuscules
            champs[1] = champs[1].title()  # Nom propre
            champs[2] = f"{float(champs[2]):.2f}"  # Format nombre
            
            donnees_traitees.append(champs)
    
    # 3. Reconstitution du texte
    return '\n'.join(','.join(ligne) for ligne in donnees_traitees)
```

### Phase de pratique (15 min)

Exercices :

1. Formatage de texte :
```python
def formatter_noms(texte):
    """
    Prend un texte avec des noms séparés par des virgules
    et retourne une liste formatée avec chaque nom
    capitalisé et numéroté
    """
    # À compléter
```

2. Traitement de données :
```python
def traiter_adresses(donnees):
    """
    Prend des adresses au format "rue, ville, code"
    et retourne un format standardisé avec
    villes en majuscules et codes postaux formatés
    """
    # À compléter
```

### Synthèse (5 min)
- Immuabilité vs mutabilité
- Utilisation de split() et ses options
- Modifications possibles sur les listes
- Utilisation de join() et reconstitution

## Points importants à retenir :

1. Concepts clés :
   - Chaînes immuables
   - Listes mutables
   - Conversion réversible

2. Méthodes essentielles :
   - split() pour convertir chaîne -> liste
   - Méthodes de liste pour modifications
   - join() pour convertir liste -> chaîne

3. Bonnes pratiques :
   - Vérifier les données d'entrée
   - Traiter les cas spéciaux
   - Optimiser les conversions