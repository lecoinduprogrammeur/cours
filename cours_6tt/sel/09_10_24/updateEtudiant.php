<?php
$id = $_POST['id'];
$nom = $_POST['nom'];
$prenom = $_POST['prenom'];
$age = $_POST[age];
$email = $_POST['email'];
$nomPhoto = $_FILES['photo']['name'];
require_once ("connection_bdd.php");
if($nomPhoto == "") {
	$ps = $pdo->prepare("UPDATE etudiants_6tt SET NOM=?,PRENOM=?,AGE=?,EMAIL=? WHERE ID=?");
	$params=array($nom,$prenom,$age,$email,$id);
	$ps->execute($params);
}
else {
	$fichierTempo=$_FILES['photo']['tmp_name'];
	move_uploaded_file($fichierTempo,"./images/$nomPhoto");
	$ps=$pdo->prepare("UPDATE etudiants_6tt SET NOM=?,PRENOM=?,AGE=?,EMAIL=?,PHOTO=? WHERE ID=?");
	$params=array($nom,$prenom,$age,$email,$nomPhoto,$id);
	$ps->execute($params);
}
header("location:accueil.php");
?>