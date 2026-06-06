class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Cat(Animal):
    def meow(self):
        print("Cat meows")


dog = Dog()
dog.sound()
dog.bark()

cat = Cat()
cat.sound()
cat.meow()