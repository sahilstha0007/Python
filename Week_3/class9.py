# base class
class Animal:
    def eat(self):
        print("I can eat!!.")

    def sleep(self):
        print("I can sleep!!")

# derived class
class Dog(Animal):
    def bark(self):
        print("I can bark! woof woof!!")

# derived class
class Lion(Animal):
    def roar(self):
        print("I can roar !")

# Create object of the Dog class
dog1 = Dog()

# Calling members of the base class
dog1.eat()
dog1.sleep()

# calling member of the derived class
dog1.bark()


# base class


# Create object of the Dog class
Lion1 = Lion()

# Calling members of the base class
Lion1.eat()
Lion1.sleep()

# calling member of the derived class
Lion1.roar()










