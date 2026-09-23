from swap_meet.item import Item
import uuid
class Clothing(Item):
    def __init__(self,id = None ,fabric = "Unknown",condition =0):
        self.fabric = fabric
        super().__init__(id,condition)
        
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

