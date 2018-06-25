/*
Navicat MySQL Data Transfer

Source Server         : wqw
Source Server Version : 50525
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50525
File Encoding         : 65001

Date: 2018-06-25 16:43:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dz
-- ----------------------------
DROP TABLE IF EXISTS `dz`;
CREATE TABLE `dz` (
  `SJC` datetime NOT NULL COMMENT '时间戳',
  `GRGH` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `LJGH` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `DZ` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `FLAG` varchar(20) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of dz
-- ----------------------------
INSERT INTO `dz` VALUES ('2018-06-21 15:37:25', '1A', '0A', 'action1', 'start');
INSERT INTO `dz` VALUES ('2018-06-21 15:38:23', '1A', '0A', 'action1', 'start');
INSERT INTO `dz` VALUES ('2018-06-21 15:41:04', '1A', '0A', 'action1', 'start');
INSERT INTO `dz` VALUES ('2018-06-21 15:41:14', '1A', '0A', 'action2', 'start');
INSERT INTO `dz` VALUES ('2018-06-21 15:41:24', '1A', '0A', 'ction2', 'end');
INSERT INTO `dz` VALUES ('2018-06-21 15:47:17', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-21 15:47:33', '1A', '0A', 'ction3', 'end');
INSERT INTO `dz` VALUES ('2018-06-25 16:30:59', '1A', '0A', 'action1', 'start');
INSERT INTO `dz` VALUES ('2018-06-25 16:31:15', '1A', '0A', 'action1', 'end');

-- ----------------------------
-- Table structure for loss
-- ----------------------------
DROP TABLE IF EXISTS `loss`;
CREATE TABLE `loss` (
  `SJ` date NOT NULL,
  `ACTION1` int(11) DEFAULT NULL,
  `ACTION2` int(11) DEFAULT NULL,
  `ACTION3` int(11) DEFAULT NULL,
  `ACTION4` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of loss
-- ----------------------------
INSERT INTO `loss` VALUES ('2018-06-24', '100', '200', '300', '400');

-- ----------------------------
-- Table structure for oee_date
-- ----------------------------
DROP TABLE IF EXISTS `oee_date`;
CREATE TABLE `oee_date` (
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
-- Records of oee_date
-- ----------------------------
INSERT INTO `oee_date` VALUES ('2018-06-24', '80', '82', '85', '78', '60', null, null, null, null, null, null);

-- ----------------------------
-- Table structure for sc
-- ----------------------------
DROP TABLE IF EXISTS `sc`;
CREATE TABLE `sc` (
  `Sno` mediumtext COLLATE utf8_bin,
  `Cno` int(11) DEFAULT NULL,
  `Grade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of sc
-- ----------------------------
INSERT INTO `sc` VALUES (0x323030323135313231, '1', '92');
INSERT INTO `sc` VALUES (0x323030323135313231, '2', '85');
INSERT INTO `sc` VALUES (0x323030323135313231, '3', '88');
INSERT INTO `sc` VALUES (0x323030323135313232, '2', '90');
INSERT INTO `sc` VALUES (0x323030323135313232, '3', '80');
INSERT INTO `sc` VALUES (0x323030323135313233, '1', '60');
INSERT INTO `sc` VALUES (0x323030323135313234, '1', '79');
