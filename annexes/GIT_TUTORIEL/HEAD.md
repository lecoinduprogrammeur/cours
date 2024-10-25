# HEAD

HEAD est un concept fondamental dans Git qui peut être expliqué sous plusieurs aspects :

**Définition de base** 

- HEAD est un pointeur spécial qui indique le dernier commit de la branche courante
- C'est essentiellement "où vous êtes maintenant" dans votre dépôt

**Caractéristiques** 

```bash
# HEAD pointe normalement vers une branche
HEAD -> main -> commit_123

# HEAD peut aussi pointer directement vers un commit (detached HEAD)
HEAD -> commit_456
```

**Représentations courantes** 

- `HEAD` : Commit actuel
- `HEAD~1` : Parent direct du commit actuel
- `HEAD~2` : Grand-parent du commit actuel
- `HEAD^` : Similaire à HEAD~1
- `HEAD^^` : Similaire à HEAD~2

**États possibles** 

a. HEAD attaché (normal) :
```
HEAD -> main -> commit_123
```
- État normal
- HEAD pointe vers une branche
- La branche pointe vers un commit

b. HEAD détaché (detached HEAD) :
```
HEAD -> commit_456
```
- État spécial
- HEAD pointe directement vers un commit
- Utile pour l'exploration temporaire
- Risque de perte de commits si on ne crée pas de branche

**Utilisations courantes** 

```bash
# Voir où pointe HEAD
git log HEAD

# Revenir en arrière temporairement
git checkout HEAD~3

# Réinitialiser au dernier commit
git reset HEAD

# Voir les différences avec HEAD
git diff HEAD
```

**Points importants à comprendre** 

- HEAD se déplace automatiquement quand :
  * Vous faites un nouveau commit
  * Vous changez de branche
  * Vous faites un reset
- HEAD est stocké dans le fichier .git/HEAD
- Un seul HEAD par dépôt

**Commandes affectant HEAD** 

```bash
git checkout     # Déplace HEAD
git reset        # Déplace HEAD et potentiellement modifie l'index/working directory
git commit       # Crée un nouveau commit et avance HEAD
git merge        # Peut créer un nouveau commit où HEAD pointera
git rebase       # Réécrit l'histoire et déplace HEAD
```

**Exemples pratiques** 

a. Navigation dans l'historique :
```bash
# Revenir 3 commits en arrière
git checkout HEAD~3

# Revenir au dernier commit
git checkout HEAD
```

b. Références relatives :
```bash
# Parent du commit actuel
git show HEAD^

# Premier parent d'un merge commit
git show HEAD^1

# Second parent d'un merge commit
git show HEAD^2
```

**Cas particuliers** 

a. Detached HEAD :
```bash
# Créer une situation de detached HEAD
git checkout <commit-hash>

# Solution : créer une branche
git checkout -b nouvelle-branche
```

b. Multiples parents (merge commits) :
```bash
HEAD^1  # Premier parent
HEAD^2  # Second parent
HEAD^   # Équivalent à HEAD^1
```

**Bonnes pratiques** 

- Toujours être conscient de où pointe HEAD
- Éviter de rester en état detached HEAD
- Utiliser `git status` pour vérifier l'état de HEAD
- Créer une branche si vous devez travailler en detached HEAD

**Le concept de HEAD est central dans Git car il permet de :**

- Savoir où vous êtes dans l'historique
- Servir de point de référence pour de nombreuses commandes
- Naviguer dans l'historique des commits
- Maintenir la cohérence du dépôt