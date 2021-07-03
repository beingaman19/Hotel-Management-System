-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 06, 2021 at 08:30 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel management`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `Name` text NOT NULL,
  `Phonenumber` int(10) NOT NULL,
  `CheckinDate` varchar(11) NOT NULL,
  `CheckoutDate` varchar(11) NOT NULL,
  `RoomNumber` int(11) NOT NULL,
  `Bill` int(10) NOT NULL,
  `Payment` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`Name`, `Phonenumber`, `CheckinDate`, `CheckoutDate`, `RoomNumber`, `Bill`, `Payment`) VALUES
('Mayank Rai', 2147483647, '6/6/21', '6/15/21', 12, 9000, 'Paid'),
('Aman Ranjan', 2147483647, '6/6/21', '6/9/21', 3, 3000, 'Paid'),
('Avirup Banerjee', 2147483647, '6/2/21', '6/10/21', 3, 8000, 'Paid'),
('Mohan Tulsyan', 2147483647, '6/3/21', '6/8/21', 4, 5000, 'Paid'),
('Arka Satpati', 2147483647, '6/1/21', '6/4/21', 5, 4000, 'Paid');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `FirstName` text NOT NULL,
  `lastname` text NOT NULL,
  `phonenumber` int(11) NOT NULL,
  `dob` varchar(8) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `emailid` varchar(100) NOT NULL,
  `password` varchar(10) NOT NULL,
  `confirmpassword` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`FirstName`, `lastname`, `phonenumber`, `dob`, `gender`, `emailid`, `password`, `confirmpassword`) VALUES
('Mayank', 'Rai', 2147483647, '5/17/99', 'Male', 'mayak@gmail.com', '1234', '1234'),
('arka', 'satpati', 2147483647, '01/02/20', 'Male', 'arka@gmail.com', '1234', '1234');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
