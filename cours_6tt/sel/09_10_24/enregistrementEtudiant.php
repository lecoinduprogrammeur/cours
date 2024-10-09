<?php
require_once ("securite.php");
?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="./css/w3.css">
	<link rel="stylesheet" type="text/css" href="./css/monStyle.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
	<?php require_once("entete_site.php") ?>
	<div class="w3-container w3-margin w3-border entete_style">
		<h3 class="w3-opacity bold_style">ENREGISTREMENT DES ETUDIANTS</h3>
	</div>
	<div class="w3-container">
		<form method="POST" action="./sauvegardeEtudiant.php" enctype="multipart/form-data" class="w3-container">
			<h4 class="w3-text-dark-grey">Veuillez remplir les champs suivants :</h4>
			<br>
			<input class="w3-input" type="text" name="nom">
			<label>NOM</label>
			<p>
			<input class="w3-input" type="text" name="prenom">
			<label>PRENOM</label>
			<p>
			<input class="w3-input" type="number" name="age">
			<label>AGE</label>
			<p>
			<input class="w3-input" type="text" name="email">
			<label>EMAIL</label>
			<p>
			<h4 class="w3-text-dark-grey">Veuillez choisir une photo :</h4>
			</br>
			<div class="w3-container w3-border entete_style">
			<input class="w3-input" type="file" name="photo">
			<label>PHOTO</label>
			</div>
			<p>
			</br>
			<button class="w3-btn w3-dark-grey" type="submit">Enregistrer</button>
		</form> 
	</div>
</body>
</html>