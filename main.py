from Physical import Physical # imports the Physical class from Physical.py
from Digital import Digital # imports the Digital class from Digital.py
from Collection import Collection # imports the Collection class from Collection.py

def main():
    print("\n\nWelcome to my Game Collection App!")
    # defines the function "main" to print the following statement

    # the "\n" will automatically add a space to the string. you will see these throughout
    # the code

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
         print(" ")
         print("☆" * 5 + " MAIN MENU " + "☆" * 5)
         print("1. Show all games")
         print("2. Add a game")
         print("3. Search for a game")
         print("Type 'quit' to exit")
         print("☆" * 20)
         print(" ")
         
         
         try:
            choice = input("\nChoose an option: ")
            if choice == "1":
                collection.show_games() # displays entire list of games



            
            elif choice == "2":
                name = input("\nEnter the game name: ") # asks user to input game name

                while True:
                    try:
                        year = int(input("\nEnter the release year: "))
                        # asks user to input release year of the game

                        if year < 1972:
                            print("\nThe very first video game was released in 1972, so that")
                            print("answer is impossible. Let's try that again!")
                            continue
                        # if the user were to input a year less than 1972, this message would
                        # pop up, then send the user back to the beginning of the input prompt
                        
                        if year > 2026:
                            print("\nHow in the hell did you get a game from the future?")
                            print("You some type of time traveler?")
                            continue
                        # same thing for the previous if statement, except it doesn't allow
                        # the user to time travel & own games that haven't yet been released

                        break 
                        # ends the loop so that it doesn't repeat in case
                        # there may be an error
                    
                    except ValueError:
                        print("\nPlease enter a valid number for the year.")
                    # prints an error if the user inputs string instead of an integer
                
                while True:
                    try:
                        price = int(input("\nEnter the price: "))
                        # prompts the user to input the price of the game

                        if price < 0:
                            print("\nPlease enter a price that is 0 or greater.")
                            continue 
                        # prevents a user from inputting a negative price, returns to beginning of loop.

                        break #self-explanatory
                    
                    except ValueError:
                        print("\nPlease enter a valid number for the price.")
                    # prints an error if the user inputs a string instead of an integer
            

                while True:

                    game_type = input("\nIs this game physical or digital? ")
                    # prompts the user to answer whether the game is physical or digital

                    if game_type.lower() == "physical": # if the game is physical,

                        console = input("\nEnter the console: ") # prompts the user to enter the console of the disc

                        game = Physical(name, year, price, console)
                        # this assigns all attributes inputted to the game
                        # by the prior prompts

                        collection.add_game(game)
                        # method adds game to the collection

                        print(f"\n{game.name} has been added to the Collection!")
                        break
                        
                    elif game_type.lower() == "digital":
                        source = input("\nEnter the source of the download: ")
                        game = Digital(name, year, price, source)
                        collection.add_game(game)
                        print(f"\n{game.name} has been added to the Collection!")
                        break

                    else:
                        print("\nInvalid game type.")
                        continue
                    




            elif choice == "3":
                while True:
                    search_game = input("\nEnter the name of the game you are searching for, or type 'exit': ")
                        # prompts user to input the name of the game they're looking for, or to exit the search

                    if search_game.lower() == "exit": # if user inputs 'exit'
                        print("\nReturning to main menu...")
                        print(" ")
                        break # statement prints, user returns to the main menu

                    found = False # condition unsatisfied until user locates the game

                    for game in collection.games:
                        if search_game.lower() in game.name.lower(): # if the term serched corresponds with a game,
                            print("\nFound it!") # prints statement saying the game was found
                            game.display_info() # displays game info
                            print("\nReturning to main menu...") # statement prints
                            found = True # condition satisfied since the game was found
                            break # ends code, leaves for loop
                    
                    if found:
                        break
                        # if found, user leaves the while loop and returns to main menu
                
                    if not found:
                        print("\nGame not found.")
                        continue
                        # if not found, user starts the beginning of while loop again
                    




            elif choice == "4":
                pass

            

            elif choice.lower() == "quit": # if the user types "quit",
                print("\nSee you around, superstar!") # prints a nice goodbye statement!
                break # ends the entire loop and exits the menu
            
            else: 
                print("\nPlease choose from the available menu options.")
                # if the user types anything but the available menu options, this will print
                # to encourage them to input something that works.


         except Exception as e:
            print(f"\nSomething went wrong: {e}")
            # this will print just in case the user happens to input anything that may break the code
             


if __name__ == "__main__":
    main()


#games = [game1, game2, game3, game4] # all of the games put into a list

#for game in games:
    #game.display_info()
    # displays all the info from the list

#main() # calls the function so that the print statement runs
