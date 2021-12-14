from save.player import CheckPlayer, CreatePlayer
from save.query import Query
from game_engine.game import Game


def create_or_return_player_id(player_name: str, game_state: Game) -> None:
    player = CheckPlayer(Query())
    player_exists = player.check_player(player_name)
    if not player_exists:
        new_player = CreatePlayer(Query())
        new_player.create_player(player_name)
        player_exists = player.check_player(player_name)

    game_state.update_player_id(player_exists[0][0])
