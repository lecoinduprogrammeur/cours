# Plan de leçon : Structure de packages, modules et fonctions

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Organisation du code en packages
- Durée prévue : 2h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'organisation du code en packages

- Objectifs disciplinaires :
  - Comprendre la structure des packages
  - Savoir créer et organiser des modules
  - Maîtriser les imports et les dépendances
  - Gérer la documentation et les tests

## Déroulement de la leçon

### 1. Structure basique d'un package (30 min)

```
mon_package/
    ├── __init__.py
    ├── module1.py
    ├── module2.py
    ├── config.py
    ├── utils/
    │   ├── __init__.py
    │   ├── helpers.py
    │   └── formatters.py
    └── tests/
        ├── __init__.py
        ├── test_module1.py
        └── test_module2.py
```

#### A. Fichier __init__.py principal
```python
# mon_package/__init__.py
"""
Mon Package - Description du package

Ce package fournit des fonctionnalités pour...
"""

from .module1 import fonction1, Classe1
from .module2 import fonction2
from .config import CONFIG

__version__ = "1.0.0"
__author__ = "Votre Nom"

# Exposer les éléments publics
__all__ = ['fonction1', 'fonction2', 'Classe1', 'CONFIG']
```

#### B. Modules principaux
```python
# mon_package/module1.py
"""Module contenant les fonctionnalités principales."""

from .config import CONFIG
from .utils.helpers import helper_function

class Classe1:
    """Classe principale du module."""
    def __init__(self):
        self.config = CONFIG
    
    def methode1(self):
        """Première méthode."""
        return helper_function()

def fonction1():
    """Fonction principale du module."""
    return "Fonction 1"
```

### 2. Structure des sous-packages (25 min)

#### A. Organisation des utilitaires
```python
# mon_package/utils/__init__.py
"""
Sous-package d'utilitaires.
Contient des fonctions et classes d'aide.
"""

from .helpers import helper_function
from .formatters import format_text

__all__ = ['helper_function', 'format_text']

# mon_package/utils/helpers.py
def helper_function():
    """Fonction d'aide."""
    return "Helper"

# mon_package/utils/formatters.py
def format_text(text):
    """Formate le texte selon les standards."""
    return text.strip().upper()
```

#### B. Configuration
```python
# mon_package/config.py
"""Configuration globale du package."""

import os
from typing import Dict, Any

CONFIG: Dict[str, Any] = {
    "debug": os.getenv("DEBUG", "False").lower() == "true",
    "encoding": "utf-8",
    "timeout": 30,
    "base_url": "https://api.example.com"
}

def get_config() -> Dict[str, Any]:
    """Retourne une copie de la configuration."""
    return CONFIG.copy()

def update_config(key: str, value: Any) -> None:
    """Met à jour la configuration."""
    CONFIG[key] = value
```

### 3. Organisation des imports (25 min)

#### A. Imports relatifs
```python
# Imports depuis le même package
from . import module2
from .config import CONFIG
from .utils import helper_function

# Imports depuis un parent
from .. import autre_package
from ..utils import autre_fonction

# Imports absolus
import json
from typing import List, Dict
from datetime import datetime
```

#### B. Gestion des dépendances
```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="mon_package",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0',
        'pandas>=1.2.0'
    ],
    python_requires='>=3.8'
)

# requirements.txt
requests>=2.25.0
pandas>=1.2.0
pytest>=6.0.0  # pour les tests
```

### 4. Documentation (25 min)

#### A. Docstrings
```python
# mon_package/module1.py
"""
Module principal contenant les fonctionnalités de base.

Ce module fournit les classes et fonctions suivantes :
- Classe1 : Classe principale pour...
- fonction1 : Fonction pour...
"""

from typing import Optional, List

class Classe1:
    """
    Classe principale du module.
    
    Attributes:
        attribut1 (str): Description de l'attribut
        attribut2 (List[int]): Liste des valeurs
        
    Examples:
        >>> obj = Classe1()
        >>> obj.methode1()
        'résultat'
    """
    
    def methode1(self) -> str:
        """
        Première méthode de la classe.
        
        Returns:
            str: Description du retour
            
        Raises:
            ValueError: Si les conditions ne sont pas remplies
        """
        return "résultat"
```

#### B. README et documentation
```markdown
# Mon Package

Description courte du package.

## Installation

```bash
pip install mon-package
```

## Utilisation

```python
from mon_package import Classe1
obj = Classe1()
resultat = obj.methode1()
```

## Documentation

Pour plus d'informations, voir [la documentation complète](docs/index.md).

## Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit les changements (`git commit -am 'Ajout de fonctionnalité'`)
4. Push la branche (`git push origin feature/amelioration`)
5. Créer une Pull Request
```

### 5. Tests (25 min)

#### A. Structure des tests
```python
# tests/test_module1.py
"""Tests pour module1."""

import pytest
from mon_package.module1 import Classe1, fonction1

def test_fonction1():
    """Teste fonction1."""
    assert fonction1() == "Fonction 1"

class TestClasse1:
    """Tests pour Classe1."""
    
    @pytest.fixture
    def instance(self):
        """Crée une instance de test."""
        return Classe1()
    
    def test_methode1(self, instance):
        """Teste methode1."""
        assert instance.methode1() == "résultat"
        
    def test_erreur(self, instance):
        """Teste la gestion d'erreur."""
        with pytest.raises(ValueError):
            instance.methode_erreur()
```

#### B. Exécution des tests
```bash
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*

# Configuration de coverage
[coverage:run]
source = mon_package
omit = tests/*

# Commandes
pytest tests/
pytest tests/ -v  # verbose
pytest tests/ -v --cov=mon_package  # avec coverage
```

### 6. Application complète (25 min)

```python
# Exemple d'application complète
mon_package/
    ├── __init__.py
    ├── config.py
    ├── api/
    │   ├── __init__.py
    │   ├── client.py
    │   └── endpoints.py
    ├── models/
    │   ├── __init__.py
    │   ├── user.py
    │   └── product.py
    ├── utils/
    │   ├── __init__.py
    │   ├── validators.py
    │   └── formatters.py
    └── tests/
        ├── __init__.py
        ├── test_api/
        │   └── test_client.py
        └── test_models/
            └── test_user.py
```

### Phase de pratique (15 min)

Exercices :

1. Création de package :
```python
def creer_package_base():
    """
    Créer un package simple avec :
    - Structure de base
    - Documentation
    - Tests unitaires
    """
    # À compléter
```

2. Organisation avancée :
```python
def organiser_package_complexe():
    """
    Créer un package plus complexe avec :
    - Sous-modules
    - API
    - Tests complets
    """
    # À compléter
```

### Synthèse (5 min)
- Structure des packages
- Organisation des modules
- Documentation
- Tests

## Points importants à retenir :

1. Structure :
   - Hiérarchie claire
   - Séparation des responsabilités
   - Organisation logique

2. Documentation :
   - Docstrings complets
   - README clair
   - Documentation utilisateur

3. Tests :
   - Tests unitaires
   - Tests d'intégration
   - Couverture de code