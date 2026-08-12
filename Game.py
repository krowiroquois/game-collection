class Game:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
    
    def set_price(self, amount):
        if amount < 0:
            print("Error: The price cannot be below zero!")
        else:
            self.price = amount

game1 = Game("Sonic the Hedgehog", 2006, 15)
game2 = Game("Bayonetta", 2010, 25)

game1.set_price(-5)
game2.set_price(35)