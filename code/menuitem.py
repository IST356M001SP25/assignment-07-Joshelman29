from dataclasses import dataclass, asdict

@dataclass
class FoodItem:
    """Class representing a food item on a menu"""
    # Core attributes of each menu item
    category: str
    name: str
    price: float
    description: str

    # converting instance to dictionary
    def convert_to_dict(self):
        """Serialize the food item to a dictionary"""
        return asdict(self)

    @classmethod
    def create_from_dict(cls, item_data):
        """Create a FoodItem from dictionary data"""
        return cls(**item_data)
    

    
# creating a new food item instance
cheese_app = FoodItem(name="Mozzarella Sticks", price=8.99, category="Starters",  
        description="Fried cheese sticks served with marinara sauce."  )

# modifying an attribute
cheese_app.category = "Appetizers"
print(cheese_app)
    
# converting to dictionary
print(cheese_app.convert_to_dict())

    # creating from dictionary
main_course = FoodItem.create_from_dict({"name": "Burger", 
                                 "price": 9.99, 
                                 "description": "A delicious burger.", 
                                 "category": "Entrees"})
print(main_course)