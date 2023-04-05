class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        print(f"My dog name is {self.name} and he {self.age} years old.")
    
    def get_info(self):
        print(f"My dog coat color is {self.coat_color}.")
    
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def display(self):
        print( f"My dog coat color is {self.coat_color}.")

    def info(self):
        print(f"My dog name is {self.name} and he {self.age} years old.")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def display(self):
        print(f"My dog coat color is {self.coat_color}.")
    
    def info(self):
        print(f"My dog coat color is {self.coat_color}.")


dog1= Dog("demon" , 1 ,"black")
dog1.description()
dog1.get_info()

dog2 = Bulldog("jimmy",2 ,"brown")
dog2.description()
dog2.get_info()

dog3 = JackRussellTerrier("Kalu",3,"white")  
dog3.description()
dog3.get_info()  


