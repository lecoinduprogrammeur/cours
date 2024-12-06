# Plan de leçon : Le module string

## Informations générales

- Date : À définir
- Classe : Débutants/Intermédiaires en programmation
- Matière : Informatique - Programmation Python
- Thème : Utilisation du module string
- Durée prévue : 1h30

## Objectifs de la leçon

- Objectif général :
  - Maîtriser l'utilisation du module string

- Objectifs disciplinaires :
  - Comprendre les constantes du module string
  - Utiliser les templates de chaînes
  - Maîtriser les fonctionnalités du module
  - Appliquer les bonnes pratiques

## Déroulement de la leçon

### 1. Introduction au module string (20 min)

#### A. Importation et constantes
```python
import string

# Constantes de caractères
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)    # Combinaison de lowercase et uppercase
print(string.digits)          # 0123456789
print(string.hexdigits)       # 0123456789abcdefABCDEF
print(string.octdigits)       # 01234567
print(string.punctuation)     # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)      # Espace, tab, newline, etc.
print(string.printable)       # Combinaison des caractères imprimables
```

#### B. Applications pratiques des constantes
```python
def generer_mot_de_passe(longueur=8):
    """Génère un mot de passe aléatoire."""
    import random
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longueur))

def valider_identifiant(identifiant):
    """Vérifie si un identifiant est valide."""
    caracteres_valides = string.ascii_letters + string.digits + '_'
    return all(c in caracteres_valides for c in identifiant)

def nettoyer_texte(texte):
    """Retire la ponctuation d'un texte."""
    return ''.join(c for c in texte if c not in string.punctuation)
```

### 2. Templates de chaînes (25 min)

#### A. Utilisation basique
```python
from string import Template

# Création d'un template simple
template = Template('Hello, $name!')
resultat = template.substitute(name='Alice')
print(resultat)  # Hello, Alice!

# Template avec plusieurs variables
template = Template('$prenom $nom a $age ans')
resultat = template.substitute(
    prenom='John',
    nom='Doe',
    age=25
)
print(resultat)  # John Doe a 25 ans
```

#### B. Utilisation avancée
```python
# Substitution avec dictionnaire
template = Template('Projet: $projet, Status: $status')
donnees = {
    'projet': 'Python',
    'status': 'En cours'
}
resultat = template.substitute(donnees)

# Substitution sécurisée (safe_substitute)
template = Template('$nom ($email)')
# Ne lève pas d'erreur si une variable manque
resultat = template.safe_substitute(nom='Alice')
print(resultat)  # Alice ($email)

# Template personnalisé
class CustomTemplate(Template):
    delimiter = '%'  # Change le délimiteur de $ à %
    
template = CustomTemplate('Bonjour %nom!')
print(template.substitute(nom='Alice'))
```

### 3. Applications pratiques (25 min)

#### A. Génération de texte
```python
def generer_lettre(template_texte, **kwargs):
    """Génère une lettre à partir d'un template."""
    template = Template(template_texte)
    try:
        return template.substitute(kwargs)
    except KeyError as e:
        return f"Erreur: Variable manquante - {e}"

# Exemple d'utilisation
template_lettre = """
Cher/Chère $nom,

Nous confirmons votre rendez-vous le $date à $heure.
Cordialement,
$entreprise
"""

lettre = generer_lettre(
    template_lettre,
    nom="Dupont",
    date="2024-03-15",
    heure="14:30",
    entreprise="Python Corp"
)
```

#### B. Validation de données
```python
def valider_identifiant_complet(identifiant):
    """Validation complète d'un identifiant."""
    # Doit commencer par une lettre
    if not identifiant[0] in string.ascii_letters:
        return False
    
    # Ne doit contenir que des lettres, chiffres et underscore
    caracteres_valides = string.ascii_letters + string.digits + '_'
    return all(c in caracteres_valides for c in identifiant)

def analyser_composition_texte(texte):
    """Analyse la composition d'un texte."""
    stats = {
        'lettres': 0,
        'chiffres': 0,
        'ponctuation': 0,
        'espaces': 0
    }
    
    for c in texte:
        if c in string.ascii_letters:
            stats['lettres'] += 1
        elif c in string.digits:
            stats['chiffres'] += 1
        elif c in string.punctuation:
            stats['ponctuation'] += 1
        elif c in string.whitespace:
            stats['espaces'] += 1
            
    return stats
```

### 4. Cas d'utilisation avancés (15 min)

```python
def formater_code(code, style='$prefix$numero'):
    """Formate des codes selon un template."""
    template = Template(style)
    def generateur(prefix, debut=1, nombre=10):
        return [
            template.substitute(
                prefix=prefix,
                numero=str(i).zfill(3)
            )
            for i in range(debut, debut + nombre)
        ]
    return generateur

# Utilisation
generateur_produit = formater_code('PROD-$numero')
codes_produits = generateur_produit('P', 1, 5)

def construire_regex_personnalise(**options):
    """Construit une expression régulière personnalisée."""
    import re
    
    patterns = {
        'lettres': f'[{string.ascii_letters}]',
        'chiffres': f'[{string.digits}]',
        'ponctuation': f'[{string.punctuation}]'
    }
    
    pattern = '^'
    if options.get('lettres_obligatoires'):
        pattern += f'(?=.*{patterns["lettres"]})'
    if options.get('chiffres_obligatoires'):
        pattern += f'(?=.*{patterns["chiffres"]})'
    
    pattern += '.{' + str(options.get('longueur_min', 1)) + ',}'
    return re.compile(pattern)
```

### 5. Bonnes pratiques (10 min)

```python
# Utilisation de constantes nommées
CARACTERES_SPECIAUX = string.punctuation + string.whitespace

# Gestion sécurisée des templates
def utiliser_template_securise(template_texte, donnees):
    """Utilise safe_substitute pour éviter les erreurs."""
    template = Template(template_texte)
    resultat = template.safe_substitute(donnees)
    return resultat

# Validation robuste
def est_alphanum_securise(texte):
    """Vérifie si le texte contient uniquement des caractères alphanumériques."""
    return all(c in (string.ascii_letters + string.digits) for c in texte)
```

### Phase de pratique (10 min)

Exercices :

1. Générateur de contenu :
```python
def creer_generateur_contenu():
    """
    Créer un générateur de contenu avec :
    - Templates personnalisables
    - Validation des entrées
    - Gestion des erreurs
    """
    # À compléter
```

2. Validateur personnalisé :
```python
def creer_validateur():
    """
    Créer un validateur qui :
    - Vérifie le format des entrées
    - Utilise les constantes de string
    - Retourne des messages d'erreur détaillés
    """
    # À compléter
```

### Synthèse (5 min)
- Constantes du module string
- Utilisation des templates
- Applications pratiques
- Bonnes pratiques

## Points importants à retenir :

1. Constantes :
   - ascii_letters, digits, punctuation
   - Utilisation pour la validation
   - Combinaisons personnalisées

2. Templates :
   - substitute vs safe_substitute
   - Gestion des erreurs
   - Templates personnalisés

3. Bonnes pratiques :
   - Validation robuste
   - Gestion sécurisée des templates
   - Utilisation des constantes nommées