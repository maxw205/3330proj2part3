CREATE TABLE PUBLISHER (
    Publisher_Name varchar(255) primary key,
    Phone varchar(255),
    Address varchar(255)
);

CREATE TABLE LIBRARY_BRANCH (
    Branch_Id int primary key,
    Branch_Name varchar(255),
    Branch_Address varchar(255)
);

CREATE TABLE BORROWER (
    Card_No int,
    Name varchar(255) primary key,
    Address varchar(255),
    Phone varchar(255)
);

CREATE TABLE BOOK (
    Book_Id int primary key,
    Title varchar(255),
    Publisher_Name varchar(255),
    Foreign key (Publisher_Name) references PUBLISHER(Publisher_Name)
);

CREATE TABLE BOOK_LOANS (
    Book_Id int,
    Branch_Id int,
    Card_No int,
    Date_Out date primary key,
    Due_Date date,
    Returned_date date,
    Foreign key (Book_Id) references BOOK(Book_Id),
    Foreign key (Branch_Id) references LIBRARY_BRANCH(Branch_Id),
    Foreign key (Card_No) references BORROWER(Card_No)
);

CREATE TABLE BOOK_COPIES (
    Book_Id int,
    Branch_Id int,
    No_Of_Copies int,
    Foreign key (Book_Id) references BOOK(Book_Id),
    Foreign key (Branch_Id) references LIBRARY_BRANCH(Branch_Id)
);

CREATE TABLE BOOK_AUTHORS (
    Book_Id int primary key,
    Author_Name varchar(255),
    Foreign key (Book_Id) references BOOK(Book_Id)
);

INSERT INTO Publisher VALUES ('HarperCollins','212-207-7000','195 Broadway, New York, NY 10007'),
	('Penguin Books','212-366-3000','475 Hudson St, New York, NY 10014'),
	('Penguin Classics','212-366-2000','123 Main St, California, CA 01383'),
	('Scribner','212-207-7474','19 Broadway, New York, NY 10007'),
	('Harper & Row','212-207-7000','1195 Border street, Montana, MT 59007'),
	('Little, Brown and Company','212-764-2000','111 Huddle St, New Jersey, NJ 32014'),
	('Faber and Faber','201-797-3800','463 south centre street, Arizona, AR 71653'),
	('Chatto & Windus','442-727-3800','Bloomsbury House, 7477 Great Russell St, Arizona, AR 72965'),
	('Ward, Lock and Co.','647-242-3434','456 Maple Ave, Texas, TX 76013 '),
	('Random House India','291-225-6634','423 baywatch centre street, Alabama, AL - 30513'),
	('Thomas Cautley Newby','243-353-2352','890 Elmwood Dr, Floride, FL 98238'),
	('Allen & Unwin','212-782-9001','22 New Wharf Rd, Arizona, AR 70654'),
	('Pan Books','313-243-5353','567 Pine Tree Rd, Colorado, CO 87348'),
	('Bantam Books','313-243-5354','1745 Broadway, New York, NY 10019'),
	('Doubleday','212-782-9000','789 Division St, Minnesota, MN 55344'),
	('American Publishing Company','682-243-3524','7652 Northgate way lane, Georgia, GA - 30054'),
	('Chapman and Hall','833-342-2343','789 Oak St, Texas, TX 76010');

INSERT INTO Library_Branch VALUES (1,'Main Branch','123 Main St, New York, NY 10003'),
	(2,'West Branch','456 West St, Arizona, AR 70622'),
	(3,'East Branch','789 East St, New Jersy, NY 32032');

