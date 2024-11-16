---
title: "Matières à enseigner en programmation Python : Niveaux Débutant et Intermédiaire" 
author: "Fabrice Dumont" 
date: "2024-11-16" 
categories:  ["cours","programmation"]
tags: []
version: "1.0"
status: ["Brouillon",**"Révision"**,"Définitif"]
license: "CC BY-NC-ND 4.0"
license_url: "https://creativecommons.org/licenses/by-nc-nd/4.0/"
---

# Matières à enseigner en programmation Python : Niveaux Débutant et Intermédiaire

## Niveau Débutant : Apprendre les bases du langage Python

### 1. Introduction à Python
- **Installation de Python et des IDE** :
  - Guide pour installer Python, VS Code, PyCharm, et Jupyter Notebook.
  - Comment vérifier l'installation avec `python --version`.
  - Exécution d'un script Python : Création et exécution d'un premier script "Hello, World!".

#### Exemple de code :
```python
print("Hello, World!")
```

### 2. Syntaxe de base
- **Variables et types de données** :
  - Définition des variables (`int`, `float`, `str`, `bool`).
  - Conversion de types (`str()`, `int()`, `float()`).

#### Exemple de code :
```python
x = 10
y = 3.14
name = "Alice"
is_student = True

print(type(x), type(y), type(name), type(is_student))
```

### 3. Opérations arithmétiques et logiques
- **Opérations de base** : Addition, soustraction, multiplication, division.
- **Opérateurs logiques** : `and`, `or`, `not`.

#### Exemple de code :
```python
a = 5
b = 2
print(a + b, a - b, a * b, a / b)

is_valid = (a > b) and (b > 0)
print(is_valid)
```

### 4. Structures de contrôle
- **Conditions (`if`, `elif`, `else`)** :
  - Utilisation des conditions pour prendre des décisions dans le code.

#### Exemple de code :
```python
age = 18
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
```

- **Boucles (`for`, `while`)** :
  - Répéter des instructions avec des boucles.

#### Exemple de code :
```python
for i in range(5):
    print(f"Tour {i + 1}")

count = 0
while count < 5:
    print(count)
    count += 1
```

### 5. Fonctions
- **Définition et appel de fonctions** :
  - Création de fonctions simples avec des paramètres et des valeurs de retour.

#### Exemple de code :
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

### Exercices pratiques (Débutant)
- Écrire un programme qui demande l'âge de l'utilisateur et affiche un message en fonction de l'âge.
- Créer un script qui calcule la somme des nombres de 1 à 100.
- Implémenter un jeu de devinettes où l'utilisateur doit deviner un nombre entre 1 et 10.

---

## Niveau Intermédiaire : Approfondir les concepts Python

### 1. Manipulation des collections
- **Listes, tuples, ensembles, et dictionnaires** :
  - Introduction aux collections et leurs opérations (ajouter, supprimer, trier).

#### Exemple de code :
```python
fruits = ["pomme", "banane", "cerise"]
fruits.append("orange")
print(fruits)

scores = {"Alice": 90, "Bob": 85}
print(scores["Alice"])
```

### 2. Manipulation des fichiers
- **Lecture et écriture dans des fichiers** :
  - Utilisation de `open()`, `read()`, et `write()` pour manipuler des fichiers texte.

#### Exemple de code :
```python
with open("data.txt", "w") as file:
    file.write("Bonjour, Python!")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### 3. Programmation fonctionnelle
- **Utilisation des fonctions lambda, map, filter** :
  - Introduction aux fonctions anonymes et à la programmation fonctionnelle.

#### Exemple de code :
```python
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)
```

### 4. Gestion des exceptions
- **Utiliser `try`, `except`, `finally`** :
  - Gestion des erreurs pour éviter que le programme ne se termine brutalement.

#### Exemple de code :
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Erreur : Division par zéro.")
finally:
    print("Opération terminée.")
```

### 5. Modules et packages
- **Importation de modules standard** :
  - Utiliser des modules comme `math`, `datetime`, et `random`.

#### Exemple de code :
```python
import math
print(math.sqrt(16))

import random
print(random.randint(1, 10))
```

### Exercices pratiques (Intermédiaire)
- Créer un script qui lit un fichier texte et affiche le nombre de mots.
- Écrire un programme qui trie une liste de noms par ordre alphabétique.
- Implémenter un calculateur simple avec des fonctions pour additionner, soustraire, multiplier et diviser.

---

## Ressources supplémentaires
- Tutoriels en ligne : W3Schools, Real Python, Python.org.
- Livres recommandés : "Automate the Boring Stuff with Python" de Al Sweigart.
- Vidéos : Chaîne YouTube "Corey Schafer", "Python Programming" (YouTube).

