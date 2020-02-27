class Order:
    def __init__(self):
        self.id = ""
        self.products = []

    def get_subtotal(self):
        subtotal = 0
        for self.product in self.products:
            subtotal += self.product.get_total_price()
        return subtotal

    def get_tax(self):
        tax = self.get_subtotal() * .065
        return tax

    def get_total(self):
        total = 0
        total = self.get_tax() + self.get_subtotal()
        return total

    def add_product(self, product):
        self.products.append(product)

    def display_receipt(self):
        print("Order: {}".format(self.id))
        for self.product in self.products:
            self.product.display()
        print("Subtotal: ${:.2f}".format(round(self.get_subtotal(), 2)))
        print("Tax: ${:.2f}".format(round(self.get_tax(), 2)))
        print("Total: ${:.2f}".format(round(self.get_total(), 2)))
