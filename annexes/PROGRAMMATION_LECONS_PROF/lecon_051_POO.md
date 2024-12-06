# Plan de leçon : POO et importation de classes

## Structure du projet
```
mon_projet/
    ├── main.py
    ├── models/
    │   ├── __init__.py
    │   ├── personne.py
    │   ├── compte.py
    │   └── vehicule.py
    └── utils/
        ├── __init__.py
        └── helpers.py
```

### 1. Création des classes (dans les fichiers séparés)

#### A. models/personne.py
```python
class Personne:
    """Classe représentant une personne."""
    
    def __init__(self, nom: str, age: int):
        """
        Constructeur de la classe Personne.
        
        Args:
            nom: Le nom de la personne
            age: L'âge de la personne
        """
        self.nom = nom
        self.age = age
        self._email = None  # Attribut protégé
    
    def presenter(self) -> str:
        """Retourne une présentation de la personne."""
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans"
    
    @property
    def email(self) -> str:
        """Getter pour l'email."""
        return self._email
    
    @email.setter
    def email(self, valeur: str) -> None:
        """Setter pour l'email avec validation."""
        if '@' not in valeur:
            raise ValueError("Email invalide")
        self._email = valeur
    
    def est_majeur(self) -> bool:
        """Vérifie si la personne est majeure."""
        return self.age >= 18
```

#### B. models/compte.py
```python
from decimal import Decimal

class CompteBancaire:
    """Classe représentant un compte bancaire."""
    
    def __init__(self, titulaire: str, solde_initial: float = 0):
        """
        Initialise un compte bancaire.
        
        Args:
            titulaire: Nom du titulaire
            solde_initial: Solde initial du compte
        """
        self.titulaire = titulaire
        self._solde = Decimal(str(solde_initial))
        self.__operations = []  # Attribut privé
    
    def deposer(self, montant: float) -> None:
        """
        Dépose de l'argent sur le compte.
        
        Args:
            montant: Montant à déposer
        
        Raises:
            ValueError: Si le montant est négatif
        """
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self._solde += Decimal(str(montant))
        self.__operations.append(("depot", montant))
    
    def retirer(self, montant: float) -> None:
        """Retire de l'argent du compte."""
        if Decimal(str(montant)) > self._solde:
            raise ValueError("Solde insuffisant")
        self._solde -= Decimal(str(montant))
        self.__operations.append(("retrait", montant))
    
    @property
    def solde(self) -> float:
        """Retourne le solde actuel."""
        return float(self._solde)
```

#### C. models/vehicule.py
```python
from typing import Optional

class Vehicule:
    """Classe représentant un véhicule."""
    
    # Attribut de classe
    nombre_vehicules = 0
    
    def __init__(self, marque: str, modele: str):
        self.marque = marque
        self.modele = modele
        self.proprietaire: Optional[str] = None
        Vehicule.nombre_vehicules += 1
    
    def __str__(self) -> str:
        """Représentation en chaîne du véhicule."""
        return f"{self.marque} {self.modele}"
    
    def affecter_proprietaire(self, nom: str) -> None:
        """Affecte un propriétaire au véhicule."""
        self.proprietaire = nom
    
    @classmethod
    def obtenir_nombre_vehicules(cls) -> int:
        """Retourne le nombre total de véhicules."""
        return cls.nombre_vehicules
```

### 2. Utilisation des classes (main.py)

```python
# Imports
from models.personne import Personne
from models.compte import CompteBancaire
from models.vehicule import Vehicule

def main():
    # Création d'objets
    personne = Personne("Alice", 25)
    compte = CompteBancaire(personne.nom, 1000)
    voiture = Vehicule("Toyota", "Corolla")
    
    # Utilisation des objets
    print(personne.presenter())
    personne.email = "alice@example.com"
    
    compte.deposer(500)
    print(f"Solde: {compte.solde}€")
    
    voiture.affecter_proprietaire(personne.nom)
    print(f"Propriétaire de la {voiture}: {voiture.proprietaire}")
    
    # Utilisation d'attributs de classe
    print(f"Nombre total de véhicules: {Vehicule.obtenir_nombre_vehicules()}")

if __name__ == "__main__":
    main()
```

