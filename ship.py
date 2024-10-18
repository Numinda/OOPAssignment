# ship.py
class Ship:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken = False
        self.__cargo = ['Cannonball', 'Cannonball', 'Eye Patch']

    def get_name(self):
        return self.__name

    def take_hit(self):
        self.__damage_counter += 1
        if self.__damage_counter >= 2:
            self.__broken = True
            print(f"{self.__name} is now broken!")

    def repair(self):
        if self.__damage_counter > 0:
            self.__damage_counter = 0
            self.__broken = False
            print(f"{self.__name} has been repaired!")
        else:
            print(f"{self.__name} does not need repairs.")

    def is_broken(self):
        return self.__broken

    def get_cargo(self):
        return self.__cargo

    def clear_cargo(self):
        self.__cargo = []

    def check_condition(self):
        if self.__damage_counter == 0:
            return "Excellent condition"
        elif self.__damage_counter == 1:
            return "Slight damage"
        else:
            return "Broken"

    def __str__(self):
        return f"Ship: {self.__name}, Condition: {self.check_condition()}, Cargo: {self.__cargo}"
