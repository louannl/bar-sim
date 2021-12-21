from save.player import Player
from save.db_connection import Query
from game_engine.game import Game
from save.save import GetGameHistory, CreateGame


def create_or_return_player_id(player_name: str, game_state: Game) -> None:
    player = Player(Query())
    player_exists = player.check_player(player_name)
    if not player_exists:
        player.create_player(player_name)
        player_exists = player.check_player(player_name)

    game_state.update_player_id(player_exists[0][0])


def save_game(game_state: Game) -> None:
    game = CreateGame(Query())
    game.create_game_save(
        game_state.get_player_id(),
        game_state.get_character_name(),
        game_state.get_win(),
        game_state.get_pints()
    )
