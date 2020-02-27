class Customer:

    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        count = 0
        for self.order in self.orders:
            count += 1
        return count

    def get_total(self):
        total = 0.00
        for self.order in self.orders:
            total += self.order.get_total()
        return total

    def add_order(self, order):
        self.orders.append(order)

    def display_summary(self):
        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${:.2f}".format(round(self.get_total(), 2)))

    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        for self.order in self.orders:
            print()
            self.order.display_receipt()
