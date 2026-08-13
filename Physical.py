from VideoG import Game

class Physical(Game):
    def __init__(self, name, year, price, console):
        super().__init__(name, year, price)
        self.console = console




game1 = Physical("Metal Gear Solid", 1999, 100, "PS1")

game1.set_price(75)

