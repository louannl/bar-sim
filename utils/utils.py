import os

from dotenv import load_dotenv

import requests
import random

load_dotenv()


def random_insult():
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    try:
        request = requests.get(url).json()
        return request['insult']
    except requests.exceptions.ConnectionError:
        print(f"Unable to connect to api {url}.")


def get_random_beer():
    beers = ['Stella Artois', 'Peroni', 'Heineken', 'Magners']
    return random.choice(beers)


def get_character(num):
    try:
        access_token = os.getenv('SUPERHERO_API_KEY')
        url = f"https://superheroapi.com/api/{access_token}/{num}"
        return requests.get(url).json()
    except requests.exceptions.ConnectionError:
        print(f"Unable to connect to api {url}.")


def get_random_superhero():
    superhero_list = {
        60: "Bane",
        69: "Batman",
        97: "Black Canary",
        309: "Harlequin",
        322: "Hellboy",
        522: "Poison Ivy",
        374: "Juggernaut",
        400: "Lady Deathstrike",
        489: "Nick Fury"
    }
    return random.choice(list(superhero_list.keys()))


def set_user_character():
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
    for player_no, player_info in player_options.items():
        player_select = input(
            f"Player {player_no}: {player_info['name']}?\nEnter 'y' to select or 'n' to keep browsing: ")
        if player_select == "y":
            return player_info["id"]
        if player_select == "n":
            pass
        else:
            print("I'm sorry that is not a recognised option. To select a player, you need to please enter 'y', to keep browsing enter 'n'. \nLet's try again.")
            set_user_character()
    browse_again = input(
        "You have browsed through all of our available player options. \nDo you want to try again? Enter 'y' to browse again or any key to exit the game: ")
    if browse_again == "y":
        print("Which player would you like to select: ")
        set_user_character()
    else:
        print("Thank you for playing Get Served.")
        exit()
