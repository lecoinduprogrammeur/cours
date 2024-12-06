# Plan de leçon : Les chaînes de caractères

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Chaînes de caractères : création, manipulation et méthodes
- Durée prévue : 2h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser la manipulation des chaînes de caractères

- Objectifs disciplinaires :
  - Comprendre l'immuabilité des chaînes
  - Maîtriser les méthodes de chaînes
  - Savoir formater les chaînes
  - Utiliser efficacement les fonctions de manipulation

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
tabulation = "Colonne 1\tColonne 2"  # Tabulation
guillemets = "Il a dit \"Bonjour\""  # Échappement des guillemets

# Chaînes brutes (raw strings)
chemin = r"C:\Users\nom"  # Pas d'interprétation des \
```

#### B. Concaténation et répétition
```python
# Concaténation avec +
prenom = "John"
nom = "Doe"
nom_complet = prenom + " " + nom

# Répétition avec *
ligne = "-" * 20  # Crée une ligne de 20 tirets

# Concaténation implicite
texte = ("Première partie "
         "deuxième partie "
         "troisième partie")

# Jointure de liste
mots = ["Python", "est", "génial"]
phrase = " ".join(mots)
```

### 2. Méthodes de base (30 min)

#### A. Méthodes de casse
```python
texte = "Python Programming"

# Changement de casse
maj = texte.upper()      # "PYTHON PROGRAMMING"
min = texte.lower()      # "python programming"
titre = texte.title()    # "Python Programming"
capit = texte.capitalize()  # "Python programming"
swap = texte.swapcase()  # "pYTHON pROGRAMMING"

# Vérification de casse
est_maj = texte.isupper()     # False
est_min = texte.islower()     # False
est_titre = texte.istitle()   # True
```

#### B. Méthodes de recherche
```python
texte = "Python est un langage Python"

# Recherche de sous-chaînes
debut = texte.startswith("Python")   # True
fin = texte.endswith("Python")       # True
contient = "est" in texte            # True

# Trouver les positions
premiere = texte.find("Python")      # 0
derniere = texte.rfind("Python")     # 23
compte = texte.count("Python")       # 2

# Index (lève une exception si non trouvé)
try:
    pos = texte.index("Java")        # ValueError
except ValueError:
    print("Non trouvé")
```

### 3. Méthodes de modification (30 min)

#### A. Nettoyage
```python
texte = "   Python   \n"

# Suppression des espaces
strip = texte.strip()          # "Python"
gauche = texte.lstrip()        # "Python   \n"
droite = texte.rstrip()        # "   Python"

# Suppression de caractères spécifiques
texte2 = "...Python..."
clean = texte2.strip('.')      # "Python"

# Remplacement
texte = "Python est Python"
nouveau = texte.replace("Python", "Java")  # "Java est Java"
limite = texte.replace("Python", "Java", 1)  # "Java est Python"
```

#### B. Division et jointure
```python
texte = "Python,Java,C++,JavaScript"

# Division
liste = texte.split(',')       # ["Python", "Java", "C++", "JavaScript"]
limite = texte.split(',', 2)   # ["Python", "Java", "C++,JavaScript"]

# Split sur les espaces
phrase = "Python est génial"
mots = phrase.split()          # ["Python", "est", "génial"]

# Partition
avant, sep, apres = "Python:Java".partition(':')  # ("Python", ":", "Java")

# Jointure
mots = ["Python", "est", "génial"]
phrase = " ".join(mots)        # "Python est génial"
csv = ",".join(mots)          # "Python,est,génial"
```

### 4. Formatage de chaînes (30 min)

#### A. f-strings (Python 3.6+)
```python
nom = "Alice"
age = 25

# Formatage simple
presentation = f"Je m'appelle {nom} et j'ai {age} ans"

# Expressions
prix = 19.99
message = f"Prix avec TVA : {prix * 1.2:.2f}€"

# Alignement
for i in range(5):
    print(f"Nombre {i:3d}")  # Aligne à droite sur 3 caractères

