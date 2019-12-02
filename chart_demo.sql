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
/*Table structure for table `t_boxpolt` */

DROP TABLE IF EXISTS `t_boxpolt`;

CREATE TABLE `t_boxpolt` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `expr` varchar(20) DEFAULT NULL,
  `AB` varchar(20) DEFAULT NULL,
  `counts` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `t_boxpolt` */

insert  into `t_boxpolt`(`id`,`expr`,`AB`,`counts`) values 
(1,'expr1','A','850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 96'),
(2,'expr2','A','960, 940, 960, 940, 880, 800, 850, 880, 900,840, 830, 790, 810, 880, 880, 830, 800, 790, 760, 800'),
(3,'expr1','B','890, 810, 810, 820, 800, 770, 760, 740, 750, 760,910, 920, 890, 860, 880, 720, 840, 850, 850, 780'),
(4,'expr2','B','890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870,870, 810, 740, 810, 940, 950, 800, 810, 870');

/*Table structure for table `t_radar_x` */

DROP TABLE IF EXISTS `t_radar_x`;

CREATE TABLE `t_radar_x` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `max` int(6) DEFAULT NULL,
  `min` int(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `t_radar_x` */

insert  into `t_radar_x`(`id`,`name`,`max`,`min`) values 
(1,'销售',6500,NULL),
(2,'管理',16000,NULL),
(3,'信息技术',30000,NULL),
(4,'客服',38000,NULL),
(5,'研发',52000,NULL),
(6,'市场',25000,NULL);

/*Table structure for table `t_radar_x2` */

DROP TABLE IF EXISTS `t_radar_x2`;

CREATE TABLE `t_radar_x2` (
  `id` int(2) NOT NULL DEFAULT '0',
  `name` varchar(20) DEFAULT NULL,
  `max` int(6) DEFAULT NULL,
  `min` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `t_radar_x2` */

insert  into `t_radar_x2`(`id`,`name`,`max`,`min`) values 
(1,'AQI',300,5),
(2,'PM2.5',250,20),
(3,'PM10',300,5),
(4,'CO',5,NULL),
(5,'NO2',200,NULL),
(0,'SO2',100,NULL);

/*Table structure for table `t_sankey_x` */

DROP TABLE IF EXISTS `t_sankey_x`;

CREATE TABLE `t_sankey_x` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4;

/*Data for the table `t_sankey_x` */

insert  into `t_sankey_x`(`id`,`name`) values 
(1,'Agricultural \'waste\''),
(2,'Bio-conversion'),
(3,'Liquid'),
(4,'Losses'),
(5,'Solid'),
(6,'Gas'),
(7,'Biofuel imports'),
(8,'Biomass imports'),
(9,'Coal imports'),
(10,'Coal'),
(11,'Coal reserves'),
(12,'District heating'),
(13,'Industry'),
(14,'Heating and cooling - commercial'),
(15,'Heating and cooling - homes'),
(16,'Electricity grid'),
(17,'Over generation / exports'),
(18,'H2 conversion'),
(19,'Road transport'),
(20,'Agriculture'),
(21,'Rail transport'),
(22,'Lighting & appliances - commercial'),
(23,'Lighting & appliances - homes'),
(24,'Gas imports'),
(25,'Ngas'),
(26,'Gas reserves'),
(27,'Thermal generation'),
(28,'Geothermal'),
(29,'H2'),
(30,'Hydro'),
(31,'International shipping'),
(32,'Domestic aviation'),
(33,'International aviation'),
(34,'National navigation'),
(35,'Marine algae'),
(36,'Nuclear'),
(37,'Oil imports'),
(38,'Oil'),
(39,'Oil reserves'),
(40,'Other waste'),
(41,'Pumped heat'),
(42,'Solar PV'),
(43,'Solar Thermal'),
(44,'Solar'),
(45,'Tidal'),
(46,'UK land based bioenergy'),
(47,'Wave'),
(48,'Wind');

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

/* Procedure structure for procedure `ist_t_graph` */

/*!50003 DROP PROCEDURE IF EXISTS  `ist_t_graph` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `ist_t_graph`()
BEGIN
  DECLARE v_node1 VARCHAR (20);
  DECLARE v_node2 VARCHAR (20);
  DECLARE v_size INT (5);
  
  DECLARE num INT DEFAULT 0;
  DECLARE cur_1 CURSOR FOR
  SELECT "结点1",10  union all 
  select "结点2",20  UNION ALL
  SELECT "结点3",30  UNION ALL
  SELECT "结点4",40  UNION ALL
  SELECT "结点5",50  UNION ALL
  SELECT "结点6",40  UNION ALL
  SELECT "结点7",30  UNION ALL
  SELECT "结点8",20;

  
  DECLARE cur_2 CURSOR FOR
  SELECT "结点1"  UNION ALL 
  SELECT "结点2"  UNION ALL
  SELECT "结点3"  UNION ALL
  SELECT "结点4"  UNION ALL
  SELECT "结点5"  UNION ALL
  SELECT "结点6"  UNION ALL
  SELECT "结点7"  UNION ALL
  SELECT "结点8";
  
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET num = 1;
  
  OPEN cur_1;
  out_loop:LOOP
      FETCH cur_1 INTO v_node1,v_size;
      IF num = 1 THEN
          LEAVE out_loop;
      END IF;
      
      OPEN cur_2;
      inner_loop:LOOP
          FETCH cur_2 INTO v_node2;
          IF num = 1 THEN
              LEAVE inner_loop;
          END IF;
          INSERT INTO t_graph (node, size, link) VALUES (v_node1, v_size, v_node2);
      end LOOP inner_loop;
      CLOSE cur_2;
      SET num=0;
    
  END LOOP out_loop;
  CLOSE cur_1;
END */$$
DELIMITER ;

/* Procedure structure for procedure `ist_t_polar` */

/*!50003 DROP PROCEDURE IF EXISTS  `ist_t_polar` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`%` PROCEDURE `ist_t_polar`()
BEGIN
  DECLARE i INT;
  SET i = 0;
  WHILE
    i < 101 DO
    INSERT INTO t_polar (id,count)
    VALUES
      (i,FLOOR( 1 + RAND() * 100));
    SET i = i + 1;
  END WHILE;
END */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
