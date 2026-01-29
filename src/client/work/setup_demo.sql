USE OperatingSystems;

-- Tabel 1: Gebruikers (Voor de FE/BE demo)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL
);

INSERT INTO users (username, role) 
VALUES ('student', 'admin'), 
       ('docent', 'viewer');

-- Tabel 2: Logs (Voor het aantonen van monitoring)
CREATE TABLE IF NOT EXISTS server_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event VARCHAR(100) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO server_logs (event) 
VALUES ('SSH Login success'), 
       ('Database backup completed'),
       ('Webserver started');