from dataclasses import dataclass, asdict

@dataclass
class FoodItem:
    """Class representing a food item on a menu"""
    # Core attributes of each menu item
    section: str  
    item_name: str  
    cost: float  
    details: str 

    # converting instance to dictionary
    def convert_to_dict(self):
        """Serialize the food item to a dictionary"""
        return asdict(self)

    @classmethod
    def create_from_dict(cls, item_data):
        """Create a FoodItem from dictionary data"""
        return cls(**item_data)
    

    
# creating a new food item instance
cheese_app = FoodItem(item_name="Mozzarella Sticks", cost=8.99, section="Starters",  
        details="Fried cheese sticks served with marinara sauce."  )

# modifying an attribute
cheese_app.section = "Appetizers"
print(cheese_app)
    
# converting to dictionary
print(cheese_app.convert_to_dict())

    # creating from dictionary
main_course = FoodItem.create_from_dict({
        "item_name": "Burger", 
        "cost": 9.99, 
        "details": "A delicious burger.", 
        "section": "Main Courses"})
print(main_course)