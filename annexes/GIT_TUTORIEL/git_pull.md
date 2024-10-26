# $ git pull

[Retour Git Commandes](./git_commandes.md)

La commande `git pull` est utilisée pour récupérer et intégrer les changements d'un dépôt distant. 

**Fonction principale** 

- Combine `git fetch` + `git merge` en une seule commande
- Récupère les modifications du dépôt distant et les fusionne dans votre branche locale

**Syntaxe de base** 

```bash
git pull [remote] [branche]
git pull origin main  # Cas le plus courant
```

**Options importantes** 

```bash
# Récupère et rebase au lieu de merger
git pull --rebase

# Pull sans fusion automatique
git pull --no-commit

# Force le pull même avec des changements locaux
git pull --force

# Spécifie la stratégie de merge
git pull --strategy=recursive
```

**Scénarios courants** 

- Mise à jour quotidienne de votre code :
  ```bash
  git pull origin main
  ```
- Pull avec rebase pour éviter les commits de merge :
  ```bash
  git pull --rebase origin main
  ```

**Points importants** 

- Peut créer des conflits qui nécessitent une résolution manuelle
- Modifie votre branche locale actuelle
- Combine deux opérations (fetch + merge/rebase)

**Bonnes pratiques** 

- Faites un `git status` avant de pull pour vérifier votre état local
- Committez ou stashez vos changements locaux avant de pull
- Utilisez `--rebase` pour maintenir un historique plus propre

**Messages d'erreur courants** 

- "Please commit your changes or stash them"
- "Merge conflict in [fichier]"
- "Cannot pull with rebase: You have unstaged changes"

**Workflow typique** 

```bash
git status              # Vérifier l'état local
git add .              # Si nécessaire
git commit -m "msg"    # Si nécessaire
git pull origin main   # Récupérer et fusionner les changements
```

**Comparaison avec `git fetch`** 

- `git fetch` : Récupère les changements sans les fusionner
- `git pull` : Récupère ET fusionne les changements

**Gestion des conflits** 

- Si des conflits surviennent :
  1. Résolvez les conflits dans les fichiers
  2. `git add` les fichiers résolus
  3. Terminez le merge avec `git commit`

**Configuration utile** 

```bash
# Configurer le comportement par défaut du pull
git config --global pull.rebase false  # merge (défaut)
git config --global pull.rebase true   # rebase
git config --global pull.ff only       # fast-forward only
```