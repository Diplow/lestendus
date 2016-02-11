from drone import drone
from warehouse import Warehouse
from product import Product
from order import Order


class Reader(object):
    def __init__(self, path):
        self.path = path

        self.deadline = input_data["deadline"]
        self.rows = input_data["rows"]
        self.columns = input_data["columns"]

        self.num_products = input_data["num_products"]
        self.num_drones = input_data["num_drones"]
        self.num_orders = input_data["num_orders"]
        self.num_warehouses = input_data["num_warehouses"]
        self.max_load = input_data["max_load"]

        self.drones = [Drone(input_data["max_load"]) for i in range(input_data["num_drones"])]
        self.products = [Product(weight) for weight in input_data["product_weights"]]
        self.warehouses = input_data["warehouses"]
        self.orders = [Order(order["row"], order["column"],  order["product_ids"], order["num_items"]) for order in input_data["orders"]]

    def _get_input(FILE_PATH):
        f = open(FILE_PATH, 'r')
        parameters = f.readline().split(' ')

        rows = int(parameters[0])
        columns = int(parameters[1])
        num_drones = int(parameters[2])
        deadline = int(parameters[3])
        max_load = int(parameters[4])
        num_products = int(f.readline())
        product_weights = [int(i) for i in f.readline().split(' ')]

        num_warehouses = int(f.readline())
        warehouses = []
        for i in range(num_warehouses):
            wh_row, wh_column = f.readline().split(' ')
            stock = [int(i) for i in f.readline().split(' ')]
            warehouses.append({
                "row": int(wh_row),
                "column": int(wh_column),
                "stock": stock
            })

        num_orders = int(f.readline())
        orders = []
        for i in range(num_orders):
            order_row, order_column = f.readline().split(' ')
            num_items = int(f.readline())
            product_ids = [int(i) for i in f.readline().split(' ')]
            orders.append({
                "row": int(order_row),
                "column": int(order_column),
                "num_items": num_items,
                "product_ids": product_ids
            }),

        return {
            "warehouses": warehouses,
            "rows": rows,
            "columns": columns,
            "num_drones": num_drones,
            "deadline": deadline,
            "max_load": max_load,
            "num_products": num_products,
            "product_weights": product_weights,
            "num_warehouses": num_warehouses,
            "num_orders": num_orders,
            "orders": orders,
        }
