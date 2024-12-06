# Leçon : Les arguments `*args` et `**kwargs` en Python

## Informations générales

- **Date :** À définir
- **Classe :** 5ème Transition Technique Informatique
- **Matière :** Programmation Python
- **Thème ou sujet :** Utilisation des arguments `*args` et `**kwargs`
- **Durée prévue :** 1 heure

## Objectifs de la leçon

- **Objectif général :** Comprendre et savoir utiliser les arguments `*args` et `**kwargs` dans une fonction Python pour rendre les fonctions plus flexibles.
- **Objectifs disciplinaires :**
  - Comprendre la différence entre `*args` et `**kwargs`.
  - Savoir quand utiliser `*args` et `**kwargs`.
  - Être capable de définir une fonction utilisant `*args` et/ou `**kwargs`.
- **Objectifs transversaux :**
  - Développer la capacité à comprendre des concepts avancés de programmation.
  - Renforcer la capacité à résoudre des problèmes complexes par la programmation.

## Prérequis

- Connaissance des fonctions en Python.
- Compréhension de la syntaxe de base de Python.
- Connaissance des listes et des dictionnaires.

## Matériel et ressources

- Ordinateur avec Python installé.
- Accès à un environnement de développement (Jupyter, VS Code, ou autre).
- Exemple de code sur projecteur.

## Déroulement de la leçon

### Introduction (10 minutes)

Présentez les concepts d'arguments positionnels et nommés dans les fonctions Python, et expliquez que `*args` et `**kwargs` permettent de gérer un nombre variable d'arguments. Utilisez des exemples concrets pour illustrer des situations où une fonction devrait accepter un nombre flexible d'arguments.

**Exemple :**
```python
# Fonction classique

def addition(a, b):
    return a + b

# Limitation : on ne peut additionner que deux nombres.
```

Introduisez l'idée de rendre cette fonction plus flexible avec `*args`.

### Phase d'apprentissage (20 minutes)

#### Explication de `*args` (10 minutes)

- `*args` est utilisé pour passer un nombre variable d'arguments positionnels à une fonction.
- **Exemple :**
  ```python
  def addition(*args):
      return sum(args)
  
  print(addition(1, 2, 3))  # Affiche 6
  print(addition(5, 10))    # Affiche 15
  ```
- Expliquez que `*args` collecte les arguments dans une tuple.

#### Explication de `**kwargs` (10 minutes)

- `**kwargs` est utilisé pour passer un nombre variable d'arguments nommés à une fonction.
- **Exemple :**
  ```python
  def afficher_info(**kwargs):
      for cle, valeur in kwargs.items():
          print(f"{cle} : {valeur}")
  
  afficher_info(nom="Alice", age=25, ville="Bruxelles")
  # Affiche :
  # nom : Alice
  # age : 25
  # ville : Bruxelles
  ```
- Expliquez que `**kwargs` collecte les arguments dans un dictionnaire.

### Phase de pratique (20 minutes)

- Proposez aux élèves de créer une fonction qui utilise à la fois `*args` et `**kwargs`.
- **Exercice :** Créer une fonction `description` qui prend un nombre variable d'attributs (par exemple des caractéristiques d'un produit) et affiche ces caractéristiques.

  **Exemple :**
  ```python
  def description(*args, **kwargs):
      for arg in args:
          print(arg)
      for cle, valeur in kwargs.items():
          print(f"{cle} : {valeur}")
  
  description("Produit X", prix=20, couleur="rouge")
  # Affiche :
  # Produit X
  # prix : 20
  # couleur : rouge
  ```

### Synthèse et récapitulation (5 minutes)

- Demandez aux élèves de rappeler les différences entre `*args` et `**kwargs`.
- Expliquez les cas d'utilisation où `*args` et `**kwargs` sont particulièrement utiles (ex. : rendre les fonctions plus modulaires et réutilisables).

### Évaluation formative (5 minutes)

- Posez quelques questions orales pour vérifier la compréhension :
  - Qu'est-ce que `*args` ?
  - Quand utiliser `**kwargs` ?
  - Peut-on mélanger `*args` et `**kwargs` dans une même fonction ?

## Devoirs et prolongements

- Proposez un exercice à réaliser à la maison : créer une fonction qui utilise `*args` et `**kwargs` pour gérer une liste de courses avec des articles optionnels et leurs quantités respectives.

- Fournir un lien vers la documentation officielle de Python sur `*args` et `**kwargs` pour permettre aux élèves d'approfondir leurs connaissances.