# Formatage avancé
nombre = 123456.789
format_nombre = f"{nombre:,.2f}"  # 123,456.79
format_binaire = f"{42:b}"        # Format binaire
format_hexa = f"{42:x}"           # Format hexadécimal
```

#### B. Méthode format()
```python
# Formatage basique
"{}{}".format("a", "b")       # "ab"

# Positions
"{1} {0}".format("b", "a")    # "a b"

# Arguments nommés
"{prenom} {nom}".format(prenom="John", nom="Doe")

# Alignement et remplissage
"{:>10}".format("test")       # "      test"
"{:*<10}".format("test")      # "test******"
"{:^10}".format("test")       # "   test   "

# Formats numériques
"{:.2f}".format(3.14159)      # "3.14"
"{:+d}".format(42)            # "+42"
"{:,}".format(1234567)        # "1,234,567"
```

### 5. Méthodes de vérification (20 min)

```python
# Vérification de contenu
"abc123".isalnum()    # True (alphanumérique)
"abc".isalpha()       # True (alphabétique)
"123".isdigit()       # True (numérique)
"   ".isspace()       # True (espaces)

# Vérification de casse
"ABC".isupper()       # True (majuscules)
"abc".islower()       # True (minuscules)
"Title Case".istitle()  # True (format titre)

# Vérification d'identifiants
"variable_name".isidentifier()  # True (identifiant Python valide)

# Vérification de type de caractères
for c in "Python3":
    print(f"{c}: {'lettre' if c.isalpha() else 'chiffre' if c.isdigit() else 'autre'}")
```

### 6. Applications pratiques (25 min)

```python
def valider_email(email):
    """Valide un format d'email basique."""
    return (
        "@" in email and
        "." in email.split("@")[1] and
        email.count("@") == 1 and
        not email.startswith("@") and
        not email.endswith("@")
    )

def formatter_texte(texte):
    """Formate un texte selon des règles spécifiques."""
    # Nettoyer les espaces
    texte = texte.strip()
    
    # Capitaliser les phrases
    phrases = texte.split(". ")
    phrases = [p.capitalize() for p in phrases if p]
    
    # Rejoindre avec ponctuation
    return ". ".join(phrases) + ("." if texte else "")

def extraire_informations(texte):
    """Extrait des informations structurées d'un texte."""
    infos = {}
    
    # Exemple: "Nom: Doe, Age: 25, Email: john@example.com"
    for partie in texte.split(", "):
        if ":" in partie:
            cle, valeur = partie.split(": ")
            infos[cle.lower()] = valeur.strip()
    
    return infos

def masquer_donnees_sensibles(texte, masque="*"):
    """Masque les données sensibles dans un texte."""
    import re
    
    # Masquer les numéros de carte
    texte = re.sub(r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}',
                   masque * 16,
                   texte)
    
    # Masquer les emails
    texte = re.sub(r'[\w\.-]+@[\w\.-]+',
                   masque * 8,
                   texte)
    
    return texte
```

### Phase de pratique (15 min)

Exercices :

1. Traitement de texte :
```python
def analyser_texte(texte):
    """
    Analyser un texte et retourner :
    - Nombre de mots
    - Nombre de phrases
    - Mots les plus fréquents
    - Statistiques sur la longueur des mots
    """
    # À compléter
```

2. Validation et formatage :
```python
def valider_et_formater(texte):
    """
    - Vérifier la validité du texte
    - Formater selon des règles spécifiques
    - Corriger les erreurs courantes
    - Retourner le texte formaté
    """
    # À compléter
```

### Synthèse (5 min)
- Création et manipulation de base
- Méthodes importantes
- Formatage et vérification
- Applications pratiques

## Points importants à retenir :

1. Immuabilité :
   - Les chaînes sont immuables
   - Les modifications créent de nouvelles chaînes
   - Attention aux opérations répétées

2. Méthodes essentielles :
   - Méthodes de recherche (find, index)
   - Méthodes de modification (strip, replace)
   - Méthodes de formatage (f-strings, format)

3. Bonnes pratiques :
   - Utiliser les f-strings pour le formatage
   - Vérifier les entrées utilisateur
   - Optimiser les manipulations de chaînes