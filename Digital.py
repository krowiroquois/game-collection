from Game import Game

class Digital(Game):
    def __init__(self, name, year, price, source):
        super().__init__(self, name, year, price)
        self.source = source