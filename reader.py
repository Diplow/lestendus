<<<<<<< HEAD

class Reader(object):

    def init(self):
        pass
=======
busy_day_file_path = '../busy_day.in'
mother_of_all_warehouses_file_path = '../mother_of_all_warehouses.in'
redundancy_file_path = '../redundancy.in'


def get_input(FILE_PATH):
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


BUSY_DAY_INPUT = get_input(busy_day_file_path)
MOTHER_OF_ALL_WAREHOUSES_INPUT = get_input(mother_of_all_warehouses_file_path)
REDUNDANCY_INPUT = get_input(redundancy_file_path)
>>>>>>> eb366a46fe707a6fd470a79c265bfedfb12bfa07
