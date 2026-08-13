from VideoG import Game

class Digital(Game):
    def __init__(self, name, year, price, source):
        super().__init__(name, year, price)
        self.source = source
        # defines attributes of the digital game class

    def display_info(self):
        print(f"{self.name} ({self.year}) - ${self.price} - Digital - {self.source}")
        # displays info about the game

if __name__ == "__main__":
    game1 = Digital("Boyfriend to Death", 2016, 0, "Official Website")
    game1.set_price(5)