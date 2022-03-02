class Phone:
    def __init__(self, pcharge, lcharge):
        self.__pcharge = pcharge
        self.__lcharge = lcharge

    def set__manufact(self):
        self.__manufact = input("?")

    def set__model(self):
        self.__model = input("What is the model?")

    def get_parts_charges(self):
        return self.__pcharge

    def get_labor_charges(self):
        return self.__lcharge

    def get_sales_tax(self):
        return self.__

    def get_total_charges(self):
        return self.__lcharge
