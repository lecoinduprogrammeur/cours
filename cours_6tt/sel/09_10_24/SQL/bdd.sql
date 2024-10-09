-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.2.0 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour cardinal_final
CREATE DATABASE IF NOT EXISTS `cardinal_final` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `cardinal_final`;

-- Listage de la structure de la table cardinal_final. etudiants_6tt
CREATE TABLE IF NOT EXISTS `etudiants_6tt` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NOM` varchar(50) NOT NULL,
  `PRENOM` varchar(50) NOT NULL,
  `AGE` int NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `PHOTO` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table cardinal_final.etudiants_6tt : ~4 rows (environ)
INSERT INTO `etudiants_6tt` (`ID`, `NOM`, `PRENOM`, `AGE`, `EMAIL`, `PHOTO`) VALUES
	(5, 'Dumont', 'Fabrice', 48, 'fabricedumont@gmail.com', 'avatar2.jpg'),
	(6, 'Coca', 'Cola', 55, 'cocacola@gmail.com', 'avatar1.jpg'),
	(7, 'El Azouzzi', 'Ayoub', 28, 'elaz.ayoub@yahoo.fr', 'ayoub.jpg'),
	(8, 'Beloeil', 'Coralie', 22, 'beloeilcoralie@hotmail.com', 'coralie.jpg');

-- Listage de la structure de la table cardinal_final. messages
CREATE TABLE IF NOT EXISTS `messages` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ID_MEMBRE` int NOT NULL,
  `EMETTEUR` varchar(50) NOT NULL,
  `MESSAGE` text NOT NULL,
  `DESTINATAIRE` varchar(50) NOT NULL,
  `MOMENT` datetime NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_messages_etudiants_6tt` (`ID_MEMBRE`),
  CONSTRAINT `FK_messages_etudiants_6tt` FOREIGN KEY (`ID_MEMBRE`) REFERENCES `etudiants_6tt` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table cardinal_final.messages : ~4 rows (environ)
INSERT INTO `messages` (`ID`, `ID_MEMBRE`, `EMETTEUR`, `MESSAGE`, `DESTINATAIRE`, `MOMENT`) VALUES
	(2, 5, 'Dumont Fabrice', 'salut, tu vas bien ?', 'Coca Cola', '2018-06-02 15:49:34'),
	(3, 5, 'Dumont Fabrice', 'As-tu revu le cours de programmation ? Moi pas :-)', 'El Azouzzi Ayoub', '2018-06-02 16:17:24'),
	(4, 7, 'El Azouzzi Ayoub', 'J\'ai réussi mon examen !!!!!!! ', 'Dumont Fabrice', '2018-06-02 18:27:28'),
	(5, 6, 'Coca Cola', 'salut Fabrice !', 'Dumont Fabrice', '2024-04-22 12:48:22');

-- Listage de la structure de la table cardinal_final. users
CREATE TABLE IF NOT EXISTS `users` (
  `LOGIN` varchar(50) NOT NULL,
  `PASSWORD` varchar(50) NOT NULL,
  `ROLE` varchar(50) NOT NULL,
  PRIMARY KEY (`LOGIN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Listage des données de la table cardinal_final.users : ~3 rows (environ)
INSERT INTO `users` (`LOGIN`, `PASSWORD`, `ROLE`) VALUES
	('admin', '21232f297a57a5a743894a0e4a801fc3', 'boss'),
	('user', 'ee11cbb19052e40b07aac0ca060c23ee', 'nonboss'),
	('user2', '7e58d63b60197ceb55a1c487989a3720', 'nonboss');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
