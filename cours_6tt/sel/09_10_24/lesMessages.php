<?php
	require_once ("securite.php");
	require_once ("connection_bdd.php");
	$req = "SELECT * FROM etudiants_6tt LEFT JOIN messages ON etudiants_6tt.ID = messages.ID_MEMBRE";
	$ps = $pdo->prepare($req);
	$ps->execute();
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
		<h3 class="w3-opacity bold_style">LISTE DES MESSAGES DES ETUDIANTS DE 6TT</h3>
	</div>
	<div class="w3-container">
	<table class="w3-table-all w3-hoverable">
		<thead>
			<tr class="w3-grey">
				<th>ID</th><th>EMETTEUR</th><th>MESSAGE</th><th>DESTINATAIRE</th><th>DATE D'ENVOI</th>
			</tr>
		</thead>
		<tbody>
		<?php while ($lesMessages=$ps->fetch()) { ?>
			<tr>
				<td><?php echo($lesMessages['ID']) ?></td>
				<td><?php echo($lesMessages['EMETTEUR']) ?></td>
				<td><?php echo($lesMessages['MESSAGE']) ?></td>
				<td><?php echo($lesMessages['DESTINATAIRE']) ?></td>
				<td><?php echo($lesMessages['MOMENT']) ?></td>
			</tr>
		<?php } ?>
		</tbody>
	</table>
	</div>
</body>
</html>