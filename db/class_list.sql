CREATE TABLE class_list (
    class_ID INT PRIMARY KEY,
    classname VARCHAR (500)
);

INSERT INTO class_list VALUES(1, '資訊二甲');
INSERT INTO class_list VALUES(2, '資訊二乙');
INSERT INTO class_list VALUES(3, '資訊二丙');
INSERT INTO class_list VALUES(4, '資訊二丁');

select * from class_list;