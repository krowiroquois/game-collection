from Physical import Physical # imports the Physical class from Physical.py
from Digital import Digital # imports the Digital class from Digital.py
from Collection import Collection # imports the Collection class from Collection.py

def main():
    print("Welcome to my Game Collection App!")
    # defines the function "main" to print the following statement

    collection = Collection()

    game1 = Physical("Metal Gear Solid", 1999, 100, "PS1")
    game2 = Physical("Sonic the Hedgehog", 2006, 15, "XBOX 360")
    game3 = Digital("Boyfriend to Death", 2016, 0, "BTD Website")
    game4 = Digital("Governor of Poker", 2016, 0, "Steam")

    collection.add_game(game1)
    collection.add_game(game2)
    collection.add_game(game3)
    collection.add_game(game4)

    while True:
         print("\nMenu")
         print("1. Show all games")
         print("2. Add a game")
         print("Type 'quit' to exit")
         
         
         try:
            choice = input("Choose an option: ")
            if choice == "1":
                collection.show_games() # displays entire list of games
            
            elif choice == "2":
                name = input("Enter the game name: ") # asks user to input game name

                while True:
                    try:
                        year = int(input("Enter the release year: "))
                        # asks user to input release year of the game

                        if year < 1972:
                            print("The very first video game was released in 1972, so that")
                            print("answer is impossible. Let's try that again!")
                            continue
                        # if the user were to input a year less than 1972, this message would
                        # pop up, then send the user back to the beginning of the "year"
                        # input prompt
                        
                        if year > 2026:
                            print("How in the hell did you get a game from the future?")
                            print("You some type of time traveler?")
                            continue
                        # same thing for the previous if statement, except it doesn't allow
                        # the user to time travel & own games that haven't yet been released

                        break 
                        # ends the loop so that it doesn't repeat in case
                        # there may be an error
                    
                    except ValueError:
                        print("Please enter a valid number for the year.")
                    # prints an error if the user inputs string instead of an integer
                
                while True:
                    try:
                        price = int(input("Enter the price: "))

                        if price < 0:
                            print("Please enter a price that is 0 or greater.")
                            continue

                        break
                    
                    except ValueError:
                        print("Please enter a valid number for the price.")
            

                while True:
                    game_type = input("Is this game physical or digital? ")

                    if game_type.lower() == "physical":
                        console = input("Enter the console: ")
                        game = Physical(name, year, price, console)
                        collection.add_game(game)
                        print(f"{game.name} has been added to the Collection!")
                        break
                        
                    elif game_type.lower() == "digital":
                        source = input("Enter the source of the download: ")
                        game = Digital(name, year, price, source)
                        collection.add_game(game)
                        print(f"{game.name} has been added to the Collection!")
                        break

                    else:
                        print("Invalid game type.")
                        continue

            elif choice == "3":
                pass

            elif choice == "4":
                pass
            

            elif choice.lower() == "quit": # if the user types "quit",
                print("See you around, superstar!") # prints a nice goodbye statement!
                break # ends the entire loop and exits the menu
            
            else: 
                print("Please choose from the available menu options.")
                # if the user types anything but the available menu options, this will print
                # to encourage them to input something that works.


         except Exception as e:
            print(f"Something went wrong: {e}")  


if __name__ == "__main__":
    main()


#games = [game1, game2, game3, game4] # all of the games put into a list

#for game in games:
    #game.display_info()
    # displays all the info from the list

#main() # calls the function so that the print statement runs
