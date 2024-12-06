# Plan de leçon : Return et différences avec print()

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Comprendre return et ses différences avec print()
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation de return et comprendre sa différence avec print()

- Objectifs disciplinaires :
  - Comprendre le rôle de return dans les fonctions
  - Distinguer l'affichage (print) du retour de valeur (return)
  - Maîtriser les différents cas d'utilisation
  - Savoir quand utiliser l'un ou l'autre

## Déroulement de la leçon

### 1. Introduction à return (20 min)

#### A. Concept de base
```python
# return renvoie une valeur depuis une fonction
def addition(a, b):
    return a + b  # Renvoie le résultat

# La valeur peut être stockée
resultat = addition(3, 4)  # resultat vaut 7
```

#### B. Caractéristiques de return
```python
# 1. return termine immédiatement la fonction
def exemple():
    print("Début")
    return "Résultat"
    print("Jamais exécuté")  # Cette ligne ne s'exécute pas

# 2. return sans valeur retourne None
def sans_retour():
    return

# 3. Pas de return = retourne None implicitement
def implicite():
    pass  # Retourne None automatiquement
```

### 2. Introduction à print() (15 min)

#### A. Fonctionnement de base
```python
# print affiche du texte dans la console
print("Hello World")  # Affiche mais ne renvoie rien

# print peut afficher plusieurs valeurs
nom = "Alice"
age = 25
print("Nom:", nom, "Age:", age)

# Options de formatage
print("Ligne 1", end=" ")  # Modifie le caractère de fin
print("Même ligne")
```

#### B. Utilisation de print
```python
# Debug et logging
print("Débug: variable =", x)

# Affichage formaté
print(f"Le résultat est {resultat}")

# Affichage sur plusieurs lignes
print("""
Ligne 1
Ligne 2
Ligne 3
""")
```

### 3. Différences fondamentales (25 min)

#### A. Return : Retourne une valeur utilisable
```python
def calculer_aire(rayon):
    return 3.14 * rayon * rayon  # Retourne une valeur

# La valeur retournée peut être utilisée
rayon = 5
aire = calculer_aire(rayon)
aire_double = aire * 2  # Possible car aire contient une valeur

# Chaînage de fonctions possible
def doubler(x):
    return x * 2

resultat = doubler(calculer_aire(5))  # Utilise la valeur retournée
```

#### B. Print : Affiche seulement
```python
def afficher_aire(rayon):
    print(3.14 * rayon * rayon)  # Affiche mais ne retourne rien

# La "valeur" ne peut pas être utilisée
rayon = 5
aire = afficher_aire(rayon)  # aire vaut None
# aire_double = aire * 2  # Erreur!

# Pas de chaînage possible
# resultat = doubler(afficher_aire(5))  # Ne fonctionnera pas
```

### 4. Cas d'utilisation appropriés (20 min)

#### A. Quand utiliser return
```python
# 1. Calculs et transformations
def convertir_celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Return car on veut utiliser le résultat

# 2. Validation de données
def est_valide(email):
    return "@" in email and "." in email  # Return un booléen

# 3. Création d'objets
def creer_personne(nom, age):
    return {
        "nom": nom,
        "age": age
    }  # Return une structure de données
```

#### B. Quand utiliser print
```python
# 1. Affichage d'informations
def afficher_menu():
    print("1. Nouveau jeu")
    print("2. Charger partie")
    print("3. Quitter")

# 2. Débogage
def debug_fonction(x):
    print(f"Débug: x = {x}")
    # Traitement...

# 3. Feedback utilisateur
def traiter_donnees(data):
    print("Traitement en cours...")
    # Traitement...
    print("Traitement terminé")
```

### 5. Combinaison des deux (15 min)

#### A. Utilisation complémentaire
```python
def traiter_commande(montant):
    # Affichage pour information
    print(f"Traitement de la commande de {montant}€")
    
    # Calculs internes
    tva = montant * 0.2
    total = montant + tva
    
    # Affichage du résultat
    print(f"TVA calculée: {tva}€")
    
    # Retour de la valeur pour utilisation ultérieure
    return total

# Utilisation
total = traiter_commande(100)
print(f"Total final: {total}€")
```

#### B. Patterns courants
```python
def valider_donnees(donnees):
    # Feedback pour débogage
    print(f"Validation de {donnees}")
    
    if not donnees:
        print("Erreur: données vides")
        return False
    
    if not isinstance(donnees, list):
        print("Erreur: format incorrect")
        return False
    
    print("Validation réussie")
    return True

# Fonction de traitement complète
def traiter_utilisateur(nom, age):
    # Logging
    print(f"Traitement pour {nom}")
    
    # Validation avec retour
    if age < 0:
        print("Âge invalide")
        return None
    
    # Traitement et retour
    resultat = {
        "nom": nom,
        "categorie": "adulte" if age >= 18 else "mineur"
    }
    
    print("Traitement terminé")
    return resultat
```

### Phase de pratique (10 min)

Exercices :

1. Fonction de calcul avec feedback :
```python
def calculer_moyenne(notes):
    """
    Calculer la moyenne des notes avec feedback
    Doit afficher les étapes et retourner le résultat
    """
    # À compléter
```

2. Fonction de validation :
```python
def valider_mot_de_passe(mdp):
    """
    Valider un mot de passe avec messages d'erreur
    Doit afficher les problèmes et retourner un booléen
    """
    # À compléter
```

### Synthèse (5 min)
- return : renvoie une valeur utilisable
- print : affiche uniquement
- Cas d'utilisation appropriés
- Combinaisons utiles

### Évaluation (5 min)
1. Quelle est la différence principale entre return et print ?
2. Quand utiliser l'un plutôt que l'autre ?
3. Comment peuvent-ils être utilisés ensemble ?

## Points importants à retenir :

1. Return :
   - Renvoie une valeur utilisable dans le code
   - Termine l'exécution de la fonction
   - Permet le chaînage de fonctions

2. Print :
   - Affiche des informations à l'écran
   - N'affecte pas le flux du programme
   - Utile pour le débogage et le feedback

3. Bonnes pratiques :
   - Ne pas confondre affichage et retour de valeur
   - Combiner les deux quand approprié
   - Return pour les valeurs, print pour l'information