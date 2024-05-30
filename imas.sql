-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: imas
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add auth group',7,'add_authgroup'),(26,'Can change auth group',7,'change_authgroup'),(27,'Can delete auth group',7,'delete_authgroup'),(28,'Can view auth group',7,'view_authgroup'),(29,'Can add auth group permissions',8,'add_authgrouppermissions'),(30,'Can change auth group permissions',8,'change_authgrouppermissions'),(31,'Can delete auth group permissions',8,'delete_authgrouppermissions'),(32,'Can view auth group permissions',8,'view_authgrouppermissions'),(33,'Can add auth permission',9,'add_authpermission'),(34,'Can change auth permission',9,'change_authpermission'),(35,'Can delete auth permission',9,'delete_authpermission'),(36,'Can view auth permission',9,'view_authpermission'),(37,'Can add auth user',10,'add_authuser'),(38,'Can change auth user',10,'change_authuser'),(39,'Can delete auth user',10,'delete_authuser'),(40,'Can view auth user',10,'view_authuser'),(41,'Can add auth user groups',11,'add_authusergroups'),(42,'Can change auth user groups',11,'change_authusergroups'),(43,'Can delete auth user groups',11,'delete_authusergroups'),(44,'Can view auth user groups',11,'view_authusergroups'),(45,'Can add auth user user permissions',12,'add_authuseruserpermissions'),(46,'Can change auth user user permissions',12,'change_authuseruserpermissions'),(47,'Can delete auth user user permissions',12,'delete_authuseruserpermissions'),(48,'Can view auth user user permissions',12,'view_authuseruserpermissions'),(49,'Can add auto answer task',13,'add_autoanswertask'),(50,'Can change auto answer task',13,'change_autoanswertask'),(51,'Can delete auto answer task',13,'delete_autoanswertask'),(52,'Can view auto answer task',13,'view_autoanswertask'),(53,'Can add dataset',14,'add_dataset'),(54,'Can change dataset',14,'change_dataset'),(55,'Can delete dataset',14,'delete_dataset'),(56,'Can view dataset',14,'view_dataset'),(57,'Can add deep learning model',15,'add_deeplearningmodel'),(58,'Can change deep learning model',15,'change_deeplearningmodel'),(59,'Can delete deep learning model',15,'delete_deeplearningmodel'),(60,'Can view deep learning model',15,'view_deeplearningmodel'),(61,'Can add department',16,'add_department'),(62,'Can change department',16,'change_department'),(63,'Can delete department',16,'delete_department'),(64,'Can view department',16,'view_department'),(65,'Can add django admin log',17,'add_djangoadminlog'),(66,'Can change django admin log',17,'change_djangoadminlog'),(67,'Can delete django admin log',17,'delete_djangoadminlog'),(68,'Can view django admin log',17,'view_djangoadminlog'),(69,'Can add django content type',18,'add_djangocontenttype'),(70,'Can change django content type',18,'change_djangocontenttype'),(71,'Can delete django content type',18,'delete_djangocontenttype'),(72,'Can view django content type',18,'view_djangocontenttype'),(73,'Can add django migrations',19,'add_djangomigrations'),(74,'Can change django migrations',19,'change_djangomigrations'),(75,'Can delete django migrations',19,'delete_djangomigrations'),(76,'Can view django migrations',19,'view_djangomigrations'),(77,'Can add django session',20,'add_djangosession'),(78,'Can change django session',20,'change_djangosession'),(79,'Can delete django session',20,'delete_djangosession'),(80,'Can view django session',20,'view_djangosession'),(81,'Can add knowledge graph',21,'add_knowledgegraph'),(82,'Can change knowledge graph',21,'change_knowledgegraph'),(83,'Can delete knowledge graph',21,'delete_knowledgegraph'),(84,'Can view knowledge graph',21,'view_knowledgegraph'),(85,'Can add model category',22,'add_modelcategory'),(86,'Can change model category',22,'change_modelcategory'),(87,'Can delete model category',22,'delete_modelcategory'),(88,'Can view model category',22,'view_modelcategory'),(89,'Can add question',23,'add_question'),(90,'Can change question',23,'change_question'),(91,'Can delete question',23,'delete_question'),(92,'Can view question',23,'view_question'),(93,'Can add similar case',24,'add_similarcase'),(94,'Can change similar case',24,'change_similarcase'),(95,'Can delete similar case',24,'delete_similarcase'),(96,'Can view similar case',24,'view_similarcase'),(97,'Can add single disease case info',25,'add_singlediseasecaseinfo'),(98,'Can change single disease case info',25,'change_singlediseasecaseinfo'),(99,'Can delete single disease case info',25,'delete_singlediseasecaseinfo'),(100,'Can view single disease case info',25,'view_singlediseasecaseinfo'),(101,'Can add train model task',26,'add_trainmodeltask'),(102,'Can change train model task',26,'change_trainmodeltask'),(103,'Can delete train model task',26,'delete_trainmodeltask'),(104,'Can view train model task',26,'view_trainmodeltask'),(105,'Can add user info',27,'add_userinfo'),(106,'Can change user info',27,'change_userinfo'),(107,'Can delete user info',27,'delete_userinfo'),(108,'Can view user info',27,'view_userinfo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auto_answer_task`
--

DROP TABLE IF EXISTS `auto_answer_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auto_answer_task` (
  `id` int NOT NULL AUTO_INCREMENT,
  `train_model_id` int NOT NULL,
  `question` varchar(1024) NOT NULL,
  `picture_path` varchar(128) DEFAULT NULL,
  `answer` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auto_answer_task`
