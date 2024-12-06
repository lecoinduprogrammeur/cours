# Plan de leçon : Variables mutables et immuables

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Mutabilité des variables
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Comprendre la différence entre variables mutables et immuables

- Objectifs disciplinaires :
  - Identifier les types mutables et immuables
  - Comprendre les implications en mémoire
  - Maîtriser le passage d'arguments
  - Éviter les pièges courants

## Déroulement de la leçon

### 1. Types immuables (25 min)

#### A. Types de base immuables
```python
# int (nombres entiers)
x = 42
print(id(x))  # Affiche l'identifiant en mémoire
x += 1        # Crée un nouvel objet
print(id(x))  # Nouvel identifiant

# float (nombres à virgule)
pi = 3.14
pi = 3.14159  # Nouveau float créé

# str (chaînes de caractères)
texte = "Hello"
print(id(texte))
texte += " World"  # Nouvelle chaîne créée
print(id(texte))   # Nouvel identifiant

# tuple (tuples)
point = (1, 2)
# point[0] = 3  # TypeError: tuple ne peut pas être modifié

# bool (booléens)
flag = True
# Les booléens sont immuables

# frozenset (ensembles gelés)
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError: frozenset n'a pas de méthode add
```

#### B. Comportement des immuables
```python
# Réutilisation d'objets (intern)
a = "hello"
b = "hello"
print(a is b)  # True (même objet en mémoire)

# Modifications créent de nouveaux objets
x = 5
y = x
x += 1
print(y)  # 5 (y n'est pas affecté)

# Immuables dans des structures de données
t = (1, [2, 3], "quatre")
# t[1].append(4)  # Possible car la liste est mutable
# t[0] = 2        # Impossible car le tuple est immuable
```

### 2. Types mutables (25 min)

#### A. Types de base mutables
```python
# list (listes)
liste = [1, 2, 3]
print(id(liste))
liste.append(4)     # Modifie la liste existante
print(id(liste))    # Même identifiant

# dict (dictionnaires)
dict = {"a": 1}
dict["b"] = 2      # Modifie le dictionnaire existant

# set (ensembles)
ensemble = {1, 2, 3}
ensemble.add(4)     # Modifie l'ensemble existant

# Objets personnalisés (classes)
class MaClasse:
    def __init__(self):
        self.valeur = 0
    
obj = MaClasse()
obj.valeur = 42    # Modifie l'objet existant
```

#### B. Comportement des mutables
```python
# Références partagées
liste1 = [1, 2, 3]
liste2 = liste1    # Référence le même objet
liste1.append(4)
print(liste2)      # [1, 2, 3, 4]

# Copie superficielle vs profonde
import copy
liste_orig = [1, [2, 3], 4]

# Copie superficielle
liste_copie = liste_orig.copy()
liste_copie[1].append(5)  # Modifie aussi liste_orig[1]

# Copie profonde
liste_copie_prof = copy.deepcopy(liste_orig)
liste_copie_prof[1].append(6)  # Ne modifie pas liste_orig
```

### 3. Implications en mémoire (20 min)

#### A. Gestion de la mémoire
```python
# Variables immuables
x = 42
y = x
x = 43  # Crée un nouvel objet, y garde l'ancien

# Variables mutables
liste1 = [1, 2, 3]
liste2 = liste1
liste1.append(4)  # Modifie l'objet partagé

# Vérification d'identité
print(id(liste1) == id(liste2))  # True
```

#### B. Passage d'arguments
```python
# Passage d'immuables
def modifier_nombre(n):
    n += 1
    return n

x = 5
modifier_nombre(x)
print(x)  # 5 (non modifié)

# Passage de mutables
def modifier_liste(lst):
    lst.append(4)

ma_liste = [1, 2, 3]
modifier_liste(ma_liste)
print(ma_liste)  # [1, 2, 3, 4] (modifié)
```

### 4. Bonnes pratiques et pièges courants (25 min)

#### A. Pièges avec les mutables
```python
# Piège 1: Valeurs par défaut mutables
def ajouter_element(element, liste=[]):  # MAUVAISE PRATIQUE
    liste.append(element)
    return liste

print(ajouter_element(1))  # [1]
print(ajouter_element(2))  # [1, 2] !

# Correction
def ajouter_element(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste

# Piège 2: Copie de structures imbriquées
liste_orig = [[1, 2], [3, 4]]
liste_copie = liste_orig.copy()  # Copie superficielle
liste_copie[0].append(5)  # Modifie aussi liste_orig[0]
```

#### B. Solutions et bonnes pratiques
```python
# Utilisation correcte de copy
import copy

# Pour les structures simples
liste1 = [1, 2, 3]
liste2 = liste1.copy()  # ou list(liste1)

# Pour les structures imbriquées
nested = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested)

# Retour de nouvelles copies
def traiter_liste(liste):
    nouvelle_liste = liste.copy()
    nouvelle_liste.append(4)
    return nouvelle_liste

# Immuabilité explicite
from typing import Tuple, FrozenSet
def fonction_sure(donnees: Tuple[int, ...]) -> FrozenSet[int]:
    return frozenset(donnees)
```

### 5. Applications pratiques (15 min)

#### A. Gestion d'état
```python
class GestionnaireEtat:
    def __init__(self):
        self._etat = []
    
    def ajouter_etat(self, nouvel_etat):
        # Copie profonde pour éviter les modifications externes
        self._etat.append(copy.deepcopy(nouvel_etat))
    
    def obtenir_etat(self, index):
        # Retourne une copie pour protéger l'état interne
        return copy.deepcopy(self._etat[index])
```

#### B. Structures de données sûres
```python
class ListeSecurisee:
    def __init__(self, donnees=None):
        self._donnees = [] if donnees is None else list(donnees)
    
    def ajouter(self, element):
        self._donnees.append(copy.deepcopy(element))
    
    def obtenir(self, index):
        return copy.deepcopy(self._donnees[index])
    
    @property
    def donnees(self):
        return copy.deepcopy(self._donnees)
```

### Phase de pratique (15 min)

Exercices :

1. Identification de problèmes :
```python
def trouver_erreurs():
    # Identifier les problèmes potentiels
    def ajouter_score(score, scores=[]):
        scores.append(score)
        return scores
    
    def modifier_point(point):
        point[0] += 1
        
    # Tester et corriger
```

2. Implémentation sécurisée :
```python
class JournalSecurise:
    """
    Implémenter une classe de journal
    qui protège ses données contre les modifications externes
    """
    pass
```

### Synthèse (5 min)
- Types mutables vs immuables
- Implications en mémoire
- Bonnes pratiques
- Pièges à éviter

### Évaluation (5 min)
1. Quels sont les types mutables et immuables en Python ?
2. Comment éviter les problèmes de référence partagée ?
3. Quand utiliser une copie profonde vs superficielle ?

## Points importants à retenir :

1. Types immuables :
   - int, float, str, tuple, bool, frozenset
   - Créent toujours de nouveaux objets
   - Plus sûrs pour les valeurs par défaut

2. Types mutables :
   - list, dict, set
   - Modifiables en place
   - Nécessitent une attention particulière

3. Bonnes pratiques :
   - Éviter les valeurs par défaut mutables
   - Utiliser des copies appropriées
   - Protéger les données internes