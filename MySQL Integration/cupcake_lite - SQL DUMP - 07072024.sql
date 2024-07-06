-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2024 at 07:26 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cupcake_lite`
--

-- --------------------------------------------------------

--
-- Table structure for table `blacklisted_userid`
--

CREATE TABLE `blacklisted_userid` (
  `UserID` varchar(12) NOT NULL,
  `RegisteredName` varchar(50) NOT NULL DEFAULT 'No recorded data',
  `Reason` varchar(120) NOT NULL DEFAULT 'No recorded data',
  `RegistryDate` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blacklist_name`
--

CREATE TABLE `blacklist_name` (
  `Name` text NOT NULL,
  `Reason` varchar(120) NOT NULL DEFAULT 'No recorded data',
  `RegistryDate` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blacklist_name`
--

INSERT INTO `blacklist_name` (`Name`, `Reason`, `RegistryDate`) VALUES
('genhack', 'Known spam bot', '2024-06-11'),
('tgt', 'Known raiders', '2024-06-11');

-- --------------------------------------------------------

--
-- Table structure for table `gserver_configs`
--

CREATE TABLE `gserver_configs` (
  `ServerID` varchar(12) NOT NULL,
  `CustomBotPrefix` varchar(5) DEFAULT 'cl.',
  `Casual_WelcomeCID` varchar(50) DEFAULT NULL,
  `Casual_UserNotifsCID` varchar(50) DEFAULT NULL,
  `ModLog_Raw` varchar(50) DEFAULT NULL,
  `ModLog_Joins` varchar(50) DEFAULT NULL,
  `ModLog_Mods` varchar(50) DEFAULT NULL,
  `ModLog_Message` varchar(50) DEFAULT NULL,
  `PrivilegeRoles_Admins` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `PrivilegeRoles_Mods` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `RegistryDate` date DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blacklisted_userid`
--
ALTER TABLE `blacklisted_userid`
  ADD PRIMARY KEY (`UserID`);

--
-- Indexes for table `blacklist_name`
--
ALTER TABLE `blacklist_name`
  ADD UNIQUE KEY `Name` (`Name`) USING HASH;

--
-- Indexes for table `gserver_configs`
--
ALTER TABLE `gserver_configs`
  ADD PRIMARY KEY (`ServerID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
