# Plan de leçon : Installation de Python et découverte de l'environnement

## Informations générales

- Date : À définir
- Classe : Débutants en programmation
- Matière : Informatique - Introduction à Python
- Thème : Installation et prise en main de l'environnement Python
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Installer Python et comprendre les différents éléments de l'environnement

- Objectifs disciplinaires :
  - Savoir télécharger et installer Python correctement
  - Identifier et comprendre les différents composants installés
  - Savoir lancer et utiliser l'interpréteur Python (IDLE)
  - Comprendre la différence entre mode interactif et mode script

- Objectifs transversaux :
  - Développer l'autonomie technique
  - Comprendre l'organisation d'un environnement de développement
  - Acquérir les bonnes pratiques d'installation de logiciels

## Prérequis
- Connaissances de base en utilisation d'ordinateur
- Droits d'administrateur sur le poste de travail
- Connexion Internet pour le téléchargement

## Matériel et ressources
- Ordinateurs avec accès Internet
- Guide d'installation étape par étape
- Captures d'écran du processus d'installation
- Fiche de vérification post-installation

## Déroulement de la leçon

### Introduction (10 min)
1. Présentation de Python et de son site officiel
2. Importance d'une installation correcte
3. Vue d'ensemble des composants à installer

### Phase 1 : Téléchargement et Installation (20 min)

1. Processus de téléchargement :
   - Visiter python.org
   - Localiser la dernière version stable
   - Choisir la version adaptée au système d'exploitation
   - Vérifier la case "Add Python to PATH" lors de l'installation

2. Composants installés :
   ```
   C:\Users\[Username]\AppData\Local\Programs\Python\Python3x\
   ├── python.exe (Interpréteur Python)
   ├── pythonw.exe (Pour applications graphiques)
   ├── Lib\ (Bibliothèques standard)
   ├── Scripts\ (Scripts et outils)
   └── Tools\ (Outils supplémentaires)
   ```

### Phase 2 : Découverte de l'environnement (30 min)

1. Composants principaux installés :

   a) IDLE (Integrated Development and Learning Environment) :
   - Éditeur de code intégré
   - Shell interactif
   - Débogueur simple
   - Coloration syntaxique

   b) L'interpréteur Python :
   - Accessible en ligne de commande
   - Exécute le code Python
   - Mode interactif vs mode script

   c) PIP (Package Installer for Python) :
   - Gestionnaire de paquets
   - Installation de bibliothèques externes
   - Mise à jour de paquets

2. Les deux modes d'utilisation :

   a) Mode interactif (Shell) :
   ```python
   >>> print("Hello World")
   Hello World
   >>> 2 + 2
   4
   ```

   b) Mode script (Fichier .py) :
   ```python
   # mon_script.py
   print("Ceci est un script")
   resultat = 2 + 2
   print(f"2 + 2 = {resultat}")
   ```

### Phase de pratique (20 min)

1. Vérification de l'installation :
   ```bash
   # Dans le terminal/invite de commandes
   python --version
   pip --version
   ```

2. Premiers pas avec IDLE :
   - Lancer IDLE
   - Tester le mode interactif
   - Créer et sauvegarder un premier script

3. Test des composants :
   - Exécuter un script depuis IDLE
   - Exécuter un script depuis le terminal
   - Installer un package simple avec pip

### Synthèse et récapitulation (5 min)
- Résumé des composants installés
- Points de vigilance
- Bonnes pratiques

### Évaluation formative (5 min)
Vérification pratique :
1. Localiser l'installation de Python
2. Lancer IDLE
3. Créer et exécuter un script simple
4. Installer un package avec pip

## Devoirs et prolongements

Devoirs :
1. Installer Python sur son ordinateur personnel
2. Créer un premier script "Hello World"
3. Explorer les menus d'IDLE

Prolongements :
- Installation d'un IDE plus avancé (PyCharm, VS Code)
- Découverte des environnements virtuels
- Installation de bibliothèques courantes (numpy, pandas)

## Points importants à retenir :

1. Après l'installation de Python, nous avons :

   - **L'interpréteur Python** :
     - python.exe : pour exécuter du code Python
     - pythonw.exe : pour les applications graphiques

   - **IDLE** (environnement de développement intégré) :
     - Éditeur de code
     - Shell interactif
     - Outils de débogage

   - **PIP** (gestionnaire de paquets) :
     - Pour installer des bibliothèques supplémentaires
     - Pour gérer les dépendances

   - **Bibliothèque standard Python** :
     - Modules préinstallés
     - Fonctionnalités de base

2. Points de vérification post-installation :
   - Python ajouté au PATH système
   - IDLE accessible depuis le menu démarrer
   - Commandes python et pip fonctionnelles dans le terminal