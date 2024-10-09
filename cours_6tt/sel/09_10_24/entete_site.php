<?php
require_once ("securite.php");
?>
<div class="class=w3-bar w3-border w3-light-grey w3-margin w3-card-4"> 
	<a href="accueil.php" class="w3-bar-item w3-button bold_style"><i class="fa fa-home"></i></a>
	<?php if ($_SESSION['PROFILE']['ROLE']=='boss'){ ?>
	<a href="enregistrementEtudiant.php" class="w3-bar-item w3-button w3-hover-dark-grey">Enregistrement Etudiant</a>
	<?php } ?>
	<a href="lesMessages.php" class="w3-bar-item w3-button w3-hover-dark-grey">Les Messages</a>
	<a href="logout.php" class="w3-bar-item w3-button w3-hover-dark-grey w3-right">Déconnection</a>
</div> 
