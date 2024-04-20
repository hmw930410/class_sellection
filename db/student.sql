CREATE TABLE student(
    student_ID VARCHAR (300),
    PASSWORD VARCHAR(10),
    student_name VARCHAR (300),
    class_ID INT,
    total_credit INT,
    table_ID int
);

--                          ID     PW   Name class TC table
INSERT INTO student VALUES ('1', '123', '小明', 2, 0, 1);  /* 正常 */
INSERT INTO student VALUES ('2', '456', '小美', 3, 0, 2);  /* 別班 */
INSERT INTO student VALUES ('3', '789', '小張', 2, 0, 3);  /* > 30 */
INSERT INTO student VALUES ('4', '135', '小萱', 2, 0, 3);  /* < 9 */

select * from student;
