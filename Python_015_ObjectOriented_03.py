class Game:
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("Help information")

    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    def start_game(self):
        print("%s play game" % self.player_name)

