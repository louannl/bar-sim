from beer_prize.beer_prize_animation import play_beer
from save.player import Player
from save.stats import Stats


class End:
    def __init__(self, stats: Stats) -> None:
        self.stats = stats

    def wins(self, player: Player) -> list:
        return self.stats.return_play_count_and_win_count(
            player.id
        )

    def wins_plays(self, wins: list) -> list:
        return self.times(wins[0]), self.times(wins[1])

    def times(self, value: int) -> list:
        times = 'time'
        if value > 1 or value == 0:
            times = 'times'
        return times

    def end(self, player: Player) -> None:
        wins, plays = self.wins(player)
        win_times, play_times = self.wins_plays([wins, plays])
        print(
            f'You have played {plays} {play_times}, and won {wins} {win_times}'
        )
        print(self.stats.display_leaderboard())
        play_beer()
