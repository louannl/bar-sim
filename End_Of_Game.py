from database_connection import connect_db
import datetime
from datetime import datetime

######## creates a time stamp for game finish #########

class GameSave():
    def save_game(self):
        self.game_time = datetime.now()
        return self.game_time

    def convert_timestamp(self):
        game_time_string = self.game_time.strftime('%d-%m-%Y')
        return game_time_string

class EndOfGame(GameSave):
    def save(self):
        game_end = GameSave()
        game_end.save_game()
        gts = game_end.convert_timestamp()
        return gts

class GameDBConnection(Exception):
    pass


class Query():
    def __init__(self):
        pass

    def game_db_query(self, db_query, params):
        db_connection = {}
        try:
            db_name = 'Game'
            db_connection = connect_db(db_name)
            cursor = db_connection.cursor()
            query = (db_query)
            cursor.execute(query, params)
            results = cursor.fetchall()
            len_results = (len(results))
            cursor.close()
            db_connection.commit()
        except Exception:
            raise GameDBConnection('Information not available!')
        finally:
            if db_connection:
                db_connection.close()
        return len_results


#### parametirisation of the SQL queries hekos protect against SQL injenction ####

#### create query to send game data to game_info table ####
    def send_game_data(self, player_name,game_character, game_time_string, end_result):
        query_string = ('''INSERT INTO game_info (Player_Name, Player_Character, Game_Result, Date_Of_Game)
        VALUES (%s,%s,%s,%s)''')
        params = (player_name, game_character,game_time_string, end_result,)
        send_game_connection = self.game_db_query(query_string, params)
        return send_game_connection



#### create query to send player to player_info table database ####
    def send_player_data(self, player_name):
        query_string =  ('''INSERT INTO player_info (Full_Name) VALUES %s''')
        params = (player_name)
        send_player_connection = self.game_db_query(query_string, params,)
        return send_player_connection


### create query to check if player already exists in player_info database ###
    def check_player(self, player_name):
        query_string = '''SELECT * FROM player_info WHERE Full_Name = %s'''
        params = (player_name,)
        query_result = (self.game_db_query(query_string, params))
        return query_result

    def update_total_plays(self, player_name):
        query_string = ('''UPDATE player_info p
        INNER JOIN (SELECT Player_Name, COUNT(Player_Name) as player_count 
        FROM game_info 
        GROUP BY Player_Name) AS g
        ON g.Player_Name = p.Full_Name
        SET p.Total_Plays = g.player_count
        WHERE Full_Name = %s''')
        params = (player_name,)
        update_total_play = self.game_db_query(query_string, params)
        return update_total_play


    def check_player_result(self, query_result, player_name):
        if query_result == 0:
            self.send_player_data(player_name)
        else:
           pass
        return query_result


### function to ecompass all the queries that get sent to the database at the end of the game ###

    def send_all_queries(self, player_name, game_character, game_time_string, end_result):
        player_checked = self.check_player(player_name)
        self.check_player_result(player_checked, player_name)
        self.send_game_data(player_name, game_character, game_time_string, end_result)
        self.update_total_plays(player_name)



