from item import Item

# Class Inheritance
class Laptop(Item):
    pay_rate = 0.6
    def __init__(self, name: str, price: float, quantity=0, processor="amd") -> None:
        # initialize attributes and methods of the parent class as per best practice using the super function
        super().__init__(name, price, quantity)

        # validate arguments
        assert processor.lower() in ["amd", "intel"], "Processsors must either be 'amd' or 'intel'"

        # assign attributes to self object
        self.__processor = processor # setting attribute to become priviate with the double underscore

    # implementing setter and getter
    # Using @property decorator sets an attribut as Read-Only
    @property
    def processor(self):
        return self.__processor

    # Use attribute.setter to then allow setting of the attribute to a new value (principle of ENCAPSULATION)
    @processor.setter
    def processor(self, value):
        if value not in ["intel", "amd", "nvidia"]:
            raise Exception("value must be either 'amd', 'intel', or 'nvidia'")
        self.__processor = value

    # Using private methods with double underscore ensures those methods are only accessible from the class level and not the instance level (principle of ABSTRACTION)
    def __get_ram(self):
        pass

    def __get_hard_disk(self):
        pass

    def __get_other_drivers(self):
        pass
    
    def change_motherboard(self) -> str:
        self.__get_ram()
        self.__get_hard_disk()
        self.__get_other_drivers()

        return "Gotten a new motherboard"
