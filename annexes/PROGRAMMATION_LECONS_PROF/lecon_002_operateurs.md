# Plan de leçon : Les opérateurs arithmétiques et logiques en Python

## Informations générales

- Date : À définir
- Classe : Niveau débutant en programmation
- Matière : Informatique - Programmation Python
- Thème : Les opérateurs arithmétiques et logiques
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des opérateurs arithmétiques et logiques en Python

- Objectifs disciplinaires :
  - Comprendre et utiliser les opérateurs arithmétiques de base
  - Maîtriser les opérations avec priorité
  - Comprendre et utiliser les opérateurs de comparaison
  - Maîtriser les opérateurs logiques (AND, OR, NOT)

- Objectifs transversaux :
  - Développer la logique mathématique
  - Renforcer la capacité à résoudre des problèmes
  - Améliorer la compréhension des expressions booléennes

## Prérequis
- Connaître les variables en Python
- Comprendre les types de données de base (int, float, bool)
- Notions de mathématiques de base

## Matériel et ressources
- Ordinateurs avec Python installé
- Support de cours avec exemples
- Fiche récapitulative des opérateurs
- Série d'exercices préparés

## Déroulement de la leçon

### Introduction (15 min)
1. Rappel sur les variables et les types
2. Introduction aux opérateurs :
   ```python
   # Les opérateurs nous permettent de manipuler les données
   x = 5 + 3  # Addition
   y = True and False  # Opération logique
   ```

### Phase d'apprentissage - Partie 1 : Opérateurs arithmétiques (40 min)

1. Les opérateurs de base :
   ```python
   # Addition (+)
   somme = 5 + 3  # résultat : 8
   
   # Soustraction (-)
   difference = 10 - 4  # résultat : 6
   
   # Multiplication (*)
   produit = 3 * 4  # résultat : 12
   
   # Division (/)
   division = 15 / 3  # résultat : 5.0 (toujours un float)
   
   # Division entière (//)
   division_entiere = 17 // 3  # résultat : 5
   
   # Modulo (%)
   reste = 17 % 3  # résultat : 2
   
   # Puissance (**)
   puissance = 2 ** 3  # résultat : 8
   ```

2. Priorité des opérations :
   - Parenthèses
   - Puissance
   - Multiplication/Division
   - Addition/Soustraction

3. Opérateurs d'assignation composés :
   ```python
   x = 5
   x += 3  # équivaut à x = x + 3
   x *= 2  # équivaut à x = x * 2
   ```

### Phase d'apprentissage - Partie 2 : Opérateurs logiques (40 min)

1. Opérateurs de comparaison :
   ```python
   # Égal à (==)
   5 == 5  # True
   
   # Différent de (!=)
   5 != 3  # True
   
   # Supérieur à (>)
   5 > 3  # True
   
   # Inférieur à (<)
   5 < 3  # False
   
   # Supérieur ou égal à (>=)
   5 >= 5  # True
   
   # Inférieur ou égal à (<=)
   5 <= 3  # False
   ```

2. Opérateurs logiques :
   ```python
   # AND (and)
   True and True  # True
   True and False  # False
   
   # OR (or)
   True or False  # True
   False or False  # False
   
   # NOT (not)
   not True  # False
   not False  # True
   ```

3. Combinaisons d'opérateurs :
   ```python
   age = 25
   permis = True
   peut_conduire = age >= 18 and permis
   ```

### Phase de pratique (15 min)

Exercices progressifs :

1. Calculs arithmétiques :
   ```python
   # Calculer le périmètre et l'aire d'un rectangle
   longueur = 5
   largeur = 3
   # À compléter...
   ```

2. Logique simple :
   ```python
   # Vérifier si un nombre est pair et positif
   nombre = 14
   # À compléter...
   ```

3. Exercice combiné :
   ```python
   # Déterminer si une personne peut accéder à une attraction
   age = 12
   taille = 1.40
   accompagne = True
   # Condition : plus de 10 ans ET (plus de 1.50m OU accompagné)
   # À compléter...
   ```

### Synthèse et récapitulation (5 min)
- Tableau des opérateurs et leur priorité
- Points clés à retenir
- Questions fréquentes

### Évaluation formative (5 min)
Mini-quiz :
1. Quel est le résultat de 15 // 4 ?
2. Quelle est la différence entre / et // ?
3. Que donne True and not False ?
4. Comment écrire "x est compris entre 0 et 10" ?

## Devoirs et prolongements

Devoirs :
1. Série d'exercices mêlant calculs et conditions
2. Créer un petit programme de calculatrice
3. Résoudre des problèmes logiques simples

Prolongements :
- Introduction aux structures conditionnelles (if/else)
- Opérations sur les chaînes de caractères
- Manipulation de dates avec opérateurs