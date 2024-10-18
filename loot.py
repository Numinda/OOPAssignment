# loot.py
class Loot:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    def __str__(self):
        return f"{self.__name}: {self.__description}"
