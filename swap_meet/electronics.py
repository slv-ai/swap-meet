from swap_meet.item import Item

class Electronics(Item):
    def __init__(self,id = None,type="Unknown",condition=0,age=0):
        self.type=type
        super().__init__(id,condition,age)

    # def get_category (self):
    #         return self.__class__.__name__

    def __str__(self):
        type = super().__str__()
        return f"{type} This is a {self.type} device."
    