### 3. Organisation des imports et bonnes pratiques

#### A. models/__init__.py
```python
"""Module contenant les modèles de l'application."""

from .personne import Personne
from .compte import CompteBancaire
from .vehicule import Vehicule

__all__ = ['Personne', 'CompteBancaire', 'Vehicule']
```

#### B. Import simplifié dans main.py
```python
from models import Personne, CompteBancaire, Vehicule
```

### 4. Héritage et polymorphisme

#### A. Exemple avec les véhicules
```python
# models/vehicule.py

class Vehicule:
    # ... (code précédent) ...
    
    def calculer_taxe(self) -> float:
        """Méthode à surcharger dans les classes dérivées."""
        raise NotImplementedError

class Voiture(Vehicule):
    def __init__(self, marque: str, modele: str, puissance: int):
        super().__init__(marque, modele)
        self.puissance = puissance
    
    def calculer_taxe(self) -> float:
        return self.puissance * 10

class Moto(Vehicule):
    def __init__(self, marque: str, modele: str, cylindree: int):
        super().__init__(marque, modele)
        self.cylindree = cylindree
    
    def calculer_taxe(self) -> float:
        return self.cylindree * 0.1
```

### 5. Tests unitaires

```python
# tests/test_personne.py
import unittest
from models import Personne

class TestPersonne(unittest.TestCase):
    def setUp(self):
        self.personne = Personne("Test", 20)
    
    def test_creation(self):
        self.assertEqual(self.personne.nom, "Test")
        self.assertEqual(self.personne.age, 20)
    
    def test_email_valide(self):
        self.personne.email = "test@example.com"
        self.assertEqual(self.personne.email, "test@example.com")
    
    def test_email_invalide(self):
        with self.assertRaises(ValueError):
            self.personne.email = "email_invalide"

if __name__ == '__main__':
    unittest.main()
```

### 6. Documentation complète

```python
"""
Module principal de l'application.

Ce module illustre l'utilisation des différentes classes
et leur interaction dans l'application.

Classes importées:
    - Personne: Gestion des informations personnelles
    - CompteBancaire: Gestion des comptes bancaires
    - Vehicule: Gestion des véhicules et dérivés

Exemple d'utilisation:
    >>> from models import Personne
    >>> personne = Personne("Alice", 25)
    >>> print(personne.presenter())
    "Je m'appelle Alice et j'ai 25 ans"
"""

# Imports et code du main.py
```

### 7. Exemple complet d'utilisation

```python
# main.py

from models import Personne, CompteBancaire, Vehicule
from models.vehicule import Voiture, Moto

def demonstration_complete():
    # Création des objets
    client = Personne("Alice", 25)
    client.email = "alice@example.com"
    
    compte = CompteBancaire(client.nom, 1000)
    compte.deposer(500)
    
    voiture = Voiture("Toyota", "Corolla", 110)
    voiture.affecter_proprietaire(client.nom)
    
    # Utilisation et interaction
    print(f"Client: {client.presenter()}")
    print(f"Email: {client.email}")
    print(f"Solde compte: {compte.solde}€")
    print(f"Véhicule: {voiture}")
    print(f"Taxe annuelle: {voiture.calculer_taxe()}€")
    
    # Gestion des erreurs
    try:
        compte.retirer(2000)  # Tentative de retrait excessif
    except ValueError as e:
        print(f"Erreur: {e}")
    
    # Statistiques
    print(f"Nombre total de véhicules: {Vehicule.obtenir_nombre_vehicules()}")

if __name__ == "__main__":
    demonstration_complete()
```

## Points importants à retenir :

1. Organisation :
   - Séparer les classes dans des fichiers distincts
   - Utiliser une structure de projet claire
   - Regrouper les imports dans __init__.py

2. Pratiques POO :
   - Constructeur bien défini
   - Encapsulation avec propriétés
   - Héritage et polymorphisme
   - Gestion des erreurs

3. Importation :
   - Imports relatifs dans les packages
   - Imports absolus dans main.py
   - Documentation des dépendances

4. Tests et documentation :
   - Tests unitaires pour chaque classe
   - Documentation claire et complète
   - Exemples d'utilisation
