# $ git init

La commande `git init` est utilisée pour initialiser un nouveau dépôt Git. 

1. Fonction principale :
   `git init` crée un nouveau dépôt Git vide dans le répertoire courant ou dans un répertoire spécifié.

2. Utilisation de base :
   - `git init` : Initialise un dépôt dans le répertoire actuel.
   - `git init <directory>` : Crée un nouveau répertoire avec le nom spécifié et l'initialise comme un dépôt Git.

3. Ce que fait la commande :
   - Crée un sous-répertoire caché `.git` qui contient toute la structure nécessaire pour le dépôt Git.
   - Crée une branche initiale (généralement nommée `master` ou `main` selon la configuration).

4. Points importants :
   - Elle ne crée pas de commit initial. Le premier commit doit être fait manuellement.
   - Elle peut être utilisée pour convertir un projet existant en un dépôt Git.
   - N'affecte pas les fichiers existants dans le répertoire.

5. Options courantes :
   - `git init --bare` : Crée un dépôt "nu" (bare repository), généralement utilisé comme dépôt central sur un serveur.

6. Utilisation typique :
   - Au début d'un nouveau projet pour commencer à suivre les changements avec Git.
   - Pour ajouter le contrôle de version Git à un projet existant.

7. Après l'initialisation :
   - Vous pouvez commencer à ajouter des fichiers (`git add`), faire des commits (`git commit`), et configurer des dépôts distants (`git remote add`).

La commande `git init` est souvent la première étape lorsqu'on commence à utiliser Git pour un nouveau projet ou lorsqu'on veut mettre un projet existant sous contrôle de version avec Git.