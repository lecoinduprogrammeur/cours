# Leçon : Les gestionnaires de contexte (`with`) en Python

## Informations générales

- **Date :** À définir
- **Classe :** 5ème Transition Technique Informatique
- **Matière :** Programmation Python
- **Thème ou sujet :** Gestionnaires de contexte (`with`)
- **Durée prévue :** 1 heure

## Objectifs de la leçon

- **Objectif général :** Comprendre l'utilisation des gestionnaires de contexte (`with`) en Python pour simplifier la gestion des ressources.
- **Objectifs disciplinaires :**
  - Savoir utiliser les gestionnaires de contexte pour ouvrir et manipuler des fichiers.
  - Comprendre les avantages d'utiliser `with` pour la gestion des ressources.
  - Savoir implémenter un gestionnaire de contexte personnalisé.
- **Objectifs transversaux :**
  - Développer la capacité à écrire du code plus propre et plus sécurisé.
  - Renforcer la compréhension de la gestion automatique des ressources.

## Prérequis

- Connaissance des bases de la programmation Python (variables, boucles, fonctions).
- Notions de base sur la manipulation de fichiers en Python.

## Matériel et ressources

- Ordinateur avec Python installé.
- Accès à un environnement de développement (Jupyter, VS Code, ou autre).

## Déroulement de la leçon

### Introduction (10 minutes)

Expliquez ce qu'est un gestionnaire de contexte en Python et pourquoi il est utile. Montrez que `with` est utilisé pour simplifier la gestion des ressources telles que les fichiers, les connexions réseau, etc. Soulignez les problèmes potentiels de gestion des ressources lorsque les fichiers ne sont pas fermés correctement et comment `with` permet de résoudre ces problèmes.

**Exemple :** Ouvrir un fichier sans `with` et l'oublier de le fermer, ce qui peut entraîner une fuite de ressources.

### Phase d'apprentissage (20 minutes)

#### Utilisation de `with` pour la gestion des fichiers (10 minutes)

- Montrez comment utiliser `with` pour ouvrir et lire un fichier de manière sûre.
- **Exemple :**
  ```python
  # Sans gestionnaire de contexte
  fichier = open("exemple.txt", "r")
  try:
      contenu = fichier.read()
      print(contenu)
  finally:
      fichier.close()
  
  # Avec gestionnaire de contexte (with)
  with open("exemple.txt", "r") as fichier:
      contenu = fichier.read()
      print(contenu)
  ```
- Expliquez que `with` garantit la fermeture du fichier, même en cas d'erreur.

#### Implémentation d'un gestionnaire de contexte personnalisé (10 minutes)

- Montrez comment créer un gestionnaire de contexte personnalisé à l'aide de la classe `contextlib` ou en définissant les méthodes `__enter__()` et `__exit__()`.
- **Exemple :**
  ```python
  from contextlib import contextmanager
  
  @contextmanager
  def gestionnaire_personnalise():
      print("Ressource ouverte")
      yield
      print("Ressource fermée")
  
  with gestionnaire_personnalise():
      print("Code à l'intérieur du gestionnaire")
  ```
- Expliquez les avantages de créer des gestionnaires de contexte personnalisés pour simplifier la gestion des ressources dans des scénarios spécifiques.

### Phase de pratique (20 minutes)

- Proposez un exercice où les élèves doivent ouvrir un fichier nommé `donnees.txt`, lire son contenu, puis écrire une nouvelle ligne à la fin du fichier en utilisant `with`.
- **Exercice :** Utiliser `with` pour ouvrir le fichier et assurer sa fermeture automatique.

  **Exemple :**
  ```python
  # Lecture du fichier avec gestionnaire de contexte
  with open("donnees.txt", "r") as fichier:
      contenu = fichier.read()
      print(f"Contenu du fichier :\n{contenu}")
  
  # Ajout d'une nouvelle ligne au fichier avec gestionnaire de contexte
  with open("donnees.txt", "a") as fichier:
      fichier.write("Nouvelle ligne ajoutée avec 'with'.\n")
  ```

### Synthèse et récapitulation (5 minutes)

- Demandez aux élèves de rappeler les avantages de l'utilisation de `with`.
- Résumez les bonnes pratiques de gestion des ressources, en insistant sur l'importance de toujours fermer les ressources (comme les fichiers) après leur utilisation.

### Évaluation formative (5 minutes)

- Posez quelques questions orales pour vérifier la compréhension :
  - Que fait le mot-clé `with` en Python ?
  - Pourquoi est-il important d'utiliser `with` pour manipuler des fichiers ?
  - Comment créer un gestionnaire de contexte personnalisé ?

## Devoirs et prolongements

- Proposez un exercice à réaliser à la maison : créer un gestionnaire de contexte personnalisé qui ouvre un fichier, affiche un message lorsque le fichier est ouvert, et un autre message lorsque le fichier est fermé.

- Fournir un lien vers la documentation officielle de Python sur les gestionnaires de contexte pour permettre aux élèves d'approfondir leurs connaissances.