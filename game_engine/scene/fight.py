
from game_engine.character.fight import FightClub
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game_engine.game.game import Game


def fight_scene(game_state: 'Game') -> str:
    fight_club = FightClub(game_state.superhero, game_state.main_character)
    fight_result = fight_club.activate_rounds_get_outcome()
    if fight_result:
        game_state.pint_counter.update_pints(2)
        return 'win'
    game_state.pint_counter.update_pints(-2)
    return 'fightTime'
