import json # imports json
from Physical import Physical # imports Physical class from Physical.py
from Digital import Digital # imports Digital class from Digital.py

class Collection: # defines the Collection class
    def __init__(self):
        self.games = []
        # empty list for the games
    
    def add_game(self, game):
        self.games.append(game)
        # method adds a game
    
    def remove_game(self, number):
        removed_game = self.games.pop(number - 1)
        print(f"\n{removed_game.name} has been removed from the collection!")
        # method removes a game using its corresponding number
        # prints a statement notifying user the game was removed
    
    def show_games(self): # method shows the games
        if not self.games: # if there are no games present,
            print("\nThe game collection is empty.")
            # statement notifies the user

        else: # otherwise,
            for number, game in enumerate(self.games, start=1):
            # loop numerates each game so that it has a corresponding number
                print(f"{number}. ", end="")
                # attaches the number to the game before the following method
                game.display_info() # displays information on the game
    
    def total_value(self): # method calculates total value of the game

        if not self.games: # if there are no games in the list,
            print("\nThere game collection is empty.") 
            print("Therefore, the total value of your collection is $0.")
            # statement notifies user that the collection is empty and that
            # the value is zero

        total = 0 # starter value for the list

        for game in self.games: # for each game,
            total += game.price # code adds up the total value in reference to the game price

        print(f"\nThe total value of your collection is ${total:.2f}")
        # statement notifies user of total value of collection
        # ":.2f" makes it so that there are two decimal points attached
        # to the overall total.
    
    def save_games(self): # defines the save_game method
        data = []
        # empty list for the data
        for game in self.games:

            if isinstance(game, Physical): # if the game is Physical,
                data.append({
                    "type": "Physical",
                    "name": game.name,
                    "year": game.year,
                    "price": game.price,
                    "console": game.console
                }) # adds all attributes corresponding to the game
            
            elif isinstance(game, Digital): # if the game is Digital,
                data.append({
                    "type": "Digital",
                    "name": game.name,
                    "year": game.year,
                    "price": game.price,
                    "source": game.source
                }) # adds all attributes corresponding to the game
        
        with open("games.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def load_games(self):
        try:
            with open("games.json", "r") as file:
                data = json.load(file)

            for game in data:

                if game["type"].lower() == "physical":
                    new_game = Physical(
                        game["name"],
                        game["year"],
                        game["price"],
                        game["console"]
                    )

                elif game["type"].lower() == "digital":
                    new_game = Digital(
                        game["name"],
                        game["year"],
                        game["price"],
                        game["source"]
                    )

                self.games.append(new_game)
        
        except FileNotFoundError:
            pass
            # if the file isn't found, code runs as usual