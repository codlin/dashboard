/*
 Navicat Premium Data Transfer

 Source Server         : 135.242.139.122
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : 135.242.139.122:33306
 Source Schema         : crt_db

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 14/09/2018 14:37:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for crt_jenkins_info
-- ----------------------------
DROP TABLE IF EXISTS `crt_jenkins_info`;
CREATE TABLE `crt_jenkins_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `passwd` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `url`(`url`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of crt_jenkins_info
-- ----------------------------
INSERT INTO `crt_jenkins_info` VALUES (1, 'http://10.52.200.190', 'scpadm', 'scpadm');
INSERT INTO `crt_jenkins_info` VALUES (2, 'http://135.242.139.122:8085', 'scpadm', 'scpadm');
INSERT INTO `crt_jenkins_info` VALUES (3, 'http://135.242.139.122:8086', 'scpadm', 'scpadm');
INSERT INTO `crt_jenkins_info` VALUES (4, 'http://135.242.139.122:8087', 'scpadm', 'scpadm');
INSERT INTO `crt_jenkins_info` VALUES (5, 'http://135.242.139.122:8088', 'scpadm', 'scpadm');

SET FOREIGN_KEY_CHECKS = 1;
