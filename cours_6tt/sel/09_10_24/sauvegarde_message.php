<?php
	$id = $_POST ['id'];
	$emetteur=$_POST['emetteur'];
	$message = $_POST ['message'];
	$dest = $_POST ['@id'];
	$moment = date("Y-m-d H:i:s");
	
	require_once ("connection_bdd.php");
	// prepare statement
	$ps=$pdo->prepare("INSERT INTO messages (ID_MEMBRE,EMETTEUR,MESSAGE,DESTINATAIRE,MOMENT) VALUES (?,?,?,?,?)");
	$params=array($id,$emetteur,$message,$dest,$moment);
	$ps->execute($params);
	header("location:accueil.php");
	//header("location:enregistrementEtudiant.php");
?>