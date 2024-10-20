# Git Commandes

------

## $ git

```bash
Fabrice@PETIT-PC MINGW64 ~/Documents/GIT_GITHUB/demo_local (main)
$ git
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   restore    Restore working tree files
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   diff       Show changes between commits, commit and working tree, etc
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   backfill   Download missing objects in a partial clone
   branch     List, create, or delete branches
   commit     Record changes to the repository
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   reset      Reset current HEAD to the specified state
   switch     Switch branches
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```

------

## #point-de-départ

------

### $ git init

La commande `git init` est utilisée pour initialiser un nouveau dépôt Git.

[git init en détails](./git_init.md) 

------

### $ git config

La commande `git config` est utilisée pour configurer les paramètres de Git.

[git config en détails](./git_config.md)

------

### $ git clone

La commande `git clone` est utilisée pour créer une copie locale d'un dépôt Git distant. 

Pas de $ git init !

[git clone en détails](./git_clone.md)

------

## #sauver-son-travail

------

### $ git add

La commande `git add` est une commande fondamentale dans Git, utilisée pour ajouter des modifications à l'index (aussi appelé "staging area"). 

[git add en détails](./git_add.md)

------

### $ git commit

La commande `git commit` est une opération fondamentale dans Git, utilisée pour enregistrer les modifications préparées dans l'index (staging area) dans l'historique du dépôt.

[git commit en détails](./git_commit.md)

------

### $ git reset

La commande `git reset` est un outil puissant et flexible utilisé pour annuler ou ajuster des changements dans Git. Elle peut modifier l'état de l'index (staging area) et, dans certains cas, l'historique des commits.

[git reset en détails](./git_reset.md)

------

### $ git status

La commande `git status` est un outil essentiel dans Git pour obtenir un aperçu de l'état actuel de votre répertoire de travail et de l'index. 

[git status en détails](./git_status.md)



