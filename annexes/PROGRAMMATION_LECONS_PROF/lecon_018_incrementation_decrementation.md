# Plan de leçon : Incrémentation et décrémentation des variables

## Informations générales

- Date : À définir
- Classe : Débutants en programmation
- Matière : Informatique - Programmation Python
- Thème : Incrémentation et décrémentation
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les opérations d'incrémentation et de décrémentation

- Objectifs disciplinaires :
  - Comprendre les différentes syntaxes
  - Maîtriser les opérateurs d'assignation combinés
  - Appliquer ces concepts dans des cas pratiques
  - Comprendre les cas particuliers

## Déroulement de la leçon

### 1. Incrémentation simple (20 min)

#### A. Syntaxe de base
```python
# Incrémentation de 1
compteur = 0
compteur = compteur + 1  # Méthode longue
print(compteur)  # 1

# Opérateur d'assignation +=
compteur += 1    # Méthode courte
print(compteur)  # 2

# Incrémentation avec d'autres valeurs
compteur += 5    # Ajoute 5
score += 10      # Ajoute 10
```

#### B. Cas d'utilisation courants
```python
# Dans une boucle
for i in range(5):
    compteur += 1

# Compteur de score
score = 0
score += 10  # Gagné 10 points
score += 5   # Bonus de 5 points

# Accumulation
total = 0
for valeur in [1, 2, 3, 4, 5]:
    total += valeur
```

### 2. Décrémentation simple (20 min)

#### A. Syntaxe de base
```python
# Décrémentation de 1
compteur = 10
compteur = compteur - 1  # Méthode longue
print(compteur)  # 9

# Opérateur d'assignation -=
compteur -= 1    # Méthode courte
print(compteur)  # 8

# Décrémentation avec d'autres valeurs
compteur -= 5    # Soustrait 5
vies -= 1        # Perd une vie
```

#### B. Cas d'utilisation courants
```python
# Compte à rebours
for i in range(10, 0, -1):
    print(i)
    
# Gestion de ressources
energie = 100
energie -= 10  # Utilisation d'énergie

# Décompte de temps
temps_restant = 60
while temps_restant > 0:
    print(temps_restant)
    temps_restant -= 1
```

### 3. Opérateurs d'assignation composés (20 min)

#### A. Types d'opérateurs
```python
# Multiplication
score *= 2   # Double le score
# Équivalent à: score = score * 2

# Division
points /= 2  # Divise par 2
# Équivalent à: points = points / 2

# Division entière
quantite //= 2  # Division entière par 2
# Équivalent à: quantite = quantite // 2

# Modulo
reste %= 3   # Reste de la division par 3
# Équivalent à: reste = reste % 3

# Puissance
nombre **= 2  # Élève au carré
# Équivalent à: nombre = nombre ** 2
```

#### B. Applications pratiques
```python
def calculer_points(base, bonus, malus):
    points = 100  # Points de départ
    
    # Bonus multiplicateur
    points *= bonus    # Applique le bonus
    
    # Malus par division
    points /= malus    # Applique le malus
    
    # Arrondissement
    points //= 1       # Garde la partie entière
    
    return points

def ajuster_volume(volume, delta):
    # Ajustement avec limites
    volume += delta
    if volume > 100:
        volume = 100
    elif volume < 0:
        volume = 0
    return volume
```

### 4. Cas particuliers et pièges (15 min)

#### A. Chaînes de caractères
```python
# Concaténation avec +=
message = "Hello"
message += " World"    # Concaténation
print(message)        # "Hello World"

# Multiplication avec *=
etoiles = "*"
etoiles *= 5          # Répète 5 fois
print(etoiles)        # "*****"
```

#### B. Listes
```python
# Ajout d'éléments
liste = [1, 2]
liste += [3, 4]       # Étend la liste
print(liste)         # [1, 2, 3, 4]

# Multiplication de listes
sequence = [0]
sequence *= 3         # Répète la liste
print(sequence)      # [0, 0, 0]
```

### 5. Applications avancées (20 min)

#### A. Compteurs multiples
```python
def suivre_statistiques():
    victoires = defaites = nuls = 0
    
    # Simulons quelques matchs
    victoires += 1    # Match gagné
    defaites += 1     # Match perdu
    nuls += 1         # Match nul
    
    total_matchs = victoires + defaites + nuls
    ratio = victoires / total_matchs if total_matchs > 0 else 0
    
    return {
        'victoires': victoires,
        'defaites': defaites,
        'nuls': nuls,
        'ratio': ratio
    }
```

#### B. Gestion de ressources
```python
class JeuPersonnage:
    def __init__(self):
        self.vie = 100
        self.energie = 100
        self.experience = 0
    
    def recevoir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0
    
    def utiliser_capacite(self, cout):
        if self.energie >= cout:
            self.energie -= cout
            return True
        return False
    
    def gagner_experience(self, montant):
        self.experience += montant
        if self.experience >= 100:
            self.monter_niveau()
    
    def monter_niveau(self):
        self.experience -= 100
        self.vie += 20
        self.energie += 10
```

### Phase de pratique (10 min)

Exercices :

1. Compteur de score :
```python
def gerer_score():
    """
    Créer un système de score avec :
    - Points de base
    - Bonus multiplicateurs
    - Pénalités
    """
    # À compléter
```

2. Gestion de ressources :
```python
class Inventaire:
    """
    Créer un système d'inventaire avec :
    - Ajout d'items
    - Retrait d'items
    - Vérification des quantités
    """
    # À compléter
```

### Synthèse (5 min)
- Différentes méthodes d'incrémentation/décrémentation
- Opérateurs d'assignation composés
- Cas particuliers
- Applications pratiques

## Points importants à retenir :

1. Syntaxe de base :
   - += pour l'incrémentation
   - -= pour la décrémentation
   - Autres opérateurs composés (*=, /=, //=, %=, **=)

2. Cas particuliers :
   - Chaînes de caractères
   - Listes et autres séquences
   - Limites et contraintes

3. Bonnes pratiques :
   - Choisir la syntaxe appropriée
   - Gérer les limites
   - Vérifier les types