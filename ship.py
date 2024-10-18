from loot import Loot

class Ship:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__is_broken = False
        self.__cargo = []  # Cargo starts empty
        self.__owner = None  # Initialize the ship owner as None
        # Add initial loot: 2 Cannonballs and 1 Eye Patch
        self.__cargo.append(Loot("Cannonball", "A heavy ball for cannon fire"))
        self.__cargo.append(Loot("Cannonball", "A heavy ball for cannon fire"))
        self.__cargo.append(Loot("Eye Patch", "A classic pirate accessory"))

    # Set the ship's owner
    def set_owner(self, pirate):
        self.__owner = pirate  # Set the pirate as the owner of the ship

    # Retrieve loot from the cargo (specific item or all items)
    def retrieve_loot(self, loot_name):
        for item in self.__cargo:
            if item.get_name() == loot_name:
                self.__cargo.remove(item)
                return item
        print(f"No {loot_name} found in the cargo.")
        return None

    # Getter for ship's name
    def get_name(self):
        return self.__name

    # Method to take a hit from a cannonball
    def take_hit(self):
        self.__damage_counter += 1  # Increment damage counter with each hit
        print(f"{self.__name} took a hit! Damage counter: {self.__damage_counter}")
        if self.__damage_counter >= 2:
            self.__is_broken = True
            print(f"{self.__name} is now broken!")

    # Method to repair the ship
    def repair(self):
        if self.__damage_counter > 0:
            self.__damage_counter = 0
            self.__is_broken = False
            print(f"{self.__name} has been repaired!")
        else:
            print(f"{self.__name} does not need repairing.")

    # Method to check if the ship is broken
    def is_broken(self):
        return self.__is_broken

    # Method to get the condition of the ship based on damage counter
    def get_condition(self):
        if self.__damage_counter == 0:
            return "Ship is in excellent condition."
        elif self.__damage_counter == 1:
            return "Ship has minor damage."
        else:
            return "Ship is broken and needs repairs."

    # Method to store an item in the ship's cargo
    def store_item(self, item):
        self.__cargo.append(item)
        print(f"Stored {item} in {self.__name}'s cargo.")

    # Method to retrieve an item from the cargo
    def retrieve_item(self, item_name):
        for item in self.__cargo:
            if item.get_name() == item_name:
                self.__cargo.remove(item)
                print(f"Retrieved {item_name} from {self.__name}'s cargo.")
                return item
        print(f"{item_name} not found in {self.__name}'s cargo.")
        return None

    # Method to check if the cargo has items
    def has_cargo(self):
        return len(self.__cargo) > 0

    # Method to retrieve all items from the cargo
    def retrieve_all_items(self):
        all_items = self.__cargo[:]
        self.__cargo.clear()
        return all_items

    # Method to get the ship's cargo
    def get_cargo(self):
        return self.__cargo

    # Method to clear the cargo (used when looted)
    def clear_cargo(self):
        self.__cargo.clear()

    # String conversion method to represent the ship
    def __str__(self):
        condition = self.get_condition()
        cargo_contents = ', '.join(str(item) for item in self.__cargo) if self.__cargo else "Empty"
        return f"Ship: {self.__name}, Condition: {condition}, Cargo: {cargo_contents}"



