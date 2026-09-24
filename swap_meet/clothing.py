from swap_meet.item import Item

class Clothing(Item):
    def __init__(self,id = None ,fabric = "Unknown",condition =0):
        self.fabric = fabric
        super().__init__(id,condition)
        
    # def get_category(self):
    #     return self.__class__.__name__
    
    def __str__(self):
        type = super().__str__()
        return f"{type} It is made from {self.fabric} fabric."

