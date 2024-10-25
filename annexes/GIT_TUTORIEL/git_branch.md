# $ git branch

La commande `git branch` sert à gérer les branches dans Git.

**Commandes de base** 

```bash
# Lister les branches locales
git branch

# Créer une nouvelle branche
git branch <nom-branche>

# Supprimer une branche
git branch -d <nom-branche>

# Renommer une branche
git branch -m <nouveau-nom>
```

**Options courantes** 

```bash
# Liste toutes les branches (locales et distantes)
git branch -a

# Liste les branches distantes
git branch -r

# Affiche plus d'informations sur les branches
git branch -v

# Force la suppression d'une branche
git branch -D <nom-branche>
```

**Gestion des branches distantes** 

```bash
# Suivre une branche distante
git branch --track <branche> origin/<branche>

# Supprimer une branche distante
git push origin --delete <branche>
```

**Informations détaillées** 

```bash
# Voir le dernier commit de chaque branche
git branch -v

# Voir les branches mergées
git branch --merged

# Voir les branches non mergées
git branch --no-merged
```

**État des branches** 

- `*` indique la branche courante
- Vert : branche courante
- Branches mergées/non-mergées

**Points importants** 

- Une branche est un pointeur vers un commit
- La création de branche est légère en Git
- Les branches sont locales par défaut

**Bonnes pratiques** 

```bash
# Vérifier l'état avant de créer/supprimer
git status

# Conventions de nommage communes
feature/nom-feature
bugfix/description-bug
hotfix/description
release/version
```

**Cas d'utilisation courants** 

```bash
# Créer une branche pour une nouvelle fonctionnalité
git branch feature/nouvelle-fonction

# Nettoyer les branches mergées
git branch --merged | grep -v "\*" | xargs git branch -d

# Renommer la branche courante
git branch -m nouveau-nom
```

**Gestion des conflits** 

```bash
# Voir quelles branches sont mergées
git branch --merged main

# Voir quelles branches ne sont pas mergées
git branch --no-merged main
```

**Messages d'erreur courants** 

- "Branch already exists"
- "Cannot delete branch - it is not fully merged"
- "refname does not exist"

**Workflow type** 

```bash
# Créer et passer sur une nouvelle branche
git branch nouvelle-feature
git checkout nouvelle-feature
# ou en une commande
git checkout -b nouvelle-feature
```

**Commandes avancées** 

```bash
# Copier un commit spécifique dans une nouvelle branche
git branch <nouvelle-branche> <commit-hash>

# Voir la branche parente
git branch --contains <commit>
```

La gestion des branches est fondamentale dans Git, permettant le développement parallèle et l'isolation des fonctionnalités. 