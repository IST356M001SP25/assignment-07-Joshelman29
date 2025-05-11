from dataclasses import dataclass, asdict

@dataclass
class FoodItem:
    # these are built-in properties
    category: str
    name: str
    price: float
    description: str

    # convert to a dictionary
    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return FoodItem(**data)
    
if __name__=='__main__':
    # example of howto use the dataclass

    # create a new FoodItem    
    mozz = FoodItem(name = "Mozzarella Sticks", 
                    price = 8.99, 
                    category="Apps", 
                    description="Fried cheese sticks served with marinara sauce.")

    # can assign a new category
    mozz.category = "Appetizers"
    print(mozz)
    # convert back to a dictionary
    print(mozz.to_dict())

    # create a new MenuItem from a dictionary
    burger = FoodItem.from_dict({"name": "Burger", 
                                 "price": 9.99, 
                                 "description": "A delicious burger.", 
                                 "category": "Entrees"})
    print(burger)

