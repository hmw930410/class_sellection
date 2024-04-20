CREATE TABLE student(
    student_ID VARCHAR (300),
    PASSWORD VARCHAR(10),
    student_name VARCHAR (300),
    class_ID INT,
    total_credit INT,
    table_ID int,
    department_ID VARCHAR(30)
);

--                          ID     PW   Name class TC table
INSERT INTO student VALUES ('1', '123', '小明', 1, 0, 1, 1);
INSERT INTO student VALUES ('2', '456', '小美', 2, 0, 2, 1); 
INSERT INTO student VALUES ('3', '789', '小張', 3, 0, 3, 1);

select * from student;
