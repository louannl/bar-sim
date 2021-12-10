DROP DATABASE IF EXISTS Game;
CREATE DATABASE Game;

USE Game;
DROP TABLE IF EXISTS player_info;
CREATE TABLE player_info (
Player_ID INT auto_increment NOT NULL,
Full_Name VARCHAR(55) NOT NULL primary key,
Total_Plays varchar(55) NULL,
key (Player_ID)
) ENGINE InnoDB;

DROP TABLE IF EXISTS game_info;
CREATE TABLE game_info (
Game_ID INT auto_increment key,
Player_Name VARCHAR(55) NOT NULL,
Player_Character VARCHAR(55) NULL,
Game_Result VARCHAR(55) NOT NULL,
Date_Of_Game VARCHAR (55) NOT NULL,
foreign key (Player_Name) references player_info(Full_Name)
) ENGINE InnoDB;

Select * FROM game_info;
SELECT * FROM player_info;
