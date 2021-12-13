from datetime import datetime
import mysql.connector
import os
from dotenv import load_dotenv
import requests

load_dotenv()


def random_insult():
    # moved URL so it exists outside of the try loop so that the except clause can access
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    try:
        request = requests.get(url).json()
        return request['insult']
    # added exception so it's not a bare except clause
    except Exception:
        raise ConnectionError(f"Unable to connect to api {url}.")


def get_character(num):
    access_token = os.getenv('SUPERHERO_API_KEY')
    url = f"https://superheroapi.com/api/{access_token}/{num}"
    try:
        return requests.get(url).json()
    # same as above
    except Exception:
        raise ConnectionError(f"Unable to connect to api {url}.")


def set_user_character():
    # dict should maybe exist outside of the function, perhaps in the db?
    # alternatively could we instead return a random selection of the superheroes? and have the user enter the
    # corresponding id?

    player_options = {
        1: {'name': 'Buffy',
            'id': 140},
        2: {'name': 'Deadpool',
            'id': 213},
        3: {'name': 'Mystique',
            'id': 480},
        4: {'name': 'Rambo',
            'id': 540}
    }
    # this only displays the name - feels like a waste of the api! will api stats come into this?
    print("Which player would you like to select:")
    # can we display all player options at once? one at a time seems like poor UX
    for player_no, player_info in player_options.items():
        player_select = input(
            f"Player {player_no}: {player_info['name']}?\nEnter y to accept or n to keep browsing:")
        if player_select == "y":
            confirmed_player_id = player_info["id"]
            print("done")
            return confirmed_player_id
        if player_select == "n":
            pass
        else:
            print(
                "I'm sorry that is not a recognised option. To select a player, you need to please press y or n. "
                "Let's try again.")
            set_user_character()
    browse_again = input(
        "You have browsed through all of our available player options. Do you want to try again? Enter y to select a "
        "player or any key to exit the game.\n")
    if browse_again == "y":
        set_user_character()
    else:
        print("Thank you for playing Get Served.")
        # I've made it an exit command as SystemExit came up with a warning that the statement did nothing
        exit()
<<<<<<< HEAD


# this gave me {'response': 'error', 'error': 'access denied'}
print(get_character(140))


def connect_db():
    con = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        auth_plugin=os.getenv('DB_AUTH_PLUGIN'),
        database=os.getenv('DB_NAME')
    )
    return con


# creates a time stamp for game finish
class EndOfGame:
    def save_game(self):
        self.game_time = datetime.now()
        return self.game_time

    def convert_timestamp(self):
        game_time_string = self.game_time.strftime('%d-%m-%Y')
        return game_time_string

    def save(self):
        self.save_game()
        gts = self.convert_timestamp()
        return gts


class GameDBConnection(Exception):
    pass


class Query:
    def __init__(self):
        pass

    def game_db_query(self, db_query, params):
        db_connection = {}
        try:
            db_connection = connect_db()
            cursor = db_connection.cursor()
            cursor.execute(db_query, (params))
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

# parameterization of the SQL queries helps protect against SQL injection
# create query to send game data to game_info table
    def send_game_data(self, player_id, character_name, game_time_string, end_result):
        query_string = ('''INSERT INTO game (player_id, main_character, result, date)
         VALUES (%s,%s,%s,%s)''')
        params = (player_id, character_name, end_result, game_time_string,)
        send_game_connection = self.game_db_query(query_string, params)
        return send_game_connection

# create query to send player to player_info table database
    def send_player_data(self, player_name):
        query_string = '''INSERT INTO player (full_name) VALUES (%s)'''
        params = (player_name,)
        send_player_connection = self.game_db_query(query_string, params)
        return send_player_connection

# create query to check if player already exists in player_info database
    def check_player(self, player_name):
        query_string = '''SELECT * FROM player WHERE Full_Name = %s'''
        params = (player_name,)
        query_result = (self.game_db_query(query_string, params))
        return query_result

# func to create query updating the total number of plays for the player after the individual game data is added
    def update_total_plays(self, player_id):
        query_string = '''UPDATE player p
        INNER JOIN (SELECT player_id, COUNT(player_id) as player_count 
        FROM game 
        GROUP BY player_id) AS g
        ON g.player_id = p.id
        SET p.total_plays = g.player_count
        WHERE id = %s'''
        params = (player_id,)
        update_total_play = self.game_db_query(query_string, params)
        return update_total_play

    def check_player_result(self, query_result, player_name):
        if query_result == 0:
            self.send_player_data(player_name)
        return query_result

    def get_player_id(self):
        query_string = '''SELECT LAST_INSERT_ID()'''
        params = None
        id_result = self.game_db_query(query_string, params)
        print(id_result)
        return id_result

# function to encompass all the queries that get sent to the database at the end of the game
    def send_all_queries(self, player_name, character_name, game_time_string, end_result):
        player_checked = self.check_player(player_name)
        self.check_player_result(player_checked, player_name)
        player_id = self.get_player_id()
        self.send_game_data(player_id, character_name, game_time_string, end_result)
        self.update_total_plays(player_id)
=======
>>>>>>> main
