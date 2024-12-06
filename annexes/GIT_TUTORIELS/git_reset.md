# $ git reset

[Retour Git Commandes](./git_commandes.md)

La commande `git reset` est un outil puissant et flexible utilisé pour annuler ou ajuster des changements dans Git. Elle peut modifier l'état de l'index (staging area) et, dans certains cas, l'historique des commits.

**Fonction principale** 
Réinitialise l'état actuel de HEAD à un état spécifié.

**Syntaxe de base** 
`git reset [<mode>] [<commit>]`

**Modes principaux** 
a. Soft (`--soft`) :

   - Déplace HEAD vers le commit spécifié.
   - Ne modifie pas l'index ni le répertoire de travail.
   - Utile pour regrouper plusieurs commits.

b. Mixed (`--mixed`, mode par défaut) :
   - Déplace HEAD et réinitialise l'index.
   - Ne modifie pas le répertoire de travail.
   - Utile pour annuler des changements dans l'index.

c. Hard (`--hard`) :
   - Déplace HEAD, réinitialise l'index et le répertoire de travail.
   - Attention : peut entraîner une perte de travail non commité.

**Utilisations courantes** 

- `git reset HEAD~1` : Annule le dernier commit (mode mixed par défaut).
- `git reset --soft HEAD~3` : Regroupe les 3 derniers commits.
- `git reset --hard origin/master` : Réinitialise la branche locale à l'état du dépôt distant.
- `git reset -- fichier.txt` : Retire un fichier spécifique de l'index.

**Points importants** 

- Peut modifier l'historique des commits, utilisez avec précaution sur des branches partagées.
- `git reset` sans arguments réinitialise tous les fichiers dans l'index.

**Cas d'utilisation** 

- Annuler des commits locaux non poussés.
- Nettoyer l'index avant un nouveau commit.
- Ajuster l'historique local des commits.

**Alternatives et comparaisons** 

- `git revert` : Crée un nouveau commit qui annule les changements d'un commit précédent.
- `git checkout` : Pour annuler des modifications dans le répertoire de travail sans toucher à l'index.

**Précautions** 

- Utilisez `git reflog` pour récupérer des commits "perdus" après un reset dur.
- Évitez d'utiliser `--hard` sur des changements non commités que vous voulez conserver.

**Exemple avancé** 
`git reset --soft HEAD~3 && git commit` : Combine les 3 derniers commits en un seul.

> [!WARNING]
>
> La commande `git reset` est un outil puissant pour gérer l'historique et l'état de votre dépôt Git. Elle offre une grande flexibilité mais doit être utilisée avec précaution, particulièrement lors de la modification de l'historique des commits.

