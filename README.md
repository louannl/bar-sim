# bar-sim

the main file contains a few lines of code showing how the end of the game is saved with just some mock variables containing

--player_name
--player_character
--end result

these can be changed to match variables in the main game if need be


End_Of_Game contains all the classes and functions required to save the game and then carry out queries to:

-- mark a time stamp for the end of the game
-- check if a player already exists in the player_info table of the database
--if it doesnt then it sends the player_info to the database
-- regardless if player is already in the player_info table, the data from the individual game is added 
   to the game_info table

gitignore contains a file .env containing my credentials to connect to the database
   
   
