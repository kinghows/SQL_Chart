/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 5.7.17-enterprise-commercial-advanced-log : Database - chart_demo
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `t_calendar` */

DROP TABLE IF EXISTS `t_calendar`;

CREATE TABLE `t_calendar` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `count` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=366 DEFAULT CHARSET=utf8mb4;

/*Data for the table `t_calendar` */

insert  into `t_calendar`(`id`,`date`,`count`) values 
(1,'2018-01-01',18389),
(2,'2018-01-02',9994),
(3,'2018-01-03',14304),
(4,'2018-01-04',1038),
(5,'2018-01-05',1779),
(6,'2018-01-06',5280),
(7,'2018-01-07',566),
(8,'2018-01-08',6491),
(9,'2018-01-09',10255),
(10,'2018-01-10',11302),
(11,'2018-01-11',5244),
(12,'2018-01-12',11818),
(13,'2018-01-13',2857),
(14,'2018-01-14',18331),
(15,'2018-01-15',2586),
(16,'2018-01-16',17437),
(17,'2018-01-17',18926),
(18,'2018-01-18',1819),
(19,'2018-01-19',11820),
(20,'2018-01-20',13142),
(21,'2018-01-21',9751),
(22,'2018-01-22',8830),
(23,'2018-01-23',14398),
(24,'2018-01-24',5001),
(25,'2018-01-25',1310),
(26,'2018-01-26',11048),
(27,'2018-01-27',10811),
(28,'2018-01-28',20413),
(29,'2018-01-29',9129),
(30,'2018-01-30',3909),
(31,'2018-01-31',11656),
(32,'2018-02-01',6055),
(33,'2018-02-02',14807),
(34,'2018-02-03',15371),
(35,'2018-02-04',11936),
(36,'2018-02-05',13067),
(37,'2018-02-06',9026),
(38,'2018-02-07',5432),
(39,'2018-02-08',19580),
(40,'2018-02-09',1105),
(41,'2018-02-10',6284),
(42,'2018-02-11',7607),
(43,'2018-02-12',18682),
(44,'2018-02-13',10089),
(45,'2018-02-14',13901),
(46,'2018-02-15',18739),
(47,'2018-02-16',11490),
(48,'2018-02-17',735),
(49,'2018-02-18',8703),
(50,'2018-02-19',813),
(51,'2018-02-20',17457),
(52,'2018-02-21',4347),
(53,'2018-02-22',8866),
(54,'2018-02-23',10786),
(55,'2018-02-24',6833),
(56,'2018-02-25',1309),
(57,'2018-02-26',5546),
(58,'2018-02-27',3302),
(59,'2018-02-28',19372),
(60,'2018-03-01',6456),
(61,'2018-03-02',13663),
(62,'2018-03-03',8446),
(63,'2018-03-04',744),
(64,'2018-03-05',17883),
(65,'2018-03-06',6681),
(66,'2018-03-07',19257),
(67,'2018-03-08',15744),
(68,'2018-03-09',20448),
(69,'2018-03-10',14507),
(70,'2018-03-11',10695),
(71,'2018-03-12',9453),
(72,'2018-03-13',14679),
(73,'2018-03-14',4537),
(74,'2018-03-15',18150),
(75,'2018-03-16',16637),
(76,'2018-03-17',8237),
(77,'2018-03-18',10774),
(78,'2018-03-19',8659),
(79,'2018-03-20',10473),
(80,'2018-03-21',5891),
(81,'2018-03-22',17536),
(82,'2018-03-23',9505),
(83,'2018-03-24',14421),
(84,'2018-03-25',3087),
(85,'2018-03-26',11675),
(86,'2018-03-27',8612),
(87,'2018-03-28',7538),
(88,'2018-03-29',11352),
(89,'2018-03-30',13649),
(90,'2018-03-31',13689),
(91,'2018-04-01',7000),
(92,'2018-04-02',13432),
(93,'2018-04-03',5662),
(94,'2018-04-04',7514),
(95,'2018-04-05',20084),
(96,'2018-04-06',17378),
(97,'2018-04-07',6140),
(98,'2018-04-08',18067),
(99,'2018-04-09',11415),
(100,'2018-04-10',2373),
(101,'2018-04-11',17121),
(102,'2018-04-12',17987),
(103,'2018-04-13',18071),
(104,'2018-04-14',15895),
(105,'2018-04-15',4764),
(106,'2018-04-16',15635),
(107,'2018-04-17',3383),
(108,'2018-04-18',9511),
(109,'2018-04-19',16905),
(110,'2018-04-20',15492),
(111,'2018-04-21',6244),
(112,'2018-04-22',4248),
(113,'2018-04-23',2008),
(114,'2018-04-24',16796),
(115,'2018-04-25',17456),
(116,'2018-04-26',16392),
(117,'2018-04-27',9093),
(118,'2018-04-28',15788),
(119,'2018-04-29',11162),
(120,'2018-04-30',7946),
(121,'2018-05-01',5746),
(122,'2018-05-02',4391),
(123,'2018-05-03',4216),
(124,'2018-05-04',7410),
(125,'2018-05-05',3900),
(126,'2018-05-06',16773),
(127,'2018-05-07',11667),
(128,'2018-05-08',7514),
(129,'2018-05-09',2068),
(130,'2018-05-10',7301),
(131,'2018-05-11',9803),
(132,'2018-05-12',6609),
(133,'2018-05-13',3138),
(134,'2018-05-14',15364),
(135,'2018-05-15',6907),
(136,'2018-05-16',7945),
(137,'2018-05-17',18502),
(138,'2018-05-18',8176),
(139,'2018-05-19',4873),
(140,'2018-05-20',19337),
(141,'2018-05-21',1567),
(142,'2018-05-22',9324),
(143,'2018-05-23',1421),
(144,'2018-05-24',18634),
(145,'2018-05-25',8405),
(146,'2018-05-26',5626),
(147,'2018-05-27',2417),
(148,'2018-05-28',14705),
(149,'2018-05-29',5774),
(150,'2018-05-30',4255),
(151,'2018-05-31',3456),
(152,'2018-06-01',4014),
(153,'2018-06-02',9201),
(154,'2018-06-03',13465),
(155,'2018-06-04',19223),
(156,'2018-06-05',15220),
(157,'2018-06-06',17931),
(158,'2018-06-07',3495),
(159,'2018-06-08',3183),
(160,'2018-06-09',4931),
(161,'2018-06-10',14607),
(162,'2018-06-11',17742),
(163,'2018-06-12',4391),
(164,'2018-06-13',8227),
(165,'2018-06-14',7465),
(166,'2018-06-15',12144),
(167,'2018-06-16',17824),
(168,'2018-06-17',12191),
(169,'2018-06-18',6981),
(170,'2018-06-19',17834),
(171,'2018-06-20',7728),
(172,'2018-06-21',4637),
(173,'2018-06-22',19503),
(174,'2018-06-23',3102),
(175,'2018-06-24',16503),
(176,'2018-06-25',12710),
(177,'2018-06-26',13543),
(178,'2018-06-27',9085),
(179,'2018-06-28',4295),
(180,'2018-06-29',13722),
(181,'2018-06-30',15225),
(182,'2018-07-01',14459),
(183,'2018-07-02',6121),
(184,'2018-07-03',6729),
(185,'2018-07-04',14782),
(186,'2018-07-05',13222),
(187,'2018-07-06',1267),
(188,'2018-07-07',6168),
(189,'2018-07-08',6540),
(190,'2018-07-09',13697),
(191,'2018-07-10',8364),
(192,'2018-07-11',20230),
(193,'2018-07-12',15559),
(194,'2018-07-13',16607),
(195,'2018-07-14',15858),
(196,'2018-07-15',8967),
(197,'2018-07-16',16763),
(198,'2018-07-17',16416),
(199,'2018-07-18',11291),
(200,'2018-07-19',6707),
(201,'2018-07-20',19163),
(202,'2018-07-21',15196),
(203,'2018-07-22',17990),
(204,'2018-07-23',3863),
(205,'2018-07-24',4844),
(206,'2018-07-25',12134),
(207,'2018-07-26',5635),
(208,'2018-07-27',11277),
(209,'2018-07-28',18980),
(210,'2018-07-29',571),
(211,'2018-07-30',5414),
(212,'2018-07-31',4856),
(213,'2018-08-01',7541),
(214,'2018-08-02',2635),
(215,'2018-08-03',10053),
(216,'2018-08-04',1861),
(217,'2018-08-05',18646),
(218,'2018-08-06',7148),
(219,'2018-08-07',19303),
(220,'2018-08-08',14572),
(221,'2018-08-09',14449),
(222,'2018-08-10',8030),
(223,'2018-08-11',16306),
(224,'2018-08-12',16939),
(225,'2018-08-13',15278),
(226,'2018-08-14',5071),
(227,'2018-08-15',19024),
(228,'2018-08-16',19409),
(229,'2018-08-17',19471),
(230,'2018-08-18',18630),
(231,'2018-08-19',14235),
(232,'2018-08-20',14787),
(233,'2018-08-21',10732),
(234,'2018-08-22',8800),
(235,'2018-08-23',11302),
(236,'2018-08-24',9611),
(237,'2018-08-25',13648),
(238,'2018-08-26',18908),
(239,'2018-08-27',13096),
(240,'2018-08-28',8259),
(241,'2018-08-29',1505),
(242,'2018-08-30',2250),
(243,'2018-08-31',6236),
(244,'2018-09-01',3928),
(245,'2018-09-02',20433),
(246,'2018-09-03',9882),
(247,'2018-09-04',7611),
(248,'2018-09-05',7909),
(249,'2018-09-06',16212),
(250,'2018-09-07',16832),
(251,'2018-09-08',15027),
(252,'2018-09-09',4140),
(253,'2018-09-10',15120),
(254,'2018-09-11',2681),
(255,'2018-09-12',7546),
(256,'2018-09-13',9188),
(257,'2018-09-14',2803),
(258,'2018-09-15',5951),
(259,'2018-09-16',848),
(260,'2018-09-17',5886),
(261,'2018-09-18',6387),
(262,'2018-09-19',13777),
(263,'2018-09-20',9224),
(264,'2018-09-21',4290),
(265,'2018-09-22',13278),
(266,'2018-09-23',13023),
(267,'2018-09-24',4779),
(268,'2018-09-25',4328),
(269,'2018-09-26',6805),
(270,'2018-09-27',540),
(271,'2018-09-28',1785),
(272,'2018-09-29',6806),
(273,'2018-09-30',8174),
(274,'2018-10-01',19952),
(275,'2018-10-02',14741),
(276,'2018-10-03',13346),
(277,'2018-10-04',2011),
(278,'2018-10-05',9517),
(279,'2018-10-06',1051),
(280,'2018-10-07',16206),
(281,'2018-10-08',17377),
(282,'2018-10-09',17768),
(283,'2018-10-10',16210),
(284,'2018-10-11',7245),
(285,'2018-10-12',7095),
(286,'2018-10-13',13240),
(287,'2018-10-14',4417),
(288,'2018-10-15',1865),
(289,'2018-10-16',15576),
(290,'2018-10-17',11784),
(291,'2018-10-18',11694),
(292,'2018-10-19',2619),
(293,'2018-10-20',17513),
(294,'2018-10-21',19206),
(295,'2018-10-22',2995),
(296,'2018-10-23',16854),
(297,'2018-10-24',14788),
(298,'2018-10-25',2879),
(299,'2018-10-26',9531),
(300,'2018-10-27',18520),
(301,'2018-10-28',3508),
(302,'2018-10-29',1479),
(303,'2018-10-30',16373),
(304,'2018-10-31',16927),
(305,'2018-11-01',15016),
(306,'2018-11-02',3802),
(307,'2018-11-03',13462),
(308,'2018-11-04',15403),
(309,'2018-11-05',16128),
(310,'2018-11-06',13935),
(311,'2018-11-07',790),
(312,'2018-11-08',1645),
(313,'2018-11-09',5355),
(314,'2018-11-10',1340),
(315,'2018-11-11',10137),
(316,'2018-11-12',6165),
(317,'2018-11-13',19915),
(318,'2018-11-14',581),
(319,'2018-11-15',2660),
(320,'2018-11-16',11055),
(321,'2018-11-17',6799),
(322,'2018-11-18',20329),
(323,'2018-11-19',749),
(324,'2018-11-20',2260),
(325,'2018-11-21',8553),
(326,'2018-11-22',15487),
(327,'2018-11-23',11276),
(328,'2018-11-24',9417),
(329,'2018-11-25',12760),
(330,'2018-11-26',15047),
(331,'2018-11-27',16458),
(332,'2018-11-28',16651),
(333,'2018-11-29',13378),
(334,'2018-11-30',16438),
(335,'2018-12-01',1557),
(336,'2018-12-02',17970),
(337,'2018-12-03',4681),
(338,'2018-12-04',8997),
(339,'2018-12-05',10440),
(340,'2018-12-06',4712),
(341,'2018-12-07',11740),
(342,'2018-12-08',4063),
(343,'2018-12-09',4594),
(344,'2018-12-10',10285),
(345,'2018-12-11',17143),
(346,'2018-12-12',14359),
(347,'2018-12-13',19865),
(348,'2018-12-14',15750),
(349,'2018-12-15',18656),
(350,'2018-12-16',5531),
(351,'2018-12-17',11186),
(352,'2018-12-18',18836),
(353,'2018-12-19',20124),
(354,'2018-12-20',3612),
(355,'2018-12-21',17190),
(356,'2018-12-22',14613),
(357,'2018-12-23',998),
(358,'2018-12-24',650),
(359,'2018-12-25',19757),
(360,'2018-12-26',16335),
(361,'2018-12-27',1904),
(362,'2018-12-28',20016),
(363,'2018-12-29',13867),
(364,'2018-12-30',8789),
(365,'2018-12-31',1845);

