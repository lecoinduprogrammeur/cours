# Guide : Environnements virtuels Python avec virtualenv

## 1. Installation de virtualenv

### A. Installation basique
```bash
# Installation de virtualenv
pip install virtualenv

# Vérification de l'installation
virtualenv --version
```

### B. Installation par système d'exploitation
```bash
# Windows
python -m pip install virtualenv

# Linux/Ubuntu
sudo apt-get update
sudo apt-get install python3-venv

# MacOS
pip3 install virtualenv
```

## 2. Création d'un environnement virtuel

### A. Structure de base
```bash
# Syntaxe de base
virtualenv nom_environnement

# Exemple
virtualenv mon_projet_env

# Avec Python spécifique
virtualenv -p python3.8 mon_projet_env
```

### B. Structure de dossier créée
```
mon_projet_env/
    ├── bin/           # Scripts d'activation (Unix)
    ├── Scripts/       # Scripts d'activation (Windows)
    ├── Lib/          # Bibliothèques Python
    └── Include/      # Headers C
```

## 3. Activation et désactivation

### A. Activation
```bash
# Windows
mon_projet_env\Scripts\activate

# Linux/MacOS
source mon_projet_env/bin/activate

# Vérification
# Le prompt devrait maintenant afficher (mon_projet_env)
```

### B. Désactivation
```bash
# Dans tous les systèmes
deactivate
```

## 4. Utilisation de base

### A. Installation de packages
```bash
# Après activation
(mon_projet_env) pip install requests
(mon_projet_env) pip install pandas numpy matplotlib

# Installation depuis requirements.txt
(mon_projet_env) pip install -r requirements.txt
```

### B. Gestion des packages
```bash
# Liste des packages installés
(mon_projet_env) pip list

# Créer requirements.txt
(mon_projet_env) pip freeze > requirements.txt

# Mettre à jour un package
(mon_projet_env) pip install --upgrade nom_package
```

## 5. Configuration avancée

### A. Options de création
```bash
# Créer avec des packages pré-installés
virtualenv --system-site-packages mon_env

# Spécifier la version Python
virtualenv -p /chemin/vers/python mon_env

# Sans pip
virtualenv --no-pip mon_env

# Avec prompts personnalisés
virtualenv --prompt="(mon-env)" mon_env
```

### B. Structure de projet
```
mon_projet/
    ├── mon_env/              # Environnement virtuel
    ├── src/                  # Code source
    ├── tests/                # Tests
    ├── requirements.txt      # Dépendances
    └── README.md            # Documentation
```

## 6. Bonnes pratiques

### A. Fichiers de configuration
```python
# requirements.txt
requests==2.26.0
pandas>=1.3.0
numpy>=1.21.0

# requirements-dev.txt
-r requirements.txt
pytest>=6.2.5
black>=21.9b0
flake8>=3.9.2
```

### B. Scripts utiles
```python
# activate_env.py
import os
import sys
import subprocess

def activate_env():
    """Active l'environnement virtuel."""
    if sys.platform == "win32":
        activate_script = "mon_env\\Scripts\\activate.bat"
    else:
        activate_script = "source mon_env/bin/activate"
    
    os.system(activate_script)

if __name__ == "__main__":
    activate_env()
```

## 7. Gestion de plusieurs environnements

### A. Organisation
```
environnements/
    ├── projet1_env/
    ├── projet2_env/
    └── projet3_env/
```

### B. Script de gestion
```python
# manage_envs.py
import os
import argparse
import virtualenv

def create_env(name):
    """Crée un nouvel environnement."""
    virtualenv.create_env(name)

def list_envs():
    """Liste les environnements disponibles."""
    envs_dir = "environnements"
    return [d for d in os.listdir(envs_dir)
            if os.path.isdir(os.path.join(envs_dir, d))]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["create", "list"])
    parser.add_argument("--name", help="Nom de l'environnement")
    
    args = parser.parse_args()
    
    if args.action == "create":
        create_env(args.name)
    elif args.action == "list":
        print("Environnements disponibles:")
        for env in list_envs():
            print(f"- {env}")

if __name__ == "__main__":
    main()
```

## 8. Diagnostic et résolution de problèmes

### A. Problèmes courants
```bash
# Réinitialiser un environnement
rm -rf mon_env
virtualenv mon_env

# Problèmes de permissions
virtualenv --user mon_env

# Conflits de packages
pip install --force-reinstall package_name
```

### B. Vérification de l'environnement
```python
# check_env.py
import sys
import os

def check_env():
    """Vérifie l'état de l'environnement virtuel."""
    # Vérifier si dans un env virtuel
    in_venv = hasattr(sys, 'real_prefix') or sys.base_prefix != sys.prefix
    
    print(f"Dans un environnement virtuel : {in_venv}")
    if in_venv:
        print(f"Chemin Python : {sys.executable}")
        print(f"Version Python : {sys.version}")
```

## Points importants à retenir :

1. Installation et création :
   - Installer virtualenv via pip
   - Créer un environnement pour chaque projet
   - Spécifier la version Python si nécessaire

2. Activation et utilisation :
   - Toujours activer l'environnement avant utilisation
   - Installer les packages après activation
   - Maintenir requirements.txt à jour

3. Bonnes pratiques :
   - Un environnement par projet
   - Documenter les dépendances
   - Utiliser des fichiers requirements séparés pour dev/prod

4. Gestion :
   - Vérifier régulièrement les packages installés
   - Nettoyer les environnements inutilisés
   - Garder les environnements à jour

