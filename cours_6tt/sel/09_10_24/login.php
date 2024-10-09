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
	<div class="w3-container w3-margin w3-border entete_style">
		<h3 class="w3-opacity bold_style">LOGIN DES ETUDIANTS</h3>
	</div>
	<div class="w3-container">
		<form method="POST" action="./authentifier.php" class="w3-container">
			<h4 class="w3-text-dark-grey">Veuillez remplir les champs suivants :</h4>
			<br>
			<input class="w3-input" type="text" name="login">
			<label>LOGIN</label>
			<p>
			<input class="w3-input" type="password" name="password">
			<label>MOT DE PASSE</label>
			<p>
			</br>
			<button class="w3-btn w3-dark-grey" type="submit">Authentifier</button>
		</form> 
	</div>
</body>
</html>