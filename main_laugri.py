from operator import itemgetter

ordered_orders = 
for t in T:
    for order in ordered_orders:
        if order.done:
            continue
        for drone in [d for d in drones if drone.available(t)]:
            if not order.done:
                fullest_warehouse = warehouses[max(enumerate([len(wh.fulfillable_items(order)) for wh in warehouses]), key=itemgetter(1))[0]]
                drone.deliver(order, fullest_warehouse.fulfillable_items(order), fullest_warehouse)
            else:
                break
