# $ git merge

La commande `git merge` est utilisée pour fusionner des branches ensemble.

**Fonction principale** 

- Intègre les changements d'une branche dans une autre
- Crée un nouveau commit de fusion (merge commit)

**Syntaxe de base** 

```bash
# Se placer sur la branche qui recevra les modifications
git checkout main

# Fusionner une autre branche dans la branche courante
git merge <nom-branche>
```

> [!WARNING]
>
> **Types de merge** 
> **a. Fast-forward merge :**
>
> - **Quand il n'y a pas de nouveaux commits sur la branche de destination**
> - **Déplace simplement le pointeur**
>
> **b. Merge commit (3-way merge) :**
>
> - **Crée un nouveau commit avec deux parents**
> - **Utilisé quand les deux branches ont divergé**

**Options importantes** 

```bash
# Crée toujours un merge commit, même si fast-forward possible
git merge --no-ff <branche>

# Annule le merge en cas de conflits
git merge --abort

# Merge sans commit automatique
git merge --no-commit <branche>
```

**Gestion des conflits** 

- Les conflits surviennent quand un même fichier est modifié différemment
- Git marque les zones de conflit dans les fichiers :
```
<<<<<<< HEAD
version actuelle
=======
version à merger
>>>>>>> branch-name
```

**Process de résolution** 

1. Identifier les fichiers en conflit (`git status`)

2. Éditer les fichiers pour résoudre les conflits

3. `git add` les fichiers résolus

4. `git commit` pour finaliser le merge

**Bonnes pratiques** 

```bash
# Avant un merge
git status                  # Vérifier l'état actuel
git pull                    # Mettre à jour la branche actuelle
git checkout feature        # Aller sur la branche à merger
git pull                    # Mettre à jour la branche feature
git checkout main          # Retourner sur main
git merge feature          # Merger feature dans main
```

**Points importants** 

- Toujours vérifier la branche active avant de merger
- Garder les branches à jour
- Comprendre l'impact du merge sur l'historique

**Stratégies de merge** 

```bash
# Spécifier une stratégie
git merge -s recursive <branche>
git merge -s ours <branche>
git merge -s theirs <branche>
```

**Messages d'erreur courants** 

- "Merge conflict in [file]"
- "Automatic merge failed"
- "Not something we can merge"

**Annuler un merge** 

```bash
# Si le merge n'est pas commité
git merge --abort

# Si le merge est commité
git reset --hard HEAD~1
```

**Workflow type** 

```bash
# Merger une feature branch dans main
git checkout main
git pull
git merge feature/nouvelle-fonctionnalite
git push
```

