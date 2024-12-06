# Plan de leçon : Classes, attributs et méthodes

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Programmation Orientée Objet (POO)
- Durée prévue : 2h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser la création et l'utilisation des classes

- Objectifs disciplinaires :
  - Comprendre les concepts de la POO
  - Maîtriser la création d'attributs et méthodes
  - Savoir utiliser les différents types de méthodes
  - Gérer l'encapsulation

## Déroulement de la leçon

### 1. Création de classe de base (25 min)

#### A. Structure de base
```python
class Personne:
    """
    Classe représentant une personne.
    
    Attributes:
        nom (str): Nom de la personne
        age (int): Âge de la personne
    """
    
    def __init__(self, nom: str, age: int):
        """
        Initialise une nouvelle personne.
        
        Args:
            nom: Le nom de la personne
            age: L'âge de la personne
        """
        self.nom = nom
        self.age = age
    
    def presenter(self):
        """Retourne une présentation de la personne."""
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans"

# Utilisation
personne = Personne("Alice", 30)
print(personne.presenter())
```

#### B. Attributs de classe et d'instance
```python
class Compteur:
    """Démontre la différence entre attributs de classe et d'instance."""
    
    # Attribut de classe (partagé par toutes les instances)
    total = 0
    
    def __init__(self, valeur_initiale: int = 0):
        # Attribut d'instance (unique à chaque instance)
        self.valeur = valeur_initiale
        Compteur.total += 1
    
    @classmethod
    def obtenir_total(cls) -> int:
        """Retourne le nombre total d'instances."""
        return cls.total

# Utilisation
c1 = Compteur(5)
c2 = Compteur(10)
print(Compteur.total)  # 2
```

### 2. Types de méthodes (30 min)

#### A. Méthodes d'instance
```python
class Rectangle:
    """Classe représentant un rectangle."""
    
    def __init__(self, longueur: float, largeur: float):
        self.longueur = longueur
        self.largeur = largeur
    
    def calculer_aire(self) -> float:
        """Calcule l'aire du rectangle."""
        return self.longueur * self.largeur
    
    def calculer_perimetre(self) -> float:
        """Calcule le périmètre du rectangle."""
        return 2 * (self.longueur + self.largeur)
    
    def agrandir(self, facteur: float) -> None:
        """Agrandit le rectangle selon un facteur."""
        self.longueur *= facteur
        self.largeur *= facteur
```

#### B. Méthodes de classe et statiques
```python
class Date:
    """Classe représentant une date."""
    
    def __init__(self, jour: int, mois: int, annee: int):
        self.jour = jour
        self.mois = mois
        self.annee = annee
    
    @classmethod
    def depuis_chaine(cls, date_str: str) -> 'Date':
        """Crée une Date à partir d'une chaîne 'JJ-MM-AAAA'."""
        jour, mois, annee = map(int, date_str.split('-'))
        return cls(jour, mois, annee)
    
    @staticmethod
    def est_bissextile(annee: int) -> bool:
        """Détermine si une année est bissextile."""
        return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)
    
    def est_valide(self) -> bool:
        """Vérifie si la date est valide."""
        return (1 <= self.mois <= 12 and 1 <= self.jour <= 31)
```

### 3. Propriétés et encapsulation (25 min)

```python
class CompteBancaire:
    """Classe représentant un compte bancaire."""
    
    def __init__(self, solde_initial: float = 0):
        self._solde = solde_initial  # Attribut protégé
        self.__operations = []       # Attribut privé
    
    @property
    def solde(self) -> float:
        """Obtient le solde actuel."""
        return self._solde
    
    @solde.setter
    def solde(self, valeur: float) -> None:
        """Définit le solde avec validation."""
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._solde = valeur
        self.__operations.append(("modification_solde", valeur))
    
    def deposer(self, montant: float) -> None:
        """Dépose de l'argent sur le compte."""
        if montant <= 0:
            raise ValueError("Le montant doit être positif")
        self._solde += montant
        self.__operations.append(("depot", montant))
    
    def obtenir_historique(self) -> list:
        """Retourne une copie de l'historique des opérations."""
        return self.__operations.copy()
```

