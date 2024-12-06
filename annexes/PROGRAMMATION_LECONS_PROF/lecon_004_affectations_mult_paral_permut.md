# Plan de leçon : Affectations multiples, parallèles et permutations en Python

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Les différents types d'affectations
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les différentes techniques d'affectation en Python

- Objectifs disciplinaires :
  - Comprendre et utiliser l'affectation multiple
  - Maîtriser l'affectation parallèle
  - Savoir effectuer des permutations de variables
  - Comprendre le déballage (unpacking) de séquences

- Objectifs transversaux :
  - Développer la pensée algorithmique
  - Améliorer la concision du code
  - Apprendre à optimiser son code

## Prérequis
- Connaître les variables en Python
- Comprendre les types de données de base
- Notions sur les séquences (listes, tuples)

## Matériel et ressources
- Ordinateurs avec Python installé
- Support de cours avec exemples
- Exercices pratiques préparés
- Environnement de développement (IDLE ou autre)

## Déroulement de la leçon

### Introduction (10 min)
1. Rappel sur l'affectation simple
2. Présentation des avantages des affectations avancées

### Phase 1 : Affectation multiple (20 min)

1. Affectation de la même valeur :
   ```python
   # Méthode classique
   x = 5
   y = 5
   z = 5
   
   # Affectation multiple
   x = y = z = 5
   print(x, y, z)  # 5 5 5
   
   # Attention aux objets mutables !
   a = b = []  # Les deux variables référencent la même liste
   a.append(1)
   print(b)  # [1] car a et b pointent vers le même objet
   ```

2. Points d'attention :
   ```python
   # Créer des listes indépendantes
   liste1, liste2 = [], []  # Correct, deux listes distinctes
   
   # Éviter avec les objets mutables
   x = y = [1, 2, 3]  # Les deux variables partagent la même liste
   ```

### Phase 2 : Affectation parallèle (20 min)

1. Affectation parallèle simple :
   ```python
   # Méthode classique
   temp = x
   x = y
   y = temp
   
   # Affectation parallèle
   x, y = 10, 20
   print(x, y)  # 10 20
   ```

2. Utilisation avec expressions :
   ```python
   # Calculs parallèles
   x, y = 1 + 2, 3 * 4
   
   # Avec des fonctions
   def get_coordinates():
       return 5, 10
   
   x, y = get_coordinates()
   ```

3. Déballage de séquences :
   ```python
   # Déballage de liste ou tuple
   coordonnees = (3, 4)
   x, y = coordonnees
   
   # Déballage partiel avec *
   premier, *milieu, dernier = [1, 2, 3, 4, 5]
   print(premier)  # 1
   print(milieu)   # [2, 3, 4]
   print(dernier)  # 5
   ```

### Phase 3 : Permutations (20 min)

1. Permutation simple :
   ```python
   # Méthode classique avec variable temporaire
   x = 5
   y = 10
   temp = x
   x = y
   y = temp
   
   # Méthode Python (permutation parallèle)
   x, y = y, x
   ```

2. Permutations multiples :
   ```python
   # Permutation de trois variables
   x, y, z = 1, 2, 3
   x, y, z = z, x, y
   
   # Rotation de valeurs
   a, b, c, d = 1, 2, 3, 4
   a, b, c, d = d, a, b, c
   ```

3. Applications pratiques :
   ```python
   # Tri de deux valeurs
   a, b = 10, 5
   if a > b:
       a, b = b, a  # Met la plus petite valeur dans a
   
   # Échange dans une liste
   liste = [1, 2, 3, 4]
   liste[0], liste[-1] = liste[-1], liste[0]  # Échange premier et dernier
   ```

### Phase de pratique (15 min)

Exercices progressifs :

1. Affectations multiples :
   ```python
   # Créer trois variables avec la même valeur
   # Créer trois listes distinctes en une ligne
   ```

2. Affectations parallèles :
   ```python
   # Échanger les valeurs de deux variables
   # Déballer une séquence de coordonnées 3D
   ```

3. Permutations complexes :
   ```python
   # Faire une rotation de 4 valeurs
   # Trier trois nombres en utilisant des permutations
   ```

### Synthèse et récapitulation (5 min)
- Tableau comparatif des méthodes
- Cas d'utilisation recommandés
- Points de vigilance

### Évaluation formative (5 min)
Questions rapides :
1. Comment échanger deux variables sans variable temporaire ?
2. Quelle est la différence entre x = y = [] et x, y = [], [] ?
3. Comment extraire le premier et dernier élément d'une liste en ignorant le reste ?

## Devoirs et prolongements

Devoirs :
1. Écrire un programme de tri de trois nombres utilisant uniquement des permutations
2. Créer une fonction qui fait une rotation de n variables
3. Expérimenter avec le déballage de séquences

Prolongements :
- Étude des affectations conditionnelles
- Utilisation avec les compréhensions de liste
- Applications dans le tri de données

## Points importants à retenir :

1. Affectation multiple :
   - Même valeur pour plusieurs variables
   - Attention aux objets mutables
   - Utile pour l'initialisation

2. Affectation parallèle :
   - Permet d'affecter plusieurs variables en une ligne
   - Plus lisible que les affectations séquentielles
   - Supporte le déballage de séquences

3. Permutations :
   - Méthode Python élégante sans variable temporaire
   - Utile pour les tris et rotations
   - Applicable aux éléments de séquences