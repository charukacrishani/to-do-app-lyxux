CREATE DATABASE IF NOT EXISTS todo;
USE todo;

CREATE TABLE IF NOT EXISTS tasks(
	id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR (20) NOT NULL,
    ddate DATE NOT NULL,
    isdone BOOLEAN NOT NULL
);

INSERT INTO tasks (task, ddate, isdone) VALUES
("gvjnjvn", "2024.06.02", true),
("gvjnj vn", "2024.05.02", false)
