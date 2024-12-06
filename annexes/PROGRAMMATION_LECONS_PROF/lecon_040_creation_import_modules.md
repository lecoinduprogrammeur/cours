# Plan de leçon : Création et importation de modules

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Création et utilisation de modules
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser la création et l'importation de modules

- Objectifs disciplinaires :
  - Comprendre la structure d'un module
  - Maîtriser les différentes méthodes d'importation
  - Savoir organiser son code en modules
  - Gérer les espaces de noms

## Déroulement de la leçon

### 1. Création d'un module (30 min)

#### A. Structure de base d'un module
```python
# mon_module.py

"""
Documentation du module.
Décrit le but et l'utilisation du module.
"""

# Imports nécessaires
import math
from datetime import datetime

# Variables du module
VERSION = "1.0.0"
AUTEUR = "John Doe"

# Fonctions
def addition(a, b):
    """Addition de deux nombres."""
    return a + b

def soustraction(a, b):
    """Soustraction de deux nombres."""
    return a - b

# Classes
class Calculator:
    """Classe de calculs mathématiques."""
    def __init__(self):
        self.historique = []
    
    def calculer(self, a, b, operation):
        resultat = operation(a, b)
        self.historique.append((a, b, resultat))
        return resultat

# Code exécuté lors de l'importation
print(f"Module {__name__} chargé")

# Code exécuté uniquement si le fichier est lancé directement
if __name__ == "__main__":
    # Tests du module
    print(addition(2, 3))
    calc = Calculator()
```

#### B. Bonnes pratiques
```python
# utilitaires.py

# 1. Documentation claire
"""
Module d'utilitaires génériques.
Contient des fonctions d'aide pour le traitement de données.
"""

# 2. Organisation logique des imports
from typing import List, Dict  # Types
import json  # Bibliothèque standard
from .helpers import formater  # Imports locaux

# 3. Variables globales en majuscules
DEFAULT_ENCODING = 'utf-8'
MAX_RETRIES = 3

# 4. Documentation des fonctions
def parser_donnees(chemin: str) -> Dict:
    """
    Parse un fichier de données.
    
    Args:
        chemin (str): Chemin vers le fichier
        
    Returns:
        Dict: Données parsées
        
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
    """
    try:
        with open(chemin, 'r', encoding=DEFAULT_ENCODING) as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Fichier non trouvé: {chemin}")
```

### 2. Méthodes d'importation (25 min)

#### A. Import basique
```python
# Import complet
import mon_module
resultat = mon_module.addition(2, 3)

# Import avec alias
import mon_module as mm
resultat = mm.addition(2, 3)

# Import sélectif
from mon_module import addition, soustraction
resultat = addition(2, 3)

# Import avec renommage
from mon_module import addition as add
resultat = add(2, 3)

# Import de tout (déconseillé)
from mon_module import *  # Éviter cette syntaxe
```

#### B. Organisation des imports
```python
# Ordre recommandé des imports
# 1. Imports de la bibliothèque standard
import os
import sys
from datetime import datetime

# 2. Imports tiers
import numpy as np
import pandas as pd

# 3. Imports locaux
from .mon_module import addition
from ..utils import helper
```

### 3. Packages et sous-modules (30 min)

#### A. Structure d'un package
```
mon_package/
    __init__.py
    module1.py
    module2.py
    sous_package/
        __init__.py
        module3.py
```

```python
# mon_package/__init__.py
"""
Initialisation du package.
"""
from .module1 import fonction1
from .module2 import fonction2

__version__ = "1.0.0"
```

#### B. Imports relatifs
```python
# mon_package/module1.py
from . import module2  # Import depuis le même package
from .sous_package import module3  # Import depuis un sous-package
from .. import autre_package  # Import depuis le parent
```

### 4. Gestion des espaces de noms (20 min)

```python
# module_a.py
var_a = "Module A"
def fonction_a():
    return "Fonction A"

# module_b.py
var_b = "Module B"
def fonction_b():
    return "Fonction B"

# main.py
import module_a
import module_b

# Espaces de noms séparés
print(module_a.var_a)
print(module_b.var_b)

# Éviter les conflits
from module_a import fonction_a as fa
from module_b import fonction_b as fb
```

### 5. Applications pratiques (25 min)

#### A. Organisation d'une application
```python
# config.py
"""Configuration générale de l'application."""
DATABASE_URL = "sqlite:///app.db"
DEBUG = True

# database.py
"""Module de gestion de la base de données."""
from .config import DATABASE_URL

def connecter():
    """Établit la connexion à la base de données."""
    pass

# utils.py
"""Utilitaires génériques."""
def formater_date(date):
    """Formate une date selon le standard de l'application."""
    pass

# main.py
"""Point d'entrée de l'application."""
from .config import DEBUG
from .database import connecter
from .utils import formater_date

def main():
    if DEBUG:
        print("Mode debug activé")
    # ...
```

#### B. Exemple de package complet
```python
# monapp/
#   __init__.py
#   config.py
#   models/
#       __init__.py
#       user.py
#       product.py
#   utils/
#       __init__.py
#       format.py
#       validation.py
#   main.py

# monapp/models/user.py
"""Modèle utilisateur."""
from ..config import USER_TABLE
from ..utils.validation import valider_email

class User:
    def __init__(self, email):
        if not valider_email(email):
            raise ValueError("Email invalide")
        self.email = email
```

### 6. Tests et débogage (15 min)

```python
# mon_module.py
def fonction_test():
    """Fonction de test."""
    return True

if __name__ == "__main__":
    # Tests
    assert fonction_test() == True
    print("Tests passés!")

# test_module.py
import unittest
from mon_module import fonction_test

class TestMonModule(unittest.TestCase):
    def test_fonction(self):
        self.assertTrue(fonction_test())
```

### Phase de pratique (15 min)

Exercices :

1. Création de package :
```python
def creer_structure_package():
    """
    Créer un package avec :
    - Plusieurs modules
    - Documentation
    - Tests
    """
    # À compléter
```

2. Organisation de code :
```python
def reorganiser_application():
    """
    Réorganiser une application en :
    - Modules logiques
    - Package structuré
    - Imports optimisés
    """
    # À compléter
```

### Synthèse (5 min)
- Structure des modules
- Méthodes d'importation
- Organisation en packages
- Bonnes pratiques

## Points importants à retenir :

1. Structure :
   - Documentation claire
   - Organisation logique
   - Tests intégrés

2. Importation :
   - Différentes méthodes
   - Organisation des imports
   - Imports relatifs

3. Bonnes pratiques :
   - Modules cohérents
   - Documentation complète
   - Tests appropriés