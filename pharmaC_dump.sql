-- MySQL dump 10.13  Distrib 8.0.29, for macos12 (x86_64)
--
-- Host: localhost    Database: pharmaC
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!50606 SET @OLD_INNODB_STATS_AUTO_RECALC=@@INNODB_STATS_AUTO_RECALC */;
/*!50606 SET GLOBAL INNODB_STATS_AUTO_RECALC=OFF */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `pharmaC`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `pharmaC` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `pharmaC`;

--
-- Table structure for table `Cart`
--

DROP TABLE IF EXISTS `Cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cart` (
  `Item_id` int NOT NULL,
  `Item_qty` int NOT NULL,
  `Order_id` int NOT NULL,
  `Item_price` int NOT NULL,
  PRIMARY KEY (`Item_id`),
  KEY `Price_idx` (`Item_price`),
  KEY `Order_id_idx` (`Order_id`),
  CONSTRAINT `Med_id` FOREIGN KEY (`Item_id`) REFERENCES `Medicine` (`Med_id`),
  CONSTRAINT `Order_id` FOREIGN KEY (`Order_id`) REFERENCES `Orders` (`Order_id`),
  CONSTRAINT `Price` FOREIGN KEY (`Item_price`) REFERENCES `Medicine` (`Med_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cart`
--

LOCK TABLES `Cart` WRITE;
/*!40000 ALTER TABLE `Cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `Cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `Customer_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `address` varchar(600) NOT NULL,
  PRIMARY KEY (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Doctor`
--

DROP TABLE IF EXISTS `Doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Doctor` (
  `doc_name` varchar(100) NOT NULL,
  `shift` enum('Morning','Night') DEFAULT NULL,
  `username` varchar(10) NOT NULL,
  `_password_` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `clock_in` datetime DEFAULT NULL,
  `clock_out` datetime DEFAULT NULL,
  PRIMARY KEY (`doc_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Doctor`
--

LOCK TABLES `Doctor` WRITE;
/*!40000 ALTER TABLE `Doctor` DISABLE KEYS */;
INSERT INTO `Doctor` VALUES ('Ahmed Allam',NULL,'ahmed11','1234',NULL,NULL),('Hassan Allam',NULL,'hassan99','1111',NULL,NULL),('Mayar Allam',NULL,'mayar25','9911',NULL,NULL);
/*!40000 ALTER TABLE `Doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medicine`
--

DROP TABLE IF EXISTS `Medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medicine` (
  `Med_id` int NOT NULL AUTO_INCREMENT,
  `Med_name` varchar(300) NOT NULL,
  `Form` enum('Tablet','Syrup','Effervescent','Drops','Spray','Ointment/Cream','Ampoule','Other') NOT NULL,
  `Treatment` varchar(400) NOT NULL,
  `Price` float NOT NULL,
  `Stock` int NOT NULL,
  `Expiry` date DEFAULT NULL,
  `Supplier` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Med_id`),
  KEY `Supplier_idx` (`Supplier`),
  CONSTRAINT `Supplier_name` FOREIGN KEY (`Supplier`) REFERENCES `Supplier` (`Supplier_name`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medicine`
--

LOCK TABLES `Medicine` WRITE;
/*!40000 ALTER TABLE `Medicine` DISABLE KEYS */;
INSERT INTO `Medicine` VALUES (7,'Corasore','Drops','Hypotension',16,40,'2025-12-03',NULL),(8,'Telfast','Tablet','Allergic Rhinitis',40,35,'2023-11-11',NULL),(9,'Brufen','Tablet','Painkiller',32,57,'2022-10-06',NULL),(10,'Congestal','Syrup','Influenza',10.5,61,'2023-11-26',NULL),(11,'Fucicort','Ointment/Cream','Antibiotic',30.5,41,'2023-03-30',NULL),(12,'Voltaren','Ointment/Cream','Muscle Pain Relief',44.75,50,'2024-07-02',NULL),(13,'Oral-B Toothbrush','Other','Oral Care',32,18,NULL,NULL),(14,'Syringue','Other','Injection equipment',4,30,NULL,NULL),(15,'Ferroglobin','Syrup','Iron supplement',30,24,NULL,NULL),(16,'Otrivin','Spray','Nasal decongestant',10,32,NULL,NULL),(17,'Pridocaine','Ointment/Cream','Local anaesthetic',13.5,50,NULL,NULL),(18,'EasyCare Ethyl Alcohol','Other','Disinfectant',17,63,NULL,NULL),(19,'Depovit','Ampoule','B12 Vitamin',35.25,10,NULL,NULL),(20,'La roche posay sunscreen','Ointment/Cream','Sun protection',379,0,NULL,NULL),(21,'Pantene 2 in 1','Other','Hair care',80,9,NULL,NULL),(22,'Mebo','Ointment/Cream','Skin burns',73,40,NULL,NULL),(23,'Surgical Masks Pack x35','Other','Infection control',50,94,NULL,NULL),(24,'Plaster','Other','Skin wounds',10,20,NULL,NULL),(25,'Molfex infant diapers','Other','Child care',122,27,NULL,NULL);
/*!40000 ALTER TABLE `Medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `Order_id` int NOT NULL AUTO_INCREMENT,
  `Time_` timestamp NOT NULL,
  `Total` float NOT NULL,
  `Payment` enum('cash','credit card') NOT NULL,
  `Customer` int NOT NULL,
  `Type` enum('In store','Delivery') NOT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `Customer_id_idx` (`Customer`),
  CONSTRAINT `Customer_id` FOREIGN KEY (`Customer`) REFERENCES `Customer` (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Supplier`
--

DROP TABLE IF EXISTS `Supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Supplier` (
  `Supplier_name` varchar(100) NOT NULL,
  `Contact` varchar(21) NOT NULL,
  `Med_name` varchar(300) NOT NULL,
  PRIMARY KEY (`Supplier_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Supplier`
--

LOCK TABLES `Supplier` WRITE;
/*!40000 ALTER TABLE `Supplier` DISABLE KEYS */;
INSERT INTO `Supplier` VALUES ('AMRIYA PHARM. IND.','034700083','Depovit'),('Gulf Pharmaceutical Industries','+962797555329','Mebo'),('La roche posay','1-800-560-1803','La roche posay sunscreen'),('Procter & Gamble','1-800-945-7768','Pantene 2 in 1');
/*!40000 ALTER TABLE `Supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!50606 SET GLOBAL INNODB_STATS_AUTO_RECALC=@OLD_INNODB_STATS_AUTO_RECALC */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-08  2:04:52
