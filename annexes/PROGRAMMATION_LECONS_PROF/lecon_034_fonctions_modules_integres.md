# Fonctions et modules intégrés Python

## 1. Fonctions intégrées (Built-in Functions)

### A. Fonctions de type et conversion
```python
# Conversion de types
int()       # Convertit en entier
float()     # Convertit en flottant
str()       # Convertit en chaîne
bool()      # Convertit en booléen
list()      # Convertit en liste
tuple()     # Convertit en tuple
set()       # Convertit en ensemble
dict()      # Convertit en dictionnaire
complex()   # Crée un nombre complexe

# Vérification de types
type()      # Retourne le type d'un objet
isinstance() # Vérifie si un objet est d'un certain type
issubclass() # Vérifie les relations d'héritage
```

### B. Fonctions mathématiques et numériques
```python
abs()       # Valeur absolue
round()     # Arrondit un nombre
pow()       # Puissance
divmod()    # Division et modulo
sum()       # Somme d'un itérable
max()       # Maximum
min()       # Minimum
len()       # Longueur d'une séquence
```

### C. Fonctions d'itération et de séquence
```python
range()     # Génère une séquence de nombres
enumerate() # Énumère un itérable
zip()       # Combine des itérables
map()       # Applique une fonction à un itérable
filter()    # Filtre un itérable
sorted()    # Trie un itérable
reversed()  # Inverse un itérable
iter()      # Crée un itérateur
next()      # Obtient l'élément suivant d'un itérateur
```

### D. Fonctions d'entrée/sortie et système
```python
print()     # Affiche des objets
input()     # Lit une entrée utilisateur
open()      # Ouvre un fichier
repr()      # Représentation d'un objet
format()    # Formate une chaîne
```

### E. Fonctions d'aide et de documentation
```python
help()      # Affiche l'aide
dir()       # Liste les attributs d'un objet
vars()      # Dictionnaire des variables
globals()   # Dictionnaire des variables globales
locals()    # Dictionnaire des variables locales
```

## 2. Modules intégrés (Built-in Modules)

### A. Modules mathématiques et numériques
```python
# math - Fonctions mathématiques
import math
math.sqrt()  # Racine carrée
math.sin()   # Sinus
math.cos()   # Cosinus
math.pi      # Constante π

# random - Nombres aléatoires
import random
random.random()     # Nombre entre 0 et 1
random.randint()    # Entier aléatoire
random.choice()     # Choix aléatoire

# statistics - Statistiques
import statistics
statistics.mean()   # Moyenne
statistics.median() # Médiane
```

### B. Modules de manipulation de données
```python
# datetime - Dates et heures
import datetime
datetime.datetime.now()  # Date et heure actuelles

# json - Manipulation JSON
import json
json.dumps()  # Sérialisation
json.loads()  # Désérialisation

# csv - Fichiers CSV
import csv
csv.reader()  # Lecture CSV
csv.writer()  # Écriture CSV
```

### C. Modules système et OS
```python
# os - Système d'exploitation
import os
os.path        # Manipulation de chemins
os.listdir()   # Liste des fichiers
os.mkdir()     # Création de dossier

# sys - Configuration Python
import sys
sys.path       # Chemins de recherche
sys.version    # Version Python

# time - Temps et délais
import time
time.sleep()   # Pause
time.time()    # Timestamp
```

### D. Modules de texte et chaînes
```python
# string - Manipulation de chaînes
import string
string.ascii_letters  # Lettres
string.digits        # Chiffres

# re - Expressions régulières
import re
re.match()    # Recherche de motif
re.split()    # Division selon motif
```

### E. Modules de collections
```python
# collections - Conteneurs spéciaux
from collections import Counter, defaultdict, deque
Counter()      # Compteur d'occurrences
defaultdict()  # Dictionnaire avec valeur par défaut
deque()        # File double

# itertools - Outils d'itération
import itertools
itertools.count()     # Compteur infini
itertools.cycle()     # Cycle infini
itertools.permutations()  # Permutations
```

### F. Modules réseau et internet
```python
# urllib - Manipulation URLs
import urllib.request
urllib.request.urlopen()  # Ouvre une URL

# http - Serveur HTTP
import http.server
http.server.HTTPServer   # Serveur HTTP

# socket - Communication réseau
import socket
socket.socket()     # Création socket
```

### G. Modules de débogage et tests
```python
# unittest - Tests unitaires
import unittest
unittest.TestCase   # Cas de test

# logging - Journalisation
import logging
logging.info()     # Log d'information
logging.error()    # Log d'erreur

# pdb - Débogueur
import pdb
pdb.set_trace()    # Point d'arrêt
```

### H. Modules de compression
```python
# gzip - Compression gzip
import gzip
gzip.open()        # Ouvre fichier gzip

# zipfile - Fichiers ZIP
import zipfile
zipfile.ZipFile()  # Manipulation ZIP
```

### I. Modules de cryptographie
```python
# hashlib - Hachage cryptographique
import hashlib
hashlib.md5()      # Hachage MD5
hashlib.sha256()   # Hachage SHA-256

# secrets - Génération sécurisée
import secrets
secrets.token_hex()  # Token hexadécimal
```

## 3. Modules d'interface utilisateur
```python
# tkinter - Interface graphique
import tkinter
tkinter.Tk()       # Fenêtre principale

# cmd - Interface ligne de commande
import cmd
cmd.Cmd            # Interpréteur de commandes
```

## Points importants à retenir :

1. Fonctions intégrées :
   - Disponibles sans import
   - Fonctions de base essentielles
   - Conversions et manipulations courantes

2. Modules standard :
   - Nécessitent un import
   - Organisés par catégorie
   - Fonctionnalités spécialisées

3. Bonnes pratiques :
   - Importer uniquement le nécessaire
   - Utiliser des alias appropriés
   - Grouper les imports par catégorie