--

LOCK TABLES `auto_answer_task` WRITE;
/*!40000 ALTER TABLE `auto_answer_task` DISABLE KEYS */;
INSERT INTO `auto_answer_task` VALUES (8,7,'What diseases do I have?','20240520031138_auto_QA_test.jpg','anaplastic'),(9,10,'What disease do I have?','20240520221305_auto_QA_test.jpg','anaplastic'),(10,13,'What disease do I have?','20240520224105_auto_QA_test.jpg','anaplastic'),(11,15,'What disease do I have?','20240520225238_auto_QA_test.jpg','anaplastic'),(12,15,'What disease do I have?','20240520231521_auto_QA_test.jpg','anaplastic'),(13,15,'What disease do I have?','20240520233709_auto_QA_test.jpg','anaplastic');
/*!40000 ALTER TABLE `auto_answer_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dataset`
--

DROP TABLE IF EXISTS `dataset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dataset` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(512) NOT NULL,
  `is_labeled` smallint NOT NULL,
  `is_single_case` smallint NOT NULL,
  `need_OCR` smallint NOT NULL,
  `status` smallint NOT NULL,
  `train_set_proportion` int DEFAULT NULL,
  `test_set_proportion` int DEFAULT NULL,
  `valid_set_proportion` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dataset`
--

LOCK TABLES `dataset` WRITE;
/*!40000 ALTER TABLE `dataset` DISABLE KEYS */;
INSERT INTO `dataset` VALUES (19,3,'VQA-Med-2019','Test',0,0,0,1,4,4,2),(41,3,'VQA-Med-2019-2','Test OCR',0,1,1,1,NULL,NULL,NULL),(48,2,'medicat','test',0,0,0,1,4,4,2);
/*!40000 ALTER TABLE `dataset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deep_learning_model`
--

DROP TABLE IF EXISTS `deep_learning_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deep_learning_model` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deep_learning_model`
--

LOCK TABLES `deep_learning_model` WRITE;
/*!40000 ALTER TABLE `deep_learning_model` DISABLE KEYS */;
INSERT INTO `deep_learning_model` VALUES (1,'ODL',1),(2,'NLM',2),(3,'VGG-Seq2Seq',2),(4,'ArticleNet',3),(5,'MMBERT',4);
/*!40000 ALTER TABLE `deep_learning_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `id` int NOT NULL AUTO_INCREMENT,
  `department` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'内科'),(2,'外科'),(3,'儿科'),(4,'妇科'),(5,'其他');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'imas','authgroup'),(8,'imas','authgrouppermissions'),(9,'imas','authpermission'),(10,'imas','authuser'),(11,'imas','authusergroups'),(12,'imas','authuseruserpermissions'),(13,'imas','autoanswertask'),(14,'imas','dataset'),(15,'imas','deeplearningmodel'),(16,'imas','department'),(17,'imas','djangoadminlog'),(18,'imas','djangocontenttype'),(19,'imas','djangomigrations'),(20,'imas','djangosession'),(21,'imas','knowledgegraph'),(22,'imas','modelcategory'),(23,'imas','question'),(24,'imas','similarcase'),(25,'imas','singlediseasecaseinfo'),(26,'imas','trainmodeltask'),(27,'imas','userinfo'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-03-30 12:16:52.375463'),(2,'auth','0001_initial','2024-03-30 12:16:53.293390'),(3,'admin','0001_initial','2024-03-30 12:16:53.518055'),(4,'admin','0002_logentry_remove_auto_add','2024-03-30 12:16:53.534824'),(5,'admin','0003_logentry_add_action_flag_choices','2024-03-30 12:16:53.549808'),(6,'contenttypes','0002_remove_content_type_name','2024-03-30 12:16:53.678157'),(7,'auth','0002_alter_permission_name_max_length','2024-03-30 12:16:53.767895'),(8,'auth','0003_alter_user_email_max_length','2024-03-30 12:16:53.801452'),(9,'auth','0004_alter_user_username_opts','2024-03-30 12:16:53.816978'),(10,'auth','0005_alter_user_last_login_null','2024-03-30 12:16:53.915630'),(11,'auth','0006_require_contenttypes_0002','2024-03-30 12:16:53.920690'),(12,'auth','0007_alter_validators_add_error_messages','2024-03-30 12:16:53.937735'),(13,'auth','0008_alter_user_username_max_length','2024-03-30 12:16:54.051137'),(14,'auth','0009_alter_user_last_name_max_length','2024-03-30 12:16:54.181875'),(15,'auth','0010_alter_group_name_max_length','2024-03-30 12:16:54.213252'),(16,'auth','0011_update_proxy_permissions','2024-03-30 12:16:54.231320'),(17,'auth','0012_alter_user_first_name_max_length','2024-03-30 12:16:54.334378'),(18,'sessions','0001_initial','2024-03-30 12:16:54.395182'),(19,'imas','0001_initial','2024-03-31 03:03:00.272057');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `knowledge_graph`
--

DROP TABLE IF EXISTS `knowledge_graph`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `knowledge_graph` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `disease_case_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `knowledge_graph`
--

LOCK TABLES `knowledge_graph` WRITE;
/*!40000 ALTER TABLE `knowledge_graph` DISABLE KEYS */;
/*!40000 ALTER TABLE `knowledge_graph` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_category`
--

DROP TABLE IF EXISTS `model_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `model_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_category`
--

LOCK TABLES `model_category` WRITE;
/*!40000 ALTER TABLE `model_category` DISABLE KEYS */;
INSERT INTO `model_category` VALUES (1,'Joint Embedding ModelsJoint Embedding Models'),(2,'Encoder-Decoder Models'),(3,'Knowledge Embedding Models'),(4,'Attention-based Models');
/*!40000 ALTER TABLE `model_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `department_id` int NOT NULL,
  `content` varchar(1024) NOT NULL,
  `date` varchar(20) NOT NULL,
  `status` smallint NOT NULL,
  `picture_path` varchar(128) DEFAULT NULL,
  `answer` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (2,3,1,'What diseases do I have?','2024-05-20',1,'2024-05-20_auto_QA_test.jpg','anaplastic | Answer2 | Answer3'),(5,3,1,'test','2024-05-20',0,'2024-05-20_QA_platform_test.png',NULL),(6,3,2,'test2','2024-05-20',0,'2024-05-20_QA_platform_test.png',NULL),(8,2,3,'Test_pat','2024-05-20',1,'2024-05-20_QA_platform_test.png','Answer');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `similar_case`
--

DROP TABLE IF EXISTS `similar_case`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `similar_case` (
  `id` int NOT NULL AUTO_INCREMENT,
  `knowledge_graph_id` int NOT NULL,
  `similar_graph_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `similar_case`
--

LOCK TABLES `similar_case` WRITE;
/*!40000 ALTER TABLE `similar_case` DISABLE KEYS */;
/*!40000 ALTER TABLE `similar_case` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `single_disease_case_info`
--

DROP TABLE IF EXISTS `single_disease_case_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `single_disease_case_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dataset_id` int NOT NULL,
  `patient_name` varchar(32) NOT NULL,
  `picture_name` varchar(32) NOT NULL,
  `whole_desc` varchar(1024) NOT NULL,
  `disease` varchar(512) DEFAULT NULL,
  `medicine` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `single_disease_case_info`
--

LOCK TABLES `single_disease_case_info` WRITE;
/*!40000 ALTER TABLE `single_disease_case_info` DISABLE KEYS */;
INSERT INTO `single_disease_case_info` VALUES (18,19,'54143.txt','synpic54143.jpg','anaplastic oligodendroglioma#multi-cystic complex mass#neoplasm','anaplastic','medicine'),(19,19,'41525.txt','synpic41525.jpg','epiploic appendagitis','epiploic appendagitis',''),(20,19,'39878.txt','synpic39878.jpg','cerebral infarct','cerebral infarct',''),(21,19,'18173.txt','synpic18173.jpg','pancreatic ductal adenocarcinoma','pancreatic ductal adenocarcinoma',''),(52,36,'1.txt','1.png','\"s2_caption\": \"Figure 1. (A) Barium enema and (B) endoscopic image of   high-grade distal colonic obstruction caused by a 5-cm anastomotic stricture.\", \"s2orc_caption\": \"Figure 1. (A) Barium enema and (B) endoscopic image of   high-grade distal colonic obstruction caused by a 5-cm anastomotic stricture.\", \"s2orc_references\": [\"Computed tomography (CT) showed a distal large bowel obstruction, and a barium enema revealed a high-grade stenosis proximal to   anastomotic site in   recto-sigmoid region (Figure 1 ).\", \"Flexible sigmoidoscopy revealed a tight, fibrotic, benign-appearing anastomotic stricture 15 cm from   anal verge ( Figure 1) .\"]','benign-appearing anastomotic stricture,high-grade distal colonic obstruction,high-grade stenosis,anastomotic stricture,bowel obstruction','Barium enema,barium enema'),(53,36,'2.txt','2.png','\"s2_caption\": \"Figure 2. Complete resolution of   colonic obstruction occurred immediately after SEMS placement, as evidenced by (A) colonoscopy and (B) plain abdominal radiograph.\", \"s2orc_caption\": \"Figure 2. Complete resolution of   colonic obstruction occurred immediately after SEMS placement, as evidenced by (A) colonoscopy and (B) plain abdominal radiograph.\", \"s2orc_references\": [\"Following stent placement,   patient had complete clinical and radiographic resolution of his large bowel obstruction (Figure 2 ).One year after stent placement,   patient presented for surveillance colonoscopy.\"]','colonic obstruction,bowel obstruction',''),(54,36,'3.txt','3.png','\"s2_caption\": \"Figure 3. Surveillance colonoscopy 1 year after SEMS placement showed patent stents in   rectum with complete tissue ingrowth that appeared friable and inflammatory in nature.\", \"s2orc_caption\": \"Figure 3. Surveillance colonoscopy 1 year after SEMS placement showed patent stents in   rectum with complete tissue ingrowth that appeared friable and inflammatory in nature.\"','friable',''),(55,36,'4.txt','4.png','\"s2_caption\": \"Figure 4. Nuclear magnetic resonance scan demonstrating   occipital lesion with irregular borders surrounded by slight edema.\", \"s2orc_caption\": \"Figure 4. Nuclear magnetic resonance scan demonstrating   occipital lesion with irregular borders surrounded by slight edema.\", \"s2orc_references\": [\"Findings from nuclear magnetic resonance imaging, with and without gadolinium enhancement, showed a hyperdense lesion located in   left temporo-occipital region with irregular borders, surrounded by slight edema (hyperintense signal on T1W and hypointense signal on T2W) (Figure 4) .Neurosurgical consultation was consistent with a probable primary occipital tumor and   patient underwent surgery on January  .\"]','primary occipital tumor,edema','gadolinium'),(56,36,'5.txt','5.png','\"s2_caption\": \"Figure 4. Endoscopic images 4 years after colonic SEMS placement. (A) Stricture at   site of   previously placed stents in   rectum with tissue hypertrophy and a small ulcer. (B) Although no visible stents were seen during   colonoscopy, a portion of   stents was visualized on abdominal radiograph.\", \"s2orc_caption\": \"Figure 4. Endoscopic images 4 years after colonic SEMS placement. (A) Stricture at   site of   previously placed stents in   rectum with tissue hypertrophy and a small ulcer. (B) Although no visible stents were seen during   colonoscopy, a portion of   stents was visualized on abdominal radiograph.\", \"s2orc_references\": [\"Tissue hypertrophy and a small ulcer were noted at   site of   stricture (Figure 4 ).\", \"A pelvic radiograph showed that   stents remained partially in place, with absence of   most proximal and distal flares (Figure 4) .\"]','hypertrophy,ulcer',''),(102,48,'1.txt','1.png','\"s2_caption\": \"Figure 1. (A) Barium enema and (B) endoscopic image of   high-grade distal colonic obstruction caused by a 5-cm anastomotic stricture.\", \"s2orc_caption\": \"Figure 1. (A) Barium enema and (B) endoscopic image of   high-grade distal colonic obstruction caused by a 5-cm anastomotic stricture.\", \"s2orc_references\": [\"Computed tomography (CT) showed a distal large bowel obstruction, and a barium enema revealed a high-grade stenosis proximal to   anastomotic site in   recto-sigmoid region (Figure 1 ).\", \"Flexible sigmoidoscopy revealed a tight, fibrotic, benign-appearing anastomotic stricture 15 cm from   anal verge ( Figure 1) .\"]','high-grade stenosis,benign-appearing anastomotic stricture,bowel obstruction,anastomotic stricture,high-grade distal colonic obstruction','Barium enema,barium enema'),(103,48,'2.txt','2.png','\"s2_caption\": \"Figure 2. Complete resolution of   colonic obstruction occurred immediately after SEMS placement, as evidenced by (A) colonoscopy and (B) plain abdominal radiograph.\", \"s2orc_caption\": \"Figure 2. Complete resolution of   colonic obstruction occurred immediately after SEMS placement, as evidenced by (A) colonoscopy and (B) plain abdominal radiograph.\", \"s2orc_references\": [\"Following stent placement,   patient had complete clinical and radiographic resolution of his large bowel obstruction (Figure 2 ).One year after stent placement,   patient presented for surveillance colonoscopy.\"]','colonic obstruction,bowel obstruction',''),(104,48,'3.txt','3.png','\"s2_caption\": \"Figure 3. Surveillance colonoscopy 1 year after SEMS placement showed patent stents in   rectum with complete tissue ingrowth that appeared friable and inflammatory in nature.\", \"s2orc_caption\": \"Figure 3. Surveillance colonoscopy 1 year after SEMS placement showed patent stents in   rectum with complete tissue ingrowth that appeared friable and inflammatory in nature.\"','friable',''),(105,48,'4.txt','4.png','\"s2_caption\": \"Figure 4. Nuclear magnetic resonance scan demonstrating   occipital lesion with irregular borders surrounded by slight edema.\", \"s2orc_caption\": \"Figure 4. Nuclear magnetic resonance scan demonstrating   occipital lesion with irregular borders surrounded by slight edema.\", \"s2orc_references\": [\"Findings from nuclear magnetic resonance imaging, with and without gadolinium enhancement, showed a hyperdense lesion located in   left temporo-occipital region with irregular borders, surrounded by slight edema (hyperintense signal on T1W and hypointense signal on T2W) (Figure 4) .Neurosurgical consultation was consistent with a probable primary occipital tumor and   patient underwent surgery on January  .\"]','edema,primary occipital tumor','gadolinium'),(106,48,'5.txt','5.png','\"s2_caption\": \"Figure 4. Endoscopic images 4 years after colonic SEMS placement. (A) Stricture at   site of   previously placed stents in   rectum with tissue hypertrophy and a small ulcer. (B) Although no visible stents were seen during   colonoscopy, a portion of   stents was visualized on abdominal radiograph.\", \"s2orc_caption\": \"Figure 4. Endoscopic images 4 years after colonic SEMS placement. (A) Stricture at   site of   previously placed stents in   rectum with tissue hypertrophy and a small ulcer. (B) Although no visible stents were seen during   colonoscopy, a portion of   stents was visualized on abdominal radiograph.\", \"s2orc_references\": [\"Tissue hypertrophy and a small ulcer were noted at   site of   stricture (Figure 4 ).\", \"A pelvic radiograph showed that   stents remained partially in place, with absence of   most proximal and distal flares (Figure 4) .\"]','ulcer,hypertrophy','');
/*!40000 ALTER TABLE `single_disease_case_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `train_model_task`
--

DROP TABLE IF EXISTS `train_model_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `train_model_task` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `task_name` varchar(50) NOT NULL,
  `dataset_id` int NOT NULL,
  `model_id` int NOT NULL,
  `date` varchar(20) NOT NULL,
  `status` smallint NOT NULL,
  `epoch` int DEFAULT NULL,
  `batch_size` int DEFAULT NULL,
  `rnn_cell` varchar(20) DEFAULT NULL,
  `embedding` varchar(20) DEFAULT NULL,
  `attention` varchar(20) DEFAULT NULL,
  `constructor` varchar(20) DEFAULT NULL,
  `after_train_model_path` varchar(128) DEFAULT NULL,
  `f1` float DEFAULT NULL,
  `recall` float DEFAULT NULL,
  `precision` float DEFAULT NULL,
  `bleu` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train_model_task`
--

LOCK TABLES `train_model_task` WRITE;
/*!40000 ALTER TABLE `train_model_task` DISABLE KEYS */;
INSERT INTO `train_model_task` VALUES (15,3,'ODL-VQA-Med-2019',19,1,'2024-05-20',1,10,1,'GRU','none','SAN','both','D:\\IDEA_Project\\IMAS\\after_train_models/',0.633551,0.52309,0.501876,11.059260717013366),(16,3,'NLM-VQA-Med-2019',19,2,'2024-05-20',1,10,8,'GRU','none','SAN','both','D:\\IDEA_Project\\IMAS\\after_train_models/',0.64188,0.693338,0.826101,21.119550622069333),(21,2,'test',19,1,'2024-05-20',1,10,1,'GRU','none','SAN','both','D:\\IDEA_Project\\IMAS\\after_train_models/',0.654284,0.73908,0.779079,26.310246319692386);
/*!40000 ALTER TABLE `train_model_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login_name` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `role` int NOT NULL,
  `age` int DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `gender` varchar(2) DEFAULT NULL,
  `marriage` varchar(10) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1,'doctor','test',1,44,'','','','',''),(2,'patient','test',0,20,'','','','',''),(3,'czs','test',1,22,'','','','',''),(10,'doctor2','test',0,0,'','','','',''),(11,'doctor3','test',1,0,'','','','','');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-30 10:52:37
