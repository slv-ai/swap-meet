import uuid
class Decor:
    def __init__(self,width = 0,length = 0):
        self.width = width
        self.length = length 
        self.id = uuid.uuid4().int
    def get_category (self):
        return "Decor"