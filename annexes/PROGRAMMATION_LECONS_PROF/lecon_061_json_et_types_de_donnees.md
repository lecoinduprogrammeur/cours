# Leçon : Lecture et écriture de différents types de données avec le module `json` en Python

## Informations générales

- **Date :** À définir
- **Classe :** 5ème Transition Technique Informatique
- **Matière :** Programmation Python
- **Thème ou sujet :** Lecture et écriture de chaînes, listes et dictionnaires au format JSON
- **Durée prévue :** 1 heure

## Objectifs de la leçon

- **Objectif général :** Comprendre et savoir manipuler différents types de données (chaînes, listes, dictionnaires) avec le module `json` en Python pour les lire et les écrire dans des fichiers texte.
- **Objectifs disciplinaires :**
  - Savoir utiliser le module `json` pour écrire des chaînes de caractères, des listes et des dictionnaires dans un fichier texte.
  - Savoir lire des chaînes de caractères, des listes et des dictionnaires depuis un fichier JSON.
  - Apprendre à manipuler des fichiers de manière sécurisée en utilisant l'instruction `with`.
- **Objectifs transversaux :**
  - Développer la capacité à gérer des données structurées de différents types pour des projets de programmation.
  - Renforcer la compréhension de la conversion de données entre différents formats.

## Prérequis

- Connaissance des bases de la programmation Python (variables, boucles, fonctions).
- Notions de base sur la manipulation de chaînes de caractères, listes et dictionnaires.

## Matériel et ressources

- Ordinateur avec Python installé.
- Accès à un environnement de développement (Jupyter, VS Code, ou autre).
- Exemple de fichier texte pour la pratique.

## Déroulement de la leçon

### Introduction (10 minutes)

Expliquez ce qu'est le format JSON (JavaScript Object Notation) et pourquoi il est si largement utilisé pour stocker différents types de données. Montrez des exemples de scénarios où l'on peut avoir besoin de stocker des chaînes, des listes et des dictionnaires, comme dans les fichiers de configuration d'une application ou les données d'un jeu.

**Exemple :** Stocker une liste de courses, une configuration de paramètres ou des informations utilisateur.

### Phase d'apprentissage (20 minutes)

#### Écriture de différents types de données dans un fichier JSON (10 minutes)

- **Chaînes de caractères :**
  ```python
  import json
  
  chaine = "Bonjour, ceci est une chaîne de caractères."
  
  with open("chaine.txt", "w") as fichier:
      json.dump(chaine, fichier)
  ```
  Expliquez que `json.dump()` permet d'écrire n'importe quel objet JSON sérialisable, y compris des chaînes de caractères, dans un fichier.

- **Listes :**
  ```python
  import json
  
  liste_courses = ["pommes", "bananes", "lait", "pain"]
  
  with open("liste.txt", "w") as fichier:
      json.dump(liste_courses, fichier, indent=4)
  ```
  Expliquez que les listes peuvent également être sérialisées au format JSON et écrites dans un fichier.

- **Dictionnaires :**
  ```python
  import json
  
  parametres = {
      "volume": 75,
      "luminosite": 50,
      "mode": "nuit"
  }
  
  with open("parametres.txt", "w") as fichier:
      json.dump(parametres, fichier, indent=4)
  ```
  Présentez comment les dictionnaires sont écrits au format JSON dans un fichier texte.

#### Lecture de différents types de données depuis un fichier JSON (10 minutes)

- **Lecture d'une chaîne de caractères :**
  ```python
  import json
  
  with open("chaine.txt", "r") as fichier:
      chaine = json.load(fichier)
      print(chaine)
  ```
  Montrez comment lire une chaîne de caractères depuis un fichier texte JSON.

- **Lecture d'une liste :**
  ```python
  import json
  
  with open("liste.txt", "r") as fichier:
      liste_courses = json.load(fichier)
      print(liste_courses)
  ```
  Expliquez que `json.load()` permet de convertir le contenu JSON en une liste Python.

- **Lecture d'un dictionnaire :**
  ```python
  import json
  
  with open("parametres.txt", "r") as fichier:
      parametres = json.load(fichier)
      print(parametres)
  ```
  Montrez comment les données d'un dictionnaire peuvent être lues et utilisées.

### Phase de pratique (20 minutes)

- Proposez un exercice où les élèves doivent écrire une chaîne de caractères, une liste, et un dictionnaire dans des fichiers JSON séparés, puis les lire et les afficher.
- **Exercice :** Créer trois fichiers (`chaine.txt`, `liste.txt`, `parametres.txt`) contenant chacun une chaîne, une liste, et un dictionnaire respectivement. Les élèves devront ensuite écrire un programme qui lit les données de chaque fichier et les affiche dans la console.

  **Exemple :**
  ```python
  import json
  
  # Lecture de la chaîne de caractères
  with open("chaine.txt", "r") as fichier:
      chaine = json.load(fichier)
      print(f"Chaîne : {chaine}")
  
  # Lecture de la liste
  with open("liste.txt", "r") as fichier:
      liste_courses = json.load(fichier)
      print(f"Liste de courses : {liste_courses}")
  
  # Lecture du dictionnaire
  with open("parametres.txt", "r") as fichier:
      parametres = json.load(fichier)
      print(f"Paramètres : {parametres}")
  ```

### Synthèse et récapitulation (5 minutes)

- Demandez aux élèves de rappeler les types de données qu'on peut enregistrer au format JSON.
- Résumez les étapes pour écrire et lire des chaînes, des listes, et des dictionnaires dans des fichiers texte au format JSON.

### Évaluation formative (5 minutes)

- Posez quelques questions orales pour vérifier la compréhension :
  - Comment écrire une liste dans un fichier JSON ?
  - Quelle fonction utiliser pour lire le contenu d'un fichier JSON ?
  - Quels types de données peut-on enregistrer au format JSON ?

## Devoirs et prolongements

- Proposez un exercice à réaliser à la maison : créer un programme qui stocke les préférences d'un utilisateur (sous forme de dictionnaire) dans un fichier JSON, puis le lit et affiche les préférences lors de la prochaine exécution.

- Fournir un lien vers la documentation officielle de Python sur le module `json` pour permettre aux élèves d'approfondir leurs connaissances.