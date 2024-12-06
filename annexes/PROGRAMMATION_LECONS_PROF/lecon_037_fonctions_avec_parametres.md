# Plan de leçon : Fonctions avec paramètres

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Création de fonctions avec paramètres
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser la création et l'utilisation de fonctions avec paramètres

- Objectifs disciplinaires :
  - Comprendre les différents types de paramètres
  - Maîtriser les valeurs par défaut
  - Savoir utiliser les arguments nommés
  - Implémenter des fonctions flexibles

## Déroulement de la leçon

### 1. Paramètres simples (20 min)

#### A. Syntaxe de base
```python
# Fonction avec un paramètre
def saluer(nom):
    print(f"Bonjour, {nom}!")

# Appel avec argument
saluer("Alice")  # Bonjour, Alice!

# Fonction avec plusieurs paramètres
def addition(a, b):
    return a + b

resultat = addition(3, 4)  # 7

# Fonction avec type hints (annotations)
def multiplier(x: int, y: int) -> int:
    return x * y
```

#### B. Ordre des paramètres
```python
def afficher_info(nom, age, ville):
    print(f"{nom} a {age} ans et vit à {ville}")

# Appel avec arguments positionnels
afficher_info("Bob", 25, "Paris")

# Appel avec arguments nommés
afficher_info(age=30, ville="Lyon", nom="Alice")

# Mélange (positionnels d'abord)
afficher_info("Charlie", ville="Marseille", age=35)
```

### 2. Valeurs par défaut (25 min)

#### A. Définition de paramètres optionnels
```python
# Paramètre avec valeur par défaut
def puissance(base, exposant=2):
    return base ** exposant

# Différents appels possibles
print(puissance(3))      # 9 (exposant par défaut = 2)
print(puissance(3, 3))   # 27

# Plusieurs valeurs par défaut
def creer_profil(nom, age=18, ville="Paris", pays="France"):
    return {
        "nom": nom,
        "age": age,
        "ville": ville,
        "pays": pays
    }

# Différentes façons d'appeler
profil1 = creer_profil("David")
profil2 = creer_profil("Emma", age=25)
profil3 = creer_profil("Frank", ville="Lyon", age=30)
```

#### B. Pièges et bonnes pratiques
```python
# PIÈGE : Valeur par défaut mutable
def ajouter_element(element, liste=[]):  # NE PAS FAIRE
    liste.append(element)
    return liste

# CORRECT : Utilisation de None
def ajouter_element(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste

# Valeurs par défaut dynamiques
from datetime import datetime

def logger(message, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    return f"[{timestamp}] {message}"
```

### 3. Arguments variables (30 min)

#### A. Arguments positionnels variables (*args)
```python
# Fonction acceptant un nombre variable d'arguments
def somme(*nombres):
    return sum(nombres)

# Différents appels
print(somme(1, 2))          # 3
print(somme(1, 2, 3, 4))    # 10

def afficher_elements(*args):
    for i, arg in enumerate(args):
        print(f"Argument {i}: {arg}")

# Fonction avec args et paramètres normaux
def operation(operateur, *nombres):
    if operateur == "+":
        return sum(nombres)
    elif operateur == "*":
        resultat = 1
        for n in nombres:
            resultat *= n
        return resultat
```

#### B. Arguments nommés variables (**kwargs)
```python
# Fonction acceptant des arguments nommés variables
def afficher_infos(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

# Appel avec différents arguments nommés
afficher_infos(nom="Alice", age=30, ville="Paris")

# Combinaison de tous les types de paramètres
def fonction_complete(arg1, arg2, *args, defaut="valeur", **kwargs):
    print(f"Arguments fixes: {arg1}, {arg2}")
    print(f"Arguments variables: {args}")
    print(f"Valeur par défaut: {defaut}")
    print(f"Arguments nommés: {kwargs}")
```

### 4. Validation des paramètres (25 min)

