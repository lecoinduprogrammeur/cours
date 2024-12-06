# Plan de leçon : Les commentaires et la documentation en Python

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Commentaires et docstrings
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les différentes formes de documentation du code Python

- Objectifs disciplinaires :
  - Comprendre l'importance et les types de commentaires
  - Maîtriser la syntaxe des docstrings
  - Savoir documenter fonctions, classes et modules
  - Appliquer les bonnes pratiques de documentation

- Objectifs transversaux :
  - Développer des habitudes de documentation
  - Améliorer la lisibilité du code
  - Favoriser la maintenance du code

## Prérequis
- Bases de la syntaxe Python
- Notions sur les fonctions et classes
- Compréhension de l'indentation Python

## Matériel et ressources
- Ordinateurs avec Python installé
- Éditeur de code avec coloration syntaxique
- Documentation PEP 257 (Docstring Conventions)
- Exemples de code bien documenté

## Déroulement de la leçon

### 1. Les commentaires simples (20 min)

#### A. Commentaire sur une ligne
```python
# Ceci est un commentaire sur une ligne
x = 42  # Commentaire en fin de ligne

# Mauvaise pratique
## Éviter les commentaires multiples
### Ne pas faire ça
```

#### B. Bonnes pratiques des commentaires
```python
# BIEN : Explique le pourquoi, pas le comment
age = int(input())  # Conversion en entier pour éviter les erreurs de type

# MAL : Décrit l'évidence
x = x + 1  # Ajoute 1 à x

# BIEN : Documentation des constantes
MAX_TENTATIVES = 3  # Limite les tentatives de connexion pour la sécurité

# BIEN : Explique un algorithme complexe
# Utilise l'algorithme de Fisher-Yates pour mélanger la liste
# de manière uniforme avec une complexité O(n)
def melanger_liste(liste):
    # ... code ...
```

### 2. Les docstrings (35 min)

#### A. Docstring de module
```python
"""Module de gestion des utilisateurs.

Ce module fournit les fonctionnalités de base pour la gestion
des utilisateurs, incluant la création, modification et suppression
de comptes utilisateurs.

Il implémente également les mécanismes de sécurité suivants:
    - Hachage des mots de passe
    - Validation des données
    - Journalisation des actions
"""

import hashlib
import logging
```

#### B. Docstring de fonction
```python
def calculer_moyenne(nombres, poids=None):
    """Calcule la moyenne pondérée d'une liste de nombres.
    
    Args:
        nombres (list): Liste des nombres à moyenner.
        poids (list, optional): Liste des poids associés. 
            Si None, utilise des poids égaux.
    
    Returns:
        float: La moyenne pondérée calculée.
    
    Raises:
        ValueError: Si les listes n'ont pas la même longueur.
        TypeError: Si les entrées ne sont pas numériques.
    
    Examples:
        >>> calculer_moyenne([1, 2, 3])
        2.0
        >>> calculer_moyenne([1, 2], [0.5, 0.5])
        1.5
    """
    # ... code ...
```

#### C. Docstring de classe
```python
class CompteBancaire:
    """Représente un compte bancaire.
    
    Cette classe gère les opérations basiques d'un compte bancaire,
    comme les dépôts, retraits et calculs d'intérêts.
    
    Attributes:
        numero (str): Numéro unique du compte.
        solde (float): Solde actuel du compte.
        proprietaire (str): Nom du propriétaire du compte.
        
    Properties:
        est_positif (bool): Indique si le solde est positif.
    
    Examples:
        >>> compte = CompteBancaire("123", "Jean Dupont")
        >>> compte.deposer(1000)
        >>> compte.solde
        1000.0
    """
    
    def __init__(self, numero, proprietaire):
        """Initialise un nouveau compte bancaire.
        
        Args:
            numero (str): Numéro du compte.
            proprietaire (str): Nom du propriétaire.
        """
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde = 0.0
```

### 3. Styles de documentation (20 min)

#### A. Style Google
```python
def transferer_argent(source, destination, montant):
    """Transfère de l'argent entre deux comptes.
    
    Args:
        source (CompteBancaire): Compte source.
        destination (CompteBancaire): Compte destination.
        montant (float): Montant à transférer.
    
    Returns:
        bool: True si le transfert est réussi, False sinon.
        
    Raises:
        ValueError: Si le montant est négatif.
    """
```

#### B. Style reStructuredText
```python
def transferer_argent(source, destination, montant):
    """Transfère de l'argent entre deux comptes.
    
    :param source: Compte source
    :type source: CompteBancaire
    :param destination: Compte destination
    :type destination: CompteBancaire
    :param montant: Montant à transférer
    :type montant: float
    :returns: True si le transfert est réussi, False sinon
    :rtype: bool
    :raises ValueError: Si le montant est négatif
    """
```

#### C. Style NumPy/SciPy
```python
def transferer_argent(source, destination, montant):
    """Transfère de l'argent entre deux comptes.
    
    Parameters
    ----------
    source : CompteBancaire
        Compte source.
    destination : CompteBancaire
        Compte destination.
    montant : float
        Montant à transférer.
        
    Returns
    -------
    bool
        True si le transfert est réussi, False sinon.
        
    Raises
    ------
    ValueError
        Si le montant est négatif.
    """
```

### 4. Outils et bonnes pratiques (10 min)

#### A. Utilisation de help()
```python
# Dans l'interpréteur Python
help(ma_fonction)
help(MaClasse)
```

#### B. Documentation générée
```python
# Utilisation de pydoc
python -m pydoc mon_module.py

# Génération de documentation avec Sphinx
sphinx-quickstart
```

### Phase de pratique (15 min)

Exercices :

1. Documentation de fonction :
```python
# Écrire la documentation complète pour une fonction de calcul
def calculer_interet(principal, taux, duree):
    # À compléter
```

2. Documentation de classe :
```python
# Documenter une classe de gestion de livres
class Livre:
    # À compléter
```

3. Amélioration de commentaires :
```python
# Transformer ces mauvais commentaires en bons commentaires
x = x + 1  # Ajoute 1
liste = []  # Crée une liste vide
```

### Synthèse (5 min)
- Importance des commentaires pertinents
- Choix du style de documentation
- Outils disponibles

### Évaluation (5 min)
1. Quand utiliser des commentaires vs docstrings ?
2. Quels éléments inclure dans une docstring ?
3. Comment documenter les exceptions ?

## Devoirs et prolongements

Devoirs :
1. Documenter un petit projet existant
2. Rédiger des docstrings pour différents types de fonctions
3. Convertir des commentaires en documentation appropriée

Prolongements :
- Génération automatique de documentation
- Tests intégrés dans la documentation
- Documentation multilingue

## Points importants à retenir :

1. Commentaires :
   - Expliquer le pourquoi, pas le comment
   - Être concis et pertinent
   - Maintenir à jour

2. Docstrings :
   - Documentation formelle du code
   - Différents styles disponibles
   - Accessibles via help()

3. Bonnes pratiques :
   - Cohérence du style
   - Documentation à jour
   - Tests dans les exemples