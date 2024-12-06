# Plan de leçon : Les fonctions id() et print() en Python

## Informations générales

- Date : À définir
- Classe : Débutants en programmation
- Matière : Informatique - Programmation Python
- Thème : Utilisation des fonctions id() et print()
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des fonctions id() et print() en Python

- Objectifs disciplinaires :
  - Comprendre le concept d'identifiant d'objet avec id()
  - Maîtriser les différentes utilisations de print()
  - Savoir formater l'affichage avec print()
  - Comprendre la différence entre les objets et leurs références

- Objectifs transversaux :
  - Développer la compréhension de la gestion de la mémoire
  - Améliorer les capacités de débogage
  - Apprendre à présenter les données de manière claire

## Prérequis
- Connaître les variables en Python
- Comprendre les types de données de base
- Notions de base sur les fonctions

## Matériel et ressources
- Ordinateurs avec Python installé
- IDLE ou éditeur de code
- Support de cours avec exemples
- Exercices pratiques

## Déroulement de la leçon

### Introduction (15 min)
1. Rappel sur les fonctions intégrées de Python
2. Importance de l'affichage et du débogage

### Phase d'apprentissage - Partie 1 : La fonction id() (30 min)

1. Présentation de id() :
   ```python
   # id() retourne l'identifiant unique d'un objet
   x = 42
   print(f"L'identifiant de x est : {id(x)}")
   ```

2. Comprendre les références :
   ```python
   # Même valeur = même identifiant pour les nombres simples
   a = 5
   b = 5
   print(id(a))  # même identifiant
   print(id(b))  # même identifiant
   
   # Objets différents = identifiants différents
   liste1 = [1, 2, 3]
   liste2 = [1, 2, 3]
   print(id(liste1))  # identifiant différent
   print(id(liste2))  # identifiant différent
   ```

3. Cas particuliers :
   ```python
   # Références multiples
   x = [1, 2, 3]
   y = x  # y référence le même objet que x
   print(id(x) == id(y))  # True
   
   # Modification d'objet
   y.append(4)  # modifie aussi x car c'est le même objet
   print(x)  # [1, 2, 3, 4]
   ```

### Phase d'apprentissage - Partie 2 : La fonction print() (30 min)

1. Utilisation de base :
   ```python
   # Affichage simple
   print("Hello World")
   
   # Affichage de plusieurs éléments
   nom = "Alice"
   age = 25
   print("Nom:", nom, "Age:", age)
   ```

2. Formatage de l'affichage :
   ```python
   # F-strings (recommandé)
   nom = "Bob"
   age = 30
   print(f"Je m'appelle {nom} et j'ai {age} ans")
   
   # Format()
   print("Je m'appelle {} et j'ai {} ans".format(nom, age))
   
   # % operator (ancien style)
   print("Je m'appelle %s et j'ai %d ans" % (nom, age))
   ```

3. Paramètres de print() :
   ```python
   # Séparateur personnalisé
   print("Python", "est", "génial", sep="-")  # Python-est-génial
   
   # Fin de ligne personnalisée
   print("Ligne 1", end=" -> ")
   print("Ligne 2")  # Ligne 1 -> Ligne 2
   
   # Redirection vers un fichier
   with open("sortie.txt", "w") as f:
       print("Texte dans fichier", file=f)
   ```

### Phase de pratique (10 min)

Exercices progressifs :

1. Identifiants et références :
   ```python
   # Créer différentes variables et comparer leurs identifiants
   x = 100
   y = 100
   z = y
   # Vérifier les identifiants
   ```

2. Formatage d'affichage :
   ```python
   # Créer un petit programme qui affiche un tableau formaté
   produits = [("Pomme", 1.20), ("Banane", 0.90)]
   # Afficher un tableau prix formaté
   ```

### Synthèse et récapitulation (5 min)
- Cas d'utilisation de id()
- Meilleures pratiques pour print()
- Points à retenir sur les références

### Évaluation formative (5 min)
Quiz pratique :
1. Quand deux variables ont-elles le même identifiant ?
2. Comment afficher plusieurs variables sur la même ligne ?
3. Quelle est la meilleure méthode de formatage en Python moderne ?

## Devoirs et prolongements

Devoirs :
1. Créer un programme utilisant différents styles de formatage
2. Expérimenter avec les identifiants de différents types d'objets
3. Créer un petit système d'affichage formaté pour un jeu de données

Prolongements :
- Étude des f-strings avancées
- Exploration d'autres fonctions built-in
- Création de fonctions d'affichage personnalisées

## Points importants à retenir :

1. La fonction id() :
   - Retourne un identifiant unique pour chaque objet
   - Utile pour comprendre les références
   - Aide au débogage

2. La fonction print() :
   - Fonction principale d'affichage
   - Nombreuses options de formatage
   - F-strings pour le formatage moderne
   - Paramètres sep, end et file pour personnaliser l'affichage