import warehouse
import math

class Drone(object):

    def __init__(self, **kwargs):
        self.load = kwargs.get('load', -1)
        self.position = warehouse.position[0] #  position uptodate (0,0)
        self.plan = None

    def available(self, turn):
        if not plan:
            return True
        return turn >= self.plan[-1]['date']

    def create_plan(self, item):


    def find_closer_route(self, item, client_position):
        """ asssuming 
        """
        warehouse_options = list()
        for w_idx, warehouse_inventory in enumerate (warehouse.inventory):
            if warehouse_inventory[item] > 0:
                warehouse_options.append((w_idx, self.compute_path(warehouse.position[w_idx], client_position)))
        return sorted(warehouse_options.sort(key = lambda x: x[1]))[0]

        def compute_path(self, warehouse_position, client_position):
            return math.sqrt( (self.position[0]-warehouse_position[0])**2 + (self.position[1]-warehouse_position[1])**2) \
                  +  math.sqrt( (client_position[0]-warehouse_position[0])**2 + (client_position[1]-warehouse_position[1])**2)





