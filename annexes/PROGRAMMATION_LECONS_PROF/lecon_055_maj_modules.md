# Guide de mise à jour des modules Python

## 1. Commandes de base pour la mise à jour

### A. Mise à jour d'un module spécifique
```bash
# Syntaxe de base
pip install --upgrade nom_du_module
# ou version courte
pip install -U nom_du_module

# Exemple avec requests
pip install --upgrade requests

# Mise à jour vers une version spécifique
pip install requests==2.28.1
```

### B. Mise à jour de PIP lui-même
```bash
# Windows
python -m pip install --upgrade pip

# Linux/MacOS
pip install --upgrade pip
# ou
python3 -m pip install --upgrade pip
```

## 2. Vérification des modules à mettre à jour

### A. Liste des modules obsolètes
```bash
# Afficher tous les modules qui peuvent être mis à jour
pip list --outdated

# Format détaillé
pip list --outdated --format=columns

# Format JSON
pip list --outdated --format=json
```

### B. Vérification des versions
```bash
# Voir la version actuelle d'un module
pip show nom_du_module

# Exemple
pip show requests
```

## 3. Mise à jour multiple

### A. Mise à jour de tous les modules
```bash
# Windows (PowerShell)
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

# Linux/MacOS
pip list --outdated | cut -d ' ' -f 1 | xargs -n1 pip install -U

# Alternative plus sûre
pip list --outdated > modules_to_update.txt
# Puis examiner le fichier et mettre à jour manuellement
```

### B. Mise à jour depuis requirements.txt
```bash
# Mise à jour de toutes les dépendances listées
pip install -r requirements.txt --upgrade

# Mise à jour avec respect des versions minimales
pip install -r requirements.txt --upgrade-strategy eager
```

## 4. Gestion des dépendances lors des mises à jour

### A. Création d'un fichier de requirements à jour
```bash
# Générer un nouveau requirements.txt avec les versions actuelles
pip freeze > requirements.txt

# Avec exclusion de certains packages
pip freeze | grep -v "package_a_exclure" > requirements.txt
```

### B. Mise à jour avec gestion des conflits
```bash
# Installation avec résolution des dépendances
pip install --upgrade --use-feature=2020-resolver nom_du_module

# Force la réinstallation
pip install --force-reinstall nom_du_module
```

## 5. Bonnes pratiques

### A. Environnement virtuel
```bash
# Création d'un nouvel environnement pour tester les mises à jour
python -m venv test_env

# Activation (Windows)
test_env\Scripts\activate

# Activation (Unix/MacOS)
source test_env/bin/activate

# Installation et test des mises à jour
pip install -r requirements.txt --upgrade
```

### B. Sauvegarde avant mise à jour
```bash
# Sauvegarder les versions actuelles
pip freeze > requirements.backup.txt

# En cas de problème, restaurer
pip install -r requirements.backup.txt --force-reinstall
```

## 6. Scripts utiles

### A. Script de mise à jour sécurisée
```python
# update_packages.py
import subprocess
import sys

def update_package(package_name):
    """Met à jour un package et gère les erreurs."""
    try:
        subprocess.check_call([
            sys.executable, 
            "-m", 
            "pip", 
            "install", 
            "--upgrade", 
            package_name
        ])
        print(f"✓ {package_name} mis à jour avec succès")
    except subprocess.CalledProcessError:
        print(f"✗ Erreur lors de la mise à jour de {package_name}")

def main():
    # Liste des packages obsolètes
    result = subprocess.run([
        sys.executable, 
        "-m", 
        "pip", 
        "list", 
        "--outdated", 
        "--format=json"
    ], capture_output=True)
    
    packages = eval(result.stdout)
    
    for package in packages:
        name = package['name']
        current = package['version']
        latest = package['latest_version']
        print(f"\nMise à jour de {name} ({current} → {latest})")
        update_package(name)

if __name__ == "__main__":
    main()
```

### B. Script de backup et restauration
```python
# backup_restore.py
import subprocess
import datetime
import os

def backup_requirements():
    """Crée une sauvegarde des requirements actuels."""
    date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"requirements_backup_{date}.txt"
    
    subprocess.run([
        "pip", 
        "freeze", 
        ">", 
        backup_file
    ], shell=True)
    
    return backup_file

def restore_requirements(backup_file):
    """Restaure à partir d'une sauvegarde."""
    if os.path.exists(backup_file):
        subprocess.run([
            "pip", 
            "install", 
            "-r", 
            backup_file, 
            "--force-reinstall"
        ])
        print(f"Restauration depuis {backup_file} terminée")
    else:
        print("Fichier de sauvegarde non trouvé")
```

## 7. Points importants à retenir

1. Avant la mise à jour :
   - Faire une sauvegarde (pip freeze)
   - Vérifier les compatibilités
   - Utiliser un environnement virtuel pour les tests

2. Pendant la mise à jour :
   - Mettre à jour un module à la fois
   - Vérifier les messages d'erreur
   - Tester après chaque mise à jour importante

3. Après la mise à jour :
   - Mettre à jour requirements.txt
   - Tester l'application
   - Documenter les changements

4. Bonnes pratiques :
   - Mettre à jour régulièrement
   - Garder PIP à jour
   - Maintenir une liste des dépendances à jour
   - Tester dans un environnement isolé

## 8. Commandes à retenir

```bash
# Vérifier les modules obsolètes
pip list --outdated

# Mettre à jour un module
pip install --upgrade nom_du_module

# Sauvegarder l'état actuel
pip freeze > backup.txt

# Mettre à jour tous les modules (avec précaution)
pip list --outdated | cut -d ' ' -f 1 | xargs -n1 pip install -U
```

