import random
import requests


class Insult:
    def __init__(self) -> None:
        self.insults = [
            '''Out, you green-sickness carrion! Out, you baggage!
            You tallow-face!''',
            '''He hath eaten me out of house and home;
            he hath put all substance into that fat belly of his.''',
            '''It is a tale Told by an idiot, full of sound and fury,
            Signifying nothing''',
            '''Give me your hand...I can tell your fortune. You are a fool.'''
        ]

    def get_random_insult(self) -> str:
        return random.choice(self.insults)
