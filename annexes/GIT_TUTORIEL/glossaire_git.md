# Glossaire Git

[Retour Git Commandes](;/git_commandes.md)

## A
- **Alias** : Raccourci personnalisé pour une commande Git.
- **Amont (Upstream)** : Référence au dépôt distant d'origine, souvent appelé "origin".
- **Arbre (Tree)** : Structure de données Git représentant un répertoire.

## B
- **Bare Repository** : Dépôt Git sans répertoire de travail, généralement utilisé comme dépôt central.
- **Blame** : Commande montrant qui a modifié chaque ligne d'un fichier et quand.
- **Branch (Branche)** : Ligne de développement indépendante, pointeur vers un commit spécifique.

## C
- **Cherry-pick** : Action de copier un commit spécifique d'une branche à une autre.
- **Clean** : État d'un répertoire de travail sans fichiers non suivis.
- **Clone** : Copie complète d'un dépôt Git, incluant tout l'historique.
- **Commit** : Instantané des modifications avec un message descriptif.
- **Commit Hash** : Identifiant unique (SHA-1) d'un commit.
- **Conflit (Conflict)** : Situation où Git ne peut pas fusionner automatiquement des modifications.

## D
- **Détacher HEAD** : État où HEAD pointe directement sur un commit plutôt que sur une branche.
- **Diff** : Différences entre deux états (commits, branches, fichiers).
- **Dépôt (Repository)** : Collection de fichiers et de leur historique complet.

## F
- **Fast-forward** : Fusion simple où la branche cible avance directement vers le commit le plus récent.
- **Fetch** : Récupération des modifications du dépôt distant sans fusion.
- **Fork** : Copie personnelle d'un dépôt distant, généralement sur une plateforme comme GitHub.

## G
- **Git Flow** : Modèle de branches pour la gestion de versions.
- **GitIgnore** : Fichier spécifiant les éléments que Git doit ignorer.

## H
- **HEAD** : Pointeur vers le dernier commit de la branche courante.
- **Hook** : Script automatique exécuté à certains moments (pre-commit, post-commit, etc.).

## I
- **Index** : Zone de préparation (staging area) où les modifications sont placées avant commit.
- **Initial Commit** : Premier commit d'un dépôt.

## L
- **Log** : Historique des commits.
- **LFS (Large File Storage)** : Extension Git pour gérer les gros fichiers.

## M
- **Merge** : Fusion de deux branches.
- **Merge Conflict** : Conflit survenant lors d'une fusion.
- **Master/Main** : Nom conventionnel de la branche principale.

## O
- **Origin** : Nom conventionnel du dépôt distant principal.
- **Orphan Branch** : Branche sans historique commun avec les autres branches.

## P
- **Patch** : Fichier décrivant des modifications.
- **Pull** : Combinaison de fetch et merge.
- **Pull Request (PR)** : Demande d'intégration de modifications (terme GitHub).
- **Push** : Envoi des commits locaux vers un dépôt distant.

## R
- **Rebase** : Réécriture de l'historique en déplaçant des commits.
- **Reflog** : Journal des modifications de références (branches, HEAD).
- **Remote** : Dépôt distant.
- **Repository** : Voir Dépôt.
- **Reset** : Réinitialisation de l'état du dépôt.
- **Revert** : Création d'un nouveau commit annulant des modifications précédentes.

## S
- **SHA-1** : Format de hachage utilisé pour identifier les commits.
- **Stash** : Zone temporaire pour stocker des modifications non commitées.
- **Staging Area** : Voir Index.
- **Submodule** : Dépôt Git imbriqué dans un autre dépôt.

## T
- **Tag** : Référence nommée et immuable vers un commit spécifique.
- **Tracking Branch** : Branche locale liée à une branche distante.
- **Tree** : Voir Arbre.

## U
- **Untracked** : Fichier non suivi par Git.
- **Upstream** : Voir Amont.

## W
- **Working Directory/Working Tree** : Répertoire de travail contenant les fichiers du projet.
- **Workflow** : Méthode d'organisation du travail avec Git.

## Symboles courants
- `^` : Référence au parent d'un commit (ex: HEAD^).
- `~n` : Référence au nième ancêtre (ex: HEAD~3).
- `@` : Alias pour HEAD.
- `--` : Séparateur entre options et noms de fichiers.