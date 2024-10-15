# Python / Manipuler les Boucles

**© Fabrice Dumont**

- [Python / Manipuler les Boucles](#python---manipuler-les-boucles)
  - [Introduction aux Boucles](#introduction-aux-boucles)
  - [Boucle `for`](#boucle-for)
  - [Boucle `while`](#boucle-while)
  - [Instructions `break` et `continue`](#instructions-break-et-continue)
  - [Boucles Imbriquées](#boucles-imbriquées)
  - [Boucle avec `else`](#boucle-avec-else)
  - [Itérer sur des Listes](#itérer-sur-des-listes)
  - [Itérer sur des Dictionnaires](#itérer-sur-des-dictionnaires)
  - [Utiliser `range()` avec `for`](#utiliser-range-avec-for)
  - [Boucle Infinie](#boucle-infinie)
  - [Boucles et Compréhensions](#boucles-et-compréhensions)
  - [Optimisation des Boucles](#optimisation-des-boucles)

Les **boucles** en Python sont utilisées pour répéter une séquence d'instructions un certain nombre de fois ou jusqu'à ce qu'une condition soit remplie. Python propose principalement deux types de boucles : la boucle `for` et la boucle `while`.

## Introduction aux Boucles

Les boucles permettent de simplifier les tâches répétitives. En Python, nous utilisons principalement :

- **Boucle `for`** : Pour itérer sur une séquence (liste, tuple, chaîne, etc.).
- **Boucle `while`** : Pour répéter des instructions tant qu'une condition est vraie.

## Boucle `for`

La boucle `for` est utilisée pour **parcourir** des éléments d'une séquence.

```python
nombres = [1, 2, 3, 4, 5]
for nombre in nombres:
    print(nombre)
```

### Utiliser `range()` avec `for`

La fonction `range()` est souvent utilisée pour générer une séquence de nombres.

```python
for i in range(5):
    print(i)  # Affiche 0, 1, 2, 3, 4
```

## Boucle `while`

La boucle `while` continue tant qu'une condition est vraie.

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1
```

## Instructions `break` et `continue`

- **`break`** : Interrompt complètement la boucle.
- **`continue`** : Saute à l'itération suivante de la boucle.

```python
for i in range(10):
    if i == 5:
        break  # Sort de la boucle quand i vaut 5
    print(i)
```

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Saute les nombres pairs
    print(i)
```

## Boucles Imbriquées

Les boucles peuvent être **imbriquées** les unes dans les autres pour parcourir des structures complexes.

```python
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```

## Boucle avec `else`

L'instruction `else` peut être utilisée avec les boucles. Elle est exécutée lorsque la boucle se termine sans interruption par `break`.

```python
for i in range(5):
    print(i)
else:
    print("Boucle terminée sans interruption.")
```

## Itérer sur des Listes

Vous pouvez utiliser une boucle pour **parcourir** les éléments d'une liste.

```python
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(fruit)
```

## Itérer sur des Dictionnaires

Pour **parcourir** les clés et les valeurs d'un dictionnaire :

```python
personne = {"nom": "Alice", "âge": 25}
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")
```

## Boucle Infinie

Une **boucle infinie** est une boucle qui continue sans fin. Soyez prudent lorsque vous utilisez une boucle `while` avec une condition toujours vraie.

```python
while True:
    print("Ceci est une boucle infinie.")
    # Utilisez `break` pour sortir de la boucle
```

## Boucles et Compréhensions

Les **compréhensions** de liste permettent de créer une nouvelle liste en utilisant une boucle de manière concise.

```python
nombres = [1, 2, 3, 4, 5]
carres = [n * n for n in nombres]
print(carres)  # [1, 4, 9, 16, 25]
```

## Optimisation des Boucles

Pour optimiser l'utilisation des boucles :

- **Limiter les calculs à l'intérieur de la boucle**.
- **Utiliser des compréhensions** lorsque cela est possible.

```python
# Mauvais exemple
somme = 0
for i in range(1000):
    somme += i

# Bon exemple (utilise sum() directement)
somme = sum(range(1000))
```