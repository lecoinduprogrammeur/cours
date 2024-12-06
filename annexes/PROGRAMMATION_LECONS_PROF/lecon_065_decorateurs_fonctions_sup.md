# Leçon : Décorateurs et fonctions d'ordre supérieur en Python

## Informations générales

- **Date :** À définir
- **Classe :** 5ème Transition Technique Informatique
- **Matière :** Programmation Python
- **Thème ou sujet :** Décorateurs et fonctions d'ordre supérieur
- **Durée prévue :** 1 heure

## Objectifs de la leçon

- **Objectif général :** Comprendre l'utilisation des décorateurs et des fonctions d'ordre supérieur en Python pour enrichir la fonctionnalité des fonctions.
- **Objectifs disciplinaires :**
  - Savoir définir et utiliser des fonctions d'ordre supérieur.
  - Comprendre le concept de fermetures (closures) en Python.
  - Savoir créer et utiliser des décorateurs pour modifier le comportement d'une fonction.
- **Objectifs transversaux :**
  - Développer la capacité à écrire du code modulaire et réutilisable.
  - Renforcer la compréhension des concepts avancés de la programmation fonctionnelle.

## Prérequis

- Connaissance des bases de la programmation Python (fonctions, paramètres, retour de valeurs).
- Notions de base sur les fonctions lambda.

## Matériel et ressources

- Ordinateur avec Python installé.
- Accès à un environnement de développement (Jupyter, VS Code, ou autre).

## Déroulement de la leçon

### Introduction (10 minutes)

Expliquez ce qu'est une fonction d'ordre supérieur, c'est-à-dire une fonction qui peut prendre une autre fonction en argument ou renvoyer une fonction. Présentez également le concept de décorateur comme une fonction qui modifie le comportement d'une autre fonction sans en altérer le code directement. Donnez des exemples concrets de leur utilité, comme la journalisation (logging) ou la mesure du temps d'exécution d'une fonction.

**Exemple :** Utiliser une fonction d'ordre supérieur pour appliquer une transformation à une liste de valeurs, ou utiliser un décorateur pour vérifier les permissions avant d'exécuter une fonction.

### Phase d'apprentissage (20 minutes)

#### Fonctions d'ordre supérieur (10 minutes)

- Montrez comment une fonction d'ordre supérieur peut prendre une autre fonction en paramètre.
- **Exemple :**
  ```python
  def appliquer_deux_fois(fonction, valeur):
      return fonction(fonction(valeur))
  
  def incrementer(x):
      return x + 1
  
  resultat = appliquer_deux_fois(incrementer, 3)
  print(resultat)  # Affiche 5
  ```
- Expliquez que les fonctions d'ordre supérieur permettent de rendre le code plus générique et réutilisable.

#### Décorateurs en Python (10 minutes)

- Expliquez ce qu'est un décorateur en Python et comment l'utiliser pour modifier le comportement d'une fonction.
- **Exemple :**
  ```python
  def mon_decorateur(fonction):
      def fonction_modifiee(*args, **kwargs):
          print("Avant l'exécution de la fonction")
          resultat = fonction(*args, **kwargs)
          print("Après l'exécution de la fonction")
          return resultat
      return fonction_modifiee
  
  @mon_decorateur
  def dire_bonjour():
      print("Bonjour!")
  
  dire_bonjour()
  # Affiche :
  # Avant l'exécution de la fonction
  # Bonjour!
  # Après l'exécution de la fonction
  ```
- Expliquez l'utilisation du symbole `@` pour appliquer un décorateur à une fonction et les avantages de cette syntaxe pour écrire du code lisible et maintenable.

### Phase de pratique (20 minutes)

- Proposez un exercice où les élèves doivent créer un décorateur qui mesure le temps d'exécution d'une fonction.
- **Exercice :** Créer un décorateur `chronometrer` qui affiche le temps nécessaire à l'exécution d'une fonction.

  **Exemple :**
  ```python
  import time
  
  def chronometrer(fonction):
      def fonction_modifiee(*args, **kwargs):
          debut = time.time()
          resultat = fonction(*args, **kwargs)
          fin = time.time()
          print(f"Temps d'exécution : {fin - debut:.4f} secondes")
          return resultat
      return fonction_modifiee
  
  @chronometrer
  def somme_des_nombres():
      time.sleep(1)  # Simuler une opération qui prend du temps
      print(sum(range(1, 1000000)))
  
  somme_des_nombres()
  ```

### Synthèse et récapitulation (5 minutes)

- Demandez aux élèves de rappeler la différence entre une fonction d'ordre supérieur et un décorateur.
- Résumez les avantages de l'utilisation des décorateurs pour enrichir les fonctions sans modifier leur code de base.

### Évaluation formative (5 minutes)

- Posez quelques questions orales pour vérifier la compréhension :
  - Qu'est-ce qu'une fonction d'ordre supérieur ?
  - Quel est le rôle d'un décorateur en Python ?
  - Comment appliquer un décorateur à une fonction ?

## Devoirs et prolongements

- Proposez un exercice à réaliser à la maison : créer un décorateur qui vérifie si l'utilisateur est connecté avant d'exécuter une fonction qui affiche des informations sensibles.

- Fournir un lien vers la documentation officielle de Python sur les décorateurs et les fonctions d'ordre supérieur pour permettre aux élèves d'approfondir leurs connaissances.