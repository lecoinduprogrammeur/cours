# Plan de leçon : Concaténation de chaînes de caractères en Python

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Concaténation de chaînes de caractères
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les différentes méthodes de concaténation en Python

- Objectifs disciplinaires :
  - Comprendre les différentes techniques de concaténation
  - Maîtriser le formatage de chaînes
  - Optimiser les opérations de concaténation
  - Gérer les conversions de types dans la concaténation

- Objectifs transversaux :
  - Développer des bonnes pratiques de manipulation de texte
  - Améliorer la performance du code
  - Apprendre à choisir la méthode appropriée

## Prérequis
- Connaissances de base en Python
- Compréhension des chaînes de caractères
- Notions sur les types de données

## Matériel et ressources
- Ordinateurs avec Python installé
- Documentation Python
- Exemples de code
- Exercices pratiques

## Déroulement de la leçon

### 1. Méthodes de base (20 min)

#### A. Opérateur + 
```python
# Concaténation simple
prenom = "Jean"
nom = "Dupont"
nom_complet = prenom + " " + nom  # "Jean Dupont"

# Avec des nombres (conversion nécessaire)
age = 25
message = "J'ai " + str(age) + " ans"  # "J'ai 25 ans"

# Répétition avec *
ligne = "-" * 20  # "--------------------"
```

#### B. Méthode join()
```python
# Join avec une liste
mots = ["Python", "est", "génial"]
phrase = " ".join(mots)  # "Python est génial"

# Join avec différents séparateurs
chemin = "/".join(["dossier", "sous-dossier", "fichier.txt"])
csv = ",".join(["nom", "age", "ville"])

# Join avec conversion automatique (tous les éléments doivent être des str)
nombres = [str(n) for n in range(5)]
resultat = "-".join(nombres)  # "0-1-2-3-4"
```

### 2. Méthodes de formatage modernes (25 min)

#### A. F-strings (Python 3.6+)
```python
# Format de base
nom = "Alice"
age = 30
message = f"Je m'appelle {nom} et j'ai {age} ans"

# Expressions dans les f-strings
x = 10
y = 20
calcul = f"La somme de {x} et {y} est {x + y}"

# Formatage des nombres
prix = 19.99
affichage = f"Prix : {prix:.2f}€"  # "Prix : 19.99€"

# Alignement et remplissage
nombre = 42
formatage = f"{nombre:0>5}"  # "00042"
```

#### B. Méthode format()
```python
# Format de base
message = "Hello {}!".format("World")

# Multiples arguments
template = "J'ai {} pommes et {} oranges"
fruits = template.format(3, 5)

# Arguments nommés
info = "Je m'appelle {nom} et j'ai {age} ans"
personne = info.format(nom="Bob", age=25)

# Index réutilisables
repeat = "{0} {1} {0}".format("hello", "world")  # "hello world hello"
```

### 3. Techniques avancées (20 min)

#### A. Formatage avec %
```python
# Style ancien mais encore utilisé
nom = "Charlie"
age = 22
message = "Je m'appelle %s et j'ai %d ans" % (nom, age)

# Types de formatage courants
pi = 3.14159
format_number = "Pi vaut %.2f" % pi  # "Pi vaut 3.14"
```

#### B. Optimisation
```python
# Mauvaise pratique (création de nombreuses chaînes temporaires)
resultat = ""
for i in range(1000):
    resultat = resultat + str(i)

# Bonne pratique (utilisation de join)
resultat = "".join(str(i) for i in range(1000))

# Utilisation de liste pour les modifications fréquentes
parties = []
for i in range(1000):
    parties.append(str(i))
resultat = "".join(parties)
```

### 4. Cas particuliers (15 min)

#### A. Gestion des types
```python
# Conversion automatique vs explicite
nombre = 42
# texte = "Nombre: " + nombre  # TypeError!
texte = "Nombre: " + str(nombre)  # OK
texte = f"Nombre: {nombre}"  # OK aussi

# Mélange de types
liste = [1, "deux", 3.0]
# ",".join(liste)  # TypeError!
",".join(str(x) for x in liste)  # OK
```

#### B. Caractères spéciaux
```python
# Caractères d'échappement
chemin = "C:\\Users\\Documents"
print_raw = r"C:\Users\Documents"  # Chaîne brute

# Unicode
emoji = "👍"
message = f"Super! {emoji}"
```

### Phase de pratique (15 min)

Exercices progressifs :

1. Formatage simple :
```python
# Créer une fonction qui formate une adresse
def formater_adresse(rue, ville, code_postal):
    # À compléter
```

2. Optimisation :
```python
# Optimiser cette fonction de concaténation
def construire_phrase(mots):
    # À compléter
```

3. Cas complexe :
```python
# Créer un formateur de tableau
def formater_tableau(donnees):
    # À compléter
```

### Synthèse (5 min)
- Comparaison des méthodes
- Cas d'utilisation recommandés
- Points de performance

### Évaluation (5 min)
1. Quelle méthode de concaténation privilégier ?
2. Comment gérer les types non-string ?
3. Comment optimiser les concaténations multiples ?

## Devoirs et prolongements

Devoirs :
1. Créer un mini-générateur de rapports
2. Optimiser un code de concaténation existant
3. Implémenter différentes méthodes de formatage

Prolongements :
- Templates string
- Internationalisation
- Formatage de nombres et dates

## Points importants à retenir :

1. Méthodes principales :
   - Opérateur + : simple mais limité
   - join() : efficace pour les listes
   - f-strings : moderne et lisible
   - format() : flexible et puissant

2. Considérations de performance :
   - Éviter la concaténation dans les boucles
   - Préférer join() pour les grandes chaînes
   - Utiliser des listes pour les modifications fréquentes

3. Bonnes pratiques :
   - Conversion explicite des types non-string
   - Choix de la méthode selon le contexte
   - Documentation claire du formatage complexe

4. Tableaux comparatifs des méthodes :
```python
# Performance (du plus au moins efficace)
"".join(liste)  # Meilleur pour les listes
f"..."          # Excellent pour le formatage simple
"...".format()  # Bon pour le formatage complexe
"..." + "..."   # À éviter dans les boucles
```