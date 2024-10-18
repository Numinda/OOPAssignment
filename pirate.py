from loot import Loot
from ship import Ship

class Pirate:
    def __init__(self, name):
        self.__name = name  # Pirate's name
        self.__inventory = [Loot("Gold Piece", "A shiny piece of gold")]  # Start with one Gold Piece
        self.__ship = None  # Pirate starts without a ship
        self.__health = 100  # Pirate's health
      
    def purchase_ship(self, ship):
        if self.has_gold_piece():  # Check if the pirate has a Gold Piece
            self.__inventory.remove(self.search_inventory("Gold Piece"))  # Remove the Gold Piece
            self.__ship = ship  # Set the ship
            ship.set_owner(self)  # Set the ship owner
            print(f"{self.__name} has purchased the ship: {ship.get_name()}!")  # Print confirmation
        else:
            print(f"{self.__name} does not have enough gold to purchase a ship.")

    def has_gold_piece(self):
        # Check if the pirate has a Gold Piece in their inventory
        return any(item.get_name() == "Gold Piece" for item in self.__inventory)

    def search_inventory(self, item_name):
        # Searches for an item in the pirate's inventory
        for item in self.__inventory:
            if item.get_name() == item_name:
                return item
        print(f"{self.__name} does not have any {item_name}.")
        return None

    def get_ship(self):
        return self.__ship  # Getter for the pirate's ship

    # Getter for pirate's name
    def get_name(self):
        return self.__name

    # Health setter with validation
    def set_health(self, health):
        if 0 <= health <= 100:
            self.__health = health
        else:
            print("Health must be between 0 and 100")

    # Method to repair the ship
    def repair_ship(self):
        if self.has_ship() and self.has_gold_piece():
            self.__inventory.remove(self.search_inventory("Gold Piece"))  # Remove Gold Piece for repair
            self.__ship.repair()  # Call the ship's repair method
        else:
            print("You either don't have a ship or no Gold to repair it.")

    # Method to fire a cannonball at another ship
    def fire_cannonball(self, target_ship):
        if self.has_ship() and self.has_cannonball():
            self.__inventory.remove(self.search_inventory("Cannonball"))  # Remove Cannonball from inventory
            target_ship.take_hit()  # Hit the target ship
            print(f"{self.__name} fired a cannonball!")
        else:
            print("You either don't have a ship or no Cannonball to fire.")

    def has_cannonball(self):
        # Check if the pirate has a Cannonball in their inventory
        return any(item.get_name() == "Cannonball" for item in self.__inventory)

    # Method to loot a ship if it's broken
    def loot_ship(self, target_ship):
        if target_ship.is_broken():
            self.__inventory.extend(target_ship.get_cargo())  # Take all the cargo from the ship
            target_ship.clear_cargo()  # Clear the cargo from the target ship
            print(f"{self.__name} has looted the ship!")
        else:
            print("The ship is not completely broken.")

    # Method to check if the pirate owns a ship
    def has_ship(self):
        return self.__ship is not None

    # Method to transfer loot from inventory to ship's cargo
    def store_loot_in_cargo(self, loot_name):
        if self.has_ship():
            item = self.search_inventory(loot_name)
            if item:
                self.__ship.store_item(item)
                self.__inventory.remove(item)
                print(f"{loot_name} stored in {self.__ship.get_name()}'s cargo.")
            else:
                print(f"{loot_name} not found in inventory.")
        else:
            print("Pirate has no ship to store items.")

    # Method to retrieve loot from ship's cargo to inventory
    def retrieve_loot_from_ship(self, loot_name):
        if self.has_ship():
            loot = self.__ship.retrieve_loot(loot_name)
            if loot:
                self.__inventory.append(loot)
                print(f"{loot_name} retrieved from {self.__ship.get_name()}'s cargo.")
        else:
            print("Pirate has no ship to retrieve items from.")

    # String representation of the pirate
    def __str__(self):
        ship_name = self.__ship.get_name() if self.__ship else "No Ship"
        return f"Pirate: {self.__name}, Ship: {ship_name}, Inventory: {self.__inventory}"
