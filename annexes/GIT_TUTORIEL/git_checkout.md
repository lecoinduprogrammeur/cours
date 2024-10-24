# $ git checkout

La commande `git checkout` est très polyvalente et sert principalement à naviguer entre les branches et les versions de fichiers.

**Fonctions principales** 

- Changer de branche
- Créer une nouvelle branche
- Restaurer des fichiers
- Naviguer dans l'historique

**Syntaxe de base** 

```bash
# Changer de branche
git checkout <nom-branche>

# Créer et changer vers une nouvelle branche
git checkout -b <nouvelle-branche>

# Restaurer un fichier à son état dans HEAD
git checkout -- <fichier>
```

**Utilisations courantes** 

a. Gestion des branches :
```bash
# Aller sur main
git checkout main

# Créer et aller sur une nouvelle branche
git checkout -b feature/nouvelle-fonctionnalite

# Revenir à la branche précédente
git checkout -
```

b. Gestion des fichiers :
```bash
# Restaurer un fichier spécifique
git checkout -- fichier.txt

# Restaurer tous les fichiers
git checkout -- .
```

**Options importantes** 

- `-b` : Crée une nouvelle branche
- `-f` : Force le changement même avec des modifications non committées
- `--track` : Configure le suivi d'une branche distante
- `--orphan` : Crée une branche sans historique

**Points importants** 

- Peut perdre des modifications non committées
- Modifie l'état du répertoire de travail
- Peut déplacer HEAD

**Bonnes pratiques** 

```bash
# Vérifier l'état avant checkout
git status

# Committer ou stash les changements si nécessaire
git stash

# Puis faire le checkout
git checkout <branche>
```

**Cas d'utilisation spéciaux** 

```bash
# Checkout d'un commit spécifique
git checkout <hash-commit>

# Créer une branche depuis un commit spécifique
git checkout -b <nouvelle-branche> <hash-commit>

# Checkout d'un tag
git checkout <nom-tag>
```

**Note importante (Git 2.23+)** 

- `git checkout` est progressivement remplacé par deux nouvelles commandes :
  - `git switch` : Pour changer de branches
  - `git restore` : Pour restaurer des fichiers

**Messages d'erreur courants** 

- "Your local changes would be overwritten"
- "PathSpec did not match any files"
- "The branch already exists"

**Workflow typique** 

```bash
git status                  # Vérifier l'état
git checkout main          # Aller sur main
git pull                   # Mettre à jour
git checkout -b feature    # Créer nouvelle branche
```

> [!TIP]
>
> La commande `git checkout` est fondamentale dans Git, mais sa polyvalence peut parfois prêter à confusion. C'est pourquoi les nouvelles commandes `git switch` et `git restore` ont été introduites pour séparer ces fonctionnalités en commandes plus spécifiques.

