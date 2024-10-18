from loot import Loot

class Ship:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__is_broken = False
        self.__cargo = []  # Cargo starts empty
        # Add initial loot: 2 Cannonballs and 1 Eye Patch
        self.__cargo.append(Loot("Cannonball", "A heavy ball for cannon fire"))
        self.__cargo.append(Loot("Cannonball", "A heavy ball for cannon fire"))
        self.__cargo.append(Loot("Eye Patch", "A classic pirate accessory"))

    def retrieve_loot(self, loot_name):
        for item in self.__cargo:
            if item.get_name() == loot_name:
                self.__cargo.remove(item)
                return item
        print(f"No {loot_name} found in the cargo.")
        return None

    def get_name(self):
        return self.__name

    def take_hit(self):
        self.__damage_counter += 1  # Increment damage counter with each hit
        print(f"{self.__name} took a hit! Damage counter: {self.__damage_counter}")
        if self.__damage_counter >= 2:
            self.__is_broken = True
            print(f"{self.__name} is now broken!")

    def repair(self):
        if self.__damage_counter > 0:
            self.__damage_counter = 0
            self.__is_broken = False
            print(f"{self.__name} has been repaired!")
        else:
            print(f"{self.__name} does not need repairing.")

    def is_broken(self):
        return self.__is_broken

    def get_condition(self):
        if self.__damage_counter == 0:
            return "Ship is in excellent condition."
        elif self.__damage_counter == 1:
            return "Ship has minor damage."
        else:
            return "Ship is broken and needs repairs."

    def store_item(self, item):
        self.__cargo.append(item)
        print(f"Stored {item} in {self.__name}'s cargo.")

    def retrieve_item(self, item_name):
        for item in self.__cargo:
            if item.get_name() == item_name:
                self.__cargo.remove(item)
                print(f"Retrieved {item_name} from {self.__name}'s cargo.")
                return item  # Return the Loot object instead of just the name
        print(f"{item_name} not found in {self.__name}'s cargo.")
        return None

    def has_cargo(self):
        return len(self.__cargo) > 0

    def retrieve_all_items(self):
        all_items = self.__cargo[:]
        self.__cargo.clear()
        return all_items

    def get_cargo(self):
        return self.__cargo

    def clear_cargo(self):
        self.__cargo.clear()

    def __str__(self):
        condition = self.get_condition()
        cargo_contents = ', '.join(str(item) for item in self.__cargo) if self.__cargo else "Empty"
        return f"Ship: {self.__name}, Condition: {condition}, Cargo: {cargo_contents}"

