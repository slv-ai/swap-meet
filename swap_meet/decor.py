import uuid
class Decor:
    def __init__(self,width = 0,length = 0):
        self.width = width
        self.length = length 
        self.id = uuid.uuid4().int
    def get_category (self):
        return self.__class__.__name__
    def __str__(self):
        return f"An object of type {self.get_category} with id {self.id}. It takes up a {self.width} by {self.length} sized space."