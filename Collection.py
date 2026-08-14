class Collection:
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