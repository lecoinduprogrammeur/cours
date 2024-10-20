# $ git add

La commande `git add` est une commande fondamentale dans Git, utilisée pour ajouter des modifications à l'index (aussi appelé "staging area").

1. Fonction principale :
   Prépare les fichiers pour le prochain commit en les ajoutant à l'index.

2. Syntaxe de base :
   `git add <fichier(s) ou répertoire(s)>`

3. Utilisations courantes :
   - `git add fichier.txt` : Ajoute un fichier spécifique à l'index.
   - `git add .` : Ajoute tous les fichiers modifiés et nouveaux du répertoire courant et ses sous-répertoires.
   - `git add *.js` : Ajoute tous les fichiers JavaScript modifiés.
   - `git add dossier/` : Ajoute tous les fichiers modifiés dans le dossier spécifié.

4. Options utiles :
   - `-p` ou `--patch` : Permet d'ajouter des parties spécifiques d'un fichier de manière interactive.
   - `-u` : Met à jour l'index avec les fichiers modifiés ou supprimés, mais n'ajoute pas de nouveaux fichiers.
   - `-A` ou `--all` : Ajoute, modifie et supprime les fichiers indexés pour correspondre au répertoire de travail.

5. Comportement :
   - Pour les nouveaux fichiers, `git add` les fait suivre par Git.
   - Pour les fichiers modifiés, `git add` met à jour l'index avec les nouvelles modifications.
   - N'affecte pas directement le dépôt jusqu'à ce qu'un commit soit effectué.

6. Points importants :
   - Les fichiers ajoutés à l'index sont préparés pour le prochain commit.
   - Vous pouvez ajouter des fichiers plusieurs fois avant de faire un commit si vous faites des modifications supplémentaires.
   - `git add` ne modifie pas l'historique du projet.

7. Bonnes pratiques :
   - Utilisez `git status` avant et après `git add` pour vérifier l'état de vos fichiers.
   - Ajoutez les fichiers de manière logique et groupée pour créer des commits cohérents.

8. Cas particuliers :
   - Pour retirer un fichier de l'index sans perdre les modifications, utilisez `git reset <fichier>`.

La commande `git add` est essentielle dans le flux de travail Git, permettant de contrôler précisément quelles modifications seront incluses dans le prochain commit. Elle offre une grande flexibilité dans la gestion des changements avant de les valider dans l'historique du projet.