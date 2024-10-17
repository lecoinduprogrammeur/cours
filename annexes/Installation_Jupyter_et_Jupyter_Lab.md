# Installation de Jupyter et Jupyter Lab

A la racine du dossier d'installation de Python où se trouve python.exe

```cmd
python -m pip install --upgrade pip
```

```cmd
pip install jupyter
```

Lancer Jupyter Notebook

```cmd
jupyter notebook
```

Pour changer le dossier de travail courant (racine) de Jupyter Notebook

```cmd
cd chemin\vers\votre\dossier
```

puis

```cmd
jupyter notebook
```

Méthode permanente :

```cmd
jupyter notebook --generate-config
```

Ouvrez le fichier de configuration (généralement situé à `C:\Users\VotreNom\\.jupyter\jupyter_notebook_config.py)

J'ai créé un dossier "jupyter" dans mon dossier "Documents"

```python
c.ServerApp.root_dir = 'C:/Users/Fabrice/Documents/jupyter'
```

Assurez-vous d'utiliser des barres obliques (/) ou des double anti-slashs (\) pour le chemin. d. Enregistrez le fichier et fermez-le.

C'est donc dans ce dossier, que Jupyter ou Jupyter Lab enregistreront vos notebooks.

Normalement, on peut aussi lancer jupyter lab

```cmd
jupyter lab
```

Installer Pandoc et  MiKTeX pour assurer les exports vers des formats 

Pandoc est un convertisseur universel de documents qui permet de transformer les notebooks Jupyter en divers formats comme PDF, HTML, ou LaTeX. Cela facilite le partage et la publication de vos travaux.

MiKTeX est une distribution LaTeX qui permet un rendu de haute qualité des équations mathématiques dans Jupyter. Cela est particulièrement utile pour les notebooks contenant des formules complexes.

La combinaison de Pandoc et MiKTeX permet d'exporter directement vos notebooks en PDF de qualité professionnelle, avec une mise en page et un formatage appropriés.

Mise à jour de MiKTeX : Assurez-vous que votre installation de MiKTeX est à jour. Les versions récentes peuvent inclure des optimisations de performance.

- Ouvrez MiKTeX Console
- Allez dans "Updates" et cliquez sur "Check for updates"
- Installez toutes les mises à jour disponibles

Installation des packages à la demande : Configurez MiKTeX pour installer les packages manquants automatiquement :

- Dans MiKTeX Console, allez dans "Settings"
- Sous "General", activez "Always install missing packages on-the-fly"

