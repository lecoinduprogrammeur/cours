# Plan de leçon : Programmation modulaire

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Organisation modulaire du code
- Durée prévue : 2h00

## Structure du projet exemple
```
mon_projet/
    ├── main.py
    ├── config/
    │   ├── __init__.py
    │   └── settings.py
    ├── models/
    │   ├── __init__.py
    │   ├── utilisateur.py
    │   └── produit.py
    ├── utils/
    │   ├── __init__.py
    │   ├── database.py
    │   └── validateurs.py
    └── tests/
        ├── __init__.py
        ├── test_utilisateur.py
        └── test_produit.py
```

## Déroulement de la leçon

### 1. Organisation des modules (25 min)

#### A. Configuration (config/settings.py)
```python
"""Module de configuration de l'application."""

# Configuration de la base de données
DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'name': 'app_db',
    'user': 'admin'
}

# Configuration générale
DEBUG = True
VERSION = "1.0.0"
MAX_ITEMS = 100

# Chemins importants
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
```

#### B. Utilitaires (utils/database.py)
```python
"""Module de gestion de la base de données."""

from typing import Any, Dict, List
from ..config.settings import DATABASE

class DatabaseConnection:
    """Gestionnaire de connexion à la base de données."""
    
    def __init__(self):
        self.host = DATABASE['host']
        self.connected = False
    
    def connect(self) -> bool:
        """Établit la connexion."""
        # Logique de connexion
        self.connected = True
        return True
    
    def execute_query(self, query: str) -> List[Dict[str, Any]]:
        """Exécute une requête SQL."""
        if not self.connected:
            raise ConnectionError("Non connecté")
        # Logique d'exécution
        return []
```

### 2. Modèles de données (30 min)

#### A. Classe de base (models/base.py)
```python
"""Module contenant la classe de base pour les modèles."""

from typing import Dict, Any
from datetime import datetime

class BaseModel:
    """Classe de base pour tous les modèles."""
    
    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertit l'objet en dictionnaire."""
        return {
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    def update(self, data: Dict[str, Any]) -> None:
        """Met à jour les attributs de l'objet."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
```

#### B. Modèle utilisateur (models/utilisateur.py)
```python
"""Module de gestion des utilisateurs."""

from typing import Optional
from .base import BaseModel
from ..utils.validateurs import valider_email

class Utilisateur(BaseModel):
    """Représente un utilisateur dans le système."""
    
    def __init__(self, nom: str, email: str):
        super().__init__()
        self.nom = nom
        self.email = self._valider_email(email)
        self._mot_de_passe: Optional[str] = None
    
    def _valider_email(self, email: str) -> str:
        """Valide et retourne l'email."""
        if not valider_email(email):
            raise ValueError("Email invalide")
        return email.lower()
    
    def to_dict(self) -> dict:
        """Surcharge pour inclure les attributs spécifiques."""
        base_dict = super().to_dict()
        return {
            **base_dict,
            'nom': self.nom,
            'email': self.email
        }
```

### 3. Validateurs et Utilitaires (20 min)

```python
# utils/validateurs.py
"""Module contenant les fonctions de validation."""

import re
from typing import Any, Callable

def valider_email(email: str) -> bool:
    """Valide un format d'email."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def valider_chaine(min_length: int = 1, max_length: int = 100) -> Callable:
    """Retourne un validateur de chaîne."""
    def validateur(texte: str) -> bool:
        return isinstance(texte, str) and min_length <= len(texte) <= max_length
    return validateur

def valider_nombre(min_val: float, max_val: float) -> Callable:
    """Retourne un validateur de nombre."""
    def validateur(valeur: Any) -> bool:
        try:
            nombre = float(valeur)
            return min_val <= nombre <= max_val
        except (TypeError, ValueError):
            return False
    return validateur
```

### 4. Programme principal (25 min)

```python
# main.py
"""Point d'entrée principal de l'application."""

from typing import List, Optional
from config.settings import VERSION
from models.utilisateur import Utilisateur
from utils.database import DatabaseConnection

class Application:
    """Classe principale de l'application."""
    
    def __init__(self):
        self.version = VERSION
        self.db = DatabaseConnection()
        self.utilisateurs: List[Utilisateur] = []
    
    def demarrer(self) -> None:
        """Démarre l'application."""
        print(f"Démarrage de l'application v{self.version}")
        self.db.connect()
    
    def creer_utilisateur(self, nom: str, email: str) -> Utilisateur:
        """Crée un nouvel utilisateur."""
        utilisateur = Utilisateur(nom, email)
        self.utilisateurs.append(utilisateur)
        return utilisateur
    
    def rechercher_utilisateur(self, email: str) -> Optional[Utilisateur]:
        """Recherche un utilisateur par email."""
        for utilisateur in self.utilisateurs:
            if utilisateur.email == email.lower():
                return utilisateur
        return None

def main():
    """Fonction principale."""
    app = Application()
    app.demarrer()
    
    try:
        # Exemple d'utilisation
        user = app.creer_utilisateur("Alice", "alice@example.com")
        print(f"Utilisateur créé: {user.to_dict()}")
    except ValueError as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    main()
```

### 5. Tests unitaires (15 min)

```python
# tests/test_utilisateur.py
"""Tests pour le module utilisateur."""

import unittest
from models.utilisateur import Utilisateur

class TestUtilisateur(unittest.TestCase):
    
    def setUp(self):
        """Initialisation avant chaque test."""
        self.nom = "Test User"
        self.email = "test@example.com"
    
    def test_creation_utilisateur(self):
        """Teste la création d'un utilisateur."""
        user = Utilisateur(self.nom, self.email)
        self.assertEqual(user.nom, self.nom)
        self.assertEqual(user.email, self.email)
    
    def test_email_invalide(self):
        """Teste la validation d'email."""
        with self.assertRaises(ValueError):
            Utilisateur(self.nom, "email_invalide")
    
    def test_to_dict(self):
        """Teste la conversion en dictionnaire."""
        user = Utilisateur(self.nom, self.email)
        data = user.to_dict()
        self.assertIn('nom', data)
        self.assertIn('email', data)
        self.assertEqual(data['nom'], self.nom)
```

### 6. Gestion des dépendances (15 min)

```python
# requirements.txt
pytest==7.3.1
python-dotenv==0.19.2
requests==2.26.0

# setup.py
from setuptools import setup, find_packages

setup(
    name="mon_projet",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'pytest>=7.3.1',
        'python-dotenv>=0.19.2',
        'requests>=2.26.0'
    ],
    python_requires='>=3.8'
)
```

## Points importants à retenir :

1. Organisation :
   - Structure claire des dossiers
   - Séparation des responsabilités
   - Imports bien organisés

2. Modularité :
   - Modules indépendants
   - Réutilisation du code
   - Maintenance facilitée

3. Bonnes pratiques :
   - Documentation claire
   - Tests unitaires
   - Gestion des dépendances

4. Avantages :
   - Code plus maintenable
   - Réutilisation facilitée
   - Tests simplifiés
   - Collaboration améliorée
