# Plan de leçon : Dictionnaires (dict)

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Manipulation des dictionnaires
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des dictionnaires

- Objectifs disciplinaires :
  - Comprendre la structure clé-valeur
  - Maîtriser les opérations sur les dictionnaires
  - Savoir manipuler les dictionnaires imbriqués
  - Appliquer les dictionnaires aux cas pratiques

## Déroulement de la leçon

### 1. Création et accès (20 min)

#### A. Création de dictionnaires
```python
# Dictionnaire vide
dict1 = {}
dict2 = dict()

# Dictionnaire avec valeurs initiales
personne = {
    "nom": "Dupont",
    "prenom": "Jean",
    "age": 30
}

# Création à partir de séquences
cles = ["a", "b", "c"]
valeurs = [1, 2, 3]
dict_zip = dict(zip(cles, valeurs))

# Création avec dict()
dict_items = dict(nom="Alice", age=25)

# Dictionnaire par compréhension
carres = {x: x**2 for x in range(5)}
```

#### B. Accès aux valeurs
```python
# Accès par clé
nom = personne["nom"]      # Lève KeyError si absent
age = personne.get("age")  # Retourne None si absent
age = personne.get("age", 0)  # Valeur par défaut si absent

# Vérification d'existence
existe = "nom" in personne  # True
absent = "taille" in personne  # False

# Obtention des clés, valeurs, items
cles = personne.keys()
valeurs = personne.values()
items = personne.items()  # Paires (clé, valeur)
```

### 2. Modification de dictionnaires (25 min)

#### A. Ajout et modification
```python
# Ajout/modification d'éléments
personne = {}
personne["nom"] = "Dupont"
personne["age"] = 30

# Mise à jour multiple
personne.update({
    "prenom": "Jean",
    "ville": "Paris"
})

# Méthode setdefault
email = personne.setdefault("email", "inconnu")
# Ajoute la clé si absente avec la valeur par défaut

# Fusion de dictionnaires
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
fusion = {**dict1, **dict2}  # Python 3.5+
```

#### B. Suppression
```python
# Suppression par clé
del personne["age"]

# Retrait et retour de la valeur
prenom = personne.pop("prenom")  # Lève KeyError si absent
prenom = personne.pop("prenom", None)  # Valeur par défaut

# Retrait du dernier item ajouté
dernier = personne.popitem()  # Tuple (clé, valeur)

# Vider le dictionnaire
personne.clear()
```

### 3. Dictionnaires imbriqués (25 min)

```python
# Structure imbriquée
utilisateurs = {
    "user1": {
        "nom": "Dupont",
        "adresse": {
            "rue": "123 rue Principale",
            "ville": "Paris"
        },
        "hobbies": ["lecture", "sport"]
    },
    "user2": {
        "nom": "Martin",
        "adresse": {
            "rue": "456 avenue Second",
            "ville": "Lyon"
        },
        "hobbies": ["musique", "voyage"]
    }
}

# Accès aux données imbriquées
ville_user1 = utilisateurs["user1"]["adresse"]["ville"]

# Modification de données imbriquées
utilisateurs["user1"]["hobbies"].append("cinéma")

# Navigation sécurisée
def get_value(dict_obj, keys_path, default=None):
    """Accède à une valeur imbriquée de manière sécurisée."""
    current = dict_obj
    for key in keys_path:
        try:
            current = current[key]
        except (KeyError, TypeError):
            return default
    return current
```

### 4. Méthodes avancées (25 min)

#### A. Copies et références
```python
# Copie superficielle
dict1 = {"a": 1, "b": [1, 2, 3]}
copie = dict1.copy()

# Copie profonde
import copy
copie_profonde = copy.deepcopy(dict1)

# Démonstration de la différence
dict1["b"][0] = 99
print(copie["b"][0])         # 99 (copie superficielle)
print(copie_profonde["b"][0])  # 1 (copie profonde)
```

#### B. Manipulations avancées
```python
def fusionner_dict_recursif(dict1, dict2):
    """Fusionne deux dictionnaires de manière récursive."""
    resultat = dict1.copy()
    for key, value in dict2.items():
        if (key in resultat and 
            isinstance(resultat[key], dict) and 
            isinstance(value, dict)):
            resultat[key] = fusionner_dict_recursif(
                resultat[key], value)
        else:
            resultat[key] = value
    return resultat

def aplatir_dict(d, parent_key='', sep='.'):
    """Aplatit un dictionnaire imbriqué."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(aplatir_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
```

### 5. Applications pratiques (25 min)

#### A. Gestion de données
```python
def compter_occurrences(sequence):
    """Compte les occurrences des éléments."""
    occurrences = {}
    for element in sequence:
        occurrences[element] = occurrences.get(element, 0) + 1
    return occurrences

def grouper_par(items, key_func):
    """Groupe des items selon une fonction clé."""
    groupes = {}
    for item in items:
        key = key_func(item)
        if key not in groupes:
            groupes[key] = []
        groupes[key].append(item)
    return groupes

def filtrer_dict(d, condition):
    """Filtre un dictionnaire selon une condition."""
    return {k: v for k, v in d.items() if condition(k, v)}
```

#### B. Cas d'utilisation avancés
```python
class Cache:
    """Implémentation simple d'un cache."""
    def __init__(self):
        self._data = {}
    
    def get(self, key, default=None):
        return self._data.get(key, default)
    
    def set(self, key, value, ttl=None):
        self._data[key] = {
            'value': value,
            'timestamp': time.time(),
            'ttl': ttl
        }
    
    def is_valid(self, key):
        if key not in self._data:
            return False
        item = self._data[key]
        if item['ttl'] is None:
            return True
        return time.time() - item['timestamp'] < item['ttl']
```

### 6. Bonnes pratiques (15 min)

```python
# Accès sécurisé
def get_safe(dict_obj, key, default=None):
    """Accès sécurisé avec valeur par défaut."""
    try:
        return dict_obj[key]
    except KeyError:
        return default

# Validation de structure
def valider_structure(dict_obj, schema):
    """Valide la structure d'un dictionnaire."""
    for key, type_attendu in schema.items():
        if key not in dict_obj:
            return False
        if not isinstance(dict_obj[key], type_attendu):
            return False
    return True

# Immutabilité
from types import MappingProxyType
def creer_dict_immutable(dict_obj):
    """Crée une vue immutable d'un dictionnaire."""
    return MappingProxyType(dict_obj)
```

### Phase de pratique (15 min)

Exercices :

1. Gestionnaire de configuration :
```python
def creer_gestionnaire_config():
    """
    Créer un gestionnaire qui :
    - Charge/sauvegarde des configurations
    - Valide les données
    - Gère les valeurs par défaut
    """
    # À compléter
```

2. Analyseur de données :
```python
def creer_analyseur():
    """
    Créer un analyseur qui :
    - Agrège des données
    - Calcule des statistiques
    - Génère des rapports
    """
    # À compléter
```

## Points importants à retenir :

1. Structure :
   - Paires clé-valeur
   - Clés uniques et hashables
   - Valeurs de tout type

2. Opérations :
   - Ajout, modification, suppression
   - Accès aux données
   - Copies et références

3. Bonnes pratiques :
   - Accès sécurisé
   - Validation des données
   - Gestion des structures imbriquées