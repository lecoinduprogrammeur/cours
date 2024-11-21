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


-- Listage de la structure de la base pour club_de_football_cardinal_mercier_2
CREATE DATABASE IF NOT EXISTS `club_de_football_cardinal_mercier_2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `club_de_football_cardinal_mercier_2`;

-- Listage de la structure de la table club_de_football_cardinal_mercier_2. joueurs
CREATE TABLE IF NOT EXISTS `joueurs` (
  `id_joueur` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `poste` varchar(30) NOT NULL,
  PRIMARY KEY (`id_joueur`),
  KEY `nom` (`nom`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table club_de_football_cardinal_mercier_2.joueurs : ~24 rows (environ)
INSERT INTO `joueurs` (`id_joueur`, `nom`, `prenom`, `age`, `poste`) VALUES
	(1, 'Dupont', 'Jean', 24, 'Attaquant'),
	(2, 'Martin', 'Luc', 22, 'Défenseur'),
	(3, 'Durand', 'Pierre', 28, 'Milieu de terrain'),
	(4, 'Leroy', 'Maxime', 25, 'Gardien'),
	(5, 'Moreau', 'Sébastien', 23, 'Attaquant'),
	(6, 'Bernard', 'Louis', 27, 'Défenseur'),
	(7, 'Guerin', 'Nicolas', 21, 'Milieu de terrain'),
	(8, 'Rousseau', 'Alexandre', 26, 'Défenseur'),
	(9, 'Fournier', 'Mathieu', 24, 'Milieu de terrain'),
	(10, 'Girard', 'Thomas', 22, 'Attaquant'),
	(11, 'Perrin', 'Hugo', 29, 'Défenseur'),
	(12, 'Dumont', 'Clément', 20, 'Milieu de terrain'),
	(13, 'Faure', 'Julien', 23, 'Attaquant'),
	(14, 'Chevalier', 'Damien', 25, 'Défenseur'),
	(15, 'Barbier', 'Adrien', 24, 'Milieu de terrain'),
	(16, 'Lemoine', 'Baptiste', 26, 'Attaquant'),
	(17, 'Renard', 'Florian', 22, 'Défenseur'),
	(18, 'Picard', 'Vincent', 27, 'Milieu de terrain'),
	(19, 'Marchand', 'Quentin', 21, 'Attaquant'),
	(20, 'Leduc', 'Romain', 23, 'Défenseur'),
	(21, 'Bensalah', 'Youssef', 24, 'Milieu de terrain'),
	(22, 'El-Mansouri', 'Karim', 22, 'Attaquant'),
	(23, 'Haddad', 'Rachid', 28, 'Défenseur'),
	(24, 'Zaidi', 'Amine', 25, 'Gardien');

-- Listage de la structure de la table club_de_football_cardinal_mercier_2. matchs
CREATE TABLE IF NOT EXISTS `matchs` (
  `id_match` int NOT NULL AUTO_INCREMENT,
  `date_match` date NOT NULL,
  `adversaire` varchar(50) NOT NULL,
  PRIMARY KEY (`id_match`),
  KEY `adversaire` (`adversaire`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table club_de_football_cardinal_mercier_2.matchs : ~10 rows (environ)
INSERT INTO `matchs` (`id_match`, `date_match`, `adversaire`) VALUES
	(1, '2024-11-10', 'Club Bruges'),
	(2, '2024-11-17', 'Anderlecht'),
	(3, '2024-11-24', 'Standard Liège'),
	(4, '2024-12-01', 'Genk'),
	(5, '2024-12-08', 'La Gantoise'),
	(6, '2024-12-15', 'Charleroi'),
	(7, '2024-12-22', 'KV Ostende'),
	(8, '2025-01-05', 'Zulte Waregem'),
	(9, '2025-01-12', 'Cercle Bruges'),
	(10, '2025-01-19', 'Eupen');

-- Listage de la structure de la table club_de_football_cardinal_mercier_2. selection_joueurs
CREATE TABLE IF NOT EXISTS `selection_joueurs` (
  `id_selection` int NOT NULL AUTO_INCREMENT,
  `nom_joueur` varchar(50) DEFAULT NULL,
  `nom_adversaire` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_selection`),
  KEY `id_joueur` (`nom_joueur`) USING BTREE,
  KEY `id_match` (`nom_adversaire`) USING BTREE,
  CONSTRAINT `FK_selection_joueurs_joueurs` FOREIGN KEY (`nom_joueur`) REFERENCES `joueurs` (`nom`),
  CONSTRAINT `FK_selection_joueurs_matchs` FOREIGN KEY (`nom_adversaire`) REFERENCES `matchs` (`adversaire`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table club_de_football_cardinal_mercier_2.selection_joueurs : ~2 rows (environ)
INSERT INTO `selection_joueurs` (`id_selection`, `nom_joueur`, `nom_adversaire`) VALUES
	(4, 'Barbier', 'Anderlecht'),
	(5, 'Lemoine', 'Anderlecht');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
