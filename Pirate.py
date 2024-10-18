# pirate.py
class Pirate:
    def __init__(self, name):
        self.__name = name
        self.__inventory = ['Gold Piece']
        self.__ship = None
        self.__health = 100

    def get_name(self):
        return self.__name

    def set_health(self, health):
        if 0 <= health <= 100:
            self.__health = health
        else:
            print("Health must be between 0 and 100")

    def buy_ship(self, ship):
        if 'Gold Piece' in self.__inventory:
            self.__inventory.remove('Gold Piece')
            self.__ship = ship
            print(f"{self.__name} has purchased the ship: {ship.get_name()}")
        else:
            print("Not enough Gold to buy a ship.")

    def repair_ship(self):
        if self.has_ship() and 'Gold Piece' in self.__inventory:
            self.__inventory.remove('Gold Piece')
            self.__ship.repair()
        else:
            print("You either don't have a ship or no Gold to repair it.")

    def fire_cannonball(self, target_ship):
        if self.has_ship() and 'Cannonball' in self.__inventory:
            self.__inventory.remove('Cannonball')
            target_ship.take_hit()
            print(f"{self.__name} fired a cannonball!")
        else:
            print("You either don't have a ship or no Cannonball to fire.")

    def loot_ship(self, target_ship):
        if target_ship.is_broken():
            self.__inventory.extend(target_ship.get_cargo())
            target_ship.clear_cargo()
            print(f"{self.__name} has looted the ship!")
        else:
            print("The ship is not completely broken.")

    def has_ship(self):
        return self.__ship is not None

    def __str__(self):
        ship_name = self.__ship.get_name() if self.__ship else "No Ship"
        return f"Pirate: {self.__name}, Ship: {ship_name}, Inventory: {self.__inventory}"