### 4. Méthodes spéciales (25 min)

```python
class Vecteur:
    """Classe représentant un vecteur 2D."""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        """Représentation lisible du vecteur."""
        return f"Vecteur({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """Représentation technique du vecteur."""
        return f"Vecteur(x={self.x}, y={self.y})"
    
    def __eq__(self, autre: 'Vecteur') -> bool:
        """Compare deux vecteurs."""
        if not isinstance(autre, Vecteur):
            return False
        return self.x == autre.x and self.y == autre.y
    
    def __add__(self, autre: 'Vecteur') -> 'Vecteur':
        """Addition de vecteurs."""
        return Vecteur(self.x + autre.x, self.y + autre.y)
    
    def __len__(self) -> int:
        """Longueur du vecteur (arrondie à l'entier)."""
        return int((self.x**2 + self.y**2)**0.5)
    
    def __getitem__(self, index: int) -> float:
        """Accès aux composantes par index."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Index hors limites")
```

### 5. Héritage (25 min)

```python
class Animal:
    """Classe de base pour les animaux."""
    
    def __init__(self, nom: str):
        self.nom = nom
    
    def faire_bruit(self) -> str:
        """Méthode à surcharger dans les classes dérivées."""
        raise NotImplementedError("Les classes dérivées doivent implémenter cette méthode")
    
    def presenter(self) -> str:
        """Présente l'animal."""
        return f"Je suis {self.nom}, un {self.__class__.__name__}"

class Chat(Animal):
    """Classe représentant un chat."""
    
    def __init__(self, nom: str, couleur: str):
        super().__init__(nom)
        self.couleur = couleur
    
    def faire_bruit(self) -> str:
        """Implémentation du bruit pour un chat."""
        return "Miaou !"
    
    def chasser(self) -> str:
        """Méthode spécifique aux chats."""
        return f"{self.nom} part à la chasse"

class Chien(Animal):
    """Classe représentant un chien."""
    
    def faire_bruit(self) -> str:
        """Implémentation du bruit pour un chien."""
        return "Wouaf !"
```

### 6. Composition et agrégation (20 min)

```python
class Adresse:
    """Classe représentant une adresse."""
    
    def __init__(self, rue: str, ville: str, code_postal: str):
        self.rue = rue
        self.ville = ville
        self.code_postal = code_postal
    
    def __str__(self) -> str:
        return f"{self.rue}, {self.code_postal} {self.ville}"

class Entreprise:
    """Classe représentant une entreprise."""
    
    def __init__(self, nom: str, adresse: Adresse):
        self.nom = nom
        self.adresse = adresse  # Composition
        self.employes = []      # Agrégation
    
    def ajouter_employe(self, employe: 'Employe') -> None:
        """Ajoute un employé à l'entreprise."""
        self.employes.append(employe)
    
    def obtenir_adresse(self) -> str:
        """Retourne l'adresse complète de l'entreprise."""
        return f"{self.nom}\n{self.adresse}"

class Employe:
    """Classe représentant un employé."""
    
    def __init__(self, nom: str, poste: str):
        self.nom = nom
        self.poste = poste
        self.entreprise = None  # Référence à l'entreprise
```

### Phase de pratique (15 min)

Exercices :

1. Système bancaire :
```python
def creer_systeme_bancaire():
    """
    Créer un système avec :
    - Comptes différents types
    - Transactions
    - Historique
    """
    # À compléter
```

2. Système de formes géométriques :
```python
def creer_systeme_formes():
    """
    Créer un système avec :
    - Formes diverses
    - Calculs géométriques
    - Transformations
    """
    # À compléter
```

## Points importants à retenir :

1. Structure de classe :
   - Attributs vs méthodes
   - Types de méthodes
   - Encapsulation

2. Méthodes spéciales :
   - __init__, __str__, __repr__
   - Opérateurs et comparaisons
   - Accesseurs

3. Relations :
   - Héritage
   - Composition
   - Agrégation