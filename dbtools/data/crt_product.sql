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

 Date: 14/09/2018 14:36:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for crt_product
-- ----------------------------
DROP TABLE IF EXISTS `crt_product`;
CREATE TABLE `crt_product`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `text` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of crt_product
-- ----------------------------
INSERT INTO `crt_product` VALUES (1, 'fzmfdd', 'FZM FDD');
INSERT INTO `crt_product` VALUES (2, 'fzmtdd', 'FZM TDD');
INSERT INTO `crt_product` VALUES (3, 'cfzcfdd', 'CFZC FDD');
INSERT INTO `crt_product` VALUES (4, 'cfzctdd', 'CFZC TDD');

SET FOREIGN_KEY_CHECKS = 1;
