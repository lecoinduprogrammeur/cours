<?php
	$id=$_GET['id'];
	require_once ("securite.php");
	require_once ("connection_bdd.php");
	$ps=$pdo->prepare("SELECT * FROM etudiants_6tt WHERE ID=?");
	$params=array($id);
	$ps->execute($params);
	$etudiant=$ps->fetch();
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
	<div class="w3-container">
		<div class="w3-card-4 w3-light-grey w3-left w3-margin-right w3-cell" style="width:20%"> <!-- style="width:20%" id="hauteur"-->
    		<img src="./images/<?php echo($etudiant['PHOTO']) ?>" style="width:100%" >
    		<br>
      		<div class="w3-container w3-dark-grey">
      			<h5><b><?php echo ($etudiant['NOM']) ?></b></h5>
				<p><?php echo ($etudiant['PRENOM']) ?></p>
      			<p><?php echo ($etudiant['EMAIL']) ?></p>
    		</div>
  		</div>
  		<div class="w3-cell w3-padding">
  			<h5><b><?php echo ($etudiant['NOM']) ?></b></h5>
			<p><b><?php echo ($etudiant['PRENOM']) ?></b></p>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sit amet scelerisque orci, sit amet suscipit orci. Ut condimentum justo at dolor pharetra, sit amet interdum enim tincidunt. Pellentesque luctus interdum justo, semper facilisis mi molestie in. Praesent cursus viverra magna sed congue. Maecenas efficitur magna lacus, a vestibulum diam consectetur non. Maecenas pulvinar ac nisi varius vehicula. Curabitur at lacus in massa luctus placerat. Aliquam erat volutpat. Duis rutrum, nibh a aliquet varius, risus justo ultrices sapien, ut rhoncus ex massa et urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc id libero non turpis posuere sodales. In scelerisque luctus odio, non malesuada arcu hendrerit et.

				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sit amet scelerisque orci, sit amet suscipit orci. Ut condimentum justo at dolor pharetra, sit amet interdum enim tincidunt. Pellentesque luctus interdum justo, semper facilisis mi molestie in. Praesent cursus viverra magna sed congue. Maecenas efficitur magna lacus, a vestibulum diam consectetur non. Maecenas pulvinar ac nisi varius vehicula. Curabitur at lacus in massa luctus placerat. Aliquam erat volutpat. Duis rutrum, nibh a aliquet varius, risus justo ultrices sapien, ut rhoncus ex massa et urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc id libero non turpis posuere sodales. In scelerisque luctus odio, non malesuada arcu hendrerit et.

				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sit amet scelerisque orci, sit amet suscipit orci. Ut condimentum justo at dolor pharetra, sit amet interdum enim tincidunt. Pellentesque luctus interdum justo, semper facilisis mi molestie in. Praesent cursus viverra magna sed congue. Maecenas efficitur magna lacus, a vestibulum diam consectetur non. Maecenas pulvinar ac nisi varius vehicula. Curabitur at lacus in massa luctus placerat. Aliquam erat volutpat. Duis rutrum, nibh a aliquet varius, risus justo ultrices sapien, ut rhoncus ex massa et urna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc id libero non turpis posuere sodales. In scelerisque luctus odio, non malesuada arcu hendrerit et.
			</p>
		</div>
	</div>
</body>
</html>


