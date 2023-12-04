from Person import Person
from Order import Order
from CoffeeBar import CoffeeBar
from Barista import Barista

amy = Person('Amy','coffee')
# print(amy.persons_order.to_string())

bob = Person('Bob', 'tea')
# print(bob.persons_order.to_string())

cat = Person('Cat', 'Milk')
# print(cat.persons_order.to_string())

#CHALLENGE 10
Kevin = Barista('Kevin', 'water', 'Hey dude!')

# CHALLENGE 6
JoesCoffeeBar = CoffeeBar('Joes', Kevin)
# CHALLENGE 7
JoesCoffeeBar.place_order(amy.persons_order)
JoesCoffeeBar.place_order(bob.persons_order)
JoesCoffeeBar.place_order(cat.persons_order)
#CHALLENGE 8 
JoesCoffeeBar.process_order()


