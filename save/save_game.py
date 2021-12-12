from datetime import datetime


class SaveGame:
    def save_game(self):
        self.game_time = datetime.now()
        return self.game_time

    def convert_timestamp(self):
        game_time_string = self.game_time.strftime('%d-%m-%Y')
        return game_time_string

    def save(self):
        self.save_game()
        gts = self.convert_timestamp()
        return gts
