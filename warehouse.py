class Warehouse(object):
    def __init__(self, row, column, stock):
        self.row = row
        self.column = column
        self.stock = stock

    def fulfillable_items(self, order):
        items = []
        for item in order.items:
            if self.stock[item] > 0:
                items.append(item)
        return items
