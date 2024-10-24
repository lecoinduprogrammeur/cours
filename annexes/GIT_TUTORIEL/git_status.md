# $ git status

La commande `git status` est un outil essentiel dans Git pour obtenir un aperçu de l'état actuel de votre répertoire de travail et de l'index.

**Fonction principale** 
Affiche l'état des fichiers dans le répertoire de travail et l'index par rapport à HEAD.

**Syntaxe de base** 
`git status`

**Informations fournies** 

- Branche courante
- État de la branche par rapport à son homologue distant (si configuré)
- Fichiers modifiés mais non indexés (not staged)
- Fichiers indexés prêts pour le commit (staged)
- Fichiers non suivis (untracked)

**Options utiles** 

- `-s` ou `--short` : Format de sortie court et plus concis
- `-b` : Affiche les informations de la branche en mode court
- `--ignored` : Affiche également les fichiers ignorés

**Exemples de sortie** 

- "Changes to be committed" : Fichiers dans l'index, prêts pour le commit
- "Changes not staged for commit" : Fichiers modifiés mais pas encore ajoutés à l'index
- "Untracked files" : Nouveaux fichiers non suivis par Git

**Utilisation pratique** 

- Vérifier l'état avant un `git add` ou un `git commit`
- S'assurer que tous les changements voulus sont inclus
- Identifier les fichiers qui ne sont pas encore suivis

**Interprétation des symboles (en mode court)** 

- `??` : Fichiers non suivis
- `A` : Nouveaux fichiers ajoutés à l'index
- `M` : Fichiers modifiés
- `D` : Fichiers supprimés

**Bonnes pratiques** 

- Utilisez fréquemment `git status` pour garder une vue d'ensemble de vos changements
- Combinez avec `git diff` pour voir les détails des modifications

**Exemple de commande et sortie** 

```bash
$ git status -s
M  README.md
?? nouveau_fichier.txt
```
Cela indique que README.md est modifié et indexé, et que nouveau_fichier.txt n'est pas suivi.

> [!TIP]
>
> `git status` est une commande très utile pour maintenir une compréhension claire de l'état de votre projet Git à tout moment. Elle aide à éviter les erreurs courantes comme oublier d'ajouter des fichiers ou commiter des changements non intentionnels.

