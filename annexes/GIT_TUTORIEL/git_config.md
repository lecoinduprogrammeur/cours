# $ git config

La commande `git config` est utilisée pour configurer les paramètres de Git. Elle est très polyvalente et permet de personnaliser de nombreux aspects du comportement de Git. 

**Niveaux de configuration** 

- `--system` : Applique à tous les utilisateurs du système
- `--global` : Applique à tous les dépôts de l'utilisateur actuel
- `--local` : Applique uniquement au dépôt courant (par défaut)

**Syntaxe de base** 

`git config [--global | --system | --local] <clé> <valeur>`

**Utilisations courantes** 

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

**Options utiles** 

- `--get` : Obtenir la valeur d'une clé
- `--unset` : Supprimer une entrée
- `--edit` : Ouvrir le fichier de configuration dans un éditeur

**Fichiers de configuration** 

- Système : `/etc/gitconfig`
- Global : `~/.gitconfig` ou `~/.config/git/config`
- Local : `.git/config` dans le dépôt

**Voici l'emplacement des différents fichiers de configuration Git sur Windows** 

1. Configuration Système (`--system`):
   ```
   C:\Program Files\Git\etc\gitconfig
   ```
   - Nécessite des droits administrateur pour modifier
   - Affecte tous les utilisateurs sur la machine
   - Parfois aussi dans : `C:\ProgramData\Git\config`

2. Configuration Globale (`--global`):
   ```
   C:\Users\<VotreNomUtilisateur>\.gitconfig
   ```
   ou
   ```
   %USERPROFILE%\.gitconfig
   ```
   - Spécifique à votre utilisateur
   - Affecte tous vos projets Git
   - Paramètres les plus couramment modifiés

3. Configuration Locale (`--local`):
   ```
   <CheminDuProjet>\.git\config
   ```
   - Dans le dossier du projet
   - Spécifique au projet en cours
   - Prioritaire sur les configurations système et globale

4. Pour vérifier les emplacements :
   ```bash
   # Voir toutes les configurations et leurs origines
   git config --list --show-origin
   
   # Voir le fichier de configuration système
   git config --list --system
   
   # Voir le fichier de configuration globale
   git config --list --global
   
   # Voir le fichier de configuration locale
   git config --list --local
   ```

5. Ordre de priorité (du plus prioritaire au moins prioritaire) :
   - Configuration locale (.git/config)
   - Configuration globale (~/.gitconfig)
   - Configuration système (gitconfig système)

6. Pour éditer directement les fichiers :
   ```bash
   # Configuration système (en admin)
   git config --system --edit
   
   # Configuration globale
   git config --global --edit
   
   # Configuration locale
   git config --local --edit
   ```

Il est recommandé d'utiliser les commandes `git config` plutôt que d'éditer directement ces fichiers pour éviter les erreurs de syntaxe.