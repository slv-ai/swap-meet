from swap_meet.item import Item
import uuid
class Clothing:
    def __init__(self,id,fabric = "unknown"):
        self.fabric = fabric
        self.id = uuid.uuid4().int
    def get_category(self):
        return "Clothing"
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

