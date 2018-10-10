/*
 Navicat Premium Data Transfer

 Source Server         : 10.66.11.20
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : 10.66.11.20:33306
 Source Schema         : crt_db

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : 65001

 Date: 14/09/2018 14:37:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for crt_jenkins_job
-- ----------------------------
DROP TABLE IF EXISTS `crt_jenkins_job`;
CREATE TABLE `crt_jenkins_job`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `job`(`job`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of crt_jenkins_job
-- ----------------------------
INSERT INTO `crt_jenkins_job` VALUES (7, 'check_site_state_cFZC_AICT');
INSERT INTO `crt_jenkins_job` VALUES (1, 'check_site_state_FDD_AICT3');
INSERT INTO `crt_jenkins_job` VALUES (4, 'check_site_state_TDD_AICT3');
INSERT INTO `crt_jenkins_job` VALUES (2, 'healthCheckup_AICT3_FDD');
INSERT INTO `crt_jenkins_job` VALUES (5, 'healthCheckup_AICT3_TDD');
INSERT INTO `crt_jenkins_job` VALUES (8, 'upgrade_cFZC_AICT');
INSERT INTO `crt_jenkins_job` VALUES (3, 'upgrade_FDD_AICT3');
INSERT INTO `crt_jenkins_job` VALUES (6, 'upgrade_TDD_AICT3');

SET FOREIGN_KEY_CHECKS = 1;
