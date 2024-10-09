<?php
	$nom = $_POST ['nom'];
	$prenom = $_POST ['prenom'];
	$age = $_POST [age];
	$email = $_POST ['email'];
	$photo = $_FILES ['photo'] ['name'];
	$fichierTempo=$_FILES['photo']['tmp_name'];
	move_uploaded_file($fichierTempo, "./images/$photo");

	require_once ("connection_bdd.php");
	// prepare statement
	$ps=$pdo->prepare("INSERT INTO etudiants_6tt (NOM,PRENOM,AGE,EMAIL,PHOTO) VALUES (?,?,?,?,?)");
	$params=array($nom,$prenom,$age,$email,$photo);
	$ps->execute($params);
	header("location:accueil.php");
?>