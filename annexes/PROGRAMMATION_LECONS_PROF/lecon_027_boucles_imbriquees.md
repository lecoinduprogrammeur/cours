# Plan de leçon : Boucles imbriquées (while, for)

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Boucles imbriquées
- Durée prévue : 2h00

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des boucles imbriquées

- Objectifs disciplinaires :
  - Comprendre le fonctionnement des boucles imbriquées
  - Savoir utiliser while-while, for-for et while-for
  - Gérer la complexité des boucles imbriquées
  - Optimiser les boucles imbriquées

## Déroulement de la leçon

### 1. Boucles while imbriquées (30 min)

#### A. Structure de base
```python
# Structure simple
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# Avec conditions dépendantes
x = 0
while x < 5:
    y = x  # y dépend de x
    while y < 5:
        print(f"({x},{y})")
        y += 1
    x += 1
```

#### B. Applications pratiques
```python
def trouver_premiers(limite):
    """Trouve les nombres premiers jusqu'à limite."""
    nombre = 2
    while nombre <= limite:
        diviseur = 2
        est_premier = True
        while diviseur * diviseur <= nombre:
            if nombre % diviseur == 0:
                est_premier = False
                break
            diviseur += 1
        if est_premier:
            print(f"{nombre} est premier")
        nombre += 1

def jeu_devinette_2d():
    """Jeu de devinette avec coordonnées x,y."""
    import random
    cible_x = random.randint(1, 5)
    cible_y = random.randint(1, 5)
    trouve = False
    
    while not trouve:
        x = int(input("Coordonnée X (1-5): "))
        y_essais = 0
        while y_essais < 3:  # 3 essais pour y par x
            y = int(input("Coordonnée Y (1-5): "))
            if x == cible_x and y == cible_y:
                trouve = True
                break
            y_essais += 1
        if not trouve:
            print("Essayez une autre ligne")
```

### 2. Boucles for imbriquées (30 min)

#### A. Structure de base
```python
# Structure simple
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# Avec différentes séquences
for lettre in 'ABC':
    for chiffre in '123':
        print(f"{lettre}{chiffre}")

# Parcours de matrices
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for ligne in matrice:
    for element in ligne:
        print(element, end=' ')
    print()  # Nouvelle ligne
```

#### B. Applications pratiques
```python
def creer_table_multiplication(n):
    """Crée une table de multiplication."""
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i*j:4}", end='')
        print()

def motifs_pyramide(hauteur):
    """Crée différents motifs de pyramide."""
    # Pyramide croissante
    for i in range(hauteur):
        for j in range(i+1):
            print("*", end='')
        print()
        
    # Pyramide avec espaces
    for i in range(hauteur):
        for espace in range(hauteur-i-1):
            print(" ", end='')
        for etoile in range(2*i+1):
            print("*", end='')
        print()
```

### 3. Boucles while-for imbriquées (25 min)

#### A. Combinaisons
```python
# While externe, for interne
nombre = 1
while nombre <= 3:
    for lettre in 'ABC':
        print(f"{nombre}{lettre}")
    nombre += 1

# For externe, while interne
for i in range(3):
    j = 0
    while j < i:
        print(f"i={i}, j={j}")
        j += 1
```

#### B. Applications pratiques
```python
def recherche_interactive():
    """Recherche interactive dans une liste."""
    elements = [1, 2, 3, 4, 5]
    continuer = True
    
    while continuer:
        cible = int(input("Valeur à chercher: "))
        trouve = False
        for element in elements:
            if element == cible:
                trouve = True
                break
        print("Trouvé" if trouve else "Non trouvé")
        continuer = input("Continuer? (o/n): ") == 'o'

def analyse_texte_interactive():
    """Analyse interactive de texte."""
    while True:
        texte = input("Entrez un texte (vide pour quitter): ")
        if not texte:
            break
        for caractere in texte:
            if caractere.isalpha():
                print(f"Lettre: {caractere}")
            elif caractere.isdigit():
                print(f"Chiffre: {caractere}")
```

