# Guide d'installation de modules avec PIP

## 1. Introduction à PIP

PIP (Package Installer for Python) est le gestionnaire de paquets standard pour Python. Il permet d'installer et de gérer des packages Python supplémentaires.

### Vérification de l'installation de PIP
```bash
# Dans le terminal/invite de commandes
pip --version
# ou
python -m pip --version
```

## 2. Commandes de base

### A. Installation de packages
```bash
# Installation simple
pip install nom_du_package

# Exemple avec requests
pip install requests

# Installation d'une version spécifique
pip install requests==2.25.1

# Installation avec version minimale
pip install "requests>=2.25.0"

# Installation de plusieurs packages
pip install requests pandas numpy

# Installation depuis requirements.txt
pip install -r requirements.txt
```

### B. Désinstallation
```bash
# Désinstaller un package
pip uninstall nom_du_package

# Avec confirmation
pip uninstall -y nom_du_package
```

### C. Mise à jour
```bash
# Mise à jour d'un package
pip install --upgrade nom_du_package
# ou
pip install -U nom_du_package

# Mise à jour de pip lui-même
python -m pip install --upgrade pip
```

## 3. Gestion des dépendances

### A. Lister les packages installés
```bash
# Liste tous les packages
pip list

# Liste au format requirements
pip freeze

# Sauvegarder la liste dans un fichier
pip freeze > requirements.txt
```

### B. Fichier requirements.txt
```txt
# requirements.txt
requests==2.25.1
pandas>=1.2.0
numpy>=1.19.2
matplotlib>=3.3.0
```

## 4. Options avancées

### A. Installation en mode développement
```bash
# Installation éditable (pour développement)
pip install -e .

# Installation des dépendances de développement
pip install -e ".[dev]"
```

### B. Installation avec des options spécifiques
```bash
# Installation sans cache
pip install --no-cache-dir nom_du_package

# Installation en mode utilisateur
pip install --user nom_du_package

# Installation en ignorant les packages installés
pip install --ignore-installed nom_du_package
```

## 5. Environnements virtuels

### A. Création d'un environnement virtuel
```bash
# Création
python -m venv mon_env

# Activation (Windows)
mon_env\Scripts\activate

# Activation (Unix/MacOS)
source mon_env/bin/activate

# Désactivation
deactivate
```

### B. Installation dans un environnement virtuel
```bash
# Après activation
(mon_env) pip install requests
```

## 6. Bonnes pratiques

### A. Structure de projet
```
mon_projet/
    ├── requirements.txt
    ├── requirements-dev.txt
    ├── setup.py
    └── src/
```

### B. Différents fichiers de requirements
```txt
# requirements.txt - Dépendances de production
requests==2.25.1
pandas==1.2.0

# requirements-dev.txt - Dépendances de développement
-r requirements.txt
pytest>=6.0.0
black>=21.0.0
flake8>=3.9.0
```

## 7. Résolution des problèmes courants

### A. Erreurs courantes et solutions
```bash
# Erreur de permissions
# Solution: Utiliser --user
pip install --user nom_du_package

# Erreur de SSL
# Solution: Ignorer SSL
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org nom_du_package

# Conflit de versions
# Solution: Forcer la réinstallation
pip install --force-reinstall nom_du_package
```

### B. Nettoyage
```bash
# Nettoyer le cache
pip cache purge

# Désinstaller tous les packages
pip freeze | xargs pip uninstall -y
```

## 8. Commandes utiles supplémentaires

```bash
# Voir les détails d'un package
pip show nom_du_package

# Vérifier les dépendances
pip check

# Chercher des packages
pip search nom_du_package  # Note: peut ne pas fonctionner sur les versions récentes

# Lister les packages obsolètes
pip list --outdated
```

## Points importants à retenir :

1. Installation :
   - Toujours vérifier la version de pip
   - Utiliser des environnements virtuels
   - Spécifier les versions dans requirements.txt

2. Maintenance :
   - Mettre à jour régulièrement
   - Garder requirements.txt à jour
   - Nettoyer les packages inutilisés

3. Sécurité :
   - Vérifier les sources des packages
   - Maintenir pip à jour
   - Utiliser des versions spécifiques

4. Bonnes pratiques :
   - Documenter les dépendances
   - Utiliser des environnements virtuels
   - Séparer les dépendances de dev et prod

Pour installer un module spécifique, il suffit généralement de suivre ces étapes :

1. Ouvrir un terminal
2. (Optionnel) Activer l'environnement virtuel
3. Exécuter : `pip install nom_du_module`
4. Vérifier l'installation : `pip show nom_du_module`
