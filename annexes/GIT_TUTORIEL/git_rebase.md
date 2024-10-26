# $ git rebase

[Retour Git Commandes](./git_commandes.md)

La commande `git rebase` est une alternative à `git merge` pour intégrer des changements. Elle réécrit l'historique des commits. 

**Fonction principale** 

- Réapplique les commits d'une branche sur une autre
- Permet de maintenir un historique plus linéaire

**Syntaxe de base** 

```bash
# Sur la branche à rebase
git rebase <branche-cible>

# Ou en une seule commande
git rebase <branche-cible> <branche-a-rebase>
```

**Cas d'utilisation** 

a. Rebase simple :
```bash
git checkout feature
git rebase main
```

b. Rebase interactif :
```bash
git rebase -i HEAD~3  # Rebase interactif sur les 3 derniers commits
```

**Options importantes** 

- `-i` ou `--interactive` : Mode interactif
- `--onto` : Rebase sur un commit spécifique
- `--continue` : Continuer après résolution de conflits
- `--abort` : Annuler le rebase
- `--skip` : Ignorer le commit actuel

**Commandes en mode interactif** 

- `pick` : Utiliser le commit
- `reword` : Modifier le message du commit
- `edit` : Modifier le commit
- `squash` : Fusionner avec le commit précédent
- `fixup` : Comme squash mais ignore le message
- `drop` : Supprimer le commit

**Points importants** 

- Ne pas faire de rebase des branches publiques/partagées
- Peut créer des conflits à résoudre
- Modifie l'historique des commits (nouveaux hashes)

**Bonnes pratiques** 

```bash
# Avant un rebase
git fetch
git status

# Créer une branche de sauvegarde
git branch backup-branch

# Faire le rebase
git rebase main feature
```

**Gestion des conflits** 

```bash
# En cas de conflit
# 1. Résoudre les conflits dans les fichiers
# 2. git add des fichiers résolus
git add .
# 3. Continuer le rebase
git rebase --continue
```

**Situations courantes** 

```bash
# Nettoyer l'historique avant push
git rebase -i HEAD~5

# Mettre à jour une branche feature avec main
git checkout feature
git rebase main
```

**À éviter** 

- Rebase sur des branches publiques
- Rebase sans backup
- Rebase de longs historiques sans nécessité

**Comparaison avec merge** 

- Merge : Préserve l'historique, crée des branches
- Rebase : Historique linéaire, plus propre mais réécrit l'historique

Messages d'erreur courants 
- "Cannot rebase: You have unstaged changes"
- "Conflict in..."
- "No rebase in progress?"

La commande `git rebase` est puissante mais nécessite une bonne compréhension de Git. Elle est particulièrement utile pour maintenir un historique propre et linéaire, mais doit être utilisée avec précaution sur des branches partagées.