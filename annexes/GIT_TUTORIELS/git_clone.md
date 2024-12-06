# $ git clone

[Retour Git Commandes](./git_commandes.md)

La commande `git clone` est utilisée pour créer une copie locale d'un dépôt Git distant.

**Syntaxe de base**
`git clone <url-du-dépôt> [nom-du-dossier]`

**Fonction principale**

- Copie un dépôt Git existant dans un nouveau répertoire local.
- Crée des branches de suivi à distance pour chaque branche du dépôt cloné.
- Crée et checkout une branche initiale qui est généralement une copie de la branche principale du dépôt distant.

**Ce que fait la commande** 

- Crée un nouveau dossier avec le nom du dépôt ou le nom spécifié.
- Initialise un dépôt `.git` dans ce dossier.
- Configure le dépôt distant d'origine (généralement nommé "origin").
- Récupère toutes les données du dépôt.
- Checkout la dernière version de la branche principale.

**Options courantes** 

- `--branch <nom>` ou `-b <nom>` : Clone une branche spécifique au lieu de la branche par défaut.
- `--depth <profondeur>` : Crée un clone superficiel avec un historique limité.
- `--bare` : Crée un clone nu, sans répertoire de travail.

**Exemples d'utilisation** 

- `git clone https://github.com/utilisateur/repo.git`
- `git clone git@github.com:utilisateur/repo.git mon-dossier`
- `git clone --branch develop https://github.com/utilisateur/repo.git`

**Points importants** 

- Fonctionne avec différents protocoles : HTTPS, SSH, Git.
- Peut nécessiter une authentification pour les dépôts privés.
- Crée automatiquement une connexion avec le dépôt distant nommée "origin".

**Avantages** 

- Rapide et efficace pour obtenir une copie complète d'un projet.
- Conserve tout l'historique et les branches du projet.
- Configure automatiquement le dépôt local pour travailler avec le dépôt distant.

**Pour cloner un dépôt GitHub sur votre ordinateur, voici les étapes à suivre** 

1. Obtenir l'URL du dépôt :
   - Allez sur la page du dépôt GitHub que vous voulez cloner.
   - Cliquez sur le bouton vert "Code".
   - Copiez l'URL fournie (HTTPS ou SSH, selon votre configuration).

2. Ouvrir votre terminal :
   - Sur Windows : Ouvrez Git Bash, PowerShell, ou l'invite de commande.
   - Sur Mac ou Linux : Ouvrez le Terminal.

3. Naviguer vers le répertoire où vous voulez cloner le dépôt :
   - Utilisez la commande `cd` pour vous déplacer dans le bon dossier.
   Exemple : `cd Documents/Projets`

4. Cloner le dépôt :
   - Utilisez la commande `git clone` suivie de l'URL que vous avez copiée.
   Exemple : `git clone https://github.com/utilisateur/nom-du-repo.git`

5. Entrer dans le répertoire cloné :
   - Utilisez `cd` pour entrer dans le nouveau dossier créé.
   Exemple : `cd nom-du-repo`

6. Vérifier que tout est en ordre :
   - Utilisez `git status` pour vérifier l'état du dépôt.

Voilà, vous avez maintenant une copie locale du dépôt GitHub sur votre ordinateur. Vous pouvez commencer à travailler sur les fichiers, créer des branches, faire des commits, etc.

Si le dépôt est privé ou si vous utilisez SSH, vous devrez peut-être vous authentifier avec vos identifiants GitHub ou votre clé SSH.

> [!WARNING]
>
> **Il n'y a pas donc besoin de lancer la commande git init avant !!!!!!**
>
> il n'y a pas besoin de lancer la commande `git init` avant de cloner un dépôt existant. Voici pourquoi :
>
> 1. git clone vs git init :
>    - `git clone` crée une copie complète du dépôt distant, y compris toute l'historique et la structure Git.
>    - `git init` est utilisé pour initialiser un nouveau dépôt Git vide.
> 2. Ce que fait git clone :
>    - Il crée un nouveau répertoire.
>    - Initialise un dépôt `.git` à l'intérieur.
>    - Récupère toutes les données du dépôt distant.
>    - Checkout une copie de travail de la dernière version.
> 3. Pourquoi pas git init :
>    - Utiliser `git init` avant `git clone` serait redondant et pourrait même causer des conflits.
>    - `git clone` fait déjà tout le nécessaire pour initialiser et configurer le dépôt local.

> [!TIP]
>
> **2 Scénarios possibles**
>
> - `git init` : Quand vous commencez un nouveau projet localement ou voulez mettre un projet existant sous Git.
> - `git clone` : Quand vous voulez copier un dépôt existant depuis un serveur distant (comme GitHub).



