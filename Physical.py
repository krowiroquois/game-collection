from VideoG import Game

class Physical(Game):
    def __init__(self, name, year, price, console):
        super().__init__(name, year, price)
        self.console = console
        # defines attributes of the physical game class
    
    def display_info(self):
        print(f"{self.name} ({self.year}) - ${self.price} - Physical - {self.console}")
        # displays info about the game

if __name__ == "__main__":
    game1 = Physical("Metal Gear Solid", 1999, 100, "PS1")
    game1.set_price(75)

