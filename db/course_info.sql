CREATE TABLE course (
    course_ID VARCHAR(300) PRIMARY KEY,
    course_name VARCHAR (300),
    credits INT,
    need VARCHAR(300),
    opendept_ID INT,
    open_class VARCHAR(300),
    class_time VARCHAR(300),
    classroom VARCHAR(300),
    teacher VARCHAR(300),
    Max_people INT,
    now_people INT,
    department_ID VARCHAR(30),
    week INT,
    begin_time INT,
    end_time INT
);

--                         代碼     名稱       學分  必修  學系   班級        時間         教室      教授  最多 現在
INSERT INTO course VALUES('0000', '系統程式'    , 3, '必修', 1, '資訊二乙', '(一)02-04', '資電402', '劉宗杰', 5, 0, 1, 1, 2, 4);
INSERT INTO course VALUES('0001', '資料庫系統'  , 3, '必修', 1, '資訊二乙', '(一)07-09', '資電511', '許懷中', 5, 0, 1, 1, 7, 9);
INSERT INTO course VALUES('0002', '機率與統計'  , 3, '必修', 1, '資訊二乙', '(二)02-04', '科航206', '游景盛', 5, 0, 1, 2, 2, 4);
INSERT INTO course VALUES('0003', 'Web程式設計' , 3, '選修' , 1, '資訊二乙', '(三)01-03', '資電234', '劉明機', 5, 0, 1, 3, 1, 3);
INSERT INTO course VALUES('0004', '互聯網路'    , 3, '選修' , 1, '資訊二乙', '(三)06-08', '資電234', '劉宗杰', 5, 0, 1, 3, 6, 8);
INSERT INTO course VALUES('0005', '多媒體系統'  , 3, '選修' , 1, '資訊二乙', '(二)06-08', '資電234', '葉春秀', 5, 0, 1, 2, 6, 8);
INSERT INTO course VALUES('0006', '電子商務安全', 3, '選修' , 1, '資訊二乙', '(一)11-13', '資電102', '魏國瑞', 5, 0, 1, 11, 11, 13);
INSERT INTO course VALUES('0007', '數位系統設計', 3, '選修' , 1, '資訊二丁', '(四)06-08', '資電125', '陳德生', 5, 0, 1, 4, 6, 8);   
INSERT INTO course VALUES('0008', '程式語言'    , 3, '選修' , 1, '資訊三丙', '(四)11-13', '資電248', '吳育倫', 5, 0, 1, 4, 11, 13);
INSERT INTO course VALUES('0009', '人工智慧導論', 3, '選修' , 1, '資訊三丙', '(五)06-08', '資電234', '林峰正', 5, 0, 1, 5, 6, 8);
INSERT INTO course VALUES('0010', '電子商務安全', 3, '選修' , 1, '資訊二乙', '(三)11-13', '資電102', '周澤捷', 5, 0, 1, 3, 11, 13);     /*相同名稱*/
INSERT INTO course VALUES('0011', '資訊安全管理', 3, '選修' , 1, '資訊三丙', '(五)01-03', '資電102', '陳映親', 5, 0, 1, 5, 1, 3);       /*超過30學分*/
INSERT INTO course VALUES('0012', '微積分(二)'  , 3, '必修', 1, '資訊一乙', '(一)07-09', '資電102', '林佩君', 5, 0, 1, 1, 7, 9);        /*衝堂*/
INSERT INTO course VALUES('0013', '信號與系統'  , 3, '必修', 2, '電子二乙', '(三)05-07', '忠304'  , '林宗志', 5, 0, 2, 3, 5, 7);        /*外系*/
INSERT INTO course VALUES('0014', 'JAVA程式語言', 4, '選修' , 1, '通訊二乙', '(三)11-13', '紀207'  , '蔡淵裕', 5, 0, 4, 3, 11, 13);     /*外系*/
INSERT INTO course VALUES('0015', '工程數學'    , 3, '選修' , 1, '資訊二乙', '(五)11-13', '資電402', '陳啟鏘', 5, 5, 1, 5, 11, 13);     /*人數已滿*/
INSERT INTO course VALUES('0016', '系統程式'    , 3, '必修', 1, '資訊二甲', '(三)02-04', '資電511', '周兆龍', 5, 0, 1, 3, 2, 4);
INSERT INTO course VALUES('0017', '資料庫系統'  , 3, '必修', 1, '資訊二甲', '(五)07-09', '資電402', '林明言', 5, 0, 1, 5, 7, 9);
INSERT INTO course VALUES('0018', '機率與統計'  , 3, '必修', 1, '資訊二甲', '(四)02-04', '資電206', '劉怡芬', 5, 0, 1, 4, 2, 4);
INSERT INTO course VALUES('0019', '系統程式'    , 3, '必修', 1, '資訊二丙', '(二)02-04', '資電511', '劉宗杰', 5, 0, 1, 2, 2, 4);
INSERT INTO course VALUES('0020', '資料庫系統'  , 3, '必修', 1, '資訊二丙', '(四)07-09', '資電402', '林明言', 5, 0, 1, 4, 7, 9);
INSERT INTO course VALUES('0021', '機率與統計'  , 3, '必修', 1, '資訊二丙', '(三)02-04', '資電206', '游景盛', 5, 0, 1, 3, 2, 4);

select * from course;