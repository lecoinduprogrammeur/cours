# Leçon : Lecture et écriture avec le module `json` en Python

## Informations générales

- **Date :** À définir
- **Classe :** 5ème Transition Technique Informatique
- **Matière :** Programmation Python
- **Thème ou sujet :** Lecture et écriture de fichiers JSON
- **Durée prévue :** 1 heure

## Objectifs de la leçon

- **Objectif général :** Comprendre et savoir manipuler des fichiers JSON en Python pour lire et écrire des données structurées.
- **Objectifs disciplinaires :**
  - Comprendre la structure des fichiers JSON.
  - Savoir lire et écrire des données JSON en utilisant le module `json`.
  - Apprendre à manipuler des fichiers de manière sécurisée en utilisant l'instruction `with`.
- **Objectifs transversaux :**
  - Développer la capacité à manipuler des fichiers de données structurées.
  - Renforcer la compréhension de la gestion des données dans des projets de programmation.

## Prérequis

- Connaissance des bases de la programmation Python (variables, boucles, fonctions).
- Notions de base sur la manipulation de chaînes de caractères et des dictionnaires.

## Matériel et ressources

- Ordinateur avec Python installé.
- Accès à un environnement de développement (Jupyter, VS Code, ou autre).
- Exemple de fichier JSON à utiliser en classe.

## Déroulement de la leçon

### Introduction (10 minutes)

Expliquez ce qu'est un fichier JSON (JavaScript Object Notation) et son utilité en tant que format de données léger, lisible par l'homme et largement utilisé pour stocker et échanger des informations. Montrez des exemples concrets de situations où JSON est utilisé, comme le stockage de données utilisateur dans des applications web ou le transfert de données entre des systèmes.

**Exemple :** Fichier JSON contenant des informations sur des utilisateurs :
```json
{
  "nom": "Alice",
  "age": 25,
  "ville": "Bruxelles"
}
```

### Phase d'apprentissage (20 minutes)

#### Lecture d'un fichier JSON (10 minutes)

- Présentez la syntaxe de base pour lire un fichier JSON avec Python en utilisant le module `json`.
- **Exemple :**
  ```python
  import json
  
  with open("exemple.json", "r") as fichier:
      data = json.load(fichier)
      print(data)
  ```
- Expliquez comment les données JSON sont converties en dictionnaire Python après la lecture.

#### Écriture dans un fichier JSON (10 minutes)

- Présentez la syntaxe de base pour écrire des données dans un fichier JSON.
- **Exemple :**
  ```python
  import json
  
  donnees = {
      "nom": "Alice",
      "age": 25,
      "ville": "Bruxelles"
  }
  
  with open("exemple.json", "w") as fichier:
      json.dump(donnees, fichier, indent=4)
  ```
- Expliquez les options de formatage, comme `indent`, pour rendre le fichier JSON plus lisible.

### Phase de pratique (20 minutes)

- Proposez un exercice où les élèves doivent lire des données d'un fichier JSON, les modifier, puis les réécrire dans le même fichier.
- **Exercice :** Créer un fichier nommé `utilisateurs.json` contenant des informations sur des utilisateurs, puis ajouter un nouvel utilisateur à chaque exécution du programme.

  **Exemple :**
  ```python
  import json
  
  with open("utilisateurs.json", "r") as fichier:
      utilisateurs = json.load(fichier)
  
  nouveaux_utilisateurs = {
      "nom": "Bob",
      "age": 30,
      "ville": "Anvers"
  }
  
  utilisateurs.append(nouveaux_utilisateurs)
  
  with open("utilisateurs.json", "w") as fichier:
      json.dump(utilisateurs, fichier, indent=4)
  ```

### Synthèse et récapitulation (5 minutes)

- Demandez aux élèves de rappeler ce qu'est JSON et comment il se différencie des fichiers texte classiques.
- Résumez les bonnes pratiques pour manipuler des fichiers JSON, notamment l'utilisation de `with` et du module `json` pour la sécurité et la lisibilité.

### Évaluation formative (5 minutes)

- Posez quelques questions orales pour vérifier la compréhension :
  - Comment lire des données à partir d'un fichier JSON ?
  - Quelle est la structure d'un fichier JSON ?
  - Pourquoi est-il important d'utiliser `with` pour ouvrir un fichier ?

## Devoirs et prolongements

- Proposez un exercice à réaliser à la maison : créer un programme qui lit des données depuis un fichier JSON contenant des informations sur une liste de produits, puis ajoute un nouveau produit à cette liste et réécrit le fichier.

- Fournir un lien vers la documentation officielle de Python sur le module `json` pour permettre aux élèves d'approfondir leurs connaissances.