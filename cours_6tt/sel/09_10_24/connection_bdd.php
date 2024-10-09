<?php
try{
	$strConnection = 'mysql:host=localhost:3308;dbname=cardinal_final';
	$pdo = new PDO ($strConnection,"root","root");
}
catch (PDOException $e){
	$msg = 'Erreur PDO dans ' . $e->getMessage();
	die ($msg);
}
?>








