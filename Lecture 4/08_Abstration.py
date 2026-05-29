# Abstration - Hiding internal details & showing only essential features. 
# It is blueprint for the classes. 

from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("MOO!")

lion = Lion() 
lion.make_sound() 

cow = Cow()
cow.make_sound() 

