class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
      
        
d = Dog('Tim', 12)
print(d.get_age())
d1 = Dog('larry', 10)
print(d1.get_name())