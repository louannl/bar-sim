DROP DATABASE IF EXISTS bar_game;
CREATE DATABASE bar_game;

USE bar_game;

DROP TABLE IF EXISTS player_info;

CREATE TABLE player (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(55) NOT NULL,
    total_plays INT DEFAULT 0
) ENGINE InnoDB;

DROP TABLE IF EXISTS game;

CREATE TABLE game (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    player_id BIGINT,
    player_character VARCHAR(55) NULL,
    won BOOL NOT NULL,
    date DATETIME NOT NULL,
    FOREIGN KEY (player_id)
        REFERENCES player(id)
        ON DELETE CASCADE
) ENGINE InnoDB;
