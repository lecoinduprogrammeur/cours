# $ git status (version II)

[Retour Git Commandes](./git_commandes.md)

La commande `git status` est un outil essentiel pour voir l'état actuel de votre dépôt Git.

**Fonction principale** 

- Affiche l'état des fichiers dans votre répertoire de travail et l'index (staging area)
- Montre la relation entre la branche locale et sa branche distante

**Syntaxe de base** 

```bash
git status
git status -s  # Format court
git status -b  # Montre aussi les infos de la branche
```

**Informations affichées** 

- Branche courante
- État par rapport à la branche distante (ahead/behind)
- Fichiers modifiés non indexés (not staged)
- Fichiers indexés (staged)
- Fichiers non suivis (untracked)

**Format de sortie standard** 

```
On branch main
Your branch is up to date with 'origin/main'

Changes to be committed:
  (fichiers dans l'index)

Changes not staged for commit:
  (fichiers modifiés mais non indexés)

Untracked files:
  (fichiers non suivis par Git)
```

**Format court (-s)** 

```
M  fichier.txt    # Modifié et staged
 M fichier2.txt   # Modifié mais non staged
?? nouveau.txt    # Non suivi
A  ajoute.txt    # Nouveau fichier staged
D  supprime.txt  # Fichier supprimé
```

**États possibles des fichiers** 

- Non suivi (untracked)
- Modifié (modified)
- Indexé (staged)
- Commité (committed)

**Options utiles** 

```bash
# Affichage court
git status -s

# Avec info de branche
git status -b

# Inclure les fichiers ignorés
git status --ignored
```

**Messages courants** 

- "nothing to commit, working tree clean"
- "Changes to be committed"
- "Changes not staged for commit"
- "Untracked files"

**Bonnes pratiques** 

- Vérifier régulièrement l'état avec `git status`
- Utiliser avant et après les commandes Git importantes
- Comprendre les différents états des fichiers

**Workflow typique** 

```bash
git status          # Vérifier l'état
git add fichier     # Ajouter des changements
git status          # Revérifier
git commit          # Commiter
git status          # Vérifier à nouveau
```

La commande `git status` est l'une des commandes Git les plus utilisées car elle fournit une vue d'ensemble claire de l'état actuel de votre travail. C'est souvent la première commande à utiliser quand vous voulez savoir où vous en êtes dans votre travail Git.