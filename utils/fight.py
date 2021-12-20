import time

from game_engine.character import Character


class FightClub:

    def __init__(self, superhero: Character, main_character: Character) -> None:
        self.superhero = superhero
        self.main_character = main_character
        self.main_char_win_speed = superhero.speed <= main_character.speed
        self.main_char_win_strength = superhero.strength <= main_character.strength
        self.main_char_win_intelligence = superhero.intelligence <= main_character.intelligence
        self.char_wins = 0

    def round1_speed(self):
        if self.main_char_win_speed:
            print(f"Nice one! Your punch makes contact with a satisfying smack!")
            self.char_wins += 1
            return True
        else:
            print(
                f"{self.superhero.name} dodges it and your fist goes crashing into the wall - ouch!")
            return False

    def round2_intelligence(self):
        if self.main_char_win_intelligence:
            print(
                f"In the background, you can hear someone just put an 80s banger on the pub jukebox. You start singing like your life depends on it 'It's the eye of the tiger, it's the thrill of the fight!'")
            time.sleep(5)
            print(
                f"Your rousing soprano voice elicits a hearty chorus back from drunken pub-goers. People start hugging. You use {self.superhero.name}'s confusion as a chance to gather your breath!")
            time.sleep(5)
            self.char_wins += 1
            return True
        else:
            print(
                f'''You try to distract {self.superhero.name} - "hey, what's that over there?!"''')
            time.sleep(5)
            print('*Crickets*. You get a mildly annoyed look in response - "Wow. You expected me to fall for that?"')
            time.sleep(5)
            return False

    def narration(self):
        print(
            f"Your opponent is coming towards you looking angry! You stumble a few steps backwards but there is no where to run...")
        time.sleep(5)
        print(f"Your opponent is picking up speed and yells araaaaaaaaaaghghhhhh as they go in to tackle you.")
        time.sleep(5)
        print(
            f"There's nothing else for it - you lower your head and start running towards {self.superhero.name} - you shout aiaiaaiaiaiaiiiiiiiiii!")
        print(f"It's a terrifying game of chicken!")
        time.sleep(5)
        print(f"There's an almighty crunch of skull hitting and skull. A silence comes across the pub...")
        time.sleep(6)

    def round3_strength(self) -> bool:
        if self.main_char_win_strength:
            print(
                f"You look around and are relieved to see {self.superhero.name} out cold on the floor. You drag your worthy foe to a nearby stool and prop him up in it. His head will hurt when he wakes up.")
            self.char_wins += 1
            return True
        else:
            print(
                f"Ooph, you find yourself flat on your back with tiny birds floating around your head. Strange, were they there earlier? You get onto your feet staggering slightly")
            return False

    def activate_rounds_get_outcome(self):
        self.round1_speed()
        self.round2_intelligence()
        self.narration()
        self.round3_strength()
        return self.char_wins >= 2
