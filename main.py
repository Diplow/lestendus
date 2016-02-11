from reader import Reader
BUSY_DAY_FILE_PATH = '../busy_day.in'
MOTHER_OF_ALL_WAREHOUSES_FILE_PATH = '../mother_of_all_warehouses.in'
REDUNDANCY_FILE_PATH = '../redundancy.in'


def format_actions_list(actions):
    Q = len(res)
    print Q
    for action in actions:
        if action["type"] in ["L", "U"]:
            print action["drone_id"], action["type"], action["warehouse_id"], action["product_id"], action["number"]
        if action["type"] == "D":
            print action["drone_id"], action["type"], action["customer_id"], action["product_id"], action["number"]
        if action["type"] == "W":
            print action["drone_id"], action["type"], action["number"]


if __name__ == "__main__":
    # init
    r = Reader("/PATH/TO/FILE")
    drones, dw, orders, T = r.init()
    items = split_orders_to_items(orders)

    # do it
    for t in xrange(T):
        for drone in drones:
            if drone.available():
                drone.do_plan(dw, items)

    # format res
    res = []
    for d in drones:
        res.append(drones.get_actions())
    format_actions_list(res)
    
