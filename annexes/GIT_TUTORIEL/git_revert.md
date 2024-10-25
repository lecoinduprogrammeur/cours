# $ git revert

La commande `git revert` permet d'annuler des commits en créant un nouveau commit d'annulation. 

**Syntaxe de base** 

```bash
# Annuler le dernier commit
git revert HEAD

# Annuler un commit spécifique
git revert <commit-hash>
```

**Options importantes** 

```bash
# Ne pas créer le commit automatiquement
git revert -n <commit>

# Annuler plusieurs commits
git revert <commit1>..<commit2>

# Résoudre les conflits
git revert --continue
git revert --abort
```

**Cas d'utilisation** 

```bash
# Annuler le dernier commit
git revert HEAD

# Annuler un commit spécifique
git revert abc123

# Annuler une plage de commits
git revert HEAD~3..HEAD
```

**Points importants** 

- Crée un nouveau commit
- Ne modifie pas l'historique existant
- Sûr pour les branches partagées
- Peut générer des conflits

**Différence avec git reset** 

- `git revert` : crée un nouveau commit d'annulation
- `git reset` : supprime les commits de l'historique

**Gestion des conflits** 

```bash
# En cas de conflit
# 1. Résoudre les conflits dans les fichiers
# 2. git add des fichiers résolus
git add .
# 3. Continuer le revert
git revert --continue
# Ou annuler l'opération
git revert --abort
```

**Bonnes pratiques** 

```bash
# Vérifier l'état avant revert
git status

# Vérifier le commit à annuler
git show <commit-hash>

# Créer une branche de sauvegarde
git branch backup-branch
```

**Messages d'erreur courants** 

- "error: commit <hash> is a merge commit"
- "error: your local changes would be overwritten"
- "conflict: failed to revert '<commit>'"

**Cas spéciaux** 

```bash
# Revert d'un merge commit
git revert -m 1 <merge-commit-hash>

# Revert sans commit automatique
git revert -n <commit>
git commit -m "Message personnalisé"
```

**Workflow typique** 

```bash
# 1. Identifier le commit à annuler
git log

# 2. Créer le revert
git revert <commit-hash>

# 3. Vérifier le résultat
git log
git status
```

**Avantages de revert** 

- Sûr pour les branches publiques
- Maintient l'historique complet
- Facilite le suivi des modifications
- Réversible

**Dans le cas d'un merge** 
```bash
# Annuler un merge
git revert -m 1 <merge-commit>

# Le paramètre -m 1 indique de conserver 
# les changements du parent principal
```

La commande `git revert` est l'outil recommandé pour annuler des changements dans des branches partagées car elle ne modifie pas l'historique existant. Elle crée plutôt un nouveau commit qui annule les changements souhaités.