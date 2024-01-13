# This is a case-study for restaurant management
from enum import Enum
from multiprocessing.connection import wait
from time import sleep

order_id_counter = 0

def get_next_order_id():
    global order_id_counter
    order_id_counter += 1
    return order_id_counter

class Menu:
    
    def __init__(self) -> None:
        self.currency = "$"
        self.menu = [
            {   
                'item': 'rice',
                'type': 'main',
                'price': 100,
            },
            {   
                'item': 'beer',
                'type': 'bar',
                'price': 50,
            },
            {   
                'item': 'shake',
                'type': 'juice',
                'price': 20,
            },
        ]
    
    def display(self):
        print("--------- Todays Menu ---------")
        for index, item in enumerate(self.menu):
            print(f"{index+1}. {item['item']}  -  {self.currency}{item['price']}")
            
        return self.menu
            
class Kitchen:
    
    def __init__(self) -> None:
        pass
    
    def prepare_food(self, item, fn_notify_waiter, fn_change_order_status, *args):
        # print(f"preparing food item {item['item']} started ...")
        # sleep(1)
        # print(f"preparing food item {item['item']} done.")
        # call the waiter to get the prepared food
        fn_notify_waiter('sample')
        # change order status from processing to done
        fn_change_order_status(*args)
          
class MainKitchen(Kitchen):
    pass

class BarKitchen(Kitchen):
    pass

class JuiceKitchen(Kitchen):
    pass

class KitchenTypes(Enum):
    main = MainKitchen()
    bar = BarKitchen()
    juice = JuiceKitchen()
    processing = 0
    done = 1
    
    @classmethod
    def has_value(cls, item):
        return item in [name for name, member in cls.__members__.items()]
    
class KitchenFactory():
    
    def __init__(self) -> None:
        self.order_status = {}
    
    def place_order_to_kitchen(self, order, fn_notify_waiter):
        # get order id
        order_id = order.id
        # get order items
        items = order.items
        # start preparing food
        self.order_status[order_id] = {
            'status': KitchenTypes.processing,
            'object': order,
        }
        # send food order to respective kitchens
        for item in items:
            # get kitchen type for item
            kitchen_type = item['type']
            # if kitchen type exists then send to prepare food
            if KitchenTypes.has_value(kitchen_type):
                # start preparing food
                KitchenTypes[kitchen_type].value.prepare_food(
                    item, 
                    fn_notify_waiter, 
                    self.change_order_status, 
                    order_id
                )
        
    def change_order_status(self, order_id):
        # get order details
        order = self.order_status[order_id]
        # update status
        order['status'] = KitchenTypes.done
        order['object'].processing_done()
    
    def check_order_status(self):
        pass
    
    def cancel_order(self):
        pass
    
    def update_order(self):
        pass

class Order:
    
    def __init__(self, table_id, items, kitchen_factory) -> None:
        
        self.id = get_next_order_id()
        self.items = items
        self.table_id = table_id
        self.status = KitchenTypes.processing
        self.kitchen_factory = kitchen_factory
        
    def processing_done(self):
        self.status = self.kitchen_factory.order_status[self.id]['status']
    
    def check_order_status(self):
        pass
    
    def cancel_order(self):
        pass
    
    def update_order(self):
        pass
            
    def get_bill(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

class Waiter:
    
    def __init__(self, id, kitchen_factory) -> None:
        self.waiter_id = id
        self.orders_placed = 0
        self.money_collected = 0
        self.tip_collected = 0
        
        self.kitchen_factory = kitchen_factory
        
        self.menu = Menu()
        self.orders = {
            'table-1' : {},
            'table-2' : {},
            'table-3' : {},
            'table-4' : {},
            'table-5' : {},
        }
        
    def get_menu(self):
        return self.menu.display()
    
    def update_my_order_details(self, table_id, items):
        # store the current order details
        self.orders[table_id][self.order.id] = {
            'order': items,
            'bill': self.order.get_bill(),
        }
        
    def place_order(self, items, table_id):
        # make a new order class
        self.order = Order(table_id, items, self.kitchen_factory)
        # place the order
        self.kitchen_factory.place_order_to_kitchen(self.order, self.get_notification)
        # update my tables served
        self.update_my_order_details(table_id, items)
        # return order id
        return self.order.id
        
    def get_notification(self, kitchen):
        print(f"notification for waiter - {self.waiter_id}, go to kitchen - {kitchen}")
    
    def get_bill(self, table_id, order_id):
        print(f"Total bill - {self.orders[table_id][order_id]['bill']}")


class Restaurant:
    
    def __init__(self) -> None:
        self.kitchen_factory = KitchenFactory()

    def start(self):
        pass
        
        
        
# restaurant = Restaurant()
# restaurant.start()

kitchen_factory = KitchenFactory()

table_1 = 'table-1'
table_2 = 'table-2'
    
waiter_1 = Waiter(1, kitchen_factory)
waiter_2 = Waiter(2, kitchen_factory)

menu = waiter_1.get_menu()

order_id = waiter_1.place_order(menu, table_1)
waiter_1.get_bill(table_1, order_id)

order_id = waiter_2.place_order(menu, table_2)
waiter_2.get_bill(table_2, order_id)