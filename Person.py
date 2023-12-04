from Order import Order
class Person:
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink
        self.persons_order = self.my_order()
        
    def my_order(self):
        current_order = Order(self.favorite_drink, self.name)
        return current_order
       

