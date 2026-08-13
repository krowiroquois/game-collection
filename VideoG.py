class Game:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
    
    def set_price(self, amount):
        if amount < 0:
            print(f"Error: The price for {self.name} cannot be below zero!")
        else:
            self.price = amount
            print(f"{self.name} {self.year} {self.price}")
    
    def display_info(self):
        print(f"{self.name} ({self.year}) - ${self.price}")

if __name__ == "__main__":
    game1 = Game("Sonic the Hedgehog", 2006, 15)
    game2 = Game("Bayonetta", 2010, 25)
    game1.set_price(-5)
    game2.set_price(35)