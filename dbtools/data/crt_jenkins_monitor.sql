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

 Date: 14/09/2018 14:37:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for crt_jenkins_monitor
-- ----------------------------
DROP TABLE IF EXISTS `crt_jenkins_monitor`;
CREATE TABLE `crt_jenkins_monitor`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `jenkins_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `crt_jenkins_monitor_task_jenkins_id_job_id_64d55940_uniq`(`task`, `jenkins_id`, `job_id`) USING BTREE,
  INDEX `crt_jenkins_monitor_jenkins_id_f0ff8feb_fk_crt_jenkins_info_id`(`jenkins_id`) USING BTREE,
  INDEX `crt_jenkins_monitor_job_id_af2d5f4e_fk_crt_jenkins_job_id`(`job_id`) USING BTREE,
  CONSTRAINT `crt_jenkins_monitor_jenkins_id_f0ff8feb_fk_crt_jenkins_info_id` FOREIGN KEY (`jenkins_id`) REFERENCES `crt_jenkins_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `crt_jenkins_monitor_job_id_af2d5f4e_fk_crt_jenkins_job_id` FOREIGN KEY (`job_id`) REFERENCES `crt_jenkins_job` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of crt_jenkins_monitor
-- ----------------------------
INSERT INTO `crt_jenkins_monitor` VALUES (1, 'LOAD_TESTLINE', 1, 1);
INSERT INTO `crt_jenkins_monitor` VALUES (2, 'LOAD_TESTLINE', 1, 2);
INSERT INTO `crt_jenkins_monitor` VALUES (3, 'LOAD_TESTLINE', 1, 3);
INSERT INTO `crt_jenkins_monitor` VALUES (4, 'LOAD_TESTLINE', 1, 4);
INSERT INTO `crt_jenkins_monitor` VALUES (5, 'LOAD_TESTLINE', 1, 5);
INSERT INTO `crt_jenkins_monitor` VALUES (6, 'LOAD_TESTLINE', 1, 6);
INSERT INTO `crt_jenkins_monitor` VALUES (7, 'LOAD_TESTLINE', 2, 1);
INSERT INTO `crt_jenkins_monitor` VALUES (8, 'LOAD_TESTLINE', 2, 2);
INSERT INTO `crt_jenkins_monitor` VALUES (9, 'LOAD_TESTLINE', 2, 3);
INSERT INTO `crt_jenkins_monitor` VALUES (10, 'LOAD_TESTLINE', 3, 4);
INSERT INTO `crt_jenkins_monitor` VALUES (11, 'LOAD_TESTLINE', 3, 5);
INSERT INTO `crt_jenkins_monitor` VALUES (12, 'LOAD_TESTLINE', 3, 6);
INSERT INTO `crt_jenkins_monitor` VALUES (13, 'LOAD_TESTLINE', 4, 7);
INSERT INTO `crt_jenkins_monitor` VALUES (14, 'LOAD_TESTLINE', 4, 8);
INSERT INTO `crt_jenkins_monitor` VALUES (15, 'LOAD_TESTLINE', 5, 7);
INSERT INTO `crt_jenkins_monitor` VALUES (16, 'LOAD_TESTLINE', 5, 8);

SET FOREIGN_KEY_CHECKS = 1;
