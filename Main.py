# main.py
from pirate import Pirate
from ship import Ship

def main():
    # Create a Pirate and a Ship
    blackbeard = Pirate("Blackbeard")
    print(blackbeard)

    # Try buying a ship
    blackbeard.buy_ship(Ship("The Black Pearl"))

    # Fire cannonball at another ship
    enemy_ship = Ship("The Flying Dutchman")
    blackbeard.fire_cannonball(enemy_ship)
    blackbeard.fire_cannonball(enemy_ship)

    # Loot the enemy ship
    blackbeard.loot_ship(enemy_ship)

    # Print the status of Blackbeard
    print(blackbeard)

if __name__ == "__main__":
    main()
