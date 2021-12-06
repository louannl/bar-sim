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
