# Learning and Refreshing on OOP (Objecte Oriented Programming) Fundamentals with Python


# The Use Case here will be a Store that sells items


# imports
from item import Item
from laptop import Laptop

laptop1 = Laptop("HP Omen", 15000, 4, "INTEL")
laptop1.apply_discount() # POLYMORPHISM is applied here as the same entity "apply discount" is used differently than it is in the parent class by virtue of modifying the pay_rate within the Laptop class
laptop1.processor = "amd"
print(laptop1.change_motherboard())
Item.instantiate_from_csv()
item6 = Item("Charger", 15000, 4)
item6.apply_discount()
print(laptop1.processor, laptop1.calculate_total_price(), Item.all_instances)

# Another good example of POLYMORPHISM in python inbuilt function is the "len" function. Cos it can be used on strings, lists etc.