import uuid

class Item:
    def __init__(self,id = None,condition=0,age = 0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if not 0 <= self.condition <= 5:
            raise ValueError('condition must be between 0 and 5')
        if self.condition < 1:
            description = "poor"
        elif 1 <= self.condition < 2:
            description = "heavily used"
        elif 2 <= self.condition < 3:
            description = "used"
        elif 3 <= self.condition < 4:
            description = "gently used"
        elif 4 <= self.condition <= 5:
            description = "mint"
      
        
        return description

    


    
    