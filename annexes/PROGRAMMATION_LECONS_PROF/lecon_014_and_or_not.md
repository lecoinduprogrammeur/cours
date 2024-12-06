# Plan de leçon : Les opérateurs logiques and, or, not

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Opérateurs logiques and, or, not
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser les opérateurs logiques en Python

- Objectifs disciplinaires :
  - Comprendre le fonctionnement de and, or, not
  - Maîtriser les tables de vérité
  - Savoir combiner les opérateurs
  - Utiliser les opérateurs dans des conditions réelles

## Déroulement de la leçon

### 1. Tables de vérité (15 min)

#### A. Opérateur AND
```python
# Table de vérité AND
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Règle : AND retourne True seulement si les deux opérandes sont True
```

#### B. Opérateur OR
```python
# Table de vérité OR
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Règle : OR retourne True si au moins un opérande est True
```

#### C. Opérateur NOT
```python
# Table de vérité NOT
print(not True)         # False
print(not False)        # True

# Règle : NOT inverse la valeur booléenne
```

### 2. Évaluation court-circuit (20 min)

#### A. Court-circuit avec AND
```python
# AND s'arrête dès qu'il trouve False
def fonction1():
    print("fonction1 appelée")
    return False

def fonction2():
    print("fonction2 appelée")
    return True

# fonction2 n'est pas appelée car fonction1 retourne False
resultat = fonction1() and fonction2()

# Utilisation pratique
utilisateur = None
# Évite l'erreur si utilisateur est None
if utilisateur and utilisateur.est_actif:
    print("Utilisateur actif")
```

#### B. Court-circuit avec OR
```python
# OR s'arrête dès qu'il trouve True
def verif1():
    print("verif1 appelée")
    return True

def verif2():
    print("verif2 appelée")
    return False

# verif2 n'est pas appelée car verif1 retourne True
resultat = verif1() or verif2()

# Utilisation pratique
valeur_defaut = 5
resultat = valeur_utilisateur or valeur_defaut
```

### 3. Priorité des opérateurs (20 min)

#### A. Ordre de priorité
```python
# Priorité : NOT > AND > OR
a = True
b = False
c = True

# Ces expressions sont différentes
resultat1 = a or b and c      # Équivalent à: a or (b and c)
resultat2 = (a or b) and c    # Parenthèses modifient la priorité

# Avec NOT
resultat3 = not a or b        # Équivalent à: (not a) or b
resultat4 = not (a or b)      # Different de resultat3
```

#### B. Utilisation des parenthèses
```python
age = 25
permis = True
assurance = True

# Sans parenthèses (peut être ambigu)
peut_conduire = age >= 18 and permis or assurance

# Avec parenthèses (plus clair)
peut_conduire = (age >= 18 and permis) or assurance

# Expressions complexes
condition = (not permis and age >= 21) or (permis and age >= 18)
```

### 4. Applications pratiques (25 min)

#### A. Validation de données
```python
def valider_utilisateur(age, email, mot_de_passe):
    """Valide les données d'un utilisateur."""
    age_valide = 13 <= age <= 120
    email_valide = "@" in email and "." in email
    mdp_valide = len(mot_de_passe) >= 8 and any(c.isdigit() for c in mot_de_passe)
    
    return age_valide and email_valide and mdp_valide

# Utilisation
est_valide = valider_utilisateur(25, "user@example.com", "password123")
```

#### B. Filtrage et recherche
```python
def filtrer_produit(produit):
    """Filtre un produit selon plusieurs critères."""
    prix_ok = 10 <= produit.prix <= 100
    stock_ok = produit.quantite > 0
    categorie_ok = produit.categorie in ["A", "B"]
    
    return prix_ok and stock_ok and categorie_ok

def rechercher_texte(texte, mots_cles):
    """Recherche si le texte contient certains mots-clés."""
    return any(mot in texte.lower() for mot in mots_cles)
```

#### C. Gestion des autorisations
```python
def peut_acceder(utilisateur):
    """Vérifie les droits d'accès."""
    est_admin = utilisateur.role == "admin"
    est_moderateur = utilisateur.role == "moderateur"
    est_premium = utilisateur.abonnement == "premium"
    
    return est_admin or (est_moderateur and est_premium)

# Cas pratiques
def peut_modifier_document(utilisateur, document):
    est_proprietaire = document.auteur == utilisateur.id
    a_droits = utilisateur.role in ["admin", "editeur"]
    
    return est_proprietaire or a_droits
```

### 5. Optimisation et bonnes pratiques (15 min)

#### A. Simplification des expressions
```python
# À éviter
if bool(age >= 18) == True:
    print("Majeur")

# Préférer
if age >= 18:
    print("Majeur")

# À éviter
if not(not condition):
    print("Double négation")

# Préférer
if condition:
    print("Plus simple")
```

#### B. Organisation des conditions
```python
# Conditions complexes
def verifier_eligibilite(candidat):
    conditions_base = (
        candidat.age >= 18 and
        candidat.diplome and
        candidat.experience >= 2
    )
    
    conditions_speciales = (
        candidat.certifications or
        candidat.recommandations >= 3
    )
    
    return conditions_base and conditions_speciales
```

### Phase de pratique (10 min)

Exercices :

1. Évaluation d'expressions :
```python
# Prédire les résultats
resultat1 = not True or False and True
resultat2 = (True or False) and not False
resultat3 = not (True and True or False)
```

2. Application pratique :
```python
def valider_mot_de_passe(mdp):
    """
    Valide un mot de passe selon plusieurs critères :
    - Au moins 8 caractères
    - Au moins un chiffre
    - Au moins une majuscule
    - Au moins un caractère spécial
    """
    # À compléter
```

### Synthèse (5 min)
- Tables de vérité
- Évaluation court-circuit
- Priorité des opérateurs
- Bonnes pratiques

### Évaluation (5 min)
1. Expliquer l'évaluation court-circuit
2. Donner l'ordre de priorité des opérateurs
3. Comment simplifier une expression complexe ?

## Points importants à retenir :

1. Fondamentaux :
   - Tables de vérité
   - Évaluation court-circuit
   - Priorité des opérateurs

2. Bonnes pratiques :
   - Utiliser des parenthèses pour la clarté
   - Simplifier les expressions
   - Organiser les conditions complexes

3. Applications :
   - Validation de données
   - Filtrage
   - Gestion des autorisations