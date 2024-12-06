import os

def creer_table_des_matieres(repertoire):
    # Nom du fichier de table des matières
    fichier_tdm = os.path.join(repertoire, "table_des_matieres.md")
    
    # Ouvrir le fichier pour écrire
    with open(fichier_tdm, 'w', encoding='utf-8') as f_tdm:
        # Parcourir les fichiers du répertoire
        for fichier in sorted(os.listdir(repertoire)):
            if fichier.endswith(".md") and fichier != "table_des_matieres.md":
                chemin_fichier = os.path.join(repertoire, fichier)
                
                # Lire la première ligne du fichier Markdown
                with open(chemin_fichier, 'r', encoding='utf-8') as f_md:
                    premiere_ligne = f_md.readline().strip()
                
                # Ajouter l'entrée dans la table des matières
                titre = premiere_ligne if premiere_ligne else "Titre non défini"
                f_tdm.write(f"1. # **{fichier}**\n")
                f_tdm.write(f"   - #{titre}\n\n")
    
    print(f"Table des matières créée : {fichier_tdm}")

# Exemple d'utilisation
repertoire_cible = "./"  # Remplacez par le chemin de votre répertoire
creer_table_des_matieres(repertoire_cible)

