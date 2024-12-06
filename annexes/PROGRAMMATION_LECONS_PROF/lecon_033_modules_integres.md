# Plan de leçon : Modules intégrés Python

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Importation et utilisation des modules intégrés
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'importation et l'utilisation des modules intégrés

- Objectifs disciplinaires :
  - Comprendre les différentes méthodes d'importation
  - Maîtriser l'utilisation des modules courants
  - Connaître les modules disponibles
  - Appliquer les bonnes pratiques d'importation

## Déroulement de la leçon

### 1. Méthodes d'importation (20 min)

#### A. Syntaxes d'importation
```python
# Importation complète
import math
resultat = math.sqrt(16)  # 4.0

# Importation avec alias
import math as m
resultat = m.sqrt(16)  # 4.0

# Importation sélective
from math import sqrt, pi
resultat = sqrt(16)  # 4.0
print(pi)  # 3.141592653589793

# Importation de tout
from math import *  # Déconseillé
resultat = sqrt(16)  # 4.0
```

#### B. Bonnes pratiques
```python
# Préférer les imports spécifiques
from math import sqrt, cos, sin  # Mieux que from math import *

# Regrouper les imports
import math
import random
import datetime

# Ordre des imports (convention)
# 1. Imports de la bibliothèque standard
import os
import sys
# 2. Imports tiers
import numpy as np
# 3. Imports locaux
from .mon_module import ma_fonction
```

### 2. Le module math en détail (25 min)

#### A. Constantes mathématiques
```python
import math

# Constantes importantes
print(math.pi)       # π (3.141592653589793)
print(math.e)        # e (2.718281828459045)
print(math.tau)      # τ (6.283185307179586)
print(math.inf)      # Infini
print(math.nan)      # Not a Number
```

#### B. Fonctions mathématiques courantes
```python
import math

# Fonctions de base
print(math.sqrt(16))       # Racine carrée: 4.0
print(math.pow(2, 3))      # Puissance: 8.0
print(math.fabs(-4.2))     # Valeur absolue: 4.2

# Fonctions trigonométriques
print(math.sin(math.pi/2))  # Sinus: 1.0
print(math.cos(0))          # Cosinus: 1.0
print(math.tan(math.pi/4))  # Tangente: 1.0

# Arrondis
print(math.ceil(3.1))      # Arrondi supérieur: 4
print(math.floor(3.9))     # Arrondi inférieur: 3
print(math.trunc(3.9))     # Troncature: 3

# Logarithmes et exponentielles
print(math.log(10))        # Logarithme naturel
print(math.log10(100))     # Logarithme base 10
print(math.exp(1))         # e^1
```

### 3. Liste des modules intégrés principaux (30 min)

#### A. Modules de base
```python
# datetime - Gestion des dates et heures
import datetime
date = datetime.datetime.now()

# random - Génération de nombres aléatoires
import random
nombre = random.randint(1, 10)

# os - Interface avec le système d'exploitation
import os
fichiers = os.listdir('.')

# sys - Variables et fonctions spécifiques au système
import sys
version = sys.version

# time - Fonctions liées au temps
import time
time.sleep(1)  # Pause d'une seconde

# json - Manipulation de données JSON
import json
donnees = json.dumps({'nom': 'Python'})
```

#### B. Modules de traitement de données
```python
# collections - Conteneurs spécialisés
from collections import Counter, defaultdict
compteur = Counter(['a', 'b', 'a'])

# itertools - Itérateurs avancés
import itertools
permutations = list(itertools.permutations([1, 2, 3]))

# functools - Outils pour fonctions
from functools import reduce
somme = reduce(lambda x, y: x + y, [1, 2, 3])

# statistics - Calculs statistiques
import statistics
moyenne = statistics.mean([1, 2, 3, 4])
```

### 4. Modules spécialisés (20 min)

