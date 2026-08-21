from Physical import Physical # imports the Physical class from Physical.py
from Digital import Digital # imports the Digital class from Digital.py
from Collection import Collection # imports the Collection class from Collection.py

def main(): # defines the function main() - overall code of the app

    print("\n\nWelcome to my Game Collection App!")
    # displays the following statement at the beginning

    # the "\n" will automatically add a space to the string when it prints in the terminal
    # you will see these throughout the code

    collection = Collection() # calls the Collection class
    collection.load_games() # loads all previous data

    while True: # runs the condition until it breaks
         print(" ")
         print(" ☆ " * 5 + " MAIN MENU " + " ☆ " * 5)
         print("1. Show all games")
         print("2. Add a game")
         print("3. Search for a game")
         print("4. Remove a game")
         print("5. Calculate overall value")
         print("Type 'quit' to exit")
         print(" ☆ " * 14)
         print(" ")
         # prints the menu options
         
         try:
            choice = input("\nChoose an option: ")
            # prompts user to input one of the 6 options

            if choice == "1": # if user chooses option 1,
                collection.show_games() # displays entire list of games

            
            elif choice == "2": # if user chooses option 2,
                name = input("\nEnter the game name: ") # asks user to input game name

                while True: # runs the condition until it breaks
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

                        console = input("\nEnter the console: ")
                        # prompts the user to enter the console of the disc

                        game = Physical(name, year, price, console)
                        # this assigns all attributes inputted to the game
                        # by the prior prompts

                        collection.add_game(game)
                        # method adds game to the collection

                        print(f"\n{game.name} has been added to the Collection!")
                        break
                        # statement prints, returns to main menu 
                        
                    elif game_type.lower() == "digital": # if the game is digital,
                        source = input("\nEnter the source of the download: ")
                        # user is prompted to input the source of the digital download

                        game = Digital(name, year, price, source)
                        # this assigns all attributes assigned to the game through
                        # prior inputs

                        collection.add_game(game)
                        # adds the game to the collection

                        print(f"\n{game.name} has been added to the Collection!")
                        break
                        #statement prints, returns to main menu

                    else:
                        print("\nInvalid game type.")
                        continue
                        # statement will notify user of invalid input, returns to beginning of loop
                    




            elif choice == "3": # if user picks choice 3,
                while True:
                    search_game = input("\nEnter the name of the game you are searching for, or type 'exit': ")
                        # prompts user to input the name of the game they're looking for, or to exit the search

                    if search_game.lower() == "exit": # if user inputs 'exit'
                        print("\nReturning to main menu...")
                        print(" ")
                        break # statement prints, user returns to the main menu

                    found = False # condition unsatisfied until user locates the game
                    # allowing the loop to function

                    for game in collection.games: # for all the games in the collection,
                        if search_game.lower() in game.name.lower(): # if the term serched corresponds with a game,
                            print("\nFound it!") # prints statement saying the game was found
                            game.display_info() # displays game info
                            print("\nReturning to main menu...") # notifies user of returning to main menu
                            found = True # condition satisfied since the game was found
                            break # ends code, leaves the for loop
                    
                    if found:
                        break
                        # if the game was found, user leaves the while loop and returns to main menu.
                        # this prevents the code from constantly looping in the search option
                
                    if not found:
                        print("\nGame not found.")
                        continue
                        # if not found, user is notified.
                        # starts the beginning of while loop again
                    




            elif choice == "4": # if user chooses 4,
                collection.show_games()
                # displays collection of games so the user can refer back to it

                while True:
                    try:
                        number = int(input("\nEnter the number of the game you would like to remove: "))
                        # prompts user to enter the number corresponding to the game they want to remove

                        if 1 <= number <= len(collection.games): # if the number corresponds to a game,
                            collection.remove_game(number) # removes the game from the list
                            break # ends loop
                        else: 
                            print("\nGame number not found.")
                            # notifies the user that a game was not found underneath the corresponding
                            # number

                    except ValueError:
                        print("\nPlease enter a valid number.")
                    # notifies user that they did not input a valid integer when attempting
                    # to remove the game
            
            elif choice == "5": # if user chooses option 5,
                collection.total_value()
                # displays total value of collection; method pulled from Collection.py

            

            elif choice.lower() == "quit": # if the user types "quit",
                collection.save_games() # saves the data of the collection
                print("\nAll progress saved!")
                print("\nSee you around, superstar! ☆⸜(｡˃ ᵕ ˂ )⸝☆")
                print(" ")
                # prints a nice goodbye statement!
                break # ends the entire loop and exits the menu
            
            else: 
                print("\nPlease choose from the available menu options by typing")
                print("the corresponding number.")
                # if the user types anything but the available menu options, this will print
                # to encourage them to input something that works.


         except Exception as e:
            print(f"\nSomething went wrong: {e}")
            # this will print just in case the user happens to input anything that may cause
            # an error in the code



if __name__ == "__main__":
    main()
    # calls the overall code
