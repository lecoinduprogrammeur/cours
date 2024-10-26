# $ git diff

[Retour Git Commandes](;/git_commandes.md)

La commande `git diff` permet de voir les différences entre les fichiers, les commits, les branches, etc. 

**Syntaxe de base** 

```bash
# Différences dans le répertoire de travail
git diff

# Différences dans l'index (staged)
git diff --staged  (ou --cached)

# Différences entre branches
git diff branche1..branche2
```

**Utilisations courantes** 

```bash
# Voir les modifications non indexées
git diff

# Voir ce qui est prêt à être commité
git diff --staged

# Comparer avec le dernier commit
git diff HEAD

# Comparer deux commits
git diff commit1 commit2
```

**Options importantes** 

```bash
# Voir uniquement les noms de fichiers
git diff --name-only

# Statistiques résumées
git diff --stat

# Ignorer les espaces
git diff -w

# Voir les différences pour un fichier spécifique
git diff -- chemin/vers/fichier
```

**Format de sortie** 

```diff
diff --git a/fichier b/fichier
index abc123..def456 100644
--- a/fichier
+++ b/fichier
@@ -1,3 +1,4 @@
 ligne inchangée
-ligne supprimée
+ligne ajoutée
 ligne inchangée
```

**Comparaisons spécifiques** 

```bash
# Entre deux branches
git diff main..feature

# Entre la branche actuelle et un commit
git diff commit_hash

# Entre deux commits
git diff commit1..commit2
```

**Options de visualisation** 

```bash
# Afficher en couleur
git diff --color-words

# Afficher le contexte
git diff -U5  (5 lignes de contexte)

# Format plus compact
git diff --compact-summary
```

**Cas d'utilisation avancés** 

```bash
# Différences depuis le dernier tag
git diff $(git describe --tags --abbrev=0)

# Différences dans un intervalle de commits
git diff commit1...commit2

# Différences de permissions
git diff --summary
```

**Symboles utilisés** 

- `-` : ligne supprimée
- `+` : ligne ajoutée
- `@@` : marqueurs de position
- `\ No newline at end of file`

**Bonnes pratiques** 

```bash
# Vérifier les changements avant commit
git diff --staged

# Examiner les modifications par fichier
git diff -- file1.txt file2.txt

# Utiliser avec git status
git status
git diff
```

**Options utiles pour la revue de code** 

```bash
# Voir les changements de caractères
git diff --word-diff

# Ignorer les changements de permissions
git diff -p --no-mode

# Générer un patch
git diff > changes.patch
```

**Messages courants et leur signification** 

- Pas de sortie = pas de différence
- `Binary files differ` = fichiers binaires
- `diff --cc` = différences dans un merge

**Intégration avec des outils externes** 

```bash
# Utiliser un outil de diff externe
git difftool

# Configurer un outil de diff
git config --global diff.tool <nom-outil>
```

La commande `git diff` est essentielle pour examiner les modifications avant de les commiter et pour comparer différentes versions du code. Elle aide à s'assurer que les changements sont corrects avant de les valider.