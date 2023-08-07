class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Scoreboard():
    def __init__(self):
        self.players = {}

    def add_player(self, name, player):
        self.players[name] = player

    def add_score(self, name, points):
        self.players[name].score += points

    def get_total_score(self):
        total_score = 0
        for name, player in self.players.items():
            total_score += player.score
        return total_score

    def get_player_score(self, name):
        return self.players[name].score
