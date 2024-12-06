# Plan de leçon : Règles et conventions de nommage des variables en Python

## Informations générales

- Date : À définir
- Classe : Débutants en programmation
- Matière : Informatique - Programmation Python
- Thème : Règles et conventions de nommage
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les règles et conventions de nommage en Python

- Objectifs disciplinaires :
  - Connaître les règles syntaxiques de nommage
  - Comprendre et appliquer les conventions PEP 8
  - Savoir choisir des noms significatifs
  - Éviter les erreurs courantes de nommage

- Objectifs transversaux :
  - Développer de bonnes pratiques de programmation
  - Améliorer la lisibilité du code
  - Acquérir une rigueur dans l'écriture du code

## Prérequis
- Connaissances de base en Python
- Savoir créer des variables simples
- Comprendre les différents types de données

## Matériel et ressources
- Ordinateurs avec Python installé
- Guide PEP 8
- Exemples de code bien/mal nommé
- Exercices pratiques

## Déroulement de la leçon

### Introduction (10 min)
1. Importance du nommage en programmation
2. Impact sur la maintenabilité du code

### Phase 1 : Règles syntaxiques (20 min)

1. Caractères autorisés :
   ```python
   # Lettres (a-z, A-Z)
   nom = "Alice"
   
   # Chiffres (0-9, pas en première position)
   age2 = 25  # Correct
   2age = 25  # Incorrect !
   
   # Underscore (_)
   mon_nom = "Bob"
   _variable_privee = "Secret"
   ```

2. Règles fondamentales :
   ```python
   # Ne pas utiliser de mots réservés Python
   class = "Python"  # Incorrect !
   
   # Case sensitive (sensible à la casse)
   age = 25
   Age = 26  # Variable différente de 'age'
   
   # Pas d'espaces ni de caractères spéciaux
   mon nom = "Alice"  # Incorrect !
   nom-complet = "Bob"  # Incorrect !
   ```

### Phase 2 : Conventions PEP 8 (25 min)

1. Snake case pour les variables et fonctions :
   ```python
   # Bon style
   nom_utilisateur = "Alice"
   calcul_moyenne = 15.5
   
   # À éviter
   nomUtilisateur = "Alice"  # camelCase
   NomUtilisateur = "Alice"  # PascalCase
   ```

2. Conventions spéciales :
   ```python
   # Variables "privées"
   _compteur_interne = 0
   
   # Variables "très privées"
   __donnees_protegees = "secret"
   
   # Constantes (en majuscules)
   PI = 3.14159
   VITESSE_LUMIERE = 299792458
   ```

3. Noms descriptifs :
   ```python
   # Mauvais nommage
   x = 3600
   n = "Bob"
   l = [1, 2, 3]
   
   # Bon nommage
   secondes_par_heure = 3600
   nom_client = "Bob"
   liste_nombres = [1, 2, 3]
   ```

### Phase 3 : Bonnes pratiques (20 min)

1. Longueur des noms :
   ```python
   # Trop court (pas assez descriptif)
   n = "Alice"
   c = 12345
   
   # Trop long (verbeux)
   nom_complet_de_lutilisateur_courant_connecte = "Alice"
   
   # Bon équilibre
   nom_utilisateur = "Alice"
   code_client = 12345
   ```

2. Contextes spécifiques :
   ```python
   # Compteurs de boucle
   for i in range(5):  # Acceptable pour les indices simples
       print(i)
   
   # Gestionnaires de fichiers
   with open("data.txt") as fichier:  # Nom explicite
       contenu = fichier.read()
   ```

3. Nommage selon le type :
   ```python
   # Listes (pluriel)
   nombres = [1, 2, 3]
   utilisateurs = ["Alice", "Bob"]
   
   # Booléens (questions ou état)
   est_actif = True
   peut_voter = False
   a_paye = True
   ```

### Phase de pratique (10 min)

Exercices progressifs :

1. Correction de noms :
   ```python
   # Corriger ces noms de variables
   x = 25
   CoutTotal = 199.99
   liste_des_nombres_premiers_inferieurs_a_cent = [2, 3, 5, 7, 11]
   ```

2. Choix de noms :
   ```python
   # Choisir des noms appropriés pour ces cas
   # Une liste de températures
   # Un booléen indiquant si un utilisateur est connecté
   # Une constante pour le nombre de jours dans une semaine
   ```

### Synthèse et récapitulation (5 min)
- Résumé des règles principales
- Points à retenir
- Erreurs fréquentes à éviter

### Évaluation formative (5 min)
Quiz rapide :
1. Quels caractères sont autorisés dans les noms de variables ?
2. Comment nommer une constante en Python ?
3. Quel style de nommage est recommandé pour les variables ?

## Devoirs et prolongements

Devoirs :
1. Analyser le nommage dans un code existant
2. Renommer des variables dans un script donné
3. Créer un mini-guide de nommage personnalisé

Prolongements :
- Conventions de nommage pour les classes
- Nommage dans les frameworks Python
- Outils de vérification de style (pylint, flake8)

## Points importants à retenir :

1. Règles syntaxiques :
   - Lettres, chiffres, underscore
   - Pas de caractères spéciaux
   - Pas de mots réservés

2. Conventions PEP 8 :
   - snake_case pour les variables
   - MAJUSCULES pour les constantes
   - _prefixe pour les éléments "privés"

3. Bonnes pratiques :
   - Noms descriptifs
   - Longueur appropriée
   - Éviter les abréviations ambiguës

4. Liste des mots réservés à éviter :
   ```python
   False    await      else       import     pass
   None     break      except     in         raise
   True     class      finally    is         return
   and      continue   for        lambda     try
   as       def        from       nonlocal   while
   assert   del        global     not        with
   async    elif       if         or         yield
   ```