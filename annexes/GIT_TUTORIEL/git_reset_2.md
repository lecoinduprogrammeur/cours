# $ git reset

[Retour Git Commandes](;/git_commandes.md)

La commande `git reset` est utilisée pour réinitialiser l'état de votre dépôt. Elle peut affecter l'historique des commits, l'index et le répertoire de travail. 

**Modes principaux** 

```bash
# Soft : Conserve les modifications dans l'index
git reset --soft <commit>

# Mixed (défaut) : Réinitialise l'index mais garde les fichiers
git reset --mixed <commit>

# Hard : Réinitialise tout, supprime les modifications
git reset --hard <commit>
```

**Syntaxe courante** 

```bash
# Annuler le dernier commit
git reset HEAD~1

# Réinitialiser à un commit spécifique
git reset <commit-hash>

# Désindexer un fichier
git reset HEAD <fichier>
```

**Effets des différents modes** 

- `--soft` : 
  * Déplace HEAD
  * Garde l'index et le répertoire de travail

- `--mixed` (défaut) :
  * Déplace HEAD
  * Réinitialise l'index
  * Garde le répertoire de travail

- `--hard` :
  * Déplace HEAD
  * Réinitialise l'index
  * Réinitialise le répertoire de travail

**Cas d'utilisation courants** 

```bash
# Annuler les changements indexés
git reset HEAD

# Revenir au dernier commit
git reset --hard HEAD

# Combiner plusieurs commits
git reset --soft HEAD~3
git commit -m "Nouveau message"
```

**Points importants** 

- Modifie l'historique des commits
- Peut causer une perte de données avec --hard
- À éviter sur des branches partagées

**Sécurité** 

```bash
# Créer une branche de sauvegarde
git branch backup-branch

# Vérifier le reflog en cas de problème
git reflog
```

**Exemples pratiques** 

```bash
# Désindexer des fichiers
git reset fichier.txt

# Annuler tous les commits après un certain point
git reset <commit-hash>

# Nettoyer complètement le répertoire
git reset --hard HEAD
```

**Comparaison avec autres commandes** 

- `git revert` : Crée un nouveau commit d'annulation
- `git checkout` : Navigation sans modification d'historique
- `git clean` : Supprime les fichiers non suivis

**Bonnes pratiques** 

```bash
# Toujours vérifier l'état avant
git status

# Créer une sauvegarde si nécessaire
git branch backup

# Utiliser --hard avec précaution
```

**Messages d'erreur courants** 

- "Cannot do hard reset with paths"
- "Updates were rejected"
- "Your local changes would be overwritten"

**Récupération après erreur** 

```bash
# Voir l'historique des actions
git reflog

# Récupérer un état précédent
git reset --hard HEAD@{n}
```

**Workflow type** 
```bash
# Vérifier l'état actuel
git status

# Voir les commits à réinitialiser
git log

# Effectuer le reset
git reset --option <commit>

# Vérifier le résultat
git status
git log
```

La commande `git reset` est puissante mais doit être utilisée avec précaution, particulièrement avec l'option `--hard`. Elle est très utile pour le nettoyage local mais peut être dangereuse sur des branches partagées.