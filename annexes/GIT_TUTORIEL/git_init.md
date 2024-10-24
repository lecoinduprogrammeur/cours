# $ git init

**La commande `git init` est utilisée pour initialiser un nouveau dépôt Git.** 

- `git init` : Initialise un dépôt dans un répertoire.
- `git init <directory>` : Crée un nouveau répertoire avec le nom spécifié et l'initialise comme un dépôt Git.
- crée un sous-répertoire caché `.git` qui contient toute la structure nécessaire pour le dépôt Git.
- crée une branche initiale (généralement nommée `master` ou `main` selon la configuration).

**Points importants** 

- Elle ne crée pas de commit initial. Le premier commit doit être fait manuellement.
- Elle peut être utilisée pour convertir un projet existant en un dépôt Git.
- N'affecte pas les fichiers existants dans le répertoire.

**Options courantes** 

- `git init --bare` : Crée un dépôt "nu" (bare repository), généralement utilisé comme dépôt central sur un serveur.

**Utilisation typique** 

- Au début d'un nouveau projet pour commencer à suivre les changements avec Git.
- Pour ajouter le contrôle de version Git à un projet existant.

**Après l'initialisation** 

- Vous pouvez commencer à ajouter des fichiers (`git add`), faire des commits (`git commit`), et configurer des dépôts distants (`git remote add`).

