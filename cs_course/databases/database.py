import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.executescript(
    """
    CREATE TABLE class 
(
    id	INT,
    grade	INT
);

INSERT INTO class (id, grade) VALUES
	('101', '10'),
	('102', '10'),
	('103', '10'),
	('104', '10'),
	('111', '11'),
	('112', '11'),
	('113', '11'),
	('114', '11'),
	('121', '12'),
	('122', '12'),
	('123', '12'),
	('124', '12');
    """
)

cursor.executescript(
    """
    CREATE TABLE student 
(
    SId	INT,
    firstname	VARCHAR(512),
    name	VARCHAR(512),
    birthdate	DATE
);

INSERT INTO student (SId, firstname, name, birthdate) VALUES
	('1', 'William', 'Campbell', '2007-05-17'),
	('2', 'Emma', 'Harris', '2007-03-28'),
	('3', 'Isabella', 'Nelson', '2007-12-17'),
	('4', 'Taylor', 'Martinez', '2007-05-25'),
	('5', 'Alyssa', 'Moore', '2006-01-01'),
	('6', 'Sofia', 'Lewis', '2006-02-28'),
	('7', 'Melissa', 'Evans', '2006-04-11'),
	('8', 'Joshua', 'Moore', '2006-09-23'),
	('9', 'Haley', 'Brown', '2005-04-04'),
	('10', 'Ava', 'Young', '2005-11-09'),
	('11', 'Joshua', 'Moore', '2005-07-02'),
	('12', 'Haley', 'Brown', '2005-10-03');
    """
)

cursor.executescript(
    """
    CREATE TABLE teacher 
(
    TId	INT,
    firstname	VARCHAR(512),
    lastname	VARCHAR(512),
    specialization	INT
);

INSERT INTO teacher (TId, firstname, lastname, specialization) VALUES
	('1', 'William', 'Campbell', '1'),
	('2', 'Emma', 'Harris', '4'),
	('3', 'Isabella', 'Nelson', '3'),
	('4', 'Taylor', 'Martinez', '5'),
	('5', 'Alyssa', 'Moore', '6'),
	('6', 'Sofia', 'Lewis', '8'),
	('7', 'Melissa', 'Evans', '7'),
	('8', 'Joshua', 'Moore', '1'),
	('9', 'Haley', 'Brown', '2'),
	('10', 'Ava', 'Young', '3'),
	('11', 'Ava', 'Robinson', '9'),
	('12', 'Ethan', 'Peterson', '10');
    """
)

cursor.executescript(
    """
    CREATE TABLE room 
(
    RId	VARCHAR(512),
    size	INT,
    type	VARCHAR(512)
);

INSERT INTO room (RId, size, type) VALUES
	('UG1', '20', '1'),
	('UG2', '21', '2'),
	('UG3', '21', '1'),
	('UG4', '23', '1'),
	('UG5', '22', '1'),
	('UG6', '24', '2'),
	('UG7', '30', '2'),
	('UG8', '20', '1'),
	('UG9', '20', '2'),
	('UG10', '21', '2'),
	('EG1', '15', '1'),
	('EG2', '18', '1'),
	('EG3', '20', '1'),
	('EG4', '21', '1'),
	('EG5', '23', '1'),
	('EG6', '25', '1'),
	('EG7', '26', '1'),
	('EG8', '28', '1'),
	('EG9', '29', '1'),
	('EG10', '30', '1'),
	('OG1', '31', '1'),
	('OG2', '28', '1'),
	('OG3', '26', '1'),
	('OG4', '24', '3'),
	('OG5', '16', '3'),
	('OG6', '19', '3'),
	('OG7', '29', '3'),
	('OG8', '22', '1'),
	('OG9', '21', '1'),
	('OG10', '25', '2');
    """
)

cursor.executescript(
    """
    CREATE TABLE points 
(
    duration	INT,
    points	INT
);

INSERT INTO points (duration, points) VALUES
	('45', '1'),
	('90', '2'),
	('135', '3'),
	('180', '4'),
	('225', '5');
    """
)

cursor.executescript(
    """
    CREATE TABLE presentation 
(
    PId	INT,
    title	VARCHAR(512),
    description	VARCHAR(512),
    starttime	VARCHAR(512),
    subject	VARCHAR(512),
    date	DATE,
    attendance	INT
);

INSERT INTO presentation (PId, title, description, starttime, subject, date, attendance) VALUES
	('1', 'HTML', 'Lorem ipsum dolor sit amet.', '7,35', '1', '2023-03-27', '15'),
	('2', 'Python', 'Lorem ipsum dolor sit amet.', '7,35', '1', '2023-03-29', '15'),
	('3', 'Experimente', 'Lorem ipsum dolor sit amet.', '9,00', '2', '2023-03-28', '20'),
	('4', '', 'Lorem ipsum dolor sit amet.', '10,15', '3', '2023-03-29', '25'),
	('5', '', 'Lorem ipsum dolor sit amet.', '11,00', '4', '2023-03-30', '20');
    """
)

cursor.executescript(
    """
    CREATE TABLE attendance 
(
    SId	INT,
    PId	INT,
    presenter	VARCHAR(512)
);

INSERT INTO attendance (SId, PId, presenter) VALUES
	('1', '1', '1'),
	('4', '5', '0'),
	('3', '4', '1'),
	('2', '2', '0'),
	('6', '3', '1');
    """
)