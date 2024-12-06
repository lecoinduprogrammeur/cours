# Plan de leçon : Les variables en Python

## Informations générales

- Date : À définir
- Classe : Niveau débutant en programmation
- Matière : Informatique - Programmation Python
- Thème : Les variables et types de données en Python
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Comprendre le concept de variable en programmation et maîtriser leur utilisation en Python

- Objectifs disciplinaires :
  - Savoir déclarer une variable en Python
  - Connaître et utiliser les différents types de données de base
  - Comprendre les règles de nommage des variables
  - Savoir modifier la valeur d'une variable

- Objectifs transversaux :
  - Développer la logique de programmation
  - Apprendre à organiser son code de manière claire
  - Acquérir le vocabulaire technique approprié

## Prérequis
- Avoir Python installé sur son ordinateur
- Savoir lancer l'interpréteur Python
- Connaissances basiques de l'utilisation d'un ordinateur

## Matériel et ressources
- Ordinateurs avec Python installé
- Éditeur de texte ou IDE Python
- Support de cours (exemples de code)
- Exercices pratiques préparés

## Déroulement de la leçon

### Introduction (15 min)
1. Analogie avec la vie réelle : 
   - Une variable est comme une boîte étiquetée dans laquelle on peut ranger une valeur
   - Exemple : une boîte étiquetée "âge" qui contient le nombre 25

2. Présentation des concepts clés :
   ```python
   age = 25  # Création d'une variable "age" contenant la valeur 25
   ```

### Phase d'apprentissage (30 min)

1. Les types de variables de base :
   ```python
   # Nombres entiers (int)
   age = 25
   
   # Nombres décimaux (float)
   taille = 1.75
   
   # Chaînes de caractères (str)
   nom = "Alice"
   
   # Booléens (bool)
   est_etudiant = True
   ```

2. Règles de nommage :
   - Utiliser des lettres, chiffres et underscore
   - Commencer par une lettre ou underscore
   - Sensible à la casse (age ≠ Age)
   - Pas de mots réservés Python

3. Modification des variables :
   ```python
   age = 25
   print(age)  # Affiche 25
   age = 26
   print(age)  # Affiche 26
   ```

### Phase de pratique (30 min)

Exercices progressifs :

1. Exercice de base :
   ```python
   # Créer trois variables de types différents
   # Afficher leur contenu avec print()
   ```

2. Exercice intermédiaire :
   ```python
   # Créer des variables pour stocker des informations personnelles
   # (nom, âge, taille, est_étudiant)
   # Les afficher dans une phrase cohérente
   ```

3. Exercice avancé :
   ```python
   # Échanger les valeurs de deux variables
   # Modifier une variable et observer le changement
   ```

### Synthèse et récapitulation (10 min)
- Révision des points clés
- Questions des élèves
- Tableau récapitulatif des types de variables

### Évaluation formative (5 min)
Quiz rapide :
1. Quelle est la syntaxe pour créer une variable en Python ?
2. Citez 3 types de variables différents
3. Donnez 2 règles de nommage des variables

## Devoirs et prolongements

Devoirs :
1. Créer un petit programme utilisant au moins 4 variables de types différents
2. Documenter chaque variable avec un commentaire

Prolongements :
- Découverte des listes et tuples
- Introduction aux opérations sur les variables
- Concept de conversion de types (casting)