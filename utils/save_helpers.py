from save.player import Player
from save.query import Query
from game_engine.game import Game
from save.save_game import GetGameHistory, CreateGame


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


def return_play_and_win_count(game_state: Game):
    win_lose_count = GetGameHistory(Query())
    results = win_lose_count.return_play_count_and_win_count(
        game_state.get_player_id())
    play_count = results[0][1]
    win_count = results[0][0]
    return win_count, play_count
