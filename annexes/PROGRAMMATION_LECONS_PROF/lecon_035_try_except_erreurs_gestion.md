# Plan de leçon : Gestion des erreurs avec try et except

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Gestion des erreurs et exceptions
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser la gestion des erreurs en Python

- Objectifs disciplinaires :
  - Comprendre le système d'exceptions Python
  - Maîtriser try/except/else/finally
  - Savoir gérer différents types d'erreurs
  - Implémenter une gestion d'erreurs robuste

## Déroulement de la leçon

### 1. Structure de base try/except (20 min)

#### A. Syntaxe fondamentale
```python
# Structure basique
try:
    # Code susceptible de générer une erreur
    resultat = 10 / 0
except:
    # Gestion de l'erreur
    print("Une erreur s'est produite")

# Avec type d'exception spécifique
try:
    nombre = int("abc")
except ValueError:
    print("Conversion impossible")

# Capture de l'exception
try:
    resultat = 10 / 0
except ZeroDivisionError as e:
    print(f"Erreur : {e}")
```

#### B. Types d'erreurs courants
```python
# Erreurs de type
try:
    len(5)  # int n'a pas de longueur
except TypeError as e:
    print(f"Erreur de type : {e}")

# Erreurs de clé
try:
    dict_exemple = {}
    valeur = dict_exemple['clé_inexistante']
except KeyError as e:
    print(f"Clé non trouvée : {e}")

# Erreurs d'index
try:
    liste = [1, 2, 3]
    element = liste[10]
except IndexError as e:
    print(f"Index invalide : {e}")
```

### 2. Gestion de multiples exceptions (25 min)

#### A. Plusieurs except
```python
def division_securisee(a, b):
    try:
        # Plusieurs erreurs possibles
        resultat = int(a) / int(b)
        return resultat
    except ValueError:
        print("Les valeurs doivent être numériques")
    except ZeroDivisionError:
        print("Division par zéro impossible")
    except Exception as e:
        print(f"Autre erreur : {e}")
    
# Test avec différentes erreurs
division_securisee("abc", "2")  # ValueError
division_securisee("10", "0")   # ZeroDivisionError
```

#### B. Groupement d'exceptions
```python
def traiter_donnees(donnees):
    try:
        # Traitement risqué
        resultat = process_data(donnees)
        return resultat
    except (ValueError, TypeError) as e:
        # Gère les deux types d'erreurs
        print(f"Erreur de données : {e}")
    except (IOError, ConnectionError) as e:
        # Gère les erreurs d'E/S et réseau
        print(f"Erreur d'accès : {e}")
```

### 3. Utilisation de else et finally (20 min)

#### A. Clause else
```python
def lire_fichier(nom_fichier):
    try:
        fichier = open(nom_fichier, 'r')
    except FileNotFoundError:
        print("Fichier non trouvé")
    else:
        # Exécuté si aucune exception dans try
        contenu = fichier.read()
        fichier.close()
        return contenu

def convertir_nombre(texte):
    try:
        nombre = int(texte)
    except ValueError:
        print("Conversion impossible")
    else:
        print("Conversion réussie !")
        return nombre
```

#### B. Clause finally
```python
def acceder_ressource():
    ressource = None
    try:
        ressource = obtenir_ressource()
        # Utilisation de la ressource
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        # Toujours exécuté, même en cas d'erreur
        if ressource:
            ressource.liberer()

def traiter_fichier(nom_fichier):
    f = None
    try:
        f = open(nom_fichier, 'r')
        # Traitement du fichier
    except FileNotFoundError:
        print("Fichier introuvable")
    finally:
        # Fermeture du fichier même en cas d'erreur
        if f:
            f.close()
```

### 4. Création d'exceptions personnalisées (20 min)

```python
# Définition d'une exception personnalisée
class MonErreurPersonnalisee(Exception):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(self.message)

class ValidationError(Exception):
    """Exception pour les erreurs de validation."""
    pass

def valider_age(age):
    if not isinstance(age, int):
        raise ValidationError("L'âge doit être un entier")
    if age < 0:
        raise ValidationError("L'âge ne peut pas être négatif")
    if age > 150:
        raise ValidationError("Âge non valide")

# Utilisation
try:
    valider_age(-5)
except ValidationError as e:
    print(f"Erreur de validation : {e}")
```

### 5. Bonnes pratiques de gestion d'erreurs (25 min)

#### A. Gestion contextuelle
```python
# Utilisation de with pour la gestion des ressources
def lire_fichier_securise(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("Fichier non trouvé")
    except IOError as e:
        print(f"Erreur de lecture : {e}")

# Gestion d'erreurs hiérarchique
def fonction_principale():
    try:
        resultat = fonction_risquee()
        return traiter_resultat(resultat)
    except Exception as e:
        logger.error(f"Erreur dans fonction_principale: {e}")
        raise  # Propage l'erreur après logging
```

#### B. Logging et débogage
```python
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)

def operation_critique():
    try:
        # Opération risquée
        resultat = processus_complexe()
    except Exception as e:
        logging.error(f"Erreur critique : {e}", exc_info=True)
        # Récupération ou notification
        notifier_administrateur(e)
        return None
```

### 6. Applications pratiques (20 min)

```python
def valider_donnees_utilisateur(donnees):
    """Validation complète des données utilisateur."""
    erreurs = []
    
    try:
        # Vérification de l'âge
        age = int(donnees.get('age', ''))
        if age < 0 or age > 150:
            erreurs.append("Âge invalide")
    except ValueError:
        erreurs.append("L'âge doit être un nombre")
    
    try:
        # Vérification de l'email
        email = donnees.get('email', '')
        if '@' not in email or '.' not in email:
            erreurs.append("Email invalide")
    except Exception as e:
        erreurs.append(f"Erreur email : {e}")
    
    if erreurs:
        raise ValidationError("\n".join(erreurs))

def transaction_securisee(operation):
    """Gestion sécurisée d'une transaction."""
    transaction = None
    try:
        transaction = demarrer_transaction()
        resultat = operation(transaction)
        transaction.commit()
        return resultat
    except Exception as e:
        if transaction:
            transaction.rollback()
        logger.error(f"Erreur de transaction : {e}")
        raise
    finally:
        if transaction:
            transaction.close()
```

### Phase de pratique (15 min)

Exercices :

1. Gestionnaire de ressources :
```python
def creer_gestionnaire_ressources():
    """
    Créer un gestionnaire qui :
    - Ouvre une ressource en sécurité
    - Gère les erreurs possibles
    - Assure la libération des ressources
    """
    # À compléter
```

2. Validation de données :
```python
def valider_formulaire():
    """
    Créer un validateur qui :
    - Vérifie plusieurs champs
    - Gère différents types d'erreurs
    - Retourne des messages d'erreur appropriés
    """
    # À compléter
```

## Points importants à retenir :

1. Structure de base :
   - try/except pour capturer les erreurs
   - else pour code sans erreur
   - finally pour nettoyage

2. Types d'exceptions :
   - Exceptions standard Python
   - Exceptions personnalisées
   - Hiérarchie des exceptions

3. Bonnes pratiques :
   - Exceptions spécifiques
   - Gestion appropriée des ressources
   - Logging des erreurs