class Order(object):
    """ 'items' attribute is a list of product_ids representing each item ordered. """
    def __init__(self, row, column, items):
        self.row = row
        self.colum = colum
        self.items = items
        self.number_of_items = len(items)
