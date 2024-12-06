# Plan de leçon : if __name__ == '__main__'

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Utilisation de if __name__ == '__main__'
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Comprendre et maîtriser l'utilisation de if __name__ == '__main__'

- Objectifs disciplinaires :
  - Comprendre le rôle de __name__
  - Maîtriser l'exécution conditionnelle
  - Organiser son code efficacement
  - Gérer les imports de modules

## Déroulement de la leçon

### 1. Introduction à __name__ (20 min)

#### A. Concept de base
```python
# Affichage de __name__
print(f"Valeur de __name__: {__name__}")

# Dans un fichier principal
if __name__ == "__main__":
    print("Ce code s'exécute uniquement si le fichier est exécuté directement")

# Démonstration de la différence
# fichier: module.py
print(f"Dans module.py, __name__ est {__name__}")

# fichier: main.py
import module
print(f"Dans main.py, __name__ est {__name__}")
```

#### B. Comportement selon le contexte
```python
# module_exemple.py
print("Ce code s'exécute toujours")

def fonction_exemple():
    print("Fonction du module")

if __name__ == "__main__":
    print("Ce code s'exécute uniquement en direct")
    fonction_exemple()

# test_import.py
import module_exemple  # Seul "Ce code s'exécute toujours" s'affiche
```

### 2. Utilisations pratiques (25 min)

#### A. Tests et débogage
```python
# calculatrice.py
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

if __name__ == "__main__":
    # Tests de base
    print("Test addition:", addition(2, 3))
    print("Test soustraction:", soustraction(5, 2))
    
    # Tests plus complexes
    assert addition(0, 0) == 0, "Test addition zéros"
    assert soustraction(10, 10) == 0, "Test soustraction égaux"
    print("Tous les tests passés!")
```

#### B. Scripts autonomes
```python
# traitement_donnees.py
def charger_donnees(fichier):
    with open(fichier) as f:
        return f.readlines()

def traiter_donnees(donnees):
    return [ligne.strip().upper() for ligne in donnees]

def sauvegarder_donnees(donnees, fichier):
    with open(fichier, 'w') as f:
        f.writelines(donnees)

if __name__ == "__main__":
    # Script autonome
    import sys
    if len(sys.argv) != 3:
        print("Usage: python traitement_donnees.py input.txt output.txt")
        sys.exit(1)
        
    donnees = charger_donnees(sys.argv[1])
    resultat = traiter_donnees(donnees)
    sauvegarder_donnees(resultat, sys.argv[2])
```

### 3. Organisation du code (20 min)

#### A. Séparation du code réutilisable
```python
# utilitaires.py
class GestionnaireFichiers:
    def __init__(self, fichier):
        self.fichier = fichier
    
    def lire(self):
        with open(self.fichier) as f:
            return f.read()

def formater_texte(texte):
    return texte.strip().upper()

if __name__ == "__main__":
    # Tests des fonctionnalités
    gestionnaire = GestionnaireFichiers("test.txt")
    texte = gestionnaire.lire()
    print(formater_texte(texte))
```

#### B. Structure modulaire
```python
# config.py
CONFIG = {
    "debug": True,
    "encoding": "utf-8"
}

def charger_config():
    return CONFIG.copy()

if __name__ == "__main__":
    # Vérification de la configuration
    config = charger_config()
    for cle, valeur in config.items():
        print(f"{cle}: {valeur}")

# application.py
from config import charger_config

def main():
    config = charger_config()
    # Utilisation de la configuration
    
if __name__ == "__main__":
    main()
```

### 4. Patrons de conception (20 min)

#### A. Patron de script
```python
# script.py
def parse_arguments():
    """Parse les arguments de la ligne de commande."""
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    return parser.parse_args()

def main():
    """Fonction principale du script."""
    args = parse_arguments()
    # Logique principale
    print(f"Traitement de {args.input} vers {args.output}")

if __name__ == "__main__":
    main()
```

#### B. Patron de bibliothèque
```python
# bibliotheque.py
class BibliothequeException(Exception):
    """Exception personnalisée pour la bibliothèque."""
    pass

class Bibliotheque:
    def __init__(self):
        self.initialise = False
    
    def initialiser(self):
        self.initialise = True
    
    def operation(self):
        if not self.initialise:
            raise BibliothequeException("Non initialisé")
        return "Opération réussie"

if __name__ == "__main__":
    # Tests de la bibliothèque
    bib = Bibliotheque()
    try:
        bib.operation()  # Doit échouer
    except BibliothequeException:
        print("Test d'erreur réussi")
    
    bib.initialiser()
    assert bib.operation() == "Opération réussie"
    print("Tous les tests passés!")
```

### 5. Bonnes pratiques (15 min)

```python
# Bonne structure de fichier
"""
Module de traitement de données.

Ce module fournit des fonctionnalités pour le traitement
de données textuelles.
"""

import sys
import logging
from typing import List, Optional

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def traiter_donnees(donnees: List[str]) -> List[str]:
    """Traite une liste de chaînes."""
    return [d.strip().upper() for d in donnees]

def main() -> Optional[int]:
    """Point d'entrée principal."""
    try:
        if len(sys.argv) != 2:
            print("Usage: python script.py fichier.txt")
            return 1
            
        with open(sys.argv[1]) as f:
            donnees = f.readlines()
        
        resultat = traiter_donnees(donnees)
        for ligne in resultat:
            print(ligne)
        
        return 0
    except Exception as e:
        logger.error(f"Erreur: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### Phase de pratique (15 min)

Exercices :

1. Script modulaire :
```python
def creer_script_modulaire():
    """
    Créer un script qui :
    - Peut être importé comme module
    - Peut être exécuté directement
    - Inclut des tests
    """
    # À compléter
```

2. Bibliothèque testable :
```python
def creer_bibliotheque():
    """
    Créer une bibliothèque qui :
    - Fournit des fonctionnalités réutilisables
    - Inclut des tests automatiques
    - Gère les erreurs proprement
    """
    # À compléter
```

### Synthèse (5 min)
- Rôle de __name__
- Organisation du code
- Tests et débogage
- Bonnes pratiques

## Points importants à retenir :

1. Utilisation :
   - Différencier exécution directe et import
   - Tests intégrés
   - Scripts autonomes

2. Organisation :
   - Séparation du code réutilisable
   - Structure modulaire
   - Gestion des erreurs

3. Bonnes pratiques :
   - Documentation claire
   - Tests appropriés
   - Gestion propre des erreurs