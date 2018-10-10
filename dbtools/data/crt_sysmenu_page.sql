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

 Date: 14/09/2018 14:36:52
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for crt_sysmenu_page
-- ----------------------------
DROP TABLE IF EXISTS `crt_sysmenu_page`;
CREATE TABLE `crt_sysmenu_page`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `index` smallint(5) UNSIGNED NOT NULL,
  `level` smallint(5) UNSIGNED NOT NULL,
  `group` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `text` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
