import os
import requests
import random

from utils.retry_decorator import retry_input
from utils.custom_exceptions import ApiError


def get_random_superhero(superhero_list):
    return random.choice(list(superhero_list.keys()))


def get_character(num):
    access_token = os.getenv('SUPERHERO_API_KEY')
    url = f"https://superheroapi.com/api/{access_token}/{num}"
    try:
        request = requests.get(url)
        request.raise_for_status()
        request = request.json()
        if request['response'] == 'error':
            raise ApiError(
                f"An error has occurred while connecting to {url}: "
                f"{request['error']}"
            )
        return request
    except requests.exceptions.RequestException:
        print(f'An error has occurred while connecting to {url}')


@retry_input
def set_user_character(player_options):
    print("Which player would you like to select:")
    for player_no, player_info in player_options.items():
        player_select = input(
            f"Player {player_no}: {player_info['name']}?\n"
            "Enter 'y' to select or 'n' to keep browsing: "
        )

        if player_select == "y":
            return player_info["id"]

        elif player_select == "n":
            pass

        else:
            print(
                "I'm sorry that is not a recognised option. To select a "
                "player, you need to please enter 'y', to keep browsing "
                "enter 'n'."
            )
            raise ValueError

    browse_again = input(
        "You have browsed through all of our available player options. \n"
        "Do you want to try again?\nEnter 'y' to "
        "browse again or any key to exit the game: "
    )

    if browse_again == "y":
        set_user_character(player_options)

    else:
        print("Thank you for playing Get Served.")
        exit()