INSERT INTO Borrower VALUES (123456,'John Smith','456 Oak St, Arizona, AR 70010','205-555-5555'),
	(789012,'Jane Doe','789 Maple Ave, New Jersey, NJ 32542','555-235-5556'),
	(345678,'Bob Johnson','12 Elm St, Arizona, AR 70345 ','545-234-5557'),
	(901234,'Sarah Kim','345 Pine St, New York, NY 10065','515-325-2158'),
	(567890,'Tom Lee','678  S Oak St, New York, NY 10045','209-525-5559'),
	(234567,'Emily Lee','389 Oaklay St, Arizona, AR 70986','231-678-5560'),
	(890123,'Michael Park','123 Pinewood St, New Jersey, NJ 32954','655-890-2161'),
	(456789,'Laura Chen','345 Mapman Ave, Arizona, AR 70776','565-985-9962'),
	(111111,'Alex Kim','983 Sine St, Arizona, AR 70451','678-784-5563'),
	(222222,'Rachel Lee','999 Apple Ave, Arizona, AR 70671','231-875-5564'),
	(333333,'William Johnson','705 Paster St, New Jersey 32002','235-525-5567'),
	(444444,'Ethan Martinez','466 Deeplm St, New York, NY 10321','555-555-5569'),
	(555555,'Grace Hernandez','315 Babes St, Arizona, AR 70862 ','455-567-5587'),
	(565656,'Sophia Park','678 Dolphin St, New York, NY 10062','675-455-5568'),
	(676767,'Olivia Lee','345 Spine St, New York, NY 10092','435-878-5569'),
	(787878,'Noah Thompson','189 GreenOak Ave, New Jersey, NJ 32453','245-555-5571'),
	(989898,'Olivia Smith','178 Elm St, New Jersey, NJ 32124','325-500-5579'),
	(121212,'Chloe Park','345 Shark St, Arizona, AR 72213','755-905-5572'),
	(232323,'William Chen','890 Sting St, New York, NY 10459','406-755-5580'),
	(343434,'Olivia Johnson','345 Pine St, New Jersey, NJ 32095','662-554-5575'),
	(454545,'Dylan Kim','567 Cowboy way St, New Jersey, NJ 32984','435-254-5578');

INSERT INTO Book_Loans VALUES (1,1,123456,'2022-01-01 00:00:00','2022-02-01 00:00:00','2022-02-01 00:00:00'),
	(2,1,789012,'2022-01-02 00:00:00','2022-02-02 00:00:00','2022-02-02 00:00:00'),
	(3,2,345678,'2022-01-03 00:00:00','2022-02-03 00:00:00','2022-02-03 00:00:00'),
	(4,3,901234,'2022-01-04 00:00:00','2022-02-04 00:00:00','2022-02-04 00:00:00'),
	(5,1,567890,'2022-01-05 00:00:00','2022-02-05 00:00:00','2022-02-09 00:00:00'),
	(6,2,234567,'2022-01-06 00:00:00','2022-02-06 00:00:00','2022-02-10 00:00:00'),
	(7,2,890123,'2022-01-07 00:00:00','2022-02-07 00:00:00','2022-03-08 00:00:00'),
	(8,3,456789,'2022-01-08 00:00:00','2022-02-08 00:00:00','2022-03-10 00:00:00'),
	(9,1,111111,'2022-01-09 00:00:00','2022-02-09 00:00:00','2022-02-06 00:00:00'),
	(10,2,222222,'2022-01-10 00:00:00','2022-02-10 00:00:00','2022-02-07 00:00:00'),
	(11,1,333333,'2022-03-01 00:00:00','2022-03-08 00:00:00','2022-02-08 00:00:00'),
	(12,3,444444,'2022-03-03 00:00:00','2022-03-10 00:00:00','2022-03-10 00:00:00'),
	(13,3,555555,'2022-02-03 00:00:00','2022-03-03 00:00:00','2022-02-18 00:00:00'),
	(14,1,565656,'2022-01-14 00:00:00','2022-02-14 00:00:00','2022-03-31 00:00:00'),
	(15,3,676767,'2022-01-15 00:00:00','2022-02-15 00:00:00','2022-02-21 00:00:00'),
	(16,2,787878,'2022-03-05 00:00:00','2022-03-12 00:00:00','2022-02-24 00:00:00'),
	(17,3,989898,'2022-03-23 00:00:00','2022-03-30 00:00:00','2022-03-30 00:00:00'),
	(18,3,121212,'2022-01-18 00:00:00','2022-02-18 00:00:00','2022-02-18 00:00:00'),
	(19,1,232323,'2022-03-24 00:00:00','2022-03-31 00:00:00','2022-03-31 00:00:00'),
	(20,3,343434,'2022-01-21 00:00:00','2022-02-21 00:00:00','2022-02-21 00:00:00'),
	(21,3,454545,'2022-01-24 00:00:00','2022-02-24 00:00:00','2022-02-24 00:00:00');

