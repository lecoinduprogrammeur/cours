# $ git config

La commande `git config` est utilisée pour configurer les paramètres de Git. Elle est très polyvalente et permet de personnaliser de nombreux aspects du comportement de Git. 

1. Niveaux de configuration :
   - `--system` : Applique à tous les utilisateurs du système
   - `--global` : Applique à tous les dépôts de l'utilisateur actuel
   - `--local` : Applique uniquement au dépôt courant (par défaut)

2. Syntaxe de base :
   `git config [--global | --system | --local] <clé> <valeur>`

3. Utilisations courantes :

   a. Configurer l'identité :
      ```
      git config --global user.name "Votre Nom"
      git config --global user.email "votre@email.com"
      ```

   b. Configurer l'éditeur par défaut :
      ```
      git config --global core.editor "code --wait"  # Pour VS Code
      ```

   c. Afficher une configuration :
      ```
      git config user.name
      git config --list
      ```

4. Options utiles :
   - `--get` : Obtenir la valeur d'une clé
   - `--unset` : Supprimer une entrée
   - `--edit` : Ouvrir le fichier de configuration dans un éditeur

5. Fichiers de configuration :
   - Système : `/etc/gitconfig`
   - Global : `~/.gitconfig` ou `~/.config/git/config`
   - Local : `.git/config` dans le dépôt

6. Exemples avancés :
   - Configurer des alias :
     ```
     git config --global alias.co checkout
     git config --global alias.br branch
     ```
   - Configurer la fusion par défaut :
     ```
     git config --global merge.conflictstyle diff3
     ```

7. Bonnes pratiques :
   - Utilisez `--global` pour les configurations personnelles
   - Utilisez `--local` pour les configurations spécifiques à un projet

8. Vérification de la configuration :
   ```
   git config --list --show-origin
   ```

La commande `git config` est essentielle pour personnaliser votre environnement Git et adapter son comportement à vos besoins ou aux exigences d'un projet spécifique. Elle est souvent utilisée lors de la première installation de Git et lors de la configuration de nouveaux environnements de développement.