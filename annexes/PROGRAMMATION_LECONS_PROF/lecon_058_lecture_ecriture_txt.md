# Leçon : Lecture et écriture dans un fichier texte en Python

## Informations générales

- **Date :** À définir
- **Classe :** 5ème Transition Technique Informatique
- **Matière :** Programmation Python
- **Thème ou sujet :** Lecture et écriture dans un fichier texte
- **Durée prévue :** 1 heure

## Objectifs de la leçon

- **Objectif général :** Comprendre et savoir manipuler des fichiers texte en Python pour lire et écrire des données.
- **Objectifs disciplinaires :**
  - Savoir ouvrir, lire et écrire dans un fichier texte.
  - Comprendre les modes d'ouverture des fichiers (`r`, `w`, `a`, `r+`).
  - Apprendre à manipuler des fichiers de manière sécurisée en utilisant l'instruction `with`.
- **Objectifs transversaux :**
  - Développer la capacité à manipuler des fichiers dans le cadre de projets de programmation.
  - Renforcer la compréhension des aspects pratiques de la gestion des données.

## Prérequis

- Connaissance des bases de la programmation Python (variables, boucles, fonctions).
- Notions de base sur la manipulation de chaînes de caractères.

## Matériel et ressources

- Ordinateur avec Python installé.
- Accès à un environnement de développement (Jupyter, VS Code, ou autre).
- Exemple de fichier texte à utiliser en classe.

## Déroulement de la leçon

### Introduction (10 minutes)

Expliquez ce qu'est un fichier texte et pourquoi il est important dans le cadre de la programmation. Montrez des exemples concrets de situations où la lecture et l'écriture de fichiers sont nécessaires, comme l'enregistrement des résultats d'un programme ou la lecture de données d'entrée pour une analyse.

**Exemple :** Un programme qui enregistre une liste de tâches dans un fichier texte pour une utilisation ultérieure.

### Phase d'apprentissage (20 minutes)

#### Lecture d'un fichier texte (10 minutes)

- Présentez la syntaxe de base pour lire un fichier texte avec Python en utilisant l'instruction `open()`.
- **Exemple :**
  ```python
  with open("exemple.txt", "r") as fichier:
      contenu = fichier.read()
      print(contenu)
  ```
- Expliquez l'importance d'utiliser `with` pour garantir que le fichier est bien fermé après utilisation.
- Mentionnez les différentes méthodes de lecture (`read()`, `readline()`, `readlines()`).

#### Écriture dans un fichier texte (10 minutes)

- Présentez la syntaxe de base pour écrire dans un fichier texte.
- **Exemple :**
  ```python
  with open("exemple.txt", "w") as fichier:
      fichier.write("Bonjour, ceci est un exemple de texte.")
  ```
- Expliquez les différents modes d'ouverture (`w` pour écrire, `a` pour ajouter, `r+` pour lire et écrire).
- Donnez des exemples concrets où chaque mode serait approprié.

### Phase de pratique (20 minutes)

- Proposez un exercice où les élèves doivent lire le contenu d'un fichier texte, puis ajouter une nouvelle ligne à ce fichier.
- **Exercice :** Créer un fichier nommé `journal.txt` et y écrire une entrée de journal. Ensuite, ajouter une nouvelle entrée à chaque exécution du programme.

  **Exemple :**
  ```python
  with open("journal.txt", "a") as fichier:
      fichier.write("Nouvelle entrée de journal : Aujourd'hui, j'ai appris à manipuler des fichiers en Python.\n")
  ```

### Synthèse et récapitulation (5 minutes)

- Demandez aux élèves de rappeler les différents modes d'ouverture des fichiers.
- Résumez les bonnes pratiques, comme l'utilisation de `with` pour la gestion des fichiers.

### Évaluation formative (5 minutes)

- Posez quelques questions orales pour vérifier la compréhension :
  - Comment lire tout le contenu d'un fichier ?
  - Quelle est la différence entre les modes `w` et `a` ?
  - Pourquoi est-il important d'utiliser `with` ?

## Devoirs et prolongements

- Proposez un exercice à réaliser à la maison : créer un programme qui lit une liste de noms à partir d'un fichier texte, puis ajoute un nouveau nom à la liste et réécrit le fichier avec la liste mise à jour.

- Fournir un lien vers la documentation officielle de Python sur la manipulation des fichiers pour permettre aux élèves d'approfondir leurs connaissances.