
from reader import Reader

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
    
