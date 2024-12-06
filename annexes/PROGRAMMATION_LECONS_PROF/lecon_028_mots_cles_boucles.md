# Plan de leçon : Mots-clés break, continue et autres dans les boucles

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Mots-clés et contrôle de flux dans les boucles
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation des mots-clés dans les boucles

- Objectifs disciplinaires :
  - Comprendre break, continue et else
  - Savoir utiliser pass et return
  - Maîtriser le contrôle de flux
  - Optimiser les boucles avec les mots-clés

## Déroulement de la leçon

### 1. Le mot-clé break (20 min)

#### A. Syntaxe et utilisation basique
```python
# Sortie simple d'une boucle
for i in range(10):
    if i == 5:
        break  # Sort de la boucle quand i atteint 5
    print(i)

# Dans une boucle while
compteur = 0
while True:
    if compteur >= 5:
        break  # Sort de la boucle infinie
    print(compteur)
    compteur += 1
```

#### B. Applications pratiques
```python
def chercher_element(liste, cible):
    """Cherche un élément et sort dès qu'il est trouvé."""
    for i, element in enumerate(liste):
        if element == cible:
            print(f"Trouvé à l'index {i}")
            break
    else:
        print("Non trouvé")

def verifier_mot_de_passe():
    """Vérifie un mot de passe avec nombre limité de tentatives."""
    tentatives = 3
    while tentatives > 0:
        mdp = input("Mot de passe: ")
        if mdp == "secret":
            print("Accès autorisé")
            break
        tentatives -= 1
        print(f"Il reste {tentatives} tentatives")
    else:
        print("Accès refusé")
```

### 2. Le mot-clé continue (20 min)

#### A. Syntaxe et utilisation basique
```python
# Sauter des itérations
for i in range(10):
    if i % 2 == 0:
        continue  # Saute les nombres pairs
    print(i)

# Dans une boucle while
compteur = 0
while compteur < 5:
    compteur += 1
    if compteur == 3:
        continue  # Saute l'itération quand compteur est 3
    print(compteur)
```

#### B. Applications pratiques
```python
def filtrer_donnees(liste):
    """Traite uniquement les données valides."""
    for element in liste:
        if not element:  # Ignore les éléments vides
            continue
        if not isinstance(element, (int, float)):
            continue
        print(f"Traitement de {element}")

def analyser_texte(texte):
    """Analyse uniquement les caractères alphabétiques."""
    frequences = {}
    for caractere in texte:
        if not caractere.isalpha():
            continue
        caractere = caractere.lower()
        frequences[caractere] = frequences.get(caractere, 0) + 1
    return frequences
```

### 3. Le mot-clé else dans les boucles (20 min)

#### A. Utilisation avec for
```python
# Vérification de condition
def verifier_nombres_pairs(liste):
    for nombre in liste:
        if nombre % 2 != 0:
            print(f"{nombre} n'est pas pair")
            break
    else:
        print("Tous les nombres sont pairs")

# Recherche avec résultat
def chercher_valeur(dictionnaire, valeur):
    for cle, val in dictionnaire.items():
        if val == valeur:
            print(f"Trouvé: {cle}")
            break
    else:
        print("Valeur non trouvée")
```

#### B. Utilisation avec while
```python
def attendre_entree_valide():
    """Attend une entrée valide avec limite de tentatives."""
    tentatives = 3
    while tentatives > 0:
        valeur = input("Entrez un nombre: ")
        if valeur.isdigit():
            print("Valeur valide !")
            break
        tentatives -= 1
    else:
        print("Nombre maximum de tentatives atteint")

def processus_avec_timeout():
    """Exécute un processus avec timeout."""
    temps = 0
    while temps < 10:  # timeout de 10 secondes
        if condition_reussie():
            print("Processus terminé")
            break
        temps += 1
    else:
        print("Timeout atteint")
```

### 4. Le mot-clé pass (15 min)

#### A. Utilisation comme placeholder
```python
# Dans une boucle vide
for i in range(5):
    pass  # Ne fait rien, mais syntaxiquement valide

# Dans une condition
def traiter_donnees(donnees):
    for item in donnees:
        if item.is_valid():
            traiter(item)
        else:
            pass  # Ignore les items invalides
```

#### B. Applications pratiques
```python
def creer_structure_base():
    """Crée une structure de base pour le développement."""
    class BaseDeDonnees:
        def connecter(self):
            pass  # À implémenter plus tard
        
        def deconnecter(self):
            pass  # À implémenter plus tard
    
    def initialiser():
        pass  # Placeholder pour l'initialisation
    
    return BaseDeDonnees()
```

### 5. Combinaisons et cas avancés (20 min)

#### A. Utilisation combinée
```python
def analyser_donnees_complexes(donnees):
    """Analyse des données avec plusieurs contrôles."""
    for section in donnees:
        # Vérification de section
        if not section.est_valide():
            continue
            
        for element in section.elements:
            # Ignore les éléments vides
            if not element:
                continue
                
            try:
                resultat = traiter_element(element)
                if resultat.est_critique():
                    print("Erreur critique trouvée")
                    break
            except Exception:
                pass  # Ignore les erreurs non critiques
        else:
            print(f"Section {section.id} traitée avec succès")
```

#### B. Patterns courants
```python
def recherche_avancee(donnees, criteres):
    """Pattern de recherche avec contrôles multiples."""
    for item in donnees:
        # Vérifications préliminaires
        if not item.est_accessible:
            continue
            
        # Vérification des critères
        for critere in criteres:
            if not critere.verifier(item):
                break
        else:
            # Tous les critères sont satisfaits
            if traitement_final(item):
                return item  # Sort de la fonction
            continue
    else:
        raise ValueError("Aucun item trouvé")
```

### Phase de pratique (15 min)

Exercices :

1. Validation de données :
```python
def valider_entrees(donnees):
    """
    Valider une série de données avec :
    - Skip des données invalides (continue)
    - Arrêt sur erreur critique (break)
    - Confirmation de succès (else)
    """
    # À compléter
```

2. Recherche complexe :
```python
def chercher_element_complexe(structure, cible):
    """
    Implémenter une recherche avec :
    - Plusieurs niveaux de boucles
    - Différentes conditions de sortie
    - Gestion des cas spéciaux
    """
    # À compléter
```

### Synthèse (5 min)
- Utilisation appropriée de break et continue
- Cas d'utilisation de else
- Rôle de pass
- Combinaisons efficaces

## Points importants à retenir :

1. Break :
   - Sort complètement de la boucle
   - Utile pour les recherches
   - Évite les drapeaux booléens

2. Continue :
   - Passe à l'itération suivante
   - Utile pour le filtrage
   - Améliore la lisibilité

3. Else :
   - S'exécute si pas de break
   - Confirme l'exécution complète
   - Alternative aux drapeaux

4. Pass :
   - Placeholder syntaxique
   - Utile pour le développement
   - Explicite l'intention de ne rien faire