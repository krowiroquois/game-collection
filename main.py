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
         print("\nGame Collection Menu")
         print("1. Show games")
         print("2. Add a game")
         print("Type 'quit' to exit")
         
         
         try:
            choice = input("Choose an option: ")
            if choice == "1":
                collection.show_games()
            
            elif choice == "2":
                name = input("Enter the game name: ")

                while True:
                    try:
                        year = int(input("Enter the release year: "))

                        if year < 1972:
                            print("The very first video game was released in 1972, so that")
                            print("answer is impossible. Please enter a valid year.")
                            continue
                            
                        break
                    
                    except ValueError:
                        print("Please enter a valid number for the year.")
                
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

            
            elif choice.lower() == "quit":
                print("See you around, superstar!")
                break
            
            else:
                print("Please choose from the available menu options.")


         except Exception as e:
            print(f"Something went wrong: {e}")  


if __name__ == "__main__":
    main()


#games = [game1, game2, game3, game4] # all of the games put into a list

#for game in games:
    #game.display_info()
    # displays all the info from the list

#main() # calls the function so that the print statement runs
