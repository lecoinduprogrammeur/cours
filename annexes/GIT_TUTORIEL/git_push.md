# $ git push

[Retour Git Commandes](./git_commandes.md)

La commande `git push` est utilisée pour envoyer les commits locaux vers un dépôt distant.

**Fonction principale** 
Envoie les commits de votre branche locale vers une branche du dépôt distant.

**Syntaxe de base** 

- `git push <remote> <branche>`
- `git push origin main` (cas le plus courant)

**Options courantes** 

- `--all` : Pousse toutes les branches
- `-u` ou `--set-upstream` : Définit la branche distante comme référence pour la branche locale
- `--force` ou `-f` : Force le push (à utiliser avec précaution)
- `--tags` : Pousse les tags

**Cas d'utilisation** 

```bash
# Push basique
git push origin main

# Premier push d'une nouvelle branche
git push -u origin nouvelle-branche

# Pousser toutes les branches
git push --all origin

# Pousser les tags
git push --tags
```

**Points importants** 

- Nécessite des droits d'accès au dépôt distant
- Les commits doivent d'abord être faits localement
- Git vérifie que le push ne crée pas de conflits

**Messages d'erreur courants** 

- "rejected" : Le dépôt distant a des changements que vous n'avez pas localement
- "non-fast-forward" : Nécessite un pull avant de pouvoir push

**Bonnes pratiques** 

- Toujours faire un `git pull` avant un push
- Éviter `--force` sur des branches partagées
- Vérifier l'état avec `git status` avant de push

**Scénarios spéciaux** 

- Push d'une branche locale vers une branche distante différente :
  `git push origin branche-locale:branche-distante`
- Supprimer une branche distante :
  `git push origin --delete nom-branche`

**Sécurité** 

- Attention avec `--force` qui peut écraser l'historique distant
- Vérifiez toujours la branche cible avant de push
- Utilisez des tokens d'accès ou SSH pour l'authentification

**Workflow typique** 

```bash
git status          # Vérifier l'état
git pull           # Récupérer les changements distants
git push           # Envoyer les changements
```

La commande `git push` est essentielle pour la collaboration, car elle permet de partager vos changements avec le reste de l'équipe via le dépôt distant.