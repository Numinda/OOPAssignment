# main.py

from pirate import Pirate
from ship import Ship
from loot import Loot

def main():
    # Create pirates
    blackbeard = Pirate("Blackbeard")
    captain_hook = Pirate("Captain Hook")
    
    # Create ships
    ship1 = Ship("Queen Anne's Revenge")
    ship2 = Ship("Jolly Roger")

    # Test purchasing a ship without gold pieces
    print("\n--- Test Purchasing Ship Without Gold ---")
    captain_hook.purchase_ship(ship1)  # Should fail as no gold

    # Blackbeard purchases a ship
    print("\n--- Test Blackbeard Purchasing Ship ---")
    blackbeard.purchase_ship(ship1)  # Should succeed

    # Test repairing a ship without gold
    print("\n--- Test Repairing Ship Without Gold ---")
    blackbeard.repair_ship()  # Should fail as he has no gold to repair

    # Blackbeard fires a cannonball at an enemy ship
    print("\n--- Test Firing Cannonball ---")
    blackbeard.fire_cannonball(ship2)  # Should succeed, damaging the ship

    # Check the ship's condition
    print("\n--- Checking Ship Condition ---")
    print(ship2.get_condition())  # Should show damage condition

    # Blackbeard tries to loot ship2 before it is broken
    print("\n--- Test Looting Ship Before It's Broken ---")
    blackbeard.loot_ship(ship2)  # Should fail as ship is not broken

    # Fire more cannonballs to break ship2
    blackbeard.fire_cannonball(ship2)  # Damages the ship again
    blackbeard.fire_cannonball(ship2)  # Now the ship should be broken

    # Check if ship2 is broken
    print("\n--- Checking If Ship Is Broken ---")
    if ship2.is_broken():
        print(f"{ship2.get_name()} is broken!")

    # Blackbeard loots the now broken ship2
    print("\n--- Test Looting Ship After It's Broken ---")
    blackbeard.loot_ship(ship2)  # Should succeed, taking all cargo

    # Show Blackbeard's inventory after looting
    print("\n--- Blackbeard's Inventory After Looting ---")
    print(blackbeard)  # Should show updated inventory

    # Test storing loot in ship's cargo
    print("\n--- Test Storing Loot in Ship's Cargo ---")
    blackbeard.store_loot_in_cargo("Gold Piece")  # Should succeed

    # Test retrieving loot from ship's cargo
    print("\n--- Test Retrieving Loot from Ship's Cargo ---")
    blackbeard.retrieve_loot_from_ship("Cannonball")  # Should succeed if cargo has it

    # Attempt to use methods without a ship
    print("\n--- Test Actions Without Ship ---")
    captain_hook.fire_cannonball(ship1)  # Should fail as captain_hook has no ship

    # Check the cargo of Blackbeard's ship
    print("\n--- Checking Blackbeard's Ship Cargo ---")
    if blackbeard.get_ship():
        print(blackbeard.get_ship().get_cargo())  # Show cargo if he has a ship

if __name__ == "__main__":
    main()

