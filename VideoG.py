class Game: # blueprint class for kind 1 and 2 of the code
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
        # defines the attributes of the Game class
    
    def set_price(self, amount): # sets the price
        if amount < 0:
            print(f"Error: The price for {self.name} cannot be below zero!")
            # if price is less than 0, a statement will print letting the user know
            # that the input is invalid
        else:
            self.price = amount
            print(f"{self.name} {self.year} {self.price}")
            # if price is equal or greater to zero, a statement will print displaying
            # the name, year, and price
    
    def display_info(self):
        print(f"{self.name} ({self.year}) - ${self.price}")
        # displays info about the game

if __name__ == "__main__":
    game1 = Game("Sonic the Hedgehog", 2006, 15)
    game2 = Game("Bayonetta", 2010, 25)
    game1.set_price(-5)
    game2.set_price(35)