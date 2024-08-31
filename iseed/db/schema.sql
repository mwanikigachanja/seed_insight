CREATE DATABASE seedinsight;

USE seedinsight;

CREATE TABLE ecozones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    min_altitude INT,
    max_altitude INT,
    description TEXT
);

CREATE TABLE crops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    variety VARCHAR(255),
    ecozone_id INT,
    maturity_period INT,
    seed_rate_per_acre INT,
    yield_per_acre INT,
    attributes TEXT,
    FOREIGN KEY (ecozone_id) REFERENCES ecozones(id)
);