/*Table structure for table `t_chart1` */

DROP TABLE IF EXISTS `t_chart1`;

CREATE TABLE `t_chart1` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `amount` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=239 DEFAULT CHARSET=utf8;

/*Data for the table `t_chart1` */

insert  into `t_chart1`(`id`,`date`,`area`,`amount`) values 
(1,'2019-11-05','重庆',2373046.88),
(3,'2019-11-05','北京',8032911.66),
(5,'2019-11-05','广州',6328125.00),
(7,'2019-11-05','深圳',15103627.05),
(9,'2019-11-05','天津',8632195.33),
(11,'2019-11-05','上海',17181345.31),
(15,'2019-11-06','重庆',2373046.88),
(17,'2019-11-06','北京',9930893.54),
(19,'2019-11-06','广州',6328125.00),
(21,'2019-11-06','深圳',14761908.30),
(23,'2019-11-06','天津',8398054.70),
(25,'2019-11-06','上海',17552670.72),
(31,'2019-11-07','重庆',2373046.88),
(33,'2019-11-07','北京',11208668.54),
(35,'2019-11-07','广州',6328125.00),
(37,'2019-11-07','深圳',14534095.80),
(39,'2019-11-07','天津',9328289.08),
(41,'2019-11-07','上海',18947170.33),
(61,'2019-11-08','重庆',2373046.88),
(63,'2019-11-08','北京',12868470.00),
(65,'2019-11-08','广州',6328125.00),
(67,'2019-11-08','深圳',13921849.70),
(69,'2019-11-08','天津',10017421.88),
(71,'2019-11-08','上海',21665893.98),
(91,'2019-11-09','重庆',2373046.88),
(93,'2019-11-09','北京',17716826.25),
(95,'2019-11-09','广州',6328125.00),
(97,'2019-11-09','深圳',13694037.20),
(99,'2019-11-09','天津',9955406.25),
(101,'2019-11-09','上海',22992158.09),
(121,'2019-11-10','重庆',2373046.88),
(123,'2019-11-10','北京',18465063.75),
(125,'2019-11-10','广州',6328125.00),
(127,'2019-11-10','深圳',14563056.50),
(129,'2019-11-10','天津',9961734.38),
(131,'2019-11-10','上海',23490268.00),
(151,'2019-11-11','重庆',2373046.88),
(153,'2019-11-11','北京',18985995.00),
(155,'2019-11-11','广州',6328125.00),
(157,'2019-11-11','深圳',14673687.93),
(159,'2019-11-11','天津',9987046.88),
(161,'2019-11-11','上海',25963869.62),
(181,'2019-11-12','重庆',2373046.88),
(183,'2019-11-12','北京',19870413.75),
(185,'2019-11-12','广州',6328125.00),
(187,'2019-11-12','深圳',16262734.01),
(189,'2019-11-12','天津',10183192.20),
(191,'2019-11-12','上海',28395845.23),
(211,'2019-11-13','重庆',2373046.88),
(213,'2019-11-13','北京',16365138.75),
(215,'2019-11-13','广州',6328125.00),
(217,'2019-11-13','深圳',15636249.63),
(219,'2019-11-13','天津',10414801.58),
(221,'2019-11-13','上海',29845820.32);

/* Procedure structure for procedure `ist_calendar` */

/*!50003 DROP PROCEDURE IF EXISTS  `ist_calendar` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `ist_calendar`()
BEGIN
  DECLARE i INT;
  SET i = 0;
  WHILE
    i < 365 DO
    INSERT INTO t_calendar (DATE,count)
    VALUES
      (DATE_SUB(STR_TO_DATE('2018-01-01','%Y-%m-%d'), INTERVAL - i DAY),FLOOR( 500 + RAND() * 20000));
    SET i = i + 1;
  END WHILE;
END */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
