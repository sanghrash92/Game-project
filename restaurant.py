class Restaurant:
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Describing the name and type of the restaurant."""
        print(f"Welcome to {self.name} restaurant. We serve {self.type} food") 
        
    def open_restaurant(self):
        print(f"The {self.name} is open for business.")
        
    def restaurant(self):
        """Print a statement the restaurant has served."""
        print(f"The restaurant has served {self.number_served} people.")
    
    def set_number_served(self, people):
        """set the reading to the new value."""
        if people >= self.number_served:
            self.number_served = people
        else:
            print("You cant undo the people.")
            
    def increment_number_served(self, people):
        self.number_served += people
        
class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to an ice cream stand."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class.
        Then initialize attributes that of an electric car."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = ['vanilla', 'mint', 'choc', 'caramel']
        
    def get_flavors(self):
        """Print the name of the flavors."""
        print(f"Here's the list of the ice-cream - {self.flavor}")
        
        
my_icecream = IceCreamStand('lorenzo\'s', 'icecream')
print(my_icecream.describe_restaurant())
my_icecream.get_flavors()