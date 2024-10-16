# Python / Manipuler les dictionnaires

**© Fabrice Dumont**

- [Python / Manipuler les dictionnaires](#python---manipuler-les-dictionnaires)
  - [Exemple](#exemple)
  - [Créer un dictionnaire](#créer-un-dictionnaire)
  - [Accéder aux Valeurs d'un Dictionnaire](#accéder-aux-valeurs-dun-dictionnaire)
  - [Ajouter ou Modifier des Paires Clé-Valeur](#ajouter-ou-modifier-des-paires-clé-valeur)
  - [Supprimer des Paires Clé-Valeur](#supprimer-des-paires-clé-valeur)
  - [Rechercher des Clés ou des Valeurs](#rechercher-des-clés-ou-des-valeurs)
  - [Itérer sur un Dictionnaire](#itérer-sur-un-dictionnaire)
  - [Méthodes Utiles des Dictionnaires](#méthodes-utiles-des-dictionnaires)

## Exemple

Un dictionnaire est une collection de paires clé-valeur en Python. Voici un exemple simple :

```python
mon_dictionnaire = {
    "nom": "Alice",
    "âge": 30,
    "profession": "Ingénieur"
}
print(mon_dictionnaire)
```

## Créer un dictionnaire

Pour créer un dictionnaire, vous pouvez utiliser des accolades `{}` et définir des paires clé-valeur séparées par des virgules :

```python
mon_dictionnaire = {
    "clé1": "valeur1",
    "clé2": "valeur2"
}
```

Il est également possible de créer un dictionnaire vide :

```python
mon_dictionnaire_vide = {}
```

## Accéder aux Valeurs d'un Dictionnaire

Pour accéder à une valeur dans un dictionnaire, utilisez la clé correspondante :

```python
nom = mon_dictionnaire["nom"]
print(nom)  # Affiche "Alice"
```

Vous pouvez aussi utiliser la méthode `get()` pour éviter une erreur si la clé n'existe pas :

```python
âge = mon_dictionnaire.get("âge", "Clé non trouvée")
print(âge)  # Affiche 30
```

## Ajouter ou Modifier des Paires Clé-Valeur

Pour ajouter une nouvelle paire clé-valeur ou modifier une valeur existante, utilisez la syntaxe suivante :

```python
mon_dictionnaire["adresse"] = "123 Rue Exemple"
mon_dictionnaire["âge"] = 31  # Met à jour la valeur de "âge"
```

## Supprimer des Paires Clé-Valeur

Pour supprimer une paire clé-valeur, vous pouvez utiliser `del` ou la méthode `pop()` :

```python
del mon_dictionnaire["profession"]
# ou
âge = mon_dictionnaire.pop("âge")
print(âge)  # Affiche 31
```

## Rechercher des Clés ou des Valeurs

Pour vérifier si une clé existe dans un dictionnaire, utilisez l'opérateur `in` :

```python
if "nom" in mon_dictionnaire:
    print("La clé 'nom' est présente.")
```

Pour vérifier si une valeur est présente :

```python
if "Alice" in mon_dictionnaire.values():
    print("La valeur 'Alice' est présente.")
```

## Itérer sur un Dictionnaire

Vous pouvez itérer sur les clés, les valeurs ou les paires clé-valeur :

```python
# Itérer sur les clés
for clé in mon_dictionnaire:
    print(clé)

# Itérer sur les valeurs
for valeur in mon_dictionnaire.values():
    print(valeur)

# Itérer sur les paires clé-valeur
for clé, valeur in mon_dictionnaire.items():
    print(f"{clé}: {valeur}")
```

## Méthodes Utiles des Dictionnaires

Voici quelques méthodes courantes des dictionnaires :

- `keys()` : Renvoie une vue des clés du dictionnaire. Cela peut être utile pour parcourir toutes les clés d'un dictionnaire.

  ```python
  clés = mon_dictionnaire.keys()
  print(clés)  # Affiche dict_keys(['nom', 'âge', 'profession'])
  ```

- `values()` : Renvoie une vue des valeurs du dictionnaire. Vous pouvez l'utiliser pour accéder à toutes les valeurs.

  ```python
  valeurs = mon_dictionnaire.values()
  print(valeurs)  # Affiche dict_values(['Alice', 30, 'Ingénieur'])
  ```

- `items()` : Renvoie une vue des paires clé-valeur sous forme de tuples. Très pratique pour itérer sur un dictionnaire.

  ```python
  paires = mon_dictionnaire.items()
  print(paires)  # Affiche dict_items([('nom', 'Alice'), ('âge', 30), ('profession', 'Ingénieur')])
  ```

- `clear()` : Vide le dictionnaire, supprimant toutes les paires clé-valeur.

  ```python
  mon_dictionnaire.clear()
  print(mon_dictionnaire)  # Affiche {}
  ```

- `copy()` : Renvoie une copie superficielle du dictionnaire. Utile pour dupliquer un dictionnaire sans affecter l'original.

  ```python
  copie_dictionnaire = mon_dictionnaire.copy()
  print(copie_dictionnaire)  # Affiche {'nom': 'Alice', 'âge': 30, 'profession': 'Ingénieur'}
  ```

- `pop()` : Supprime une clé spécifiée et renvoie la valeur correspondante. Si la clé n'existe pas, vous pouvez fournir une valeur par défaut.

  ```python
  âge = mon_dictionnaire.pop("âge", "Clé non trouvée")
  print(âge)  # Affiche 30
  ```

- `update()` : Met à jour le dictionnaire avec les paires clé-valeur d'un autre dictionnaire ou des paires fournies en argument.

  ```python
  mon_dictionnaire.update({"nationalité": "Française", "âge": 31})
  print(mon_dictionnaire)  # Affiche {'nom': 'Alice', 'profession': 'Ingénieur', 'nationalité': 'Française', 'âge': 31}
  ```