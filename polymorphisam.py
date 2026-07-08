class Dog:
    def speak(self):
        print("Dog says: Bark")

class Cat:
    def speak(self):
        print("Cat says: Meow")

# Same function works for different objects
def make_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)