INSERT INTO Book_Copies VALUES (1,1,3),
	(2,1,2),
	(3,2,1),
	(4,3,4),
	(5,1,5),
	(6,2,3),
	(7,2,2),
	(8,3,1),
	(9,1,4),
	(10,2,2),
	(11,1,3),
	(12,3,2),
	(13,3,1),
	(14,1,5),
	(15,3,1),
	(16,2,3),
	(17,3,2),
	(18,3,2),
	(19,1,5),
	(20,3,1),
	(21,3,1);

INSERT INTO Book_Authors VALUES (1,'Harper Lee'),
	(2,'George Orwell'),
	(3,'Jane Austen'),
	(4,'F. Scott Fitzgerald'),
	(5,'Gabriel Garcia Marquez'),
	(6,'George Orwell'),
	(7,'J.D. Salinger'),
	(8,'William Golding'),
	(9,'Aldous Huxley'),
	(10,'Oscar Wilde'),
	(11,'Paulo Coelho'),
	(12,'Arundhati Roy'),
	(13,'Emily Bronte'),
	(14,'J.R.R. Tolkien'),
	(15,'J.R.R. Tolkien'),
	(16,'Douglas Adams'),
	(17,'Anne Frank'),
	(18,'Dan Brown'),
	(19,'Mark Twain'),
	(20,'Mark Twain'),
	(21,'Charles Dickens');


INSERT INTO Book VALUES (1,'To Kill a Mockingbird','HarperCollins'),
	(2,'1984','Penguin Books'),
	(3,'Pride and Prejudice','Penguin Classics'),
	(4,'The Great Gatsby','Scribner'),
	(5,'One Hundred Years of Solitude','Harper & Row'),
	(6,'Animal Farm','Penguin Books'),
	(7,'The Catcher in the Rye','Little, Brown and Company'),
	(8,'Lord of the Flies','Faber and Faber'),
	(9,'Brave New World','Chatto & Windus'),
	(10,'The Picture of Dorian Gray','Ward, Lock and Co.'),
	(11,'The Alchemist','HarperCollins'),
	(12,'The God of Small Things','Random House India'),
	(13,'Wuthering Heights','Thomas Cautley Newby'),
	(14,'The Hobbit','Allen & Unwin'),
	(15,'The Lord of the Rings','Allen & Unwin'),
	(16,'The Hitchhiker''s Guide to the Galaxy','Pan Books'),
	(17,'The Diary of a Young Girl','Bantam Books'),
	(18,'The Da Vinci Code','Doubleday'),
	(19,'The Adventures of Huckleberry Finn','Penguin Classics'),
	(20,'The Adventures of Tom Sawyer','American Publishing Company'),
	(21,'A Tale of Two Cities','Chapman and Hall');

CREATE VIEW vBookLoanInfo AS
select borrower.card_no, name, date_out, due_date, returned_date, abs(julianday(Date_out) - julianday(Due_Date)),title, iif(julianday(Returned_date) - julianday(Due_Date) > 0,julianday(Returned_date) - julianday(Due_Date),0), branch_id, iif(julianday(Returned_date) - julianday(Due_Date) > 0, LateFee,0)
from borrower 
left join book_loans on borrower.card_no=book_loans.card_no
natural join book
natural join library_branch;
