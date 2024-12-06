# Plan de leçon : Variables string

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Manipulation des chaînes de caractères
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des chaînes de caractères

- Objectifs disciplinaires :
  - Comprendre la création et manipulation des chaînes
  - Maîtriser les méthodes de chaînes
  - Savoir formater les chaînes
  - Gérer les cas spéciaux

## Déroulement de la leçon

### 1. Création de chaînes (20 min)

#### A. Syntaxes de base
```python
# Guillemets simples ou doubles
simple = 'Python'
double = "Python"

# Chaînes multiligne
multiligne = """
Première ligne
Deuxième ligne
Troisième ligne
"""

# Caractères d'échappement
special = "Ligne 1\nLigne 2"  # Saut de ligne
tabulation = "Texte\ttabulé"  # Tabulation
guillemets = 'Il a dit "Bonjour"'  # Guillemets dans la chaîne

# Chaînes brutes (raw strings)
chemin = r"C:\Users\nom\dossier"  # Les \ ne sont pas interprétés

# Concaténation
message = "Hello" + " " + "World"
repetition = "Ha" * 3  # "HaHaHa"
```

#### B. Accès aux caractères
```python
texte = "Python"
premier = texte[0]     # 'P'
dernier = texte[-1]    # 'n'

# Slicing
partie = texte[1:4]    # 'yth'
debut = texte[:2]      # 'Py'
fin = texte[2:]        # 'thon'
inverse = texte[::-1]  # 'nohtyP'

# Longueur
longueur = len(texte)  # 6
```

### 2. Méthodes de chaînes (25 min)

#### A. Modification de casse
```python
texte = "Python Programming"

# Changement de casse
maj = texte.upper()         # "PYTHON PROGRAMMING"
min = texte.lower()         # "python programming"
titre = texte.title()       # "Python Programming"
capit = texte.capitalize()  # "Python programming"

# Vérification de casse
est_maj = texte.isupper()   # False
est_min = texte.islower()   # False
est_titre = texte.istitle() # True
```

#### B. Recherche et remplacement
```python
texte = "Python est un langage Python"

# Recherche
position = texte.find("Python")      # 0
derniere = texte.rfind("Python")     # 22
compte = texte.count("Python")       # 2

# Remplacement
nouveau = texte.replace("Python", "Java")
nouveau_limite = texte.replace("Python", "Java", 1)  # Premier uniquement

# Vérification
debut = texte.startswith("Python")   # True
fin = texte.endswith("Python")       # True
contient = "est" in texte            # True
```

### 3. Méthodes de nettoyage (20 min)

```python
# Suppression d'espaces
texte = "   Python   "
net = texte.strip()         # "Python"
gauche = texte.lstrip()     # "Python   "
droite = texte.rstrip()     # "   Python"

# Suppression de caractères spécifiques
texte2 = "...Python..."
net2 = texte2.strip('.')    # "Python"

# Division en liste
phrase = "Python est génial"
mots = phrase.split()       # ["Python", "est", "génial"]
csv = "a,b,c"
elements = csv.split(',')   # ["a", "b", "c"]

# Jointure
mots = ["Python", "est", "génial"]
phrase = " ".join(mots)     # "Python est génial"
```

### 4. Formatage de chaînes (25 min)

#### A. f-strings (Python 3.6+)
```python
# Formatage simple
nom = "Alice"
age = 25
message = f"{nom} a {age} ans"

# Expressions
prix = 19.99
total = f"Total: {prix * 1.2:.2f}€"

# Formatage avancé
nombre = 42
binaire = f"{nombre:b}"      # Format binaire
hexa = f"{nombre:x}"         # Format hexadécimal
aligne = f"{nom:>10}"        # Alignement à droite
zeros = f"{nombre:05d}"      # Padding avec zéros
```

#### B. Méthode format()
```python
# Formatage basique
"Hello {}!".format("World")

# Positions
"{1} {0}".format("World", "Hello")

# Nommé
"Je m'appelle {nom} et j'ai {age} ans".format(
    nom="Bob",
    age=30
)

# Alignement et remplissage
"{:>10}".format("test")      # Aligné à droite
"{:*<10}".format("test")     # Padding à gauche avec *
"{:^10}".format("test")      # Centré
```

### 5. Opérations avancées (25 min)

#### A. Manipulation avancée
```python
def inverser_mots(phrase):
    """Inverse l'ordre des mots."""
    mots = phrase.split()
    return " ".join(reversed(mots))

def camel_case(texte):
    """Convertit en camelCase."""
    mots = texte.split()
    return mots[0].lower() + "".join(m.capitalize() for m in mots[1:])

def snake_case(texte):
    """Convertit en snake_case."""
    return "_".join(mot.lower() for mot in texte.split())

def compter_mots(texte):
    """Compte les occurrences des mots."""
    mots = texte.lower().split()
    return {mot: mots.count(mot) for mot in set(mots)}
```

#### B. Validation et nettoyage
```python
def nettoyer_texte(texte):
    """Nettoie un texte."""
    # Supprime ponctuation et espaces multiples
    import string
    texte = texte.translate(str.maketrans("", "", string.punctuation))
    return " ".join(texte.split())

def est_email_valide(email):
    """Vérifie si un email est valide (basique)."""
    return (
        "@" in email
        and "." in email.split("@")[1]
        and email.count("@") == 1
    )

def masquer_donnees(texte):
    """Masque les données sensibles."""
    mots = texte.split()
    return " ".join(
        "*" * len(mot) if len(mot) > 3 else mot
        for mot in mots
    )
```

### 6. Cas pratiques (15 min)

```python
def formatter_nom(prenom, nom):
    """Formate un nom complet."""
    return f"{prenom.capitalize()} {nom.upper()}"

def generer_slug(titre):
    """Génère un slug pour URL."""
    return "-".join(
        mot.lower()
        for mot in titre.split()
        if mot.isalnum()
    )

def formater_telephone(numero):
    """Formate un numéro de téléphone."""
    numero = "".join(c for c in numero if c.isdigit())
    return ".".join(numero[i:i+2] for i in range(0, len(numero), 2))
```

### Phase de pratique (15 min)

Exercices :

1. Traitement de texte :
```python
def traiter_texte():
    """
    Créer un système qui :
    - Nettoie le texte
    - Formate selon des règles
    - Valide le résultat
    """
    # À compléter
```

2. Formatage avancé :
```python
def formater_donnees():
    """
    Créer un formateur qui :
    - Gère différents formats
    - Valide les entrées
    - Produit une sortie propre
    """
    # À compléter
```

## Points importants à retenir :

1. Création :
   - Différentes syntaxes
   - Caractères spéciaux
   - Accès aux caractères

2. Méthodes :
   - Modification de casse
   - Recherche et remplacement
   - Nettoyage

3. Formatage :
   - f-strings
   - méthode format()
   - Alignement et padding