CREATE TABLE `course` (
    `course_ID` VARCHAR (300) PRIMARY KEY,
    `course_name` VARCHAR (300),
    `credits` INT,
    `begin_time` INT,
    `end_time` INT
);

INSERT INTO `course` VALUES('IECS0000', '系統程式', 3);
INSERT INTO `course` VALUES('IECS0001', '資料庫系統', 3);
INSERT INTO `course` VALUES('IECS0002', '機率與統計', 3);
INSERT INTO `course` VALUES('IECS0003', '大學精進英文', 2);
INSERT INTO `course` VALUES('IECS0004', '互聯網路', 3);
INSERT INTO `course` VALUES('IECS0005', 'web程式設計', 3);
INSERT INTO `course` VALUES('IECS0006', '系統分析與設計', 3);
INSERT INTO `course` VALUES('IECS0007', '電子商務', 3);
