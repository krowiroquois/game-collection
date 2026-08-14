class Collection:
    def __init__(self):
        self.games = []
    
    def add_game(self, game):
        self.games.append(game)
    
    def show_games(self):
        if not self.games:
            print("The game collection is empty.")
        else:
            for number, game in enumerate(self.games, start=1):
                print(f"{number}. ", end="")
                game.display_info()