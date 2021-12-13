import os
from sys import exit

from dotenv import load_dotenv
import requests

load_dotenv()


def random_insult():
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    try:
        request = requests.get(url).json()
        return request['insult']
    except requests.exceptions.ConnectionError:
        print(f"Unable to connect to api {url}.")


def get_character(num):
    access_token = os.getenv('SUPERHERO_API_KEY')
    web_address = "https://superheroapi.com/api/"
    url = f"{web_address}/{access_token}/{num}"
    try:
        return requests.get(url).json()
    except requests.exceptions.ConnectionError:
        print(f"Unable to connect to api {web_address}.")


def set_user_character():
    # dict should maybe exist outside of the function, perhaps in the db?

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

    print("Which player would you like to select:")
    # can we display all player options at once? one at a time seems like poor UX
    for player_no, player_info in player_options.items():
        player_select = input(f"Player {player_no}: {player_info['name']}?\nEnter 'y' to select or 'n' to keep browsing: ")
        if player_select == "y":
            confirmed_player_id = player_info["id"]
            return confirmed_player_id
        if player_select == "n":
            pass
        else:
            print(
                "I'm sorry that is not a recognised option. To select a player, you need to please enter 'y', to keep browsing enter 'n'. "
                "Let's try again.")
            set_user_character()
    browse_again = input(
        "You have browsed through all of our available player options. Do you want to try again? Enter 'y' to browse again or any key to exit the game.\n")
    if browse_again == "y":
        print("Which player would you like to select: ")
        set_user_character()
    else:
        print("Thank you for playing Get Served.")
        exit()
