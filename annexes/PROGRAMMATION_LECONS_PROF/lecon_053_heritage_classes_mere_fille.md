# Plan de leçon : Héritage, classes mère et filles

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Héritage et polymorphisme
- Durée prévue : 2h00

## Structure du code

### 1. Classe mère (base) simple

```python
class Animal:
    """Classe mère pour tous les animaux."""
    
    def __init__(self, nom: str, age: int):
        """
        Initialise un animal.
        
        Args:
            nom: Nom de l'animal
            age: Âge de l'animal
        """
        self.nom = nom
        self.age = age
    
    def faire_bruit(self) -> str:
        """Méthode à surcharger dans les classes filles."""
        raise NotImplementedError("Cette méthode doit être implémentée")
    
    def presenter(self) -> str:
        """Présente l'animal."""
        return f"Je suis {self.nom}, un {self.__class__.__name__} de {self.age} ans"
```

### 2. Classes filles simples

```python
class Chat(Animal):
    """Classe fille représentant un chat."""
    
    def __init__(self, nom: str, age: int, couleur: str):
        # Appel du constructeur de la classe mère
        super().__init__(nom, age)
        # Attribut spécifique à Chat
        self.couleur = couleur
    
    def faire_bruit(self) -> str:
        """Implémentation du bruit pour un chat."""
        return "Miaou!"
    
    def chasser(self) -> str:
        """Méthode spécifique aux chats."""
        return f"{self.nom} part à la chasse"

class Chien(Animal):
    """Classe fille représentant un chien."""
    
    def __init__(self, nom: str, age: int, race: str):
        super().__init__(nom, age)
        self.race = race
    
    def faire_bruit(self) -> str:
        """Implémentation du bruit pour un chien."""
        return "Wouf!"
    
    def chercher(self) -> str:
        """Méthode spécifique aux chiens."""
        return f"{self.nom} va chercher le bâton"
```

### 3. Héritage multiple

```python
class Animal:
    def __init__(self, nom: str):
        self.nom = nom

class Volant:
    def voler(self) -> str:
        return "Je vole!"

class Nageur:
    def nager(self) -> str:
        return "Je nage!"

class Canard(Animal, Volant, Nageur):
    """Classe avec héritage multiple."""
    
    def __init__(self, nom: str):
        super().__init__(nom)
    
    def faire_bruit(self) -> str:
        return "Coin coin!"
```

### 4. Héritage avec propriétés

```python
class Vehicule:
    """Classe mère pour les véhicules."""
    
    def __init__(self, marque: str, modele: str):
        self._marque = marque
        self._modele = modele
        self._vitesse = 0
    
    @property
    def vitesse(self) -> float:
        """Vitesse actuelle du véhicule."""
        return self._vitesse
    
    @vitesse.setter
    def vitesse(self, valeur: float) -> None:
        """Définit la vitesse avec validation."""
        if valeur < 0:
            raise ValueError("La vitesse ne peut pas être négative")
        self._vitesse = valeur
    
    def description(self) -> str:
        """Description du véhicule."""
        return f"{self._marque} {self._modele}"

class Voiture(Vehicule):
    """Classe fille pour les voitures."""
    
    def __init__(self, marque: str, modele: str, nb_portes: int):
        super().__init__(marque, modele)
        self.nb_portes = nb_portes
    
    @property
    def vitesse(self) -> float:
        """Surcharge de la propriété avec limite."""
        return self._vitesse
    
    @vitesse.setter
    def vitesse(self, valeur: float) -> None:
        """Limite la vitesse maximale."""
        if valeur > 200:
            raise ValueError("Vitesse maximale dépassée")
        super(Voiture, self.__class__).vitesse.fset(self, valeur)
```

### 5. Classes abstraites

```python
from abc import ABC, abstractmethod

class FormeGeometrique(ABC):
    """Classe abstraite pour les formes géométriques."""
    
    @abstractmethod
    def aire(self) -> float:
        """Calcule l'aire de la forme."""
        pass
    
    @abstractmethod
    def perimetre(self) -> float:
        """Calcule le périmètre de la forme."""
        pass
    
    def description(self) -> str:
        """Méthode non abstraite."""
        return f"Je suis un {self.__class__.__name__}"

class Rectangle(FormeGeometrique):
    """Implémentation d'une forme concrète."""
    
    def __init__(self, longueur: float, largeur: float):
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self) -> float:
        return self.longueur * self.largeur
    
    def perimetre(self) -> float:
        return 2 * (self.longueur + self.largeur)

class Cercle(FormeGeometrique):
    """Autre forme concrète."""
    
    def __init__(self, rayon: float):
        self.rayon = rayon
    
    def aire(self) -> float:
        return 3.14159 * self.rayon ** 2
    
    def perimetre(self) -> float:
        return 2 * 3.14159 * self.rayon
```

### 6. Héritage avec mixins

```python
class LoggerMixin:
    """Mixin pour ajouter des capacités de logging."""
    
    def log(self, message: str) -> None:
        print(f"{self.__class__.__name__}: {message}")

class SerializableMixin:
    """Mixin pour la sérialisation."""
    
    def to_dict(self) -> dict:
        return {
            key: value 
            for key, value in self.__dict__.items() 
            if not key.startswith('_')
        }

class Produit(LoggerMixin, SerializableMixin):
    """Classe utilisant des mixins."""
    
    def __init__(self, nom: str, prix: float):
        self.nom = nom
        self.prix = prix
    
    def modifier_prix(self, nouveau_prix: float) -> None:
        self.log(f"Modification du prix de {self.prix} à {nouveau_prix}")
        self.prix = nouveau_prix
```

### 7. Exemple d'utilisation

```python
def main():
    # Création d'instances
    chat = Chat("Minou", 3, "noir")
    chien = Chien("Rex", 5, "Berger Allemand")
    
    # Utilisation du polymorphisme
    animaux = [chat, chien]
    for animal in animaux:
        print(animal.presenter())
        print(f"Bruit: {animal.faire_bruit()}")
    
    # Méthodes spécifiques
    print(chat.chasser())
    print(chien.chercher())
    
    # Avec formes géométriques
    formes = [
        Rectangle(5, 3),
        Cercle(2)
    ]
    
    for forme in formes:
        print(f"{forme.description()}:")
        print(f"Aire: {forme.aire()}")
        print(f"Périmètre: {forme.perimetre()}")
    
    # Avec mixins
    produit = Produit("Ordinateur", 999.99)
    produit.modifier_prix(899.99)
    print(produit.to_dict())

if __name__ == "__main__":
    main()
```

## Points importants à retenir :

1. Héritage simple :
   - Une classe fille hérite de tous les attributs et méthodes
   - super() pour appeler la classe mère
   - Possibilité de surcharger les méthodes

2. Héritage multiple :
   - Python supporte l'héritage multiple
   - Ordre de résolution des méthodes (MRO)
   - Mixins pour ajouter des fonctionnalités

3. Classes abstraites :
   - Définition d'interfaces
   - Méthodes abstraites obligatoires
   - Garantie de l'implémentation

4. Bonnes pratiques :
   - Éviter l'héritage profond
   - Préférer la composition quand possible
   - Documenter clairement l'héritage

5. Avantages :
   - Réutilisation du code
   - Organisation hiérarchique
   - Polymorphisme
