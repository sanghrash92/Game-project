class User:
    """making a profile class."""
    
    def __init__(self, first_name, last_name, age, sex):
        """Describing the users info."""
        self.name = first_name
        self.last = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0
        
    def describe_user(self):
        """A summary of the user"""
        print(f"{self.name} {self.last} {self.age} {self.sex}")
              
    def greet_user(self):
        """A personalised greeting."""
        print(f"Hello {self.name} {self.last}! How are you?")
        print(f"You are {self.age} and you identify as {self.sex}.")
        
    def login(self):
        print(f"This is the amount of time you've tried to log in = {self.login_attempts}.")
    
    def increment_login(self, users):
        """Keeping a track of people logging in."""
        if users >= self.login_attempts:
            self.login_attempts = users
            self.login_attempts += users
              
                
class Admin(User):
    """Represents aspects of user class, specific to admin privilege."""
    
    def __init__(self, first_name, last_name, age, sex):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an admin."""
        super().__init__(first_name, last_name, age, sex)
        self.privilege = ['can add post', 'can delete post', 'can ban user']
        
    def show_privileges(self):
        """Prints the privileges the admin has."""
        
        return f"Here's the list of privilege - {self.privilege}."

my_profile = Admin('Sanji', 'Bhattachan', 20, 'M')
print(my_profile.show_privileges())