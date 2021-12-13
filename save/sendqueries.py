from save.save_game import SaveGame
from save.player import CheckPlayer
from save.query import Query


def db_queries(player_name, character_name, game_time_string, end_result):
    check = CheckPlayer()
    checked_player = check.check_player(player_name)
    add_player = Query()
    add_player.check_result(checked_player, player_name)
    add_player.get_id(player_name)
    add_player.insert_game(player_name, character_name,
                           end_result, game_time_string)
    add_player.update_total_plays(player_name)
    return check


def end_game(player_name, character_name, end_result):
    finish = SaveGame()
    game_time_string = finish.save()
    send_queries = db_queries(
        player_name, character_name, game_time_string, end_result)
    return send_queries
