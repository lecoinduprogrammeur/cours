# $ git log

La commande `git log` permet de visualiser l'historique des commits.

**Syntaxe de base** 

```bash
git log                    # Affichage standard
git log --oneline         # Format condensé
git log --graph          # Affichage graphique
```

**Options courantes** 

```bash
# Limiter le nombre de commits
git log -n 5

# Afficher les différences
git log -p

# Format court avec graph
git log --oneline --graph --all

# Format personnalisé
git log --pretty=format:"%h - %an, %ar : %s"
```

**Filtres utiles** 

```bash
# Par auteur
git log --author="nom"

# Par date
git log --since="2 weeks ago"
git log --before="2024-01-01"

# Par message
git log --grep="bug"

# Par fichier
git log -- fichier.txt
```

**Options de présentation** 

- `--oneline` : Une ligne par commit
- `--graph` : Affichage graphique des branches
- `--decorate` : Montre les références (branches, tags)
- `--stat` : Statistiques des fichiers modifiés

**Format personnalisé (%pretty=format:)** 

- `%h` : Hash court
- `%H` : Hash complet
- `%an` : Nom de l'auteur
- `%ad` : Date de l'auteur
- `%s` : Sujet du commit
- `%b` : Corps du message

**Exemples pratiques** 

```bash
# Vue graphique complète
git log --graph --oneline --all --decorate

# Commits récents avec stats
git log --stat -n 5

# Recherche de commits
git log --grep="fix" --oneline

# Format personnalisé
git log --pretty=format:"%C(yellow)%h%Creset - %s %Cgreen(%cr)" --abbrev-commit
```

**Navigation dans le log** 

- Espace : Page suivante
- b : Page précédente
- q : Quitter
- / : Rechercher
- n : Résultat suivant

**Cas d'utilisation avancés** 

```bash
# Voir les commits fusionnés
git log --merges

# Voir les commits non fusionnés
git log --no-merges

# Différences entre branches
git log main..feature

# Fichiers modifiés par commit
git log --name-status
```

**Alias utiles (à configurer)** 

```bash
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

**Bonnes pratiques** 

- Utilisez les options appropriées selon le contexte
- Créez des alias pour les formats fréquemment utilisés
- Combinez avec `grep` pour des recherches efficaces

**Exemples de recherches spécifiques** 

```bash
# Chercher des modifications dans un fichier
git log -p fichier.txt

# Commits d'un auteur sur une période
git log --author="nom" --since="1 month ago"

# Commits touchant une ligne spécifique
git log -L 10,20:fichier.txt
```

