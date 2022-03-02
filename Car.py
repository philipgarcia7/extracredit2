class Phone:
    def __init__(self, make, year, model):
        self.__make = make
        self.__year = year
        self.__model = model

    def set_make(self):
        self.__make = input("Make:")

    def set_year(self):
        self.__year = input("Year: ")

    def set_model(self):
        self.__model = input("Model:")

    def get_make(self):
        return self.__make

    def get_year(self):
        return self.__year

    def get_model(self):
        return self.__model
