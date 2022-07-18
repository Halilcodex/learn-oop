import csv

# Object/Class Definition
class Item:
    # Declaring classs variables/attributes
    pay_rate = 0.8
    all_instances = []
    # declare instance attributes using the init method
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # To ensure sanity of values, assert that price and quantity are to be positives
        assert price >= 0, f"Price must be greater than or equal to zero: {price} provided"
        assert quantity >= 0, f"Quantity must be greater than or equal to zero: {quantity} provided"

        # Then assign variables to instance as attributes (i.e. assign to self object)
        self.name = name
        self.price = price
        self.quantity = quantity

        # Keep a record of all instances declared
        Item.all_instances.append(self)

    # declaring other methods within the class
    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # declaring a class method which is to be used to instantiate our classes from a csv file
    @classmethod
    def instantiate_from_csv(cls):
        with open("data.csv", 'r') as f:
            data = list(csv.DictReader(f))
            [Item(price=float(item.get("price")), quantity=int(item.get("quantity")), name=item.get("name")) for item in data]

    # declaring a static method
    @staticmethod
    def is_an_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else: return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