```python
# re - Expressions régulières
import re
motif = re.compile(r'\d+')
resultat = motif.findall('abc123def456')

# pathlib - Gestion des chemins de fichiers
from pathlib import Path
chemin = Path('dossier/fichier.txt')

# urllib - Gestion des URLs
from urllib.request import urlopen
# page = urlopen('https://python.org')

# sqlite3 - Base de données SQLite
import sqlite3
conn = sqlite3.connect('base.db')

# csv - Manipulation de fichiers CSV
import csv
with open('donnees.csv', 'r') as f:
    lecteur = csv.reader(f)

# hashlib - Fonctions de hachage
import hashlib
hash_md5 = hashlib.md5(b"texte").hexdigest()
```

### 5. Liste complète des modules intégrés importants

#### A. Traitement de données
```python
# Modules de base
- builtins: Fonctions et types intégrés
- abc: Classes abstraites
- array: Tableaux de valeurs
- collections: Conteneurs spécialisés
- copy: Opérations de copie
- enum: Support pour énumérations
- numbers: Nombres abstraits
- math: Fonctions mathématiques
- cmath: Nombres complexes
- decimal: Arithmétique décimale
- fractions: Nombres rationnels
- random: Génération de nombres aléatoires
- statistics: Calculs statistiques
```

#### B. Manipulation de texte
```python
# Modules texte
- string: Opérations sur les chaînes
- re: Expressions régulières
- difflib: Comparaison de séquences
- textwrap: Formatage de texte
- unicodedata: Base de données Unicode
```

#### C. Gestion de données
```python
# Modules données
- datetime: Dates et heures
- calendar: Calendriers
- collections: Collections spécialisées
- heapq: Files de priorité
- bisect: Algorithmes de tri
- array: Tableaux homogènes
- weakref: Références faibles
```

#### D. Système et fichiers
```python
# Modules système
- os: Interface système d'exploitation
- sys: Configuration Python
- time: Fonctions temps
- argparse: Analyse arguments ligne de commande
- logging: Journalisation
- platform: Accès aux données de la plateforme
- io: Outils d'E/S principaux
```

#### E. Internet et réseaux
```python
# Modules réseau
- urllib: Gestion des URLs
- http: Clients HTTP
- ftplib: Client FTP
- poplib: Client POP3
- imaplib: Client IMAP4
- smtplib: Client SMTP
- socketserver: Framework serveur réseau
```

### 6. Applications pratiques (15 min)

```python
# Exemple d'utilisation combinée
import math
import statistics
import random
from datetime import datetime

def analyser_donnees(taille_echantillon):
    """Exemple d'utilisation de plusieurs modules."""
    # Générer des données
    donnees = [random.gauss(0, 1) for _ in range(taille_echantillon)]
    
    # Calculer des statistiques
    stats = {
        'moyenne': statistics.mean(donnees),
        'mediane': statistics.median(donnees),
        'ecart_type': statistics.stdev(donnees),
        'max': max(donnees),
        'min': min(donnees)
    }
    
    # Arrondir les résultats
    stats = {k: math.ceil(v * 100) / 100 for k, v in stats.items()}
    
    # Ajouter horodatage
    stats['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return stats
```

### Phase de pratique (15 min)

Exercices :

1. Calculatrice scientifique :
```python
def calculatrice_scientifique():
    """
    Créer une calculatrice utilisant :
    - math pour les calculs
    - statistics pour les analyses
    - datetime pour l'historique
    """
    # À compléter
```

2. Gestionnaire de données :
```python
def gestionnaire_donnees():
    """
    Créer un gestionnaire qui :
    - Lit des données (csv)
    - Les analyse (statistics)
    - Les sauvegarde (json)
    """
    # À compléter
```

### Synthèse (5 min)
- Méthodes d'importation
- Modules principaux
- Applications pratiques
- Bonnes pratiques

## Points importants à retenir :

1. Importation :
   - Différentes syntaxes
   - Choix de la méthode appropriée
   - Organisation des imports

2. Modules essentiels :
   - math pour les calculs
   - datetime pour les dates
   - os/sys pour le système
   - json/csv pour les données

3. Bonnes pratiques :
   - Imports spécifiques
   - Organisation des imports
   - Documentation des dépendances