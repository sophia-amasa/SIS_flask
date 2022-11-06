-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.29 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for students
CREATE DATABASE IF NOT EXISTS `students` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `students`;

-- Dumping structure for table students.colleges
CREATE TABLE IF NOT EXISTS `colleges` (
  `CollegeCode` varchar(10) NOT NULL,
  `CollegeName` varchar(50) NOT NULL,
  PRIMARY KEY (`CollegeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table students.colleges: ~5 rows (approximately)
INSERT INTO `colleges` (`CollegeCode`, `CollegeName`) VALUES
	('CASS', 'College of Arts & Social Sciences'),
	('CCS', 'College of Computer Studies'),
	('CEBA', 'College of Economics, Business, & Accountancy'),
	('CED', 'College of Education'),
	('COET', 'College of Engineering & Technology'),
	('CSM', 'College of Science & Mathematics');

-- Dumping structure for table students.course_info
CREATE TABLE IF NOT EXISTS `course_info` (
  `course_code` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `course` varchar(50) DEFAULT NULL,
  `college` varchar(1040) NOT NULL,
  PRIMARY KEY (`course_code`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table students.course_info: ~25 rows (approximately)
INSERT INTO `course_info` (`course_code`, `course`, `college`) VALUES
	('BAENG', 'BA in English', 'CASS'),
	('BAFIL', 'BA in Filipino', 'CASS'),
	('BAHIS', 'BA in History', 'CASS'),
	('BAPOLSCI', 'BA in Political Science', 'CASS'),
	('BSACC', 'BS in Accountancy', 'CEBA'),
	('BSBIO', 'BS in General Biology', 'CSM'),
	('BSCEENG', 'BS in Ceramics Engineering', 'COET'),
	('BSCHEM', 'BS in Chemistry', 'CSM'),
	('BSCHEMENG', 'BS in Chemical Engineering', 'COET'),
	('BSCIVENG', 'BS in Civil Engineering', 'COET'),
	('BSCOMENG', 'BS in Computer Engineering', 'COET'),
	('BSCS', 'BS in Computer Science', 'CCS'),
	('BSEBIO', 'BSE in Biology', 'CED'),
	('BSECE', 'BS in Electronics and Communications Engineering', 'COET'),
	('BSEET', 'BS in Environmental Engineering Technology', 'COET'),
	('BSELECENG', 'BS in Electrical Engineering', 'COET'),
	('BSIT', 'BS in Information Technology', 'CCS'),
	('BSMATH', 'BS in Mathematics', 'CSM'),
	('BSME', 'BS in Mechanical Engineering', 'COET'),
	('BSMETENG', 'BS in Metallurgical Engineering', 'COET'),
	('BSMINENG', 'BS in Mining Engineering', 'COET'),
	('BSNURSING', 'BS in Nursing', 'CON'),
	('BSPHYSICS', 'BS in Physics', 'CSM'),
	('BSPSYCH', 'BS in Psychology', 'CASS'),
	('BSSTAT', 'BS in Statistics', 'CSM');

-- Dumping structure for table students.students
CREATE TABLE IF NOT EXISTS `students` (
  `student_id` varchar(9) NOT NULL,
  `full_name` varchar(50) DEFAULT NULL,
  `college` varchar(5040) NOT NULL,
  `course_code` varchar(10) DEFAULT NULL,
  `year_level` int DEFAULT NULL,
  `gender` enum('Male','Female') DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `FK_students_course_info` (`course_code`),
  CONSTRAINT `FK_students_course_info` FOREIGN KEY (`course_code`) REFERENCES `course_info` (`course_code`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table students.students: ~52 rows (approximately)
INSERT INTO `students` (`student_id`, `full_name`, `college`, `course_code`, `year_level`, `gender`) VALUES
	('2000-0002', 'C', 'CCS', 'BSCS', 2, 'Female'),
	('2000-0003', 'B', 'CCS', 'BSCS', 1, 'Female'),
	('2000-0004', 'E', 'CEBA', 'BSACC', 2, 'Female'),
	('2000-0413', 'Rachel Park', 'CASS', 'BAENG', 3, 'Female'),
	('2000-0642', 'Weston Cuevas', 'CASS', 'BAPOLSCI', 2, 'Male'),
	('2000-0936', 'Fredrick Leon', 'CASS', 'BSPSYCH', 1, 'Male'),
	('2000-1449', 'Sean Cooper', 'CASS', 'BAFIL', 2, 'Male'),
	('2000-1735', 'Jenna Suarez', 'CCS', 'BSCS', 1, 'Female'),
	('2000-2712', 'Melody Weeks', 'COET', 'BSCOMENG', 1, 'Female'),
	('2001-0781', 'Mavis Hayden', 'CSM', 'BSCHEM', 4, 'Female'),
	('2001-1892', 'Sonya Wagner', 'CSM', 'BSPHYSICS', 3, 'Female'),
	('2001-2802', 'Princess Vang', 'CSM', 'BSSTAT', 1, 'Female'),
	('2002-0385', 'Sherman Saunders', 'COET', 'BSCOMENG', 1, 'Male'),
	('2003-1354', 'Ferdinand Russell', 'CASS', 'BAENG', 4, 'Male'),
	('2004-0788', 'Bernadine Hinton', 'CASS', 'BSPSYCH', 5, 'Female'),
	('2004-0994', 'Wiley Maynard', 'COET', 'BSELECENG', 4, 'Male'),
	('2004-1465', 'Ruthie Montes', 'CSM', 'BSPHYSICS', 3, 'Male'),
	('2004-2522', 'Keith Crosby', 'COET', 'BSCHEMENG', 1, 'Male'),
	('2005-0315', 'Ernest Key', 'COET', 'BSCHEMENG', 4, 'Male'),
	('2005-1987', 'Kenny Warren', 'CSM', 'BSPHYSICS', 1, 'Male'),
	('2006-2589', 'Clint Chandler', 'CCS', 'BSCS', 2, 'Male'),
	('2007-0231', 'Sherley Taylor', 'CASS', 'BAHIS', 4, 'Female'),
	('2007-1942', 'Pasquale Bryant', 'CASS', 'BAPOLSCI', 2, 'Male'),
	('2008-0545', 'Travis Allen', 'CASS', 'BAPOLSCI', 5, 'Female'),
	('2008-0806', 'Jaime Reilly', 'CCS', 'BSCS', 4, 'Male'),
	('2008-2095', 'Leslie Cochran', 'CEBA', 'BSACC', 2, 'Female'),
	('2009-0852', 'Tobias Nash', 'CSM', 'BSPHYSICS', 2, 'Male'),
	('2009-0998', 'Misty Walter', 'CON', 'BSNURSING', 4, 'Female'),
	('2010-1559', 'Dionne Zavala', 'COET', 'BSELECENG', 3, 'Female'),
	('2010-2977', 'Estela Livingston', 'CSM', 'BSSTAT', 1, 'Female'),
	('2012-1014', 'Sterling Cain', 'CSM', 'BSBIO', 4, 'Male'),
	('2013-1708', 'Shari Ellison', 'COET', 'BSCHEMENG', 3, 'Male'),
	('2014-1115', 'Morris Lane', 'CASS', 'BAPOLSCI', 3, 'Female'),
	('2014-1852', 'Elba Howe', 'CCS', 'BSIT', 1, 'Female'),
	('2014-2103', 'Eldridge Donaldson', 'CSM', 'BSPHYSICS', 1, 'Male'),
	('2015-0019', 'Tracie Anthony', 'CASS', 'BAHIS', 3, 'Female'),
	('2015-1391', 'Janelle Hodges', 'CSM', 'BSSTAT', 4, 'Female'),
	('2015-1741', 'Kendrick Mclean', 'CON', 'BSNURSING', 4, 'Male'),
	('2016-0840', 'Dirk Whitaker', 'CASS', 'BAFIL', 5, 'Male'),
	('2016-2679', 'Luan Vincent', 'COET', 'BSCIVENG', 4, 'Female'),
	('2017-0710', 'Nichole Mccormick', 'CSM', 'BSCHEM', 4, 'Female'),
	('2017-0733', 'Brenda Moore', 'CCS', 'BSCS', 3, 'Female'),
	('2017-1379', 'Mia Caldwell', 'CSM', 'BSMATH', 5, 'Female'),
	('2017-2649', 'Martina Wilson', 'CASS', 'BAENG', 1, 'Female'),
	('2018-0168', 'Marion Roach', 'CSM', 'BSSTAT', 3, 'Male'),
	('2019-0050', 'Eusebio Mcclain', 'CEBA', 'BSACC', 5, 'Male'),
	('2019-1954', 'Willa Townsend', 'COET', 'BSCOMENG', 3, 'Female'),
	('2020-0424', 'Sophia Nicolette Amasa', 'CCS', 'BSCS', 2, 'Female'),
	('2020-1455', 'Holly Robinson', 'CSM', 'BSSTAT', 4, 'Female'),
	('2020-1850', 'Virgie Daniel', 'CASS', 'BAPOLSCI', 3, 'Female'),
	('2020-2953', 'Bret Gay', 'COET', 'BSCHEMENG', 1, 'Male'),
	('2021-1428', 'Ike Preston', 'COET', 'BSCIVENG', 5, 'Female'),
	('2021-1451', 'Blaine Glenn', 'CCS', 'BSCS', 2, 'Male'),
	('2021-2430', 'Jessica Orr', 'COET', 'BSCIVENG', 5, 'Female');

-- Dumping structure for table students.users
CREATE TABLE IF NOT EXISTS `users` (
  `user_password` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `role` varchar(5) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table students.users: ~0 rows (approximately)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
