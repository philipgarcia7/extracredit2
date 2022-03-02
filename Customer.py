class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self):
        self.__name = input("Name:")

    def set_address(self):
        self.__address = input("Address: ")

    def set_phone(self):
        self.__phone = input("Phone Number:")

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
