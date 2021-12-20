
from game_engine.game import Game
from utils.fight import FightClub


def fight_scene(game_state: Game) -> str:
    fight_club = FightClub(game_state.superhero, game_state.main_character)
    fight_result = fight_club.activate_rounds_get_outcome()
    if fight_result:
        game_state.update_pints(2)
        return 'win'
    game_state.update_pints(-2)
    return 'fightTime'
