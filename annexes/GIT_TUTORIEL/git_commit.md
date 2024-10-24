# $ git commit

La commande `git commit` est une opération fondamentale dans Git, utilisée pour enregistrer les modifications préparées dans l'index (staging area) dans l'historique du dépôt.

**Fonction principale** 
Crée un nouveau commit contenant les changements actuellement dans l'index, avec un message décrivant ces changements.

**Syntaxe de base** 
`git commit`

**Options courantes** 

- `-m "message"` : Permet de spécifier le message de commit directement dans la ligne de commande.
- `-a` : Ajoute automatiquement tous les fichiers modifiés (mais pas les nouveaux fichiers) à l'index avant de faire le commit.
- `--amend` : Modifie le dernier commit au lieu d'en créer un nouveau.

**Exemples d'utilisation** 

- `git commit -m "Ajout de la fonctionnalité X"`
- `git commit -am "Correction de bugs dans le module Y"`
- `git commit --amend`

**Comportement** 

- Ouvre un éditeur de texte pour saisir le message de commit si `-m` n'est pas utilisé.
- Crée un nouveau point dans l'historique du projet avec un identifiant unique (hash SHA-1).
- Enregistre l'auteur, la date, et le message du commit.

**Bonnes pratiques pour les messages de commit** 

- Utilisez une première ligne courte (50 caractères max) résumant les changements.
- Laissez une ligne vide après la première ligne.
- Ajoutez des détails supplémentaires si nécessaire dans les lignes suivantes.

**Points importants** 

- Un commit ne modifie que l'historique local jusqu'à ce qu'il soit poussé vers un dépôt distant.
- Les commits sont la base pour suivre l'évolution du projet et collaborer avec d'autres.

**Cas particuliers** 

- `git commit --allow-empty` : Crée un commit vide, utile pour déclencher des CI/CD pipelines.
- `git commit --date="date"` : Permet de spécifier une date personnalisée pour le commit.

**Vérification** 

- Utilisez `git log` pour voir l'historique des commits après avoir effectué un commit.

La commande `git commit` est cruciale dans le flux de travail Git, car elle crée des points de sauvegarde dans l'historique du projet. Elle permet de garder une trace claire et organisée des changements apportés au fil du temps.