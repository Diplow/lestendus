from copy import deepcopy

class Warehouse(object):
    def __init__(self, row, column, stock):
        self.row = row
        self.column = column
        self.stock = stock

    def _can_fulfill_order(self, order):
        tmp = deepcopy(self.stock)
        for item in order.items():
            if self.stock[item] == 0:
                self.stock = tmp
                return False
            else:
                self.stock[item] -= 1
        return True
