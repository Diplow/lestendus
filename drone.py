import math

class Drone(object):

    def __init__(self, idx, warehouses, load):
        self.load = load
        self.row = warehouses[0].row
        self.column = warehouses[0].column
        self.plan = list()
        self.idx = idx

    def available(self, turn):
        if not self.plan:
            return True
        return turn >= self.plan[-1]['date']

    def create_plan(self, order, warehouses, t):
        warehouse, number  = self.find_closer_warehouse(order, warehouses)
        self.plan.append({"type":"L", "drone_id": self.idx, "warehouse_id": warehouse,\
                "product_id": order.items[0], "number": 1})
        self.plan.append({"type":"D", "drone_id": self.idx, "customer_id": order.id,\
                "product_id": order.items[0], "number": 1, "date": number + t})

    def find_closer_warehouse(self, order, warehouses):
        warehouse_options = list()
        for w_idx, warehouse in enumerate(warehouses):
            if warehouse.stock[order.items[0]] > 0:
                warehouse_options.append((w_idx, self.compute_path(warehouse, order)))
        return sorted(warehouse_options, key=lambda x: x[1])[0]

    def compute_path(self, warehouse, order):
        return math.sqrt( (self.row-warehouse.row)**2 + (self.column-warehouse.column)**2) \
                  +  math.sqrt( (order.row-warehouse.row)**2 + (order.column-warehouse.column)**2)





