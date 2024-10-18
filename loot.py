# loot.py

class Loot:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    # Getter for the loot name
    def get_name(self):
        return self.__name

    # Getter for the loot description
    def get_description(self):
        return self.__description

    # String conversion method to describe the loot
    def __str__(self):
        return f"{self.__name}: {self.__description}"