### 4. Optimisation et bonnes pratiques (20 min)

#### A. Contrôle de complexité
```python
# Éviter la complexité excessive
def mauvais_exemple():
    for i in range(n):
        for j in range(n):
            for k in range(n):  # Complexité O(n³)
                print(i, j, k)

# Meilleure approche
def bon_exemple():
    resultats = []
    for i in range(n):
        for j in range(n):
            resultats.append((i, j))
    return resultats

# Utilisation de break et continue
def recherche_optimisee(matrice, cible):
    for i, ligne in enumerate(matrice):
        if max(ligne) < cible:  # Skip si pas possible
            continue
        for j, valeur in enumerate(ligne):
            if valeur == cible:
                return (i, j)
            if valeur > cible:
                break  # Passe à la ligne suivante
    return None
```

#### B. Lisibilité et maintenance
```python
def traiter_donnees_2d(donnees):
    """Exemple de boucles imbriquées bien structurées."""
    def traiter_ligne(ligne):
        """Sous-fonction pour améliorer la lisibilité."""
        resultats = []
        for element in ligne:
            if element.strip():
                resultats.append(element)
        return resultats
    
    resultats = []
    for ligne in donnees:
        elements_traites = traiter_ligne(ligne)
        if elements_traites:
            resultats.extend(elements_traites)
    
    return resultats
```

### 5. Cas d'utilisation avancés (20 min)

#### A. Traitement de données complexes
```python
def analyser_donnees_structurees(donnees):
    """Analyse de données avec structure complexe."""
    statistiques = {}
    
    for categorie, items in donnees.items():
        statistiques[categorie] = {'total': 0, 'moyenne': 0}
        somme = 0
        compte = 0
        
        for item in items:
            while isinstance(item, (list, tuple)):
                # Gère les structures imbriquées
                for valeur in item:
                    if isinstance(valeur, (int, float)):
                        somme += valeur
                        compte += 1
                break
        
        if compte > 0:
            statistiques[categorie]['total'] = somme
            statistiques[categorie]['moyenne'] = somme / compte
    
    return statistiques
```

#### B. Algorithmes complexes
```python
def recherche_chemin(labyrinthe):
    """Trouve un chemin dans un labyrinthe."""
    def est_valide(x, y):
        return (0 <= x < len(labyrinthe) and 
                0 <= y < len(labyrinthe[0]) and 
                labyrinthe[x][y] == 0)
    
    debut = (0, 0)
    fin = (len(labyrinthe)-1, len(labyrinthe[0])-1)
    pile = [(debut, [debut])]
    
    while pile:
        (x, y), chemin = pile.pop()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nouveau_x, nouveau_y = x + dx, y + dy
            if (nouveau_x, nouveau_y) == fin:
                return chemin + [(nouveau_x, nouveau_y)]
            if est_valide(nouveau_x, nouveau_y):
                pile.append(((nouveau_x, nouveau_y),
                           chemin + [(nouveau_x, nouveau_y)]))
    return None
```

### Phase de pratique (15 min)

Exercices :

1. Création de motifs :
```python
def creer_motif_complexe(taille):
    """
    Créer un motif complexe utilisant des boucles
    imbriquées (par exemple, un damier ou une spirale)
    """
    # À compléter
```

2. Analyse de données :
```python
def analyser_donnees_groupees(donnees):
    """
    Analyser des données groupées avec structure
    imbriquée et produire des statistiques
    """
    # À compléter
```

### Synthèse (5 min)
- Types de boucles imbriquées
- Cas d'utilisation appropriés
- Bonnes pratiques d'optimisation
- Gestion de la complexité

## Points importants à retenir :

1. Structure :
   - while-while pour conditions dépendantes
   - for-for pour séquences définies
   - while-for pour combinaisons hybrides

2. Optimisation :
   - Éviter la complexité excessive
   - Utiliser break/continue judicieusement
   - Structurer le code clairement

3. Bonnes pratiques :
   - Limiter la profondeur d'imbrication
   - Extraire les sous-fonctions
   - Documenter le code complexe