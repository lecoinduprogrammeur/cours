# Python /  Manipuler les listes

**© Fabrice Dumont**

Les **listes** en Python sont des collections ordonnées qui peuvent contenir des éléments de différents types (nombres, chaînes, booléens, etc.). Une liste est définie en utilisant des **crochets** `[ ]` et les éléments sont séparés par des **virgules**.

## Exemple 

```python
ma_liste = [1, 2, 3, "Python", True]
```

## Créer une liste 

```python
vide = []  # Liste vide
nombres = [1, 2, 3, 4, 5]  # Liste de nombres
mixte = [1, "chat", 3.5, False]  # Liste mixte
```

## Accéder aux Éléments d'une Liste

Les éléments d'une liste sont indexés à partir de 0.

```python
animaux = ["chat", "chien", "poisson"]
print(animaux[0])  # chat
print(animaux[2])  # poisson
```

Vous pouvez aussi utiliser des **indices négatifs** pour accéder aux éléments en partant de la fin.

```python
print(animaux[-1])  # poisson
```

## Slices de Liste

Vous pouvez obtenir des sous-listes avec la syntaxe de **slice**.

```python
nombres = [0, 1, 2, 3, 4, 5]
print(nombres[1:4])  # [1, 2, 3]
print(nombres[:3])   # [0, 1, 2]
print(nombres[3:])   # [3, 4, 5]
```

## Modifier les Éléments d'une Liste

Les listes sont **mutables**, c'est-à-dire que leurs éléments peuvent être modifiés.

```python
animaux[1] = "oiseau"
print(animaux)  # ["chat", "oiseau", "poisson"]
```

## Ajouter des Éléments

**append()** : Ajoute un élément à la fin de la liste.

```python
animaux.append("cheval")

# ["chat", "oiseau", "poisson", "cheval"]
```

**insert(index, valeur)** : Insère un élément à une position spécifique.

```python
animaux.insert(1, "tortue")

# ["chat", "tortue", "oiseau", "poisson", "cheval"]
```

**extend(iterable)** : Ajoute plusieurs éléments à la liste.

```python
animaux.extend(["serpent", "lion"])

# ["chat", "tortue", "oiseau", "poisson", "cheval", "serpent", "lion"]
```

## Supprimer des Éléments

**remove(valeur)** : Supprime la première occurrence d'une valeur donnée.

```python
animaux.remove("oiseau")

# ["chat", "tortue", "poisson", "cheval", "serpent", "lion"]
```

**pop(index)** : Supprime l'élément à un index donné (par défaut, le dernier élément) et le retourne.

```python
animaux.pop(2)

# ["chat", "tortue", "cheval", "serpent", "lion"]
```

**del** : Supprime un élément à un index spécifique ou une tranche de la liste.

```python
del animaux[1]

# ["chat", "cheval", "serpent", "lion"]
```

## Rechercher des Éléments

**index(valeur)** : Retourne l'indice de la première occurrence de la valeur.

```python
index = animaux.index("cheval")  # 1
```

**in** : Vérifie si un élément est présent dans la liste.

```python
existe = "lion" in animaux  # True
```

## Autres Méthodes des Listes

**count(valeur)** : Retourne le nombre de fois qu'une valeur apparaît.

```python
nombres = [1, 2, 2, 3, 4]
print(nombres.count(2))  # 2
```

**reverse()** : Inverse l'ordre des éléments de la liste.

```python
nombres.reverse()

# [4, 3, 2, 2, 1]
```

**sort()** : Trie les éléments dans l'ordre croissant (ou décroissant avec `reverse=True`).

```python
nombres.sort()

# [1, 2, 2, 3, 4]

nombres.sort(reverse=True)

# [4, 3, 2, 2, 1]
```

## Boucle sur une Liste

Vous pouvez itérer sur les éléments d'une liste avec une boucle `for`.

```python
for animal in animaux:
    print(animal)
```

## Longueur d'une Liste

Utilisez la fonction **len()** pour obtenir la longueur d'une liste.

```python
print(len(animaux))  # 4
```

## Copie de Liste

Pour copier une liste, vous pouvez utiliser plusieurs méthodes :

- **Slice** :

```python
copie = animaux[:]
```

- **copy()** :

