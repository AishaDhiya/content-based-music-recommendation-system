/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - music app
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`music app` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `music app`;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`user_id`,`feedback`,`date`) values (14,9,'feedback','2022-02-04'),(18,13,'something good','2022-03-03'),(19,13,'good application','2022-03-03');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values (1,'admin','123','admin'),(2,'Amal','1234','user'),(8,'nowri','09876','user'),(11,'hello','2222','user'),(12,'kooi','3333','user'),(13,'a','a','user'),(14,'manu','1289','user'),(15,'naveen','naveen','user');

/*Table structure for table `mfcc` */

DROP TABLE IF EXISTS `mfcc`;

CREATE TABLE `mfcc` (
  `mfcc_id` int(11) NOT NULL AUTO_INCREMENT,
  `music_id` int(11) DEFAULT NULL,
  `chroma_stft` varchar(100) DEFAULT NULL,
  `spec_cent` varchar(100) DEFAULT NULL,
  `spec_bw` varchar(100) DEFAULT NULL,
  `rolloff` varchar(100) DEFAULT NULL,
  `zcr` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`mfcc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `mfcc` */

insert  into `mfcc`(`mfcc_id`,`music_id`,`chroma_stft`,`spec_cent`,`spec_bw`,`rolloff`,`zcr`) values (1,1,'0.29678944','2034.721285028306','2263.776107529761','4375.471156765692','0.08524408640499692'),(2,2,'0.31062913','2030.7274377453514','2563.6177967909025','4765.5558816715275','0.06928841212408199'),(3,3,'0.2309259','1065.329699913535','1525.0574953929408','2030.7130655665308','0.03489461522193471'),(4,4,'0.31062913','2030.7274377453514','2563.6177967909025','4765.5558816715275','0.06928841212408199'),(5,5,'0.35760534','1939.754878647196','2175.8806186941497','4076.911051527696','0.08617109840574931'),(6,6,'0.31062913','2030.7274377453514','2563.6177967909025','4765.5558816715275','0.06928841212408199'),(7,7,'0.2309259','1065.329699913535','1525.0574953929408','2030.7130655665308','0.03489461522193471'),(8,8,'0.29678944','2034.721285028306','2263.776107529761','4375.471156765692','0.08524408640499692'),(9,9,'0.29678944','2034.721285028306','2263.776107529761','4375.471156765692','0.08524408640499692'),(10,10,'0.2309259','1065.329699913535','1525.0574953929408','2030.7130655665308','0.03489461522193471'),(11,11,'0.29678944','2034.721285028306','2263.776107529761','4375.471156765692','0.08524408640499692'),(12,12,'0.29678944','2034.721285028306','2263.776107529761','4375.471156765692','0.08524408640499692'),(13,13,'0.37252656','2620.148867926266','2603.5759904072465','5514.3225693121185','0.11231241436647067'),(14,14,'0.40420768','2073.463740640802','2262.5271784572747','4442.841597502214','0.08879362895613871');

/*Table structure for table `most_played` */

DROP TABLE IF EXISTS `most_played`;

CREATE TABLE `most_played` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `music_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `most_played` */

insert  into `most_played`(`id`,`music_id`,`user_id`) values (1,1,13),(2,1,15),(3,3,15),(4,1,15),(5,3,15),(6,1,15),(7,14,15),(8,11,15),(9,9,15);

/*Table structure for table `mtype` */

DROP TABLE IF EXISTS `mtype`;

CREATE TABLE `mtype` (
  `muid` int(11) DEFAULT NULL,
  `type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `mtype` */

insert  into `mtype`(`muid`,`type`) values (1,1),(2,1),(3,1),(4,2),(5,2),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0);

/*Table structure for table `music` */

DROP TABLE IF EXISTS `music`;

CREATE TABLE `music` (
  `m_id` int(11) NOT NULL AUTO_INCREMENT,
  `language` varchar(100) DEFAULT NULL,
  `singer` varchar(100) DEFAULT NULL,
  `year` varchar(100) DEFAULT NULL,
  `file` varchar(100) DEFAULT NULL,
  `sname` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `music` */

insert  into `music`(`m_id`,`language`,`singer`,`year`,`file`,`sname`) values (1,'Malayalam','aa','2021','static/music/One_day.mp3','One_day'),(2,'Malayalam','aa','2021','static/music/20220624030542.wav','One_day'),(3,'Malayalam','aa','2021','static/music/20220624030542.wav','One_day'),(4,'Malayalam','aa','2022','static/music/20220624030542.wav','One_day'),(5,'Malayalam','yyy','2000','static/music/20220624030542.wav','ABBA_-_Dont_shup_me_down'),(6,'Malayalam','aa','1990','static/music/20220702004917.wav','Etho rathri'),(7,'Malayalam','aa','1990','static/music/20220702005140.wav','Uyire'),(8,'Malayalam','aa','2000','static/music/20220702005504.wav','One_day'),(9,'Malayalam','aa','2021','static/music/20220702005620.wav','One_day'),(10,'Malayalam','aa','2022','static/music/20220702005705.wav','Uyire'),(11,'Malayalam','aa','1990','static/music/20220702010237.wav','One_day'),(12,'Malayalam','aa','1990','static/music/20220702010352.wav','One_day'),(13,'Malayalam','aa','2000','static/music/20220702011024.wav','Avril_Lavigne_-_Bite_Me'),(14,'Malayalam','aa','2000','static/music/20220702011100.wav','The_Weeknd_-_Save_Your_Tears_Official_Music_Video');

/*Table structure for table `playlist` */

DROP TABLE IF EXISTS `playlist`;

CREATE TABLE `playlist` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `music` varchar(500) DEFAULT NULL,
  `type` varchar(500) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `playlist` */

insert  into `playlist`(`pid`,`user_id`,`music`,`type`,`description`,`date`) values (1,13,'abc','aaa','sample des','12/12/12'),(2,15,'storage_emulated_0_Android_media_com.whatsapp_WhatsApp_Media_WhatsApp_Audio_AUD-20220519-WA0073.opus','h','hhhh','2022-07-01');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`lid`,`fname`,`lname`,`dob`,`place`,`post`,`pin`,`gender`,`phone`,`email`) values (1,2,'Amal','CT','1970-01-20','Malappuram','Malappuram',679329,'Male',9080706050,'amal@gmail.com'),(2,3,'anagha','k','2022-01-10','calicut','cct',5555,'female',5555666,'amalajkj'),(3,4,'hari','DT','2022-01-12','kannur','kannur',2222,'male',1598745,'jhbhj'),(4,4,'Hamna','K','2000-01-02','Malappuram','Malappuram',679329,'Female',9895817109,'hamnakermd@gmail.com'),(8,8,'nowri','kv','1998-05-04','calicut','calicut',987654,'Female',9898989800,'hh@gmail.com'),(9,9,'ha','llo','2000-05-05','cct','cct',12344,'Female',98754311,'hasd@gmail.com'),(10,10,'ha','llo','2000-05-05','cct','cct',12344,'Female',98754311,'hasd@gmail.com'),(13,13,'Hamna','K','0000-00-00','Wndr','wndr',679111,'Female',9895816809,'mn@gmail.com'),(14,14,'manu','hh','2000-08-09','knr','knr',678905,'Male',9876543219,'har@gmail.com'),(15,15,'naveen','john','1993-04-21','kakkayam','kakkayam',673615,'Male',9876543210,'naveentjohn@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