#### A. Vérifications de base
```python
def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

def creer_utilisateur(nom, age):
    if not isinstance(nom, str):
        raise TypeError("Le nom doit être une chaîne")
    if not isinstance(age, int):
        raise TypeError("L'âge doit être un entier")
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif")
    
    return {"nom": nom, "age": age}
```

#### B. Validation avancée
```python
def configurer_application(**config):
    # Valeurs par défaut
    parametres_defaut = {
        "debug": False,
        "port": 8000,
        "host": "localhost"
    }
    
    # Validation des types
    validateurs = {
        "debug": lambda x: isinstance(x, bool),
        "port": lambda x: isinstance(x, int) and 0 <= x <= 65535,
        "host": lambda x: isinstance(x, str)
    }
    
    # Fusion avec les valeurs par défaut
    parametres = {**parametres_defaut, **config}
    
    # Validation
    for param, valeur in parametres.items():
        if param in validateurs and not validateurs[param](valeur):
            raise ValueError(f"Valeur invalide pour {param}: {valeur}")
    
    return parametres
```

### 5. Documentation et annotations (20 min)

```python
from typing import List, Dict, Optional

def calculer_statistiques(
    nombres: List[float],
    precision: int = 2,
    inclure_extremes: bool = True
) -> Dict[str, float]:
    """
    Calcule des statistiques sur une liste de nombres.
    
    Args:
        nombres (List[float]): Liste des nombres à analyser
        precision (int, optional): Nombre de décimales. Defaults to 2.
        inclure_extremes (bool, optional): Inclure min/max. Defaults to True.
    
    Returns:
        Dict[str, float]: Dictionnaire des statistiques calculées
    
    Raises:
        ValueError: Si la liste est vide
        TypeError: Si les éléments ne sont pas numériques
    """
    if not nombres:
        raise ValueError("La liste ne peut pas être vide")
        
    resultats = {
        "moyenne": round(sum(nombres) / len(nombres), precision),
        "total": sum(nombres)
    }
    
    if inclure_extremes:
        resultats.update({
            "minimum": min(nombres),
            "maximum": max(nombres)
        })
    
    return resultats
```

### 6. Applications pratiques (15 min)

```python
def creer_calculatrice(
    operation: str = "somme",
    arrondir: bool = False,
    decimales: int = 2
):
    """Crée une fonction calculatrice personnalisée."""
    def calculer(*nombres):
        if not nombres:
            return 0
            
        if operation == "somme":
            resultat = sum(nombres)
        elif operation == "moyenne":
            resultat = sum(nombres) / len(nombres)
        elif operation == "produit":
            resultat = 1
            for n in nombres:
                resultat *= n
        else:
            raise ValueError(f"Opération inconnue : {operation}")
            
        if arrondir:
            resultat = round(resultat, decimales)
            
        return resultat
        
    return calculer

# Utilisation
somme = creer_calculatrice()
moyenne = creer_calculatrice("moyenne", arrondir=True)
```

### Phase de pratique (15 min)

Exercices :

1. Fonction polyvalente :
```python
def creer_formatter_texte():
    """
    Créer une fonction qui formate du texte avec :
    - Différentes options de casse
    - Longueur maximale optionnelle
    - Préfixe/suffixe optionnels
    """
    # À compléter
```

2. Validateur paramétrable :
```python
def creer_validateur():
    """
    Créer un validateur flexible qui :
    - Accepte différents types de données
    - Permet des règles personnalisées
    - Retourne des messages d'erreur détaillés
    """
    # À compléter
```

### Synthèse (5 min)
- Types de paramètres
- Valeurs par défaut
- Arguments variables
- Validation et documentation

## Points importants à retenir :

1. Paramètres :
   - Positionnels vs nommés
   - Valeurs par défaut
   - Arguments variables

2. Validation :
   - Vérification des types
   - Validation des valeurs
   - Gestion des erreurs

3. Bonnes pratiques :
   - Documentation claire
   - Validation robuste
   - Utilisation appropriée des valeurs par défaut