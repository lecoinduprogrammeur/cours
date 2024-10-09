<?php
	$id=$_GET['id'];
	require_once ("securite.php");
	require_once ("connection_bdd.php");
	$ps=$pdo->prepare("SELECT * FROM etudiants_6tt WHERE ID=?");
	$params=array($id);
	$ps->execute($params);
	$etudiant=$ps->fetch(); 
?>


<?php
	$req = "SELECT * FROM etudiants_6tt";
	$ps2 = $pdo->prepare($req); 
	$ps2->execute();
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
	<div class="w3-container w3-margin">
		<table class="w3-table-all w3-hoverable">
			<thead>
				<tr class="w3-grey">
					<th>ID</th><th>PRENOM</th><th>NOM</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td><?php echo($etudiant['ID']) ?></td>
					<td><?php echo($etudiant['PRENOM']) ?></td>
					<td><?php echo($etudiant['NOM']) ?></td>
				</tr>
			</tbody>
		</table>
	</div>
	<div class="w3-container w3-margin">
		<FORM method="post" action="./sauvegarde_message.php">
		<input class="w3-input" type="hidden" name="id" value="<?php echo ($etudiant['ID']) ?>">
		<input class="w3-input" type="hidden" name="emetteur" value="<?php echo($etudiant['NOM'].' '.$etudiant['PRENOM']) ?>">
		<p>
		<TEXTAREA name="message" rows=10 cols=100></TEXTAREA>
		<p>
		<label>Message</label>
		<p>
		@
		<select name="@id">
			<?php while ($etudiant=$ps2->fetch()) { ?>
				<?php if ($etudiant['ID']!=$id) { ?>
  					<option><?php echo($etudiant['NOM'].' '.$etudiant['PRENOM']) ?></option>
				<?php } ?>
  			<?php } ?>
		</select>
		<p>
		<button class="w3-btn w3-dark-grey" type="submit">Envoyer</button>
		</FORM>
	</div>
</body>
</html>





