-- Creates users table.
--  only if TABLES AND JUST TANENNNNNNNNNN
-- NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
-- NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
