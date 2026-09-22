from swap_meet.item import Item
class Electronics(Item):
    def __init__(self,type="unknown"):
        self.type=type
    def get_category (self):
            return self.__class__.__name__
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
       

