class CoffeeBar:
    def __init__(self, name, barista):
        self.name = name
        self.orders_list= []
        self.barista = barista

    def place_order(self, order):
        self.orders_list.append(order)
             
    def process_order(self):
        for order in self.orders_list:
            print(self.barista.greeting, order.to_string())


