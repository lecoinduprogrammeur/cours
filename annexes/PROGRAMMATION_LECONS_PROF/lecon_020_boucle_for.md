# Plan de leçon : La boucle for

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Structure et utilisation de la boucle for
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation de la boucle for

- Objectifs disciplinaires :
  - Comprendre la structure et le fonctionnement
  - Maîtriser l'itération sur différentes séquences
  - Utiliser range() efficacement
  - Implémenter des cas d'utilisation courants

## Déroulement de la leçon

### 1. Structure de base (20 min)

#### A. Syntaxe fondamentale
```python
# Structure de base
for element in sequence:
    # Instructions à répéter pour chaque élément

# Exemple avec une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

# Exemple avec une chaîne
mot = "Python"
for lettre in mot:
    print(lettre)

# Exemple avec range
for i in range(5):
    print(i)  # Affiche 0, 1, 2, 3, 4
```

#### B. La fonction range()
```python
# range avec un argument (fin)
for i in range(3):
    print(i)  # 0, 1, 2

# range avec deux arguments (début, fin)
for i in range(2, 5):
    print(i)  # 2, 3, 4

# range avec trois arguments (début, fin, pas)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# range décrémentant
for i in range(10, 0, -1):
    print(i)  # Compte à rebours de 10 à 1
```

### 2. Itération sur différentes séquences (25 min)

#### A. Listes et tuples
```python
# Itération sur liste
nombres = [1, 2, 3, 4, 5]
somme = 0
for nombre in nombres:
    somme += nombre

# Itération sur tuple
coordonnees = [(1, 2), (3, 4), (5, 6)]
for x, y in coordonnees:
    print(f"Point: ({x}, {y})")

# Énumération
fruits = ["pomme", "banane", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

#### B. Dictionnaires
```python
# Itération sur les clés (par défaut)
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
for nom in scores:
    print(nom)

# Itération sur les valeurs
for score in scores.values():
    print(score)

# Itération sur les paires clé-valeur
for nom, score in scores.items():
    print(f"{nom}: {score}")
```

### 3. Contrôle de boucle (20 min)

#### A. break et continue
```python
# Utilisation de break
for nombre in range(1, 11):
    if nombre == 5:
        break
    print(nombre)

# Utilisation de continue
for nombre in range(1, 6):
    if nombre == 3:
        continue
    print(nombre)
```

#### B. Else avec for
```python
# Recherche d'élément
def chercher_nombre(nombres, cible):
    for n in nombres:
        if n == cible:
            print("Trouvé!")
            break
    else:
        print("Non trouvé")

# Vérification de condition
def verifier_tous_pairs(nombres):
    for n in nombres:
        if n % 2 != 0:
            print("Nombre impair trouvé")
            break
    else:
        print("Tous les nombres sont pairs")
```

### 4. Cas d'utilisation courants (30 min)

#### A. Traitement de données
```python
# Calcul de moyenne
def calculer_moyenne(notes):
    total = 0
    for note in notes:
        total += note
    return total / len(notes)

# Filtrage
def filtrer_nombres_pairs(nombres):
    pairs = []
    for n in nombres:
        if n % 2 == 0:
            pairs.append(n)
    return pairs

# Transformation de données
def convertir_temperatures(celsius_list):
    fahrenheit_list = []
    for temp in celsius_list:
        fahrenheit = (temp * 9/5) + 32
        fahrenheit_list.append(fahrenheit)
    return fahrenheit_list
```

#### B. Parcours de matrices
```python
# Parcours d'une matrice 2D
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Par lignes
for ligne in matrice:
    for element in ligne:
        print(element, end=' ')
    print()

# Par indices
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(f"matrice[{i}][{j}] = {matrice[i][j]}")
```

#### C. Génération de structures
```python
# Création de table de multiplication
def table_multiplication(n):
    table = []
    for i in range(1, 11):
        table.append(f"{n} x {i} = {n * i}")
    return table

# Création de pyramide
def creer_pyramide(hauteur):
    for i in range(1, hauteur + 1):
        print('*' * i)
```

### 5. Compréhensions de liste (20 min)

```python
# Version classique
carres = []
for x in range(10):
    carres.append(x ** 2)

# Avec compréhension de liste
carres = [x ** 2 for x in range(10)]

# Avec condition
pairs = [x for x in range(10) if x % 2 == 0]

# Compréhensions imbriquées
matrice = [[i + j for j in range(3)] for i in range(3)]
```

### 6. Optimisation et bonnes pratiques (15 min)

#### A. Performance
```python
# Éviter la modification pendant l'itération
# Mauvais
liste = [1, 2, 3, 4, 5]
for item in liste:
    if item % 2 == 0:
        liste.remove(item)  # Modifie la liste pendant l'itération

# Bon
liste = [1, 2, 3, 4, 5]
liste = [item for item in liste if item % 2 != 0]

# Utiliser enumerate plutôt que range(len())
# Mauvais
liste = ['a', 'b', 'c']
for i in range(len(liste)):
    print(f"{i}: {liste[i]}")

# Bon
for i, valeur in enumerate(liste):
    print(f"{i}: {valeur}")
```

#### B. Lisibilité
```python
# Nommer clairement les variables d'itération
# Mauvais
for x in donnees:
    pass

# Bon
for utilisateur in utilisateurs:
    pass

# Extraire les boucles complexes dans des fonctions
def traiter_utilisateurs(utilisateurs):
    for utilisateur in utilisateurs:
        if utilisateur.est_actif:
            for role in utilisateur.roles:
                if role.niveau >= 3:
                    # Traitement
                    pass
```

### Phase de pratique (15 min)

Exercices :

1. Traitement de données :
```python
def analyser_texte(texte):
    """
    Analyser un texte et retourner:
    - Nombre de mots
    - Longueur moyenne des mots
    - Mots les plus longs
    """
    # À compléter
```

2. Création de motifs :
```python
def creer_damier(taille):
    """
    Créer un damier de taille donnée
    utilisant des caractères # et _
    """
    # À compléter
```

### Synthèse (5 min)
- Structure et fonctionnement
- Différents types d'itération
- Cas d'utilisation
- Bonnes pratiques

## Points importants à retenir :

1. Syntaxe :
   - Structure de base de la boucle
   - Utilisation de range()
   - break, continue, else

2. Types d'itération :
   - Séquences (listes, tuples)
   - Dictionnaires
   - Chaînes de caractères

3. Optimisation :
   - Compréhensions de liste
   - Éviter les modifications pendant l'itération
   - Utiliser enumerate