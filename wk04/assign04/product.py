class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        subtotal = self.price * self.quantity
        return subtotal

    def display(self):
        display = '{} ({}) - ${:.2f}'.format(self.name, self.quantity, round(self.get_total_price(), 2))
        print(display)

