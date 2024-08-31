CREATE DATABASE medihelpdb;
USE medihelpdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE ,
    nic VARCHAR(100) UNIQUE,
    age VARCHAR(100),
    gender VARCHAR(100),
    address VARCHAR(100),
    mobile VARCHAR(100) UNIQUE,
    img VARCHAR(255),
    password VARCHAR(100)
);

select * from users;

CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
);

INSERT INTO admins (email, password) VALUES ('admin@gmail.com', 'admin@123');
select * from admins;

CREATE TABLE doctor (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    hospital TEXT NOT NULL,
    contact TEXT NOT NULL,
    specifications TEXT NOT NULL
);

INSERT INTO doctor (name, hospital, contact, specifications)
VALUES
('Dr. Dilip Kumara', 'Colombo National Hospital', '011-212-3456', 'BA - Cellulitis'),
('Dr. Amal Bandara', 'Kandy National Hospital', '081-223-4567', 'BA - Impetigo'),
('Dr. Pasan Jayasuriya', 'Galle Teaching Hospital', '091-234-5678', 'FU - Athlete Foot'),
('Dr. Chandana Rathnayake', 'Anuradhapura General Hospital', '025-245-6789', 'FU - Ringworm');


CREATE TABLE prediction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    prediction VARCHAR(255) NOT NULL,
    datetime DATETIME NOT NULL,
    age INT NOT NULL,
    FOREIGN KEY (userId) REFERENCES users(id)
);
