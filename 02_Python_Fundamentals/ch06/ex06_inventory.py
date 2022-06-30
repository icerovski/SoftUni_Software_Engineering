'''
Create a class Inventory. The __init__ method should accept only the __capacity: int (private attribute) of
the inventory. You can read more about private attributes here. Each inventory should also have an attribute called
items - empty list, where all the items will be stored. The class should also have 3 methods:
• add_item(item: str) - adds the item in the inventory if there is space for it. Otherwise, returns
"not enough room in the inventory"
• get_capacity() - returns the value of __capacity
• __repr__() - returns "Items: {items}.\nCapacity left: {left_capacity}". The items should
be separated by ", "
'''

class Inventory:
    items = []

    def __init__(self, __capacity: int) -> None:
        # https://www.tutorialsteacher.com/python/public-private-protected-modifiers
        self.__capacity = __capacity
    
    def add_item(self, item: str):
        if len(Inventory.items) >= self.__capacity:
            return 'not enough room in the inventory'
        Inventory.items.append(item)

    def get_capacity(self):
        return self.__capacity

    def format_lst(self, lst):
        return ', '.join(lst)

    def __repr__(self) -> str:
        return f'Items: {self.format_lst(Inventory.items)}.\nCapacity left: {self.get_capacity() - len(Inventory.items)}'


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)