/* CUSTOMER TABLE 생성 */

CREATE TABLE `customer` (
  `CustomerID` int NOT NULL AUTO_INCREMENT,
  `PhoneNumber` char(13) NOT NULL,
  `Id` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `SchoolMail` varchar(100) NOT NULL,
  PRIMARY KEY (`CustomerID`),
  UNIQUE KEY `PhoneNumber_UNIQUE` (`PhoneNumber`),
  UNIQUE KEY `SchoolMail_UNIQUE` (`SchoolMail`),
  UNIQUE KEY `Id_Passsword_UNIQUE` (`Id`, `PassWord`),
  CONSTRAINT `valid_phone_number` CHECK (regexp_like(`PhoneNumber`,_utf8mb4'010-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')),
  CONSTRAINT `Valid_SchoolMail` CHECK ((`SchoolMail` like _utf8mb4'%_@yonsei.ac.kr'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* DAYS_MEAL TABLE 생성 */

CREATE TABLE `days_meal` (
  `Days` date NOT NULL,
  `Meal` varchar(6) NOT NULL,
  PRIMARY KEY (`Days`,`Meal`),
  CONSTRAINT `valid_meal` CHECK ((`meal` in (_utf8mb4'Lunch',_utf8mb4'Dinner')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* DEMAND_SURVEY TABLE 생성 */

CREATE TABLE `demand_survey` (
  `Days` date NOT NULL,
  `Meal` varchar(6) NOT NULL,
  `CustomerID` int NOT NULL,
  `Total_Preference` varchar(3) NOT NULL,
  `Rice_Preference` decimal(1,0) NOT NULL,
  `Soup_Preference` decimal(1,0) NOT NULL,
  `Noodle_Preference` decimal(1,0) NOT NULL,
  `Main_Preference` decimal(1,0) NOT NULL,
  `Side1_Preference` decimal(1,0) NOT NULL,
  `Side2_Preference` decimal(1,0) NOT NULL,
  `Kimchi_Preference` decimal(1,0) NOT NULL,
  PRIMARY KEY (`Days`,`Meal`,`CustomerID`),
  KEY `fk_DEMAND_SURVEY_DATE_TIME1_idx` (`Days`,`Meal`),
  KEY `fk_DEMAND_SURVEY_CUSTOMER1_idx` (`CustomerID`),
  CONSTRAINT `fk_DEMAND_SURVEY_CUSTOMER1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_DEMAND_SURVEY_DATE_TIME1` FOREIGN KEY (`Days`, `Meal`) REFERENCES `days_meal` (`Days`, `Meal`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `valid_kimchi` CHECK (regexp_like(`Kimchi_Preference`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_main` CHECK (regexp_like(`Main_Preference`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_noodle` CHECK (regexp_like(`Noodle_Preference`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_rice` CHECK (regexp_like(`Rice_Preference`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_side1` CHECK (regexp_like(`Side1_Preference`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_side2` CHECK (regexp_like(`Side2_Preference`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_soup` CHECK (regexp_like(`Soup_Preference`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_total` CHECK ((`Total_Preference` in (_utf8mb4'yes',_utf8mb4'no')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* LEFTOVER TABLE 생성 */

CREATE TABLE `leftover` (
  `Days` date NOT NULL,
  `Meal` varchar(6) NOT NULL,
  `End_Weight` varchar(45) DEFAULT NULL,
  `Actual_Demand` varchar(45) DEFAULT NULL,
  `Leftover_Per_Person` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Days`,`Meal`),
  KEY `fk_LEFTOVER_DATE_TIME1_idx` (`Days`,`Meal`),
  CONSTRAINT `fk_LEFTOVER_DATE_TIME1` FOREIGN KEY (`Days`, `Meal`) REFERENCES `days_meal` (`Days`, `Meal`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* MENU_EVALUATION_QUANTITY TABLE 생성 */

CREATE TABLE `menu_evaluation_quantity` (
  `Days` date NOT NULL,
  `Meal` varchar(6) NOT NULL,
  `CustomerID` int NOT NULL,
  `Rice_Preference_Quantity` decimal(1,0) NOT NULL,
  `Soup_Preference_Quantity` decimal(1,0) NOT NULL,
  `Noodle_Preference_Quantity` decimal(1,0) NOT NULL,
  `Main_Preference_Quantity` decimal(1,0) NOT NULL,
  `Side1_Preference_Quantity` decimal(1,0) NOT NULL,
  `Side2_Preference_Quantity` decimal(1,0) NOT NULL,
  `Kimchi_Preference_Quantity` decimal(1,0) NOT NULL,
  PRIMARY KEY (`Days`,`Meal`,`CustomerID`),
  KEY `fk_MENU_EVALUATION_QUANTITY_DATE_TIME1_idx` (`Days`,`Meal`),
  KEY `fk_MENU_EVALUATION_QUANTITY_CUSTOMER2_idx` (`CustomerID`),
  CONSTRAINT `fk_MENU_EVALUATION_QUANTITY_CUSTOMER2` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_MENU_EVALUATION_QUANTITY_DATE_TIME1` FOREIGN KEY (`Days`, `Meal`) REFERENCES `days_meal` (`Days`, `Meal`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `valid_kimchi_quantity` CHECK (regexp_like(`Kimchi_Preference_Quantity`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_main_quantity` CHECK (regexp_like(`Main_Preference_Quantity`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_noodle_quantity` CHECK (regexp_like(`Noodle_Preference_Quantity`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_rice_quantity` CHECK (regexp_like(`Rice_Preference_Quantity`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_side1_quantity` CHECK (regexp_like(`Side1_Preference_Quantity`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_side2_quantity` CHECK (regexp_like(`Side2_Preference_Quantity`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_soup_quantity` CHECK (regexp_like(`Soup_Preference_Quantity`,_utf8mb4'[1-5]'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* MENU_EVALUATION_TASTE TABLE 생성 */

CREATE TABLE `menu_evaluation_taste` (
  `Days` date NOT NULL,
  `Meal` varchar(45) NOT NULL,
  `CustomerID` int NOT NULL,
  `Rice_Preference_Taste` decimal(1,0) NOT NULL,
  `Soup_Preference_Taste` decimal(1,0) NOT NULL,
  `Noodle_Preference_Taste` decimal(1,0) NOT NULL,
  `Main_Preference_Taste` decimal(1,0) NOT NULL,
  `Side1_Preference_Taste` decimal(1,0) NOT NULL,
  `Side2_Preference_Taste` decimal(1,0) NOT NULL,
  `Kimchi_Preference_Taste` decimal(1,0) NOT NULL,
  PRIMARY KEY (`Days`,`Meal`,`CustomerID`),
  KEY `fk_MENU_EVALUATION_TASTE_DATE_TIME1_idx` (`Days`,`Meal`),
  KEY `fk_MENU_EVALUATION_TASTE_CUSTOMER1_idx` (`CustomerID`),
  CONSTRAINT `fk_MENU_EVALUATION_TASTE_CUSTOMER1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_MENU_EVALUATION_TASTE_DATE_TIME1` FOREIGN KEY (`Days`, `Meal`) REFERENCES `days_meal` (`Days`, `Meal`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `valid_kimchi_taste` CHECK (regexp_like(`Kimchi_Preference_Taste`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_main_taste` CHECK (regexp_like(`Main_Preference_Taste`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_noodle_taste` CHECK (regexp_like(`Noodle_Preference_Taste`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_rice_taste` CHECK (regexp_like(`Rice_Preference_Taste`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_side1_taste` CHECK (regexp_like(`Side1_Preference_Taste`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_side2_taste` CHECK (regexp_like(`Side2_Preference_Taste`,_utf8mb4'[1-5]')),
  CONSTRAINT `valid_soup_taste` CHECK (regexp_like(`Soup_Preference_Taste`,_utf8mb4'[1-5]'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* MENU_MANAGEMENT TABLE 생성 */

CREATE TABLE `menu_management` (
  `Days` date NOT NULL,
  `Meal` varchar(6) NOT NULL,
  `Rice` varchar(45) NOT NULL,
  `Soup` varchar(45) NOT NULL,
  `Noodle` varchar(45) NOT NULL,
  `Main` varchar(45) NOT NULL,
  `Side1` varchar(45) NOT NULL,
  `Side2` varchar(45) NOT NULL,
  `Kimchi` varchar(45) NOT NULL,
  `Initial_Weight` varchar(45) DEFAULT NULL,
  `Production_Cost` varchar(45) NOT NULL,
  PRIMARY KEY (`Days`,`Meal`),
  KEY `fk_MENU_MANAGEMENT_DATE_TIME1_idx` (`Days`,`Meal`),
  CONSTRAINT `fk_MENU_MANAGEMENT_DATE_TIME1` FOREIGN KEY (`Days`, `Meal`) REFERENCES `days_meal` (`Days`, `Meal`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/* ANNOUNCE VIEW 생성 */

CREATE VIEW announce AS
SELECT l.days, l.meal, m.initial_weight, end_weight,
((rice_preference + soup_preference + noodle_preference + main_preference + side1_preference
+ side2_preference + kimchi_preference)/7) as Avg_Demand,
((rice_preference_taste + soup_preference_taste + noodle_preference_taste + main_preference_taste
 + side1_preference_taste + side2_preference_taste + kimchi_preference_taste)/7) as Avg_taste,
 ((rice_preference_quantity + soup_preference_quantity + noodle_preference_quantity + main_preference_quantity
 + side1_preference_quantity + side2_preference_quantity + kimchi_preference_quantity)/7) as Avg_quantity
from leftover as l join demand_survey as s join menu_evaluation_quantity as q 
join menu_evaluation_taste as t join menu_management as m
ON l.days = s.days
AND s.days = q.days
AND q.days = t.days
AND t.days = m.days
AND l.meal = s.meal
AND s.meal = q.meal
AND q.meal = t.meal
AND t.meal = m.meal
AND s.customerid = q.customerid
AND q.customerid = t.customerid;

/* ANNOUNCEMENT VIEW 생성 */

CREATE VIEW ANNOUNCEMENT AS
SELECT days, meal, initial_weight, end_weight, AVG(avg_demand) AS Average_Demand, 
AVG(avg_taste) AS Average_Taste, AVG(avg_quantity) AS Average_Quantity
FROM announce
GROUP BY days, meal;

/* LEFTOVER_VIEW VIEW 생성*/

CREATE VIEW LEFTOVER_VIEW AS
SELECT L.days, L.meal, M.initial_weight, L.end_weight, L.actual_demand
, (L.end_weight / M.initial_weight) AS wasted_ratio
, (M.production_cost * L.end_weight / M.initial_weight + end_weight * 130) AS wasted_cost
FROM leftover AS L JOiN menu_management AS M
ON L.days = M.days
AND L.meal = M.meal;

/* Update_ID procedure 생성 */

DELIMITER //

CREATE PROCEDURE Update_ID
			(IN		insertcustomerID INT,
            IN		newID VARCHAR(45),
            IN 		oldID VARCHAR(45),
            IN		insertpassword VARCHAR(45))
BEGIN
    
	UPDATE CUSTOMER
	SET ID = newID
	WHERE customerid = insertcustomerid
    AND id = oldid
    AND password = insertpassword;

END
//

DELIMITER ;
