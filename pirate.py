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

    def get_name(self):
        return self.__name  # Getter for pirate's name

    def set_health(self, health):
        if 0 <= health <= 100:
            self.__health = health
        else:
            print("Health must be between 0 and 100")

    def repair_ship(self):
        if self.has_ship() and self.has_gold_piece():
            self.__inventory.remove(self.search_inventory("Gold Piece"))  # Remove Gold Piece for repair
            self.__ship.repair()  # Call the ship's repair method
        else:
            print("You either don't have a ship or no Gold to repair it.")

    def fire_cannonball(self, target_ship):
        if self.has_ship() and self.search_inventory("Cannonball"):
            cannonball = self.search_inventory("Cannonball")
            self.__inventory.remove(cannonball)  # Remove Cannonball from inventory
            target_ship.take_hit()  # Hit the target ship
            print(f"{self.__name} fired a cannonball!")
        else:
            print("You either don't have a ship or no Cannonball to fire.")

    def loot_ship(self, target_ship):
        if target_ship.is_broken():
            self.__inventory.extend(target_ship.get_cargo())  # Take all the cargo from the ship
            target_ship.clear_cargo()  # Clear the cargo from the target ship
            print(f"{self.__name} has looted the ship!")
        else:
            print("The ship is not completely broken.")

    def has_ship(self):
        return self.__ship is not None

    def find_item(self, item_name):
        for item in self.__inventory:
            if item.get_name() == item_name:
                self.__inventory.remove(item)
                return item
        print(f"{self.__name} does not have any {item_name}.")
        return None

    def store_in_ship(self, item_name=None):
        if self.has_ship():
            if item_name:
                item = self.find_item(item_name)
                if item:
                    self.__ship.store_item(item)
            else:
                while self.__inventory:
                    item = self.__inventory.pop()
                    self.__ship.store_item(item)

    def retrieve_from_ship(self, item_name=None):
        if self.has_ship():
            if item_name:
                item = self.__ship.retrieve_item(item_name)
                if item:
                    self.__inventory.append(item)
            else:
                while self.__ship.has_cargo():
                    item = self.__ship.retrieve_all_items()
                    self.__inventory.append(item)

    def __str__(self):
        ship_name = self.__ship.get_name() if self.__ship else "No Ship"
        return f"Pirate: {self.__name}, Ship: {ship_name}, Inventory: {self.__inventory}"

