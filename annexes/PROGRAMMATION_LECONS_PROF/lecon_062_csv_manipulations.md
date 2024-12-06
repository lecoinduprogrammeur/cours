# Leçon : Manipulation de fichiers CSV en Python

## Informations générales

- **Date :** À définir
- **Classe :** 5ème Transition Technique Informatique
- **Matière :** Programmation Python
- **Thème ou sujet :** Lecture et écriture de fichiers CSV
- **Durée prévue :** 1 heure

## Objectifs de la leçon

- **Objectif général :** Comprendre et savoir manipuler des fichiers CSV en Python pour lire et écrire des données tabulaires.
- **Objectifs disciplinaires :**
  - Savoir utiliser le module `csv` pour lire et écrire des données dans un fichier CSV.
  - Comprendre les différences entre les fichiers texte, JSON et CSV.
  - Apprendre à manipuler des fichiers de manière sécurisée en utilisant l'instruction `with`.
- **Objectifs transversaux :**
  - Développer la capacité à travailler avec des données structurées de manière tabulaire.
  - Renforcer la compréhension des formats de données utilisés dans l'échange et le stockage de données.

## Prérequis

- Connaissance des bases de la programmation Python (variables, boucles, fonctions).
- Notions de base sur la manipulation de fichiers texte et JSON.

## Matériel et ressources

- Ordinateur avec Python installé.
- Accès à un environnement de développement (Jupyter, VS Code, ou autre).
- Exemple de fichier CSV pour la pratique.

## Déroulement de la leçon

### Introduction (10 minutes)

Expliquez ce qu'est un fichier CSV (Comma-Separated Values) et comment il est utilisé pour stocker des données tabulaires, comme des feuilles de calcul. Montrez des exemples concrets de scénarios où les fichiers CSV sont utilisés, tels que le stockage des informations sur les étudiants ou la collecte de données issues de formulaires.

**Exemple :** Stocker des informations sur des employés :
```csv
nom,age,departement
Alice,30,Informatique
Bob,25,RH
Charlie,28,Marketing
```

### Phase d'apprentissage (20 minutes)

#### Écriture dans un fichier CSV (10 minutes)

- Présentez la syntaxe de base pour écrire des données dans un fichier CSV en utilisant le module `csv`.
- **Exemple :**
  ```python
  import csv
  
  # Données à écrire dans le fichier CSV
  employes = [
      ["nom", "age", "departement"],
      ["Alice", 30, "Informatique"],
      ["Bob", 25, "RH"],
      ["Charlie", 28, "Marketing"]
  ]
  
  with open("employes.csv", "w", newline="") as fichier:
      writer = csv.writer(fichier)
      writer.writerows(employes)
  ```
- Expliquez que `csv.writer()` est utilisé pour écrire des lignes dans un fichier CSV et que `writerows()` permet d'écrire plusieurs lignes à la fois.

#### Lecture du contenu d'un fichier CSV (10 minutes)

- Montrez comment lire les données d'un fichier CSV en utilisant le module `csv`.
- **Exemple :**
  ```python
  import csv
  
  with open("employes.csv", "r") as fichier:
      reader = csv.reader(fichier)
      for ligne in reader:
          print(ligne)
  ```
- Expliquez que `csv.reader()` permet de lire chaque ligne du fichier CSV et de les convertir en liste Python.

### Phase de pratique (20 minutes)

- Proposez un exercice où les élèves doivent créer un fichier CSV contenant des informations sur les étudiants (nom, âge, classe), puis le lire et afficher chaque ligne.
- **Exercice :** Créer un fichier `etudiants.csv` et y écrire des informations sur au moins trois étudiants. Ensuite, écrire un programme qui lit les données du fichier et les affiche dans la console.

  **Exemple :**
  ```python
  import csv
  
  # Écriture des informations des étudiants
  etudiants = [
      ["nom", "age", "classe"],
      ["Alice", 15, "5ème"],
      ["Bob", 16, "5ème"],
      ["Charlie", 15, "5ème"]
  ]
  
  with open("etudiants.csv", "w", newline="") as fichier:
      writer = csv.writer(fichier)
      writer.writerows(etudiants)
  
  # Lecture des informations des étudiants
  with open("etudiants.csv", "r") as fichier:
      reader = csv.reader(fichier)
      for ligne in reader:
          print(ligne)
  ```

### Synthèse et récapitulation (5 minutes)

- Demandez aux élèves de rappeler la structure des fichiers CSV et les avantages de ce format pour stocker des données tabulaires.
- Résumez les étapes pour écrire et lire des fichiers CSV en Python, en insistant sur l'utilisation du module `csv`.

### Évaluation formative (5 minutes)

- Posez quelques questions orales pour vérifier la compréhension :
  - Comment écrire plusieurs lignes dans un fichier CSV ?
  - Quelle fonction utilise-t-on pour lire les données d'un fichier CSV ?
  - Dans quel cas serait-il préférable d'utiliser un fichier CSV plutôt qu'un fichier JSON ?

## Devoirs et prolongements

- Proposez un exercice à réaliser à la maison : créer un programme qui lit un fichier CSV contenant des informations sur les produits d'un magasin (nom, prix, quantité), puis demande à l'utilisateur d'ajouter un nouveau produit. Le fichier doit être mis à jour avec les nouvelles informations.

- Fournir un lien vers la documentation officielle de Python sur le module `csv` pour permettre aux élèves d'approfondir leurs connaissances.