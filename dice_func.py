# simple dice function


class DiceDecider:

    def __init__(self):
        self.action = None
        self.dice_result = None

    def dice_roll(self):
        import random
        self.dice_result = random.randint(1, 6)
        return self.dice_result

    def odd_or_even(self):
        self.dice_roll()
        if (self.dice_result % 2) == 0:
            return True
        else:
            return False

    def try_action_50_50(self, action):
        if self.odd_or_even():
            print("Success! You have managed to {}".format(action))
        else:
            try_new_thing = input("Oh no! You failed to {}, would you like to try something else? y/n ".format(action))
            if try_new_thing == 'y':
                action = input("What would you like to try instead? ")
                self.try_action_50_50(action)
            else:
                exit()

    def try_action_custom_odds(self, action, min_num_to_do_action):
        dice_roll = self.dice_roll()
        if dice_roll <= min_num_to_do_action:
            print("Success! You have managed to {}".format(action))
        else:
            try_new_thing = input("Oh no! You failed to {}, would you like to try something else? y/n ".format(action))
            if try_new_thing == 'y':
                action = input("What would you like to try instead? ")
                self.try_action_custom_odds(action, min_num_to_do_action)
            else:
                exit()
