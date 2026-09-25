def my_max(collection,key):
    if not collection:
        return None
    max_item = collection[0]
    for item in collection:
        if key(item) > key(max_item):
            max_item = item
    return max_item

def my_min(collection,key):
    if not collection:
        return None
    min_item = collection[0]
    for item in collection:
        if key(item) < key(min_item):
            min_item = item
    return min_item
    

class Vendor:
    def __init__(self,inventory = None):
        self.inventory = [] if inventory is None else inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return None
    
    def get_by_id(self,item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None

    def swap_items(self,other_vendor,my_item,their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.remove(their_item)

        other_vendor.add(my_item)
        self.add(their_item)
        return True

    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self.inventory[0],other_vendor.inventory[0] = other_vendor.inventory[0],self.inventory[0]
        # my_item = self.inventory[0]
        # friend_item = other_vendor.inventory[0]
        # self.remove(my_item)
        # other_vendor.add(my_item)

        # other_vendor.remove(friend_item)
        # self.add(friend_item)
        return True

    def get_by_category(self,category):
        items = []
        for item in self.inventory:
            if item.get_category() == category:
                items.append(item)
        return items

    def get_best_by_category(self,category):
        category_items = self.get_by_category(category)
        if not category_items:
            return None
        return my_max(category_items, key = lambda item :item.condition)
        best_condition = 0.0
        for item in category_items:
            if item.condition > best_condition:
                best_condition = item.condition
        best_items = [item for item in category_items if item.condition == best_condition]
        return best_items[0]

    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if not my_best_item or not their_best_item :
            return False
        
        return self.swap_items(other_vendor,my_best_item,their_best_item)

    ## Below code by using swap_first_item ##
    
    # def swap_best_by_category(self,other_vendor,my_priority,their_priority):
    #     my_best_item = self.get_best_by_category(their_priority)
    #     their_best_item = other_vendor.get_best_by_category(my_priority)
    #     if not my_best_item or not their_best_item :
    #         return False
    #     self.inventory.remove(my_best_item)
    #     self.inventory.insert(0,my_best_item)

    #     other_vendor.inventory.remove(their_best_item)
    #     other_vendor.inventory.insert(0,their_best_item)
    #     return self.swap_first_item(other_vendor)

    def swap_by_newest(self,other_vendor,my_priority):
        """
        swap the old item  with new item from other vendor
        """
        my_items = self.get_by_category(my_priority)
        print("my_items :" ,my_items)

        vendor_items = other_vendor.get_by_category(my_priority)
        print("vendor_items :",vendor_items)

        if not my_items or not vendor_items:
            return False
        
        my_item = my_max(my_items,key = lambda item : item.age)
        vendor_item = my_min(vendor_items,key= lambda item : item.age)
        print("my_item_to_swap : ", my_item)
        print("vendor_item_to_swap :",vendor_item)

        return self.swap_items(other_vendor,my_item,vendor_item)

