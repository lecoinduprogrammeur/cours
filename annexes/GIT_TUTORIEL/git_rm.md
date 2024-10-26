# $ git rm

[Retour Git Commandes](;/git_commandes.md)

La commande `git rm` est utilisée pour supprimer des fichiers du suivi Git et du répertoire de travail. 

**Syntaxe de base** 

```bash
# Supprimer un fichier du suivi Git et du disque
git rm fichier.txt

# Supprimer un dossier et son contenu
git rm -r dossier/
```

-r -> recursif

**Options principales** 

```bash
# Garder le fichier sur le disque mais arrêter le suivi
git rm --cached fichier.txt

# Forcer la suppression
git rm -f fichier.txt

# Mode verbeux (plus d'informations)
git rm -v fichier.txt
```

**Cas d'utilisation courants** 

```bash
# Supprimer plusieurs fichiers
git rm fichier1.txt fichier2.txt

# Utiliser des motifs (patterns)
git rm *.txt

# Arrêter le suivi des fichiers de build
git rm --cached build/*
```

> [!IMPORTANT]
>
> **Différences importantes** 
>
> - `git rm` : Supprime du suivi Git ET du disque
> - `git rm --cached` : Supprime uniquement du suivi Git
> - `rm fichier.txt` : Supprime uniquement du disque
>
> **Points importants** 
>
> - Nécessite un commit après l'opération
> - Les fichiers supprimés avec --cached restent dans l'historique
> - Peut être annulé avant le commit avec git reset

**Messages d'erreur courants** 

```bash
# Fichier modifié dans l'index
"error: the following file has changes staged in the index:"
Solution: utiliser -f ou --cached

# Fichier non suivi
"fatal: pathspec 'fichier' did not match any files"
```

**Bonnes pratiques** 

```bash
# Vérifier l'état avant suppression
git status

# Vérifier quels fichiers seront affectés
git rm -n *.txt  # Dry run

# Commiter après la suppression
git commit -m "Supprime les fichiers inutiles"
```

**Scénarios typiques** 

```bash
# Arrêter le suivi de fichiers de configuration
git rm --cached config.local.php

# Nettoyer des fichiers générés
git rm -r dist/

# Supprimer des fichiers sensibles
git rm --cached passwords.txt
```

**Combinaison avec .gitignore** 

```bash
# 1. Arrêter le suivi
git rm --cached fichier-sensible.txt

# 2. Ajouter au .gitignore
echo "fichier-sensible.txt" >> .gitignore
```

**Récupération en cas d'erreur** 

```bash
# Avant commit
git reset HEAD fichier.txt

# Après commit (récupère la dernière version)
git checkout HEAD~1 fichier.txt
```

**Workflow type** 
```bash
# 1. Vérifier l'état
git status

# 2. Supprimer les fichiers
git rm fichiers-obsoletes/*

# 3. Vérifier les changements
git status

# 4. Commiter
git commit -m "Supprime les fichiers obsolètes"
```

La commande `git rm` est importante pour maintenir un dépôt propre et pour gérer correctement les fichiers qui ne doivent plus être suivis. Elle doit être utilisée avec précaution car elle peut supprimer des fichiers du disque.