# Leçon : Lecture et écriture avec le module `json` dans un fichier texte

## Informations générales

- **Date :** À définir
- **Classe :** 5ème Transition Technique Informatique
- **Matière :** Programmation Python
- **Thème ou sujet :** Lecture et écriture de scores de joueurs dans un fichier texte au format JSON
- **Durée prévue :** 1 heure

## Objectifs de la leçon

- **Objectif général :** Comprendre et savoir manipuler des fichiers texte pour stocker des données structurées en utilisant le module `json` en Python.
- **Objectifs disciplinaires :**
  - Savoir créer un fichier texte pour stocker des données au format JSON.
  - Savoir lire, écrire et mettre à jour des données JSON dans un fichier texte.
  - Apprendre à manipuler des fichiers de manière sécurisée en utilisant l'instruction `with`.
- **Objectifs transversaux :**
  - Développer la capacité à gérer des données structurées pour des projets de programmation.
  - Renforcer la compréhension des méthodes de gestion des scores ou des données utilisateur.

## Prérequis

- Connaissance des bases de la programmation Python (variables, boucles, fonctions).
- Notions de base sur la manipulation de chaînes de caractères et des dictionnaires.

## Matériel et ressources

- Ordinateur avec Python installé.
- Accès à un environnement de développement (Jupyter, VS Code, ou autre).
- Exemple de fichier texte pour la pratique.

## Déroulement de la leçon

### Introduction (10 minutes)

Expliquez aux élèves l'importance de pouvoir enregistrer et charger des données structurées, comme les scores de joueurs dans un jeu. Introduisez le format JSON comme un moyen pratique de stocker ces informations. Donnez des exemples de scénarios d'utilisation, tels que les classements de joueurs ou la sauvegarde d'avancements dans un jeu.

**Exemple :** Stocker les scores de plusieurs joueurs dans un fichier texte afin de les récupérer à chaque partie :
```json
[
  {"nom": "Alice", "score": 1500},
  {"nom": "Bob", "score": 2000}
]
```

### Phase d'apprentissage (20 minutes)

#### Création et écriture dans un fichier texte (10 minutes)

- Présentez la syntaxe de base pour créer un fichier texte et y écrire des scores au format JSON en utilisant le module `json`.
- **Exemple :**
  ```python
  import json
  
  scores = [
      {"nom": "Alice", "score": 1500},
      {"nom": "Bob", "score": 2000}
  ]
  
  with open("scores.txt", "w") as fichier:
      json.dump(scores, fichier, indent=4)
  ```
- Expliquez que `json.dump()` permet de convertir une liste de dictionnaires en une structure JSON, puis de l'écrire dans le fichier.

#### Lecture du contenu d'un fichier texte (10 minutes)

- Montrez comment lire les scores à partir d'un fichier texte.
- **Exemple :**
  ```python
  import json
  
  with open("scores.txt", "r") as fichier:
      scores = json.load(fichier)
      for joueur in scores:
          print(f"Joueur : {joueur['nom']}, Score : {joueur['score']}")
  ```
- Expliquez que `json.load()` permet de lire le contenu JSON du fichier et de le convertir en une structure Python (liste de dictionnaires).

### Phase de pratique (20 minutes)

- Proposez un exercice où les élèves doivent charger les scores existants depuis un fichier texte, ajouter un nouveau score, puis réécrire le fichier avec le score mis à jour.
- **Exercice :** Créer un programme qui lit les scores des joueurs, ajoute un nouveau score, puis réécrit le fichier.

  **Exemple :**
  ```python
  import json
  
  # Lecture des scores existants
  with open("scores.txt", "r") as fichier:
      scores = json.load(fichier)
  
  # Ajout d'un nouveau joueur
  nouveau_joueur = {"nom": "Charlie", "score": 1800}
  scores.append(nouveau_joueur)
  
  # Réécriture du fichier avec les nouveaux scores
  with open("scores.txt", "w") as fichier:
      json.dump(scores, fichier, indent=4)
  ```

### Synthèse et récapitulation (5 minutes)

- Demandez aux élèves de rappeler pourquoi il est utile de sauvegarder des données sous forme de fichiers JSON.
- Résumez les étapes pour créer, lire et mettre à jour un fichier texte contenant des données JSON.

### Évaluation formative (5 minutes)

- Posez quelques questions orales pour vérifier la compréhension :
  - Quelle est la différence entre `json.dump()` et `json.load()` ?
  - Comment ajouter un nouvel élément aux données JSON existantes ?
  - Pourquoi est-il important d'utiliser l'instruction `with` pour ouvrir un fichier ?

## Devoirs et prolongements

- Proposez un exercice à réaliser à la maison : créer un programme qui lit un fichier JSON contenant des informations sur des joueurs et leurs scores, puis demande à l'utilisateur d'ajouter un nouveau score. Le fichier doit être réécrit avec les nouvelles informations.

- Fournir un lien vers la documentation officielle de Python sur le module `json` pour permettre aux élèves d'approfondir leurs connaissances.