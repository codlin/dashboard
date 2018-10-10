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

 Date: 14/09/2018 14:37:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for crt_testcase
-- ----------------------------
DROP TABLE IF EXISTS `crt_testcase`;
CREATE TABLE `crt_testcase`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `casename` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `path_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `casename`(`casename`) USING BTREE,
  INDEX `crt_testcase_path_id_313e11f8_fk_crt_testcasepath_id`(`path_id`) USING BTREE,
  CONSTRAINT `crt_testcase_path_id_313e11f8_fk_crt_testcasepath_id` FOREIGN KEY (`path_id`) REFERENCES `crt_testcasepath` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 396 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of crt_testcase
-- ----------------------------
INSERT INTO `crt_testcase` VALUES (1, 'LTE4443_Swap_of_2nd_Unlicensed_Cell_for_2nd_Licensed_Cell_in_1L_+_2U_Configuration', NULL);
INSERT INTO `crt_testcase` VALUES (2, 'LTE4443_Addition_of_3rd_Cell_Licensed_in_1L+1U_Configuration', NULL);
INSERT INTO `crt_testcase` VALUES (3, 'LTE4443_Deleting_a_Licensed_Cell_in_2L_+_1U_Configuration', NULL);
INSERT INTO `crt_testcase` VALUES (4, 'LTE4443_Deleting_a_Unlicensed_Cell_in_2L_+_1U_Configuration_CA_Still_Enabled', NULL);
INSERT INTO `crt_testcase` VALUES (5, 'LTE4443_Swap_of_2nd_Licensed_Cell_for_2nd_Unlicensed_Cell', NULL);
INSERT INTO `crt_testcase` VALUES (6, 'LTE4443_Deleting_an_Unlicensed_Cell_in_2L_+_1U_Configuration_Ca_Disabled', NULL);
INSERT INTO `crt_testcase` VALUES (7, 'LTE4443_Addition_of_3rd_Cell_Unlicensed_in_2L_Configuration', NULL);
INSERT INTO `crt_testcase` VALUES (8, 'LTE4483_03_Feature_Deactivation', NULL);
INSERT INTO `crt_testcase` VALUES (9, 'LTE4483_01_Feature_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (10, 'NMAP_Scan_ETH_ON_RnD_ON_LMT', NULL);
INSERT INTO `crt_testcase` VALUES (11, 'NMAP_Scan_ETH_ON_SSH_ON_LMT', NULL);
INSERT INTO `crt_testcase` VALUES (12, 'NMAP_Scan_ETH_OFF_VLAN_LMT', NULL);
INSERT INTO `crt_testcase` VALUES (13, 'NMAP_Scan_ETH_ON_SSH_OFF_LMT', NULL);
INSERT INTO `crt_testcase` VALUES (14, 'NMAP_Scan_ETH_ON_RnD_OFF_LMT', NULL);
INSERT INTO `crt_testcase` VALUES (15, 'TC26179_Remote_Syslogs', NULL);
INSERT INTO `crt_testcase` VALUES (16, 'TC26177_Remote_Syslogs', NULL);
INSERT INTO `crt_testcase` VALUES (17, 'TC0_import_certification', NULL);
INSERT INTO `crt_testcase` VALUES (18, 'Automated_BTS_Performance_Management_Measurements_Disable_And_Enable', NULL);
INSERT INTO `crt_testcase` VALUES (19, 'Automated_BTS_Performance_Management_PM_Upload_Period_Change_30min_To_15min', NULL);
INSERT INTO `crt_testcase` VALUES (20, 'PortSwap_Configuration_File_Same_File_Is_Downloaded', NULL);
INSERT INTO `crt_testcase` VALUES (21, 'PortSwap_Cell_Blocking_And_Unblocking', NULL);
INSERT INTO `crt_testcase` VALUES (22, 'PortSwap_BTS_Startup_Reset_Into_Test_Dedicated_State', NULL);
INSERT INTO `crt_testcase` VALUES (23, 'PortSwap_BTS_Startup_Site_Reset', NULL);
INSERT INTO `crt_testcase` VALUES (24, 'PortSwap_Automated_BTS_Performance_Management_Measurements_Disable_And_Enable', NULL);
INSERT INTO `crt_testcase` VALUES (25, 'LTE439-R_X2_Intra-Freq_Handover_With_SGW_HO', NULL);
INSERT INTO `crt_testcase` VALUES (26, 'IPv6_4Vlan_20MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (27, 'IPv6_4Vlan_20MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (28, 'IPv6_Virtual_IP_4Vlan_15MHz', NULL);
INSERT INTO `crt_testcase` VALUES (29, 'IPv6_4Vlan_15MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (30, 'IPv6_4Vlan_15MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (31, 'IPv6_Virtual_IP_4Vlan_20MHz', NULL);
INSERT INTO `crt_testcase` VALUES (32, 'IPv6_4Vlan_20MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (33, 'IPv6_4Vlan_15MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (34, 'LTE4411_03_Feature_Deactivation_of_LTE4411', NULL);
INSERT INTO `crt_testcase` VALUES (35, 'LTE4411_02_Intra_frequency_HO_for_CAT-M1', NULL);
INSERT INTO `crt_testcase` VALUES (36, 'LTE4411_01_Feature_Activation_of_LTE4411', NULL);
INSERT INTO `crt_testcase` VALUES (37, 'LTE2959-L_CP_08_SFN_To_Standalone.robot_for_ENB723', NULL);
INSERT INTO `crt_testcase` VALUES (38, 'LTE2959-L_CP_02_Standalone_To_SFN_With_UldlCA_Enable_For_ENB722', NULL);
INSERT INTO `crt_testcase` VALUES (39, 'LTE2959-L_CP_03_Stable_Throughput_Over_Dedicated_GBR_Bearers_On_QCI2_QCI3_And_QCI4_Simultaneously', NULL);
INSERT INTO `crt_testcase` VALUES (40, 'LTE2959-L_CP_05_Maximum_Traffic_Stability_Test_On_SFN_DL_CA_UDP_UE_Movement', NULL);
INSERT INTO `crt_testcase` VALUES (41, 'LTE2959-L_CP_07_Intra_ENB_Handover_For_Dual_Cell_SFN_Configuration', NULL);
INSERT INTO `crt_testcase` VALUES (42, 'LTE2959-L_CP_04_Successful_Attach_to_dual_cell_CA_SFN_on_bandwidth_10+15MHz', NULL);
INSERT INTO `crt_testcase` VALUES (43, 'LTE2959-L_CP_06_LTE3637:_2FZPs_can_be_configured_with_the_same_switch_hub_for_cell_split_And_FZ_Ants_under_one_mFZP_can_be_moved_to_the_second_master_FZP', NULL);
INSERT INTO `crt_testcase` VALUES (44, 'LTE2959-L_CP_01_Standalone_To_SFN_With_UldlCA_Enable_For_ENB723', NULL);
INSERT INTO `crt_testcase` VALUES (45, 'LTE2774-A_01_Parameters_Recommission_With_Feature_Activation.robot', NULL);
INSERT INTO `crt_testcase` VALUES (46, 'FZM_Case_LTE3756-B-f-10MHz_R1_And_20MHz_R2_And_10_MHZ_R3_2CC_DL_FW2PIRA_LAA_-_2CC_DL_CA_Lock_Scell_during_CA_data_transfer,_Pcell_on_R1_OM_only_no_UE', NULL);
INSERT INTO `crt_testcase` VALUES (47, 'LTE2774-A_02_Interaction_With_VoLTE_Uplink_Coverage_Boosting_in_Regular_TX_Mode.robot', NULL);
INSERT INTO `crt_testcase` VALUES (48, 'FZM_Case_LTE3756-B-f-10MHz_R1_And_20MHz_R2_And_10_MHZ_R3_2CC_DL_FW2PIRA_LAA_-_2CC_DL_CA_Pcell_on_R1,_Scell_on_R2_OM_only_no_UE', NULL);
INSERT INTO `crt_testcase` VALUES (49, 'FZM_Case_LTE3756-B-f-10MHz_R1_And_20MHz_R2_And_10_MHZ_R3_2CC_DL_FW2PIRA_LAA_-_2CC_DL_CA_Pcell_on_R1,_Scell_on_R3_OM_only_no_UE', NULL);
INSERT INTO `crt_testcase` VALUES (50, 'LTE2774-A_03_Feature_Deactivation_at_Cell_reconfiguration.robot', NULL);
INSERT INTO `crt_testcase` VALUES (51, 'FZM_Case_LTE3756-B-f-10MHz_R1_And_20MHz_R2_And_10_MHZ_R3_2CC_DL_FW2PIRA_LTE-U_-_2CC_DL_CA_Pcell_on_R1,_Scell_on_R2_OM_only_no_UE', NULL);
INSERT INTO `crt_testcase` VALUES (52, 'LBT5699-A_00_Initial_Test_Environment_And_Check_New_Counters_Are_Added', NULL);
INSERT INTO `crt_testcase` VALUES (53, 'FZM_Case_LTE3756-A-f-20MHz_R1_And_10MHz_R2_And_10MHz_R3_256QAM_3CC_DL_CA_-_3CC_DL_CA_Block_one_Scell_during_CA_data_transfer,_Pcell_on_R2_OM_only_no_UE', NULL);
INSERT INTO `crt_testcase` VALUES (54, 'LTE4708_Attach_UE_and_Reset_S1', NULL);
INSERT INTO `crt_testcase` VALUES (55, 'LBT5699-A_02_Initial_Burst_Waiting_For_Scheduling_Applicability_Delay_In_DL_PM_Counter_Check', NULL);
INSERT INTO `crt_testcase` VALUES (56, 'FZM_Case_LTE3756-A-f-10MHz_R1_And_10MHz_R2_And_20MHz_R3_3CC_DL_CA_-_3CC_DL_CA_Pcell_on_R1,_Scell_on_R2andR3_OM_only_no_UE', NULL);
INSERT INTO `crt_testcase` VALUES (57, 'LBT5699-A_01_Remove_Old_Initial_Brust_Scheduling_Delay_Counters_From_LTE3778&LTE3865', NULL);
INSERT INTO `crt_testcase` VALUES (58, 'LBT5699-A_03_Initial_Burst_Waiting_For_Scheduling_Applicability_Delay_In_DL_CA_For_NonGBR', NULL);
INSERT INTO `crt_testcase` VALUES (59, 'LTE2860-A-a-6', NULL);
INSERT INTO `crt_testcase` VALUES (60, 'LTE2860-A-c-3', NULL);
INSERT INTO `crt_testcase` VALUES (61, 'LTE2860-A-a-5', NULL);
INSERT INTO `crt_testcase` VALUES (62, 'LTE2860-A-c-5', NULL);
INSERT INTO `crt_testcase` VALUES (63, 'LTE2860-A-a-3', NULL);
INSERT INTO `crt_testcase` VALUES (64, 'LTE2860-A-c-1-2', NULL);
INSERT INTO `crt_testcase` VALUES (65, 'LTE2860-A-c-4', NULL);
INSERT INTO `crt_testcase` VALUES (66, 'LBT5523_02_Site_Reset_Service_Downtime_With_Two_Cell', NULL);
INSERT INTO `crt_testcase` VALUES (67, 'LBT5523_01_eNB_Performance_For_A_Consistency_Check_Of_A_Downloaded_Configuration', NULL);
INSERT INTO `crt_testcase` VALUES (68, 'LBT5523_05_Cold_Reset_BTS_Manual', NULL);
INSERT INTO `crt_testcase` VALUES (69, 'LBT5523_04_Duration_Of_Alarm_Reporting', NULL);
INSERT INTO `crt_testcase` VALUES (70, 'LTE3060.0001_-_Alarm_monitoring_from_BTSSM_-_DyingGasp_ethOAM', NULL);
INSERT INTO `crt_testcase` VALUES (71, 'FZ.OM.PERF.0022_-_eNB_Reset_Time_Cold', NULL);
INSERT INTO `crt_testcase` VALUES (72, 'LBT5523_03_Cold_Reset_BTS_By_Command', NULL);
INSERT INTO `crt_testcase` VALUES (73, 'LTE2675_05_Two_Scells_Change_Frequency', NULL);
INSERT INTO `crt_testcase` VALUES (74, 'LTE2675_02_Channel_Selection_Modify_lteuContiguousChannelPriority_during_data_transfer', NULL);
INSERT INTO `crt_testcase` VALUES (75, 'FDD_10MHz_BTS_Activation_256QAM', NULL);
INSERT INTO `crt_testcase` VALUES (76, 'LTE2675_01_Enable_Feature', NULL);
INSERT INTO `crt_testcase` VALUES (77, 'FDD_10MHz_256QAM_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (78, 'FDD_10MHz_256QAM_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (79, 'LTE2675_04_One_Scell_Changes_Frequency', NULL);
INSERT INTO `crt_testcase` VALUES (80, 'FDD_10MHz_256QAM_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (81, 'LTE2675_03_Channel_Selection_Modify_The_List_Of_Wifi_Channels_During_Data_Transfer', NULL);
INSERT INTO `crt_testcase` VALUES (82, 'LTE3819_15_Coexistence_of_Cat-M_and_NB_IoT_UEs_on_10_MHz_cells_without_LTE2664_interworking', NULL);
INSERT INTO `crt_testcase` VALUES (83, 'LTE3819_16_Coexistence_of_Cat-M_and_NB_IoT_UEs_on_10_MHz_cells_with_LTE2664_interworking', NULL);
INSERT INTO `crt_testcase` VALUES (84, 'LTE3128_05_Attach_Cat-M_UE_and_run_UDP_UL_t-put_on_9_and_7_mcs', NULL);
INSERT INTO `crt_testcase` VALUES (85, 'LTE3128_02_Attach_Cat-M_UE', NULL);
INSERT INTO `crt_testcase` VALUES (86, 'LTE3128_03_Attach_Cat-M_UE_and_run_UDP_DL_and_UL_t-put_7_and_7_mcs', NULL);
INSERT INTO `crt_testcase` VALUES (87, 'LTE3870_Attach_UE_And_Modify_Parameter_Impact_On_Connection', NULL);
INSERT INTO `crt_testcase` VALUES (88, 'LTE3128_01_Attach_Cat-M_UE_and_check_RRC_Connected_to_Idle_state', NULL);
INSERT INTO `crt_testcase` VALUES (89, 'LTE3128_04_Attach_Cat-M_UE_and_run_UDP_DL_and_UL_t-put_9_and_10_mcs', NULL);
INSERT INTO `crt_testcase` VALUES (90, 'FDD_3MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (91, 'FDD_10MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (92, 'FDD_10MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (93, 'FDD_10MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (94, 'FDD_20MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (95, 'FDD_20MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (96, 'FDD_10MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (97, 'FDD_20MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (98, 'FDD_20MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (99, 'FDD_3MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (100, 'FDD_3MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (101, 'FDD_20MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (102, 'FDD_3MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (103, 'FDD_20MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (104, 'FDD_10MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (105, 'FDD_3MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (106, 'FDD_20MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (107, 'FDD_10MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (108, 'FDD_10MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (109, 'FDD_10MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (110, 'FDD_3MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (111, 'FDD_10MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (112, 'FDD_20MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (113, 'FDD_10MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (114, 'FDD_20MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (115, 'Graceful_Cell_Shutdown', NULL);
INSERT INTO `crt_testcase` VALUES (116, 'LTE3397_5_Object_locking_required_param_in_delta_commission', NULL);
INSERT INTO `crt_testcase` VALUES (117, 'LTE3397_4_Plan_provisioning_with_TRS_reset_required_parameter', NULL);
INSERT INTO `crt_testcase` VALUES (118, 'LTE2729_01_Verify_the_enabling_of_feature', NULL);
INSERT INTO `crt_testcase` VALUES (119, 'LTE2729_03_Feature_Activation_by_creating_CAREL', NULL);
INSERT INTO `crt_testcase` VALUES (120, 'Configuration_File_Same_File_Is_Downloaded', NULL);
INSERT INTO `crt_testcase` VALUES (121, 'LTE3397_1_Plan_provisioning_with_BTS_no_reset_required_parameter', NULL);
INSERT INTO `crt_testcase` VALUES (122, 'LTE3397_3_Plan_provisioning_with_BTS_reset_required_parameter', NULL);
INSERT INTO `crt_testcase` VALUES (123, 'LTE3397_2_Plan_provisioning_with_TRS_no_reset_required_parameter', NULL);
INSERT INTO `crt_testcase` VALUES (124, 'Automated_BTS_Performance_Management_Cell_Block_15min', NULL);
INSERT INTO `crt_testcase` VALUES (125, 'LTE3296_1_Activate_Validate_plan_against_detected_hardware', NULL);
INSERT INTO `crt_testcase` VALUES (126, 'LTE3296_2_Activate_deactivate_location_lock', NULL);
INSERT INTO `crt_testcase` VALUES (127, 'LTE1858-A_Changing_CA_activation_method,_eNodeB_reset_and_200M_throughput_with_CA_verification', NULL);
INSERT INTO `crt_testcase` VALUES (128, 'Changing_CA_activation_method,_eNodeB_reset_and_200M_throughput_with_CA_verification', NULL);
INSERT INTO `crt_testcase` VALUES (129, '200M_DL_and_10M_UL_data_transfer_with_CA_verification', NULL);
INSERT INTO `crt_testcase` VALUES (130, 'LTE1858-A_Parsing_commissioning_to_activate_LTE1858', NULL);
INSERT INTO `crt_testcase` VALUES (131, 'LTE1858-A_200M_DL_and_10M_UL_data_transfer_with_CA_verification', NULL);
INSERT INTO `crt_testcase` VALUES (132, 'Parsing_commissioning_to_activate_LTE1858', NULL);
INSERT INTO `crt_testcase` VALUES (133, 'LTE2946_01_UPlane_DL_Latency_of_performing_inter-freq_X2_handover', NULL);
INSERT INTO `crt_testcase` VALUES (134, 'LTE2946_01_UPlane_DL_Latency_of_performing_inter-freq_X2_handover_with_Cplane', NULL);
INSERT INTO `crt_testcase` VALUES (135, 'LTE2946_04_Ue_Ping_UL_data_transfer', NULL);
INSERT INTO `crt_testcase` VALUES (136, 'LTE3011_FDD_20MHz_BTS_Activation_ULCA', NULL);
INSERT INTO `crt_testcase` VALUES (137, 'LTE2946_03_Ue_attach_and_detach_latency_test', NULL);
INSERT INTO `crt_testcase` VALUES (138, 'LTE2946_02_UPlane_UL_Latency_of_performing_inter-freq_X2_handover', NULL);
INSERT INTO `crt_testcase` VALUES (139, 'FZ.OM.PERF.0013_-_SWM_-_Duration_of_a_manual_triggered_SW_configuration_upload_for_single_BTS_eNB', NULL);
INSERT INTO `crt_testcase` VALUES (140, 'FZ.OM.PERF.0001_-_ASC_-_Autoconnection_Performance_on_EMSSIM', NULL);
INSERT INTO `crt_testcase` VALUES (141, 'FZ.OM.PERF.0027_-_PM_data_upload', NULL);
INSERT INTO `crt_testcase` VALUES (142, '02_LBT5243_Paramter_Deactivation', NULL);
INSERT INTO `crt_testcase` VALUES (143, 'FZ.OM.PERF.0011_-_CM_-_CM_plan_provision_with_30_parameters_-_EMSSIM', NULL);
INSERT INTO `crt_testcase` VALUES (144, 'FZ.OM.PERF.0022_-_eNB_Reset_Time_-_Remote_power_cycle_executed_via_FZM', NULL);
INSERT INTO `crt_testcase` VALUES (145, 'FZ.OM.PERF.0009_-_CM_-_CM_plan_upload_-_EMSSIM_01', NULL);
INSERT INTO `crt_testcase` VALUES (146, 'FZ.OM.PERF.0023_-_ENBM_-_eNB_Reset_Time_Warm', NULL);
INSERT INTO `crt_testcase` VALUES (147, 'FZ.OM.REGR.0011_-_Test_ConnectionEstablishedReply_NackReason_-_EMSSIM', NULL);
INSERT INTO `crt_testcase` VALUES (148, 'FZ.OM.PERF.0020_-_FM_-_Creation_and_uploading_of_standard_symptom_data', NULL);
INSERT INTO `crt_testcase` VALUES (149, '01_LBT5243_Paramter_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (150, 'FZ.OM.PERF.0010_-_CM_-_Configuration_plan_activation_for_a_single_BTS_eNB', NULL);
INSERT INTO `crt_testcase` VALUES (151, 'ANR_Handover_Inter_eNB_Handover_via_X2_PM_Counters', NULL);
INSERT INTO `crt_testcase` VALUES (152, 'ANR_S1_Handover_Inter_eNB_PM_Counters', NULL);
INSERT INTO `crt_testcase` VALUES (153, 'Adjacent_Cell_Configuration_ANR_Handover_Inter_eNB_Handover_via_X2', NULL);
INSERT INTO `crt_testcase` VALUES (154, 'Adjacent_Cell_Configuration_ANR_S1_Handover_Inter_eNB', NULL);
INSERT INTO `crt_testcase` VALUES (155, 'LTE1679_Measurement_gaps_offset_alignment_to_DRX_disabled_offset', NULL);
INSERT INTO `crt_testcase` VALUES (156, 'Check_PM_Counters_ANR_Handover_Inter_eNB_Handover_via_X2', NULL);
INSERT INTO `crt_testcase` VALUES (157, 'Check_PM_Counters_ANR_S1_Handover_Inter_eNB', NULL);
INSERT INTO `crt_testcase` VALUES (158, 'ANR_Handover_Inter_eNB_Handover_via_X2_Interface_No_Data', NULL);
INSERT INTO `crt_testcase` VALUES (159, 'LTE1679_Measurement_gaps_offset_alignment_to_DRX_enabled_offset', NULL);
INSERT INTO `crt_testcase` VALUES (160, 'ANR_S1_Handover_Inter_eNB_Handover_via_S1_Interface_Intra_Band_IFHO_UDP_Data', NULL);
INSERT INTO `crt_testcase` VALUES (161, 'LBT5628_02_Attach_UE_And_Verify_Max_DL_UL_TPUT_For_FWEE_As_Master', NULL);
INSERT INTO `crt_testcase` VALUES (162, 'LBT5628_01_Standalone_To_SFN_For_FWEE_As_Master', NULL);
INSERT INTO `crt_testcase` VALUES (163, 'LBT5628_03_SFN_Master_And_Ants_To_Standalone_For_FWEE_As_Master', NULL);
INSERT INTO `crt_testcase` VALUES (164, 'LTE2959-L_06_Alarm_LOS_Alarms_Vertification_On_SFN_ANT', NULL);
INSERT INTO `crt_testcase` VALUES (165, 'LTE2959-L_09_Disable_LTE2959-L_SFN_Feature', NULL);
INSERT INTO `crt_testcase` VALUES (166, 'LTE2959-L_07_Restore_Vendor_Certification', NULL);
INSERT INTO `crt_testcase` VALUES (167, 'LTE2959-L_03_Reset_Of_FZ_Master_With_Operator_Certificate', NULL);
INSERT INTO `crt_testcase` VALUES (168, 'LTE2959-L_01_Enable_LTE2959-L_SFN_Feature', NULL);
INSERT INTO `crt_testcase` VALUES (169, 'LTE2959-L_05_Reset_Of_FZ_Ant_With_Operator_Certificate', NULL);
INSERT INTO `crt_testcase` VALUES (170, 'LTE2959-L_02_CMP_Parameters_Recommisioning_With_BTSSM', NULL);
INSERT INTO `crt_testcase` VALUES (171, 'LTE2959-L_04_Alarm_LOS_Alarms_Vertification_On_SFN_Master', NULL);
INSERT INTO `crt_testcase` VALUES (172, 'LTE2959-L_08_Chang_some_parameter_and_wait_it_effect', NULL);
INSERT INTO `crt_testcase` VALUES (173, 'LTE2600-B_01_EIFx_Received_Packets_And_Octets_PM_Counters_Verify', NULL);
INSERT INTO `crt_testcase` VALUES (174, 'LTE2600-B_02_EIFx_Transmitted_Packets_And_Octets_PM_Counters_Verify', NULL);
INSERT INTO `crt_testcase` VALUES (175, 'LTE2600-B_04_PacketForwarding_PBG-EIF1_LMP-ran_DC-none_WIFI_enable', NULL);
INSERT INTO `crt_testcase` VALUES (176, 'LTE2600-B_03_Change_The_VLAN_ID_Online_And_Verify_PM_Counters', NULL);
INSERT INTO `crt_testcase` VALUES (177, '4Vlan_15MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (178, '4Vlan_20MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (179, '4Vlan_20MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (180, '4Vlan_15MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (181, '4Vlan_20MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (182, 'Virtual_IP_4Vlan_20MHz', NULL);
INSERT INTO `crt_testcase` VALUES (183, 'Virtual_IP_4Vlan_15MHz', NULL);
INSERT INTO `crt_testcase` VALUES (184, '4Vlan_15MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (185, 'LTE3552_06_Session_Start_On_Dedicated_PLMN', NULL);
INSERT INTO `crt_testcase` VALUES (186, 'LTE3552_03_Adding_SAI_To_MBSFNArea', NULL);
INSERT INTO `crt_testcase` VALUES (187, 'LTE2839_04_Number_of_sessions_falls_below_sessions-MBSFN_Area_Limit', NULL);
INSERT INTO `crt_testcase` VALUES (188, 'LTE3552_05_EMSsim_Overlap_Resolve', NULL);
INSERT INTO `crt_testcase` VALUES (189, 'LTE2839_01_Disabling_EMBMS_Enhancements_For_Public_Safety', NULL);
INSERT INTO `crt_testcase` VALUES (190, 'LTE3552_01_SyncArea_Session_Limit', NULL);
INSERT INTO `crt_testcase` VALUES (191, 'LTE2839_03_Number_of_sessions_fexceeds_sessions-MBSFN_Area_Limit', NULL);
INSERT INTO `crt_testcase` VALUES (192, 'LTE3279-Q_03_eMBMS_Sync_Parameters_Modification_via_Emssim', NULL);
INSERT INTO `crt_testcase` VALUES (193, 'LTE3279-Q_01_AutoAdjustLeapUTC_TAI_and_GregorianUTC_UTC', NULL);
INSERT INTO `crt_testcase` VALUES (194, 'LTE3552_02_MBSFN_Area_Limit', NULL);
INSERT INTO `crt_testcase` VALUES (195, 'LTE3552_04_MBSFN_Overlap_Config', NULL);
INSERT INTO `crt_testcase` VALUES (196, 'LTE2839_02_Enabling_EMBMS_Enhancements_For_Public_Safety', NULL);
INSERT INTO `crt_testcase` VALUES (197, 'LTE2839_00_Initial_eMBMS_Feature', NULL);
INSERT INTO `crt_testcase` VALUES (198, 'LTE3279-Q_02_eMBMS_ElapsedCountIncludesHeader_Check', NULL);
INSERT INTO `crt_testcase` VALUES (199, 'LTE3552_07_Session_Update_On_Dedicated_PLMN', NULL);
INSERT INTO `crt_testcase` VALUES (200, 'FDD_15MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (201, 'FDD_15MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (202, 'FDD_15MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (203, 'FDD_20MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (204, 'FDD_15MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (205, 'FDD_15MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (206, 'FDD_15MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (207, 'FDD_15MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (208, 'FDD_15MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (209, 'FDD_15MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (210, 'FDD_15MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (211, 'LBT5576_01_Snapshot_Collection_Robustness_Check', NULL);
INSERT INTO `crt_testcase` VALUES (212, 'LTE2807-A_02_Start_of_a_new_MBMS_session_M1_and_M3_over_IPv6', NULL);
INSERT INTO `crt_testcase` VALUES (213, 'LTE2807-A_04_Start_of_a_new_MBMS_session_M1_over_IPv4_and_M3_over_IPv6', NULL);
INSERT INTO `crt_testcase` VALUES (214, 'LTE2807-A_00_Initial_Embms_Environment_For_LTE2807-A', NULL);
INSERT INTO `crt_testcase` VALUES (215, 'LTE4597_03_Verify_command_line_attemps_to_fetch_all_supported_files', NULL);
INSERT INTO `crt_testcase` VALUES (216, 'LBT5518_01_PRS-14_Parameter_Coexistence_With_Cat-M', NULL);
INSERT INTO `crt_testcase` VALUES (217, 'LTE4597_01_Verify_BTS_Site_Manager_command_line', NULL);
INSERT INTO `crt_testcase` VALUES (218, 'LTE2807-A_03_Stop_a_MBMS_session_M1_and_M3_over_IPv6', NULL);
INSERT INTO `crt_testcase` VALUES (219, 'LBT5444_Verify_TaTimer_Special_Value_Infinity', NULL);
INSERT INTO `crt_testcase` VALUES (220, 'LTE4057-A-f_01_Check_New_Added_Counter', NULL);
INSERT INTO `crt_testcase` VALUES (221, 'LTE2807-A_01_Start_Of_MBMS_Service_Provision', NULL);
INSERT INTO `crt_testcase` VALUES (222, 'LTE4597_04_Verify_command_line_starts_SFP_monitor_and_stop_after_120_seconds', NULL);
INSERT INTO `crt_testcase` VALUES (223, 'LTE4597_02_Verify_command_line_block_unblock_site', NULL);
INSERT INTO `crt_testcase` VALUES (224, 'UERelay_FDD_5MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (225, 'UERelay_FDD_5MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (226, 'UERelay_FDD_5MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (227, 'UERelay_FDD_5MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (228, 'UERelay_FDD_5MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (229, 'UERelay_FDD_5MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (230, '4Vlan_5MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (231, '4Vlan_10MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (232, '4Vlan_10MHz_UL_UDP_Packet_Reassembly', NULL);
INSERT INTO `crt_testcase` VALUES (233, 'Virtual_IP_4Vlan_10MHz', NULL);
INSERT INTO `crt_testcase` VALUES (234, '4Vlan_10MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (235, '4Vlan_10MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (236, '4Vlan_5MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (237, 'Modify_TRS_Parameters_4Vlan_10MHz', NULL);
INSERT INTO `crt_testcase` VALUES (238, 'Virtual_IP_4Vlan_5MHz', NULL);
INSERT INTO `crt_testcase` VALUES (239, 'Traffic_Shapping_UL_UDP_4Vlan_10MHz', NULL);
INSERT INTO `crt_testcase` VALUES (240, 'Traffic_Shapping_UL_UDP_4Vlan_5MHz', NULL);
INSERT INTO `crt_testcase` VALUES (241, '4Vlan_5MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (242, 'PortSwap_BTS_Startup_BTS_Block_And_Unblock', NULL);
INSERT INTO `crt_testcase` VALUES (243, 'PortSwap_Automated_BTS_Power_Reset', NULL);
INSERT INTO `crt_testcase` VALUES (244, 'PortSwap_Automated_BTS_Recovery_LTE_Ping_Lost_Between_Node_CCS_And_Application', NULL);
INSERT INTO `crt_testcase` VALUES (245, 'PortSwap_Automated_BTS_Performance_Management_PM_Upload_Period_Change_30min_To_15min', NULL);
INSERT INTO `crt_testcase` VALUES (246, 'LTE2175_ERAB_REL_ENB_ACT_QCI7', NULL);
INSERT INTO `crt_testcase` VALUES (247, 'LTE2175_ERAB_REL_ENB_ACT_QCI6', NULL);
INSERT INTO `crt_testcase` VALUES (248, 'LTE2175_ERAB_REL_ENB_ACT_QCI5', NULL);
INSERT INTO `crt_testcase` VALUES (249, 'IPv6_4Vlan_5MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (250, 'IPv6_Traffic_Shapping_UL_UDP_4Vlan_10MHz', NULL);
INSERT INTO `crt_testcase` VALUES (251, 'IPv6_Virtual_IP_4Vlan_10MHz', NULL);
INSERT INTO `crt_testcase` VALUES (252, 'IPv6_4Vlan_5MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (253, 'IPv6_4Vlan_10MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (254, 'IPv6_4Vlan_10MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (255, 'IPv6_4Vlan_10MHz_UL_UDP_Packet_Reassembly', NULL);
INSERT INTO `crt_testcase` VALUES (256, 'IPv6_4Vlan_10MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (257, 'IPv6_4Vlan_5MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (258, 'IPv6_Virtual_IP_4Vlan_5MHz', NULL);
INSERT INTO `crt_testcase` VALUES (259, 'IPv6_Traffic_Shapping_UL_UDP_4Vlan_5MHz', NULL);
INSERT INTO `crt_testcase` VALUES (260, 'IPv6_Modify_TRS_Parameters_4Vlan_10MHz', NULL);
INSERT INTO `crt_testcase` VALUES (261, 'IPv6_FDD_10MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (262, 'IPv6_FDD_10MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (263, 'IPv6_FDD_10MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (264, 'IPv6_FDD_15MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (265, 'IPv6_FDD_15MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (266, 'IPv6_FDD_15MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (267, 'IPv6_FDD_10MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (268, 'IPv6_FDD_15MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (269, 'IPv6_FDD_15MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (270, 'IPv6_FDD_10MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (271, 'IPv6_FDD_15MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (272, 'IPv6_FDD_15MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (273, 'IPv6_FDD_10MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (274, 'IPv6_FDD_15MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (275, 'IPv6_FDD_10MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (276, 'IPv6_FDD_10MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (277, 'IPv6_FDD_15MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (278, 'IPv6_FDD_10MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (279, 'IPv6_FDD_10MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (280, 'IPv6_FDD_15MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (281, 'IPv6_FDD_5MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (282, 'IPv6_FDD_5MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (283, 'IPv6_FDD_5MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (284, 'IPv6_FDD_20MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (285, 'IPv6_FDD_20MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (286, 'IPv6_FDD_20MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (287, 'IPv6_FDD_5MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (288, 'IPv6_FDD_5MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (289, 'IPv6_FDD_20MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (290, 'IPv6_FDD_5MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (291, 'IPv6_FDD_20MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (292, 'IPv6_FDD_20MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (293, 'IPv6_FDD_5MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (294, 'IPv6_FDD_20MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (295, 'IPv6_FDD_20MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (296, 'IPv6_FDD_5MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (297, 'IPv6_FDD_20MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (298, 'IPv6_FDD_5MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (299, 'IPv6_FDD_20MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (300, 'IPv6_FDD_5MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (301, 'FDD_5MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (302, 'FDD_5MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (303, 'FDD_5MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (304, 'FDD_5MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (305, '4Vlan_3MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (306, 'FDD_5MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (307, '4Vlan_3MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (308, 'FDD_5MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (309, 'FDD_5MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (310, 'FDD_5MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (311, '4Vlan_3MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (312, 'FDD_5MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (313, 'FDD_5MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (314, 'Automated_BTS_Power_Reset', NULL);
INSERT INTO `crt_testcase` VALUES (315, 'BTS_Startup_BTS_Block_And_Unblock', NULL);
INSERT INTO `crt_testcase` VALUES (316, 'BTS_Startup_Reset_Into_Test_Dedicated_State', NULL);
INSERT INTO `crt_testcase` VALUES (317, 'Cell_Blocking_And_Unblocking', NULL);
INSERT INTO `crt_testcase` VALUES (318, 'Automated_BTS_Recovery_LTE_Ping_Lost_Between_Node_CCS_And_Application', NULL);
INSERT INTO `crt_testcase` VALUES (319, 'BTS_Startup_Site_Reset', NULL);
INSERT INTO `crt_testcase` VALUES (320, 'PortSwap_FDD_5MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (321, 'PortSwap_FDD_5MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (322, 'PortSwap_FDD_5MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (323, 'PortSwap_FDD_5MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (324, 'PortSwap_FDD_5MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (325, 'PortSwap_FDD_5MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (326, 'PortSwap_FDD_5MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (327, 'PortSwap_FDD_5MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (328, 'PortSwap_FDD_5MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (329, 'Portswap_FDD_5MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (330, 'LTE2299_S1Linksetup_with_IPv4_configuration', NULL);
INSERT INTO `crt_testcase` VALUES (331, 'LTE2299_interface_and_application_configuration_with_IPv4_IPv6', NULL);
INSERT INTO `crt_testcase` VALUES (332, 'LTE2299_S1Linksetup_with_IPv4_IPv6_configuration', NULL);
INSERT INTO `crt_testcase` VALUES (333, 'LTE2299_IPv6_configuration_with_collapsed_and_non_collapsed_case', NULL);
INSERT INTO `crt_testcase` VALUES (334, 'LTE2299_Concurrant_traffic_with_IPv4_IPv6_configuration', NULL);
INSERT INTO `crt_testcase` VALUES (335, 'LTE2299_IPv4_configuration_with_collapsed_and_non_collapsed_case', NULL);
INSERT INTO `crt_testcase` VALUES (336, 'LTE2299_S1Linksetup_with_IPv6_configuration', NULL);
INSERT INTO `crt_testcase` VALUES (337, 'LTE2175_ERAB_REL_ENB_ACT_QCI9', NULL);
INSERT INTO `crt_testcase` VALUES (338, 'LTE2175_ERAB_REL_ENB_ACT_QCI8', NULL);
INSERT INTO `crt_testcase` VALUES (339, 'PortSwap_4Vlan_20MHz_UDP', NULL);
INSERT INTO `crt_testcase` VALUES (340, 'PortSwap_Virtual_IP_4Vlan_20MHz', NULL);
INSERT INTO `crt_testcase` VALUES (341, 'PortSwap_4Vlan_20MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (342, 'PortSwap_Automated_BTS_Performance_Management_Cell_Block_15min', NULL);
INSERT INTO `crt_testcase` VALUES (343, 'PortSwap_4Vlan_20MHz_TCP', NULL);
INSERT INTO `crt_testcase` VALUES (344, 'OM_Technical_Logs_with_Cell_Delete', NULL);
INSERT INTO `crt_testcase` VALUES (345, 'FZM_Testability_SysLog_UDP_IP_Configuration', NULL);
INSERT INTO `crt_testcase` VALUES (346, 'CC_S_AaSysLog_StartupfileCheck', NULL);
INSERT INTO `crt_testcase` VALUES (347, 'PMO_Trace_BasicCellTrace_MBA', NULL);
INSERT INTO `crt_testcase` VALUES (348, 'OM_Technical_Logs_after_CellSetup', NULL);
INSERT INTO `crt_testcase` VALUES (349, 'QT_DSP_memory_dumps_check', NULL);
INSERT INTO `crt_testcase` VALUES (350, 'DSP_SWversion_enquiry', NULL);
INSERT INTO `crt_testcase` VALUES (351, 'OM_TechnicalLogsSUEcallonFSM1', NULL);
INSERT INTO `crt_testcase` VALUES (352, 'BlackBoxFileCheckFrom_FZMConsole', NULL);
INSERT INTO `crt_testcase` VALUES (353, 'PostResults_accessible_via_LMPPort', NULL);
INSERT INTO `crt_testcase` VALUES (354, 'Technical_Logs_BlackBoxFileCheck', NULL);
INSERT INTO `crt_testcase` VALUES (355, 'Check_PM_Counters_Inter_Frequency_Inter_eNB_X2_Handover', NULL);
INSERT INTO `crt_testcase` VALUES (356, 'Adjacent_Cell_Configuration_Inter_eNB_Handover_Via_S1', NULL);
INSERT INTO `crt_testcase` VALUES (357, 'Inter_Frequency_Inter_eNB_X2_Handover_with_TCP_Data', NULL);
INSERT INTO `crt_testcase` VALUES (358, 'Check_PM_Counters_Inter_eNB_Handover_Via_S1', NULL);
INSERT INTO `crt_testcase` VALUES (359, 'S1_Handover_Inter_eNB_Handover_Via_S1_Interface_With_TCP_Data', NULL);
INSERT INTO `crt_testcase` VALUES (360, 'Inter_Frequency_Inter_eNB_X2_Handover_PM_Counters', NULL);
INSERT INTO `crt_testcase` VALUES (361, 'Check_Frame_Alignment', NULL);
INSERT INTO `crt_testcase` VALUES (362, 'Adjacent_Cell_Configuration_Inter_Frequency_Inter_eNB_X2_Handover', NULL);
INSERT INTO `crt_testcase` VALUES (363, 'Inter_eNB_Handover_Via_S1_PM_Counters', NULL);
INSERT INTO `crt_testcase` VALUES (364, 'ETWS_SIB11', NULL);
INSERT INTO `crt_testcase` VALUES (365, 'LTE1559_TC2_Sent_chunks_monitoring', NULL);
INSERT INTO `crt_testcase` VALUES (366, 'LTE1559_TC1_Randomized_MME_reinitialization', NULL);
INSERT INTO `crt_testcase` VALUES (367, 'LTE1559_TC3_Received_Chunks_Monitoring', NULL);
INSERT INTO `crt_testcase` VALUES (368, 'LTE2014-A-d_MME_Balancing', NULL);
INSERT INTO `crt_testcase` VALUES (369, 'LTE2023_TC1_Feature_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (370, 'LBT5395_UC04_-_Two_LAA_cells_must_use_WiFi_channels_from_one_single_bonding_pair', NULL);
INSERT INTO `crt_testcase` VALUES (371, 'LBT5395_UC05_-_Pmax_ranges_for_ETSI', NULL);
INSERT INTO `crt_testcase` VALUES (372, 'PortSwap_FDD_10MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (373, 'PortSwap_FDD_15MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (374, 'PortSwap_FDD_10MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (375, 'PortSwap_FDD_10MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (376, 'PortSwap_FDD_15MHz_BTS_Activation', NULL);
INSERT INTO `crt_testcase` VALUES (377, 'PortSwap_FDD_10MHz_UDP_Single_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (378, 'PortSwap_FDD_10MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (379, 'PortSwap_FDD_15MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (380, 'PortSwap_FDD_15MHz_UDP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (381, 'PortSwap_FDD_10MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (382, 'PortSwap_FDD_10MHz_TCP_Multi_UE_UL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (383, 'PortSwap_FDD_10MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (384, 'PortSwap_FDD_15MHz_TCP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (385, 'PortSwap_FDD_10MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (386, 'PortSwap_FDD_10MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (387, 'PortSwap_FDD_15MHz_TCP_Single_UE_DL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (388, 'PortSwap_FDD_15MHz_Set_Attenuation', NULL);
INSERT INTO `crt_testcase` VALUES (389, 'PortSwap_FDD_15MHz_UDP_Single_UE_UL_Peak_Throughput', NULL);
INSERT INTO `crt_testcase` VALUES (390, 'PortSwap_FDD_15MHz_TCP_Multi_UE_DL_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (391, 'PortSwap_FDD_15MHz_UDP_Multi_UE_Bi-Directional_Call_Stability', NULL);
INSERT INTO `crt_testcase` VALUES (392, 'Automated_BTS_Performance_Management_Cell_Block_30min', NULL);
INSERT INTO `crt_testcase` VALUES (393, 'NMAP_Scan_ETH_OFF_SSH_ON_LMT', NULL);
INSERT INTO `crt_testcase` VALUES (394, 'NMAP_Scan_ETH_OFF_RnD_ON_SSH_ON_LMT', NULL);
INSERT INTO `crt_testcase` VALUES (395, 'NMAP_Scan_ETH_OFF_RnD_ON_LMT', NULL);

SET FOREIGN_KEY_CHECKS = 1;
