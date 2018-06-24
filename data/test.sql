/*
 Navicat MySQL Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 50714
 Source Host           : localhost
 Source Database       : test

 Target Server Type    : MySQL
 Target Server Version : 50714
 File Encoding         : utf-8

 Date: 06/24/2018 15:32:24 PM
*/

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `DZ`
-- ----------------------------
DROP TABLE IF EXISTS `DZ`;
CREATE TABLE `DZ` (
  `SJC` datetime NOT NULL COMMENT '时间戳',
  `GRGH` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `LJGH` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `DZ` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `FLAG` varchar(20) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `DZ`
-- ----------------------------
BEGIN;
INSERT INTO `DZ` VALUES ('2018-06-21 15:37:25', '1A', '0A', 'action1', 'start'), ('2018-06-21 15:38:23', '1A', '0A', 'action1', 'start'), ('2018-06-21 15:41:04', '1A', '0A', 'action1', 'start'), ('2018-06-21 15:41:14', '1A', '0A', 'action2', 'start'), ('2018-06-21 15:41:24', '1A', '0A', 'ction2', 'end'), ('2018-06-21 15:47:17', '1A', '0A', 'action3', 'start'), ('2018-06-21 15:47:33', '1A', '0A', 'ction3', 'end');
COMMIT;

-- ----------------------------
--  Table structure for `LOSS`
-- ----------------------------
DROP TABLE IF EXISTS `LOSS`;
CREATE TABLE `LOSS` (
  `SJ` date NOT NULL,
  `ACTION1` int(11) DEFAULT NULL,
  `ACTION2` int(11) DEFAULT NULL,
  `ACTION3` int(11) DEFAULT NULL,
  `ACTION4` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Table structure for `OEE_DATE`
-- ----------------------------
DROP TABLE IF EXISTS `OEE_DATE`;
CREATE TABLE `OEE_DATE` (
  `SJC` date NOT NULL,
  `O8` float DEFAULT NULL,
  `O9` float DEFAULT NULL,
  `O10` float DEFAULT NULL,
  `O11` float DEFAULT NULL,
  `O12` float DEFAULT NULL,
  `O13` float DEFAULT NULL,
  `O14` float DEFAULT NULL,
  `O15` float DEFAULT NULL,
  `O16` float DEFAULT NULL,
  `O17` float DEFAULT NULL,
  `O18` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `OEE_DATE`
-- ----------------------------
BEGIN;
INSERT INTO `OEE_DATE` VALUES ('2018-06-24', '9', null, null, null, null, null, null, null, null, null, null);
COMMIT;

-- ----------------------------
--  Table structure for `SC`
-- ----------------------------
DROP TABLE IF EXISTS `SC`;
CREATE TABLE `SC` (
  `Sno` mediumtext COLLATE utf8_bin,
  `Cno` int(11) DEFAULT NULL,
  `Grade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `SC`
-- ----------------------------
BEGIN;
INSERT INTO `SC` VALUES ('200215121', '1', '92'), ('200215121', '2', '85'), ('200215121', '3', '88'), ('200215122', '2', '90'), ('200215122', '3', '80'), ('200215123', '1', '60'), ('200215124', '1', '79');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
