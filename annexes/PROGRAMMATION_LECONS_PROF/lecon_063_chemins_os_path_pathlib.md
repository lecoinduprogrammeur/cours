# Leçon : Gestion des chemins de fichiers avec `os`, `os.path` et `pathlib` en Python

## Informations générales

- **Date :** À définir
- **Classe :** 5ème Transition Technique Informatique
- **Matière :** Programmation Python
- **Thème ou sujet :** Gestion des chemins de fichiers avec les modules `os`, `os.path`, et `pathlib`
- **Durée prévue :** 1 heure

## Objectifs de la leçon

- **Objectif général :** Comprendre et savoir manipuler les chemins de fichiers et de répertoires en utilisant les modules `os`, `os.path`, et `pathlib` en Python.
- **Objectifs disciplinaires :**
  - Savoir utiliser `os` et `os.path` pour manipuler les chemins de fichiers.
  - Savoir utiliser le module `pathlib` pour des opérations modernes sur les chemins.
  - Comparer et comprendre les différences entre les modules `os.path` et `pathlib`.
- **Objectifs transversaux :**
  - Développer la capacité à naviguer dans le système de fichiers pour gérer des ressources.
  - Renforcer la compréhension de la gestion des fichiers et des répertoires dans les projets de programmation.

## Prérequis

- Connaissance des bases de la programmation Python (variables, boucles, fonctions).
- Notions de base sur la manipulation de fichiers texte.

## Matériel et ressources

- Ordinateur avec Python installé.
- Accès à un environnement de développement (Jupyter, VS Code, ou autre).

## Déroulement de la leçon

### Introduction (10 minutes)

Expliquez la nécessité de gérer les chemins de fichiers dans les projets Python, surtout lors de la manipulation de fichiers et de répertoires. Présentez les modules `os`, `os.path`, et `pathlib` comme des outils permettant de rendre ces opérations plus simples et multiplateformes.

**Exemple :** Charger un fichier de données ou créer un dossier pour enregistrer des résultats dans un projet.

### Phase d'apprentissage (20 minutes)

#### Utilisation du module `os` et `os.path` (10 minutes)

- Présentez les fonctions du module `os` et `os.path` pour manipuler les chemins.
- **Exemples :**
  ```python
  import os
  
  # Obtenir le répertoire courant
  repertoire_courant = os.getcwd()
  print(f"Répertoire courant : {repertoire_courant}")
  
  # Créer un nouveau dossier
  nouveau_dossier = os.path.join(repertoire_courant, "nouveau_dossier")
  os.makedirs(nouveau_dossier, exist_ok=True)
  print(f"Dossier créé : {nouveau_dossier}")
  
  # Vérifier si un fichier ou un dossier existe
  existe = os.path.exists(nouveau_dossier)
  print(f"Le dossier existe : {existe}")
  ```
- Expliquez l'utilisation de `os.path.join()` pour construire des chemins de manière sécurisée, indépendamment du système d'exploitation.

#### Utilisation du module `pathlib` (10 minutes)

- Présentez `pathlib` comme une alternative moderne et plus intuitive pour manipuler les chemins de fichiers.
- **Exemples :**
  ```python
  from pathlib import Path
  
  # Obtenir le répertoire courant
  repertoire_courant = Path.cwd()
  print(f"Répertoire courant : {repertoire_courant}")
  
  # Créer un nouveau dossier
  nouveau_dossier = repertoire_courant / "nouveau_dossier"
  nouveau_dossier.mkdir(exist_ok=True)
  print(f"Dossier créé : {nouveau_dossier}")
  
  # Vérifier si un fichier ou un dossier existe
  existe = nouveau_dossier.exists()
  print(f"Le dossier existe : {existe}")
  ```
- Expliquez que `pathlib` permet d'utiliser des objets `Path` qui rendent la manipulation des chemins plus naturelle et intuitive.

### Phase de pratique (20 minutes)

- Proposez un exercice où les élèves doivent créer un dossier nommé `projet` dans le répertoire courant, puis créer un fichier `data.txt` à l'intérieur de ce dossier.
- **Exercice :** Utiliser à la fois `os` et `pathlib` pour créer un répertoire et un fichier, puis vérifier leur existence.

  **Exemple :**
  ```python
  import os
  from pathlib import Path
  
  # Avec os
  repertoire_courant = os.getcwd()
  projet_dossier = os.path.join(repertoire_courant, "projet")
  os.makedirs(projet_dossier, exist_ok=True)
  fichier_path = os.path.join(projet_dossier, "data.txt")
  with open(fichier_path, "w") as fichier:
      fichier.write("Données de test")
  
  # Avec pathlib
  projet_dossier_path = Path.cwd() / "projet"
  projet_dossier_path.mkdir(exist_ok=True)
  fichier_path = projet_dossier_path / "data.txt"
  fichier_path.write_text("Données de test avec pathlib")
  ```

### Synthèse et récapitulation (5 minutes)

- Demandez aux élèves de rappeler les différences entre `os.path` et `pathlib`.
- Résumez les avantages de l'utilisation de `pathlib` pour la manipulation des chemins de fichiers par rapport à `os.path`.

### Évaluation formative (5 minutes)

- Posez quelques questions orales pour vérifier la compréhension :
  - Quelle est la différence entre `os.path.join()` et l'opérateur `/` de `pathlib` ?
  - Comment vérifier si un fichier ou un dossier existe en utilisant `pathlib` ?
  - Pourquoi est-il utile d'utiliser `exist_ok=True` lors de la création d'un dossier ?

## Devoirs et prolongements

- Proposez un exercice à réaliser à la maison : créer un programme qui vérifie l'existence d'un dossier nommé `backup` dans le répertoire courant, puis crée un fichier nommé `log.txt` à l'intérieur de ce dossier pour enregistrer la date et l'heure de la création du fichier.

- Fournir un lien vers la documentation officielle de Python sur les modules `os` et `pathlib` pour permettre aux élèves d'approfondir leurs connaissances.