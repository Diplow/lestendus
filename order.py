class Order(object):
    """ 'items' attribute is a list of product_ids representing each item ordered. """
    def __init__(self, id, row, column, items):
        self.id = id
        self.row = row
        self.column = column
        self.items = items
        self.number_of_items = len(items)
