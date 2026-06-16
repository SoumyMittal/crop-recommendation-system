class Farmer:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location

    def display_info(self):
        print(f"Farmer: {self.__name}")
        print(f"Location: {self.__location}")
