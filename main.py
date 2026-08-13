from Physical import Physical
from Digital import Digital

def main():
    print("Welcome to my Game Collection App!")

main()

game1 = Physical("Metal Gear Solid", 1999, 100, "PS1")
game2 = Physical("Sonic the Hedgehog", 2006, 15, "XBOX 360")
game3 = Digital("Boyfriend to Death", 2016, 0, "BTD Website")
game4 = Digital("Governor of Poker", 2016, 0, "Steam")

games = [game1, game2, game3, game4]

for game in games:
    game.display_info()
