# pirate.py

class Pirate:
    def __init__(self, name):
        self.__name = name
        self.__inventory = ['Gold Piece']  # Start with a single Gold Piece
        self.__ship = None  # No ship initially
        self.__health = 100  # Health starts at 100

    # Getter for pirate's name
    def get_name(self):
        return self.__name

    # Health setter with validation
    def set_health(self, health):
        if 0 <= health <= 100:
            self.__health = health
        else:
            print("Health must be between 0 and 100")

    # Method to buy a ship
    def buy_ship(self, ship):
        if 'Gold Piece' in self.__inventory:
            self.__inventory.remove('Gold Piece')  # Remove Gold Piece from inventory
            self.__ship = ship  # Assign the ship to the pirate
            print(f"{self.__name} has purchased the ship: {ship.get_name()}")
        else:
            print("Not enough Gold to buy a ship.")

    # Method to repair the ship
    def repair_ship(self):
        if self.has_ship() and 'Gold Piece' in self.__inventory:
            self.__inventory.remove('Gold Piece')  # Remove Gold Piece for repair
            self.__ship.repair()  # Call the ship's repair method
        else:
            print("You either don't have a ship or no Gold to repair it.")

    # Method to fire a cannonball at another ship
    def fire_cannonball(self, target_ship):
        if self.has_ship() and 'Cannonball' in self.__inventory:
            self.__inventory.remove('Cannonball')  # Remove Cannonball from inventory
            target_ship.take_hit()  # Hit the target ship
            print(f"{self.__name} fired a cannonball!")
        else:
            print("You either don't have a ship or no Cannonball to fire.")

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
        if self.__ship:
            return True
        else:
            print("You cannot perform this action without a ship.")
            return False

    # Method to check the pirate's inventory for an item
    def find_item(self, item_name):
        for item in self.__inventory:
            if item == item_name:
                self.__inventory.remove(item)
                return item
        print(f"{self.__name} does not have any {item_name}.")
        return None

    # Method to transfer loot from inventory to ship's cargo
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

    # Method to retrieve loot from ship's cargo to inventory
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

    # String representation of the pirate, showing the pirate's name, ship's name, and inventory
    def __str__(self):
        ship_name = self.__ship.get_name() if self.__ship else "No Ship"
        return f"Pirate: {self.__name}, Ship: {ship_name}, Inventory: {self.__inventory}"

