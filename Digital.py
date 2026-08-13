from VideoG import Game

class Digital(Game):
    def __init__(self, name, year, price, source):
        super().__init__(name, year, price)
        self.source = source

    def display_info(self):
        print(f"{self.name} ({self.year}) - ${self.price} - Digital - {self.source}")

if __name__ == "__main__":
    game1 = Digital("Boyfriend to Death", 2016, 0, "Official Website")
    game1.set_price(5)