```python
copie = animaux.copy()
```

- **list()** :

```python
copie = list(animaux)
```

## Compréhension de Liste

Les **compréhensions de liste** permettent de créer des listes de manière concise.

```python
carrés = [x**2 for x in range(6)]

# [0, 1, 4, 9, 16, 25]
```

## Fusionner des Listes

Vous pouvez concaténer des listes en utilisant l'opérateur `+`.

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
fusion = liste1 + liste2

# [1, 2, 3, 4, 5, 6]
```

## Listes Imbriquées

Vous pouvez également créer des listes imbriquées (listes de listes).

```python
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrice[1][2])  # 6
```

## Méthodes Complètes des Listes

Voici un résumé des principales méthodes des listes en Python :

- **append(x)** : Ajoute `x` à la fin de la liste.
- **extend(iterable)** : Étend la liste en ajoutant tous les éléments de l'itérable.
- **insert(i, x)** : Insère `x` à la position `i`.
- **remove(x)** : Supprime la première occurrence de `x`.
- **pop([i])** : Supprime et retourne l'élément à la position `i`.
- **clear()** : Supprime tous les éléments de la liste.
- **index(x, [start, [end]])** : Retourne l'index de la première occurrence de `x`.
- **count(x)** : Retourne le nombre de fois que `x` apparaît dans la liste.
- **sort(key=None, reverse=False)** : Trie la liste en place.
- **reverse()** : Inverse les éléments de la liste en place.
- **copy()** : Retourne une copie superficielle de la liste.

## Fonctions Supplémentaires pour les Listes

Voici quelques fonctions Python utiles, souvent utilisées pour travailler avec des listes :

**enumerate()**

La fonction `enumerate()` est utilisée pour itérer à la fois sur les **indices** et les **valeurs** d'une liste, ce qui est très pratique quand vous avez besoin de connaître la position de chaque élément pendant une boucle.

```python
animaux = ["chat", "chien", "poisson"]
for index, animal in enumerate(animaux):
    print(f"Index: {index}, Animal: {animal}")
```

Exécution :

```python
Index: 0, Animal: chat
Index: 1, Animal: chien
Index: 2, Animal: poisson
```

**zip()**

La fonction `zip()` permet de combiner deux ou plusieurs listes, élément par élément. Elle retourne un **itérateur** de tuples, chaque tuple contenant des éléments des listes correspondantes.

```python
prenoms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for prenom, age in zip(prenoms, ages):
    print(f"{prenom} a {age} ans")
```

Exécution :

```python
Alice a 25 ans
Bob a 30 ans
Charlie a 35 ans
```

**map()**

La fonction `map()` applique une fonction donnée à chaque élément d'une liste. `map()` retourne un itérateur, qui peut être converti en une liste.

```python
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))
print(carres)
```

Exécution :

```python
[1, 4, 9, 16, 25]
```

**filter()**

La fonction `filter()` est utilisée pour filtrer les éléments d'une liste en fonction d'une condition spécifique. Comme `map()`, `filter()` retourne un itérateur.

```python
nombres = [1, 2, 3, 4, 5]
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)
```

Exécution :

```python
[2, 4]
```

**sum()**

La fonction `sum()` permet d'additionner toutes les valeurs numériques d'une liste.

```python
nombres = [1, 2, 3, 4, 5]
total = sum(nombres)
print(total)
```

Exécution :

```python
15
```

**min() et max()**

Les fonctions `min()` et `max()` permettent de trouver respectivement la plus petite et la plus grande valeur d'une liste.

```python
nombres = [10, 20, 5, 25, 15]
print(min(nombres))  # 5
print(max(nombres))  # 25
```

**all() et any()**

- **all()** : Retourne `True` si **tous** les éléments de la liste sont `True`.

- **any()** : Retourne `True` si **au moins un** des éléments de la liste est `True`.

```python
conditions = [True, True, False]
print(all(conditions))  # False (car un des éléments est False)
print(any(conditions))  # True (car au moins un des éléments est True)
```

**len()** (rappel)

La fonction `len()` est utilisée pour obtenir la **longueur** (le nombre d'éléments) d'une liste.

```python
animaux = ["chat", "chien", "poisson"]
print(len(animaux))  # 3
```

## Utilisation Combinée

Certaines de ces fonctions peuvent être combinées pour des tâches plus complexes. Par exemple, vous pouvez utiliser `enumerate()` pour itérer sur des listes tout en utilisant `filter()` pour ignorer certains éléments.

```python
nombres = [1, 2, 3, 4, 5, 6]
for index, nombre in enumerate(filter(lambda x: x % 2 == 0, nombres)):
    print(f"Index filtré: {index}, Nombre: {nombre}")
```

Exécution :

```python
Index filtré: 0, Nombre: 2
Index filtré: 1, Nombre: 4
Index filtré: 2, Nombre: 6
```

## Compréhensions de Liste Avancées

Les **compréhensions de liste** permettent d'intégrer des conditions (`if`) et même des boucles imbriquées pour créer des listes de manière concise.

- **Avec une condition `if`** :

```python
nombres = [1, 2, 3, 4, 5, 6]
pairs = [x for x in nombres if x % 2 == 0]
print(pairs)  # [2, 4, 6]
```

- **Avec des boucles imbriquées** :

```python
produit_cartesien = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
print(produit_cartesien)

# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
```

## Copier des Listes (Profond vs Superficiel)

Quand vous copiez une liste avec `copy()` ou avec un slice (`[:]`), cela crée une **copie superficielle**. Cela signifie que les objets imbriqués dans la liste ne sont pas copiés.

```python
originale = [[1, 2, 3], [4, 5, 6]]
copie = originale[:]
copie[0][0] = 100
print(originale)  # [[100, 2, 3], [4, 5, 6]]
print(copie)      # [[100, 2, 3], [4, 5, 6]]
```

Pour effectuer une **copie profonde**, où tous les objets imbriqués sont aussi copiés, utilisez le module `copy` avec `deepcopy()`.

```python
import copy
copie_profonde = copy.deepcopy(originale)
copie_profonde[0][0] = 200
print(originale)         # [[100, 2, 3], [4, 5, 6]]
print(copie_profonde)    # [[200, 2, 3], [4, 5, 6]]
```

## Tri avancé des Listes

**Customisation du Tri** : La méthode `sort()` et la fonction `sorted()` acceptent un paramètre optionnel `key`, qui permet de spécifier une fonction de tri personnalisée.

```python
etudiants = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
etudiants_triees = sorted(etudiants, key=lambda x: x[1])
print(etudiants_triees)  # Trie par âge : [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
```

**Tri en fonction de la longueur des éléments** :

```python
mots = ["Python", "est", "génial"]
mots_triees = sorted(mots, key=len)
print(mots_triees)  # ['est', 'Python', 'génial'] (tri par longueur)
```

## Listes Imbriquées et Boucles

Vous pouvez utiliser des boucles imbriquées pour itérer sur des **listes imbriquées**.

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for ligne in matrice:
    for element in ligne:
        print(element, end=" ")
```

Exécution :

```python
1 2 3 4 5 6 7 8 9
```

## Énumérations et Découpage de Listes

Vous pouvez également découper une liste en plusieurs sous-listes en utilisant une boucle et des compréhensions.

Exemple : Découpage d'une liste en sous-listes de taille fixe :

```python
def decouper_liste(liste, taille):
    return [liste[i:i + taille] for i in range(0, len(liste), taille)]

nombres = [1, 2, 3, 4, 5, 6, 7, 8]
sous_listes = decouper_liste(nombres, 3)
print(sous_listes)  # [[1, 2, 3], [4, 5, 6], [7, 8]]
```

## Conversion entre Listes et Autres Types

Vous pouvez facilement **convertir** des listes vers d'autres types de collections comme des tuples, ensembles, ou des chaînes.

- **Liste vers Tuple** :

```python
liste = [1, 2, 3]
tuple_converti = tuple(liste)
print(tuple_converti)  # (1, 2, 3)
```

- **Liste vers Chaîne** (pour les chaînes) :

```python
mots = ['Python', 'est', 'génial']
phrase = " ".join(mots)
print(phrase)  # 'Python est génial'
```

- **Liste vers Ensemble** :

```python
liste = [1, 2, 2, 3, 4]
ensemble = set(liste)
print(ensemble)  # {1, 2, 3, 4} (les doublons sont supprimés)
```

