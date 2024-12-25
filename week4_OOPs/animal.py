class Animal:
    def eat(self):
        print("I can eat!")
        
    def sleep(self):
        print("I can sleep!")
#derived class
class Dog(Animal):
    def bark(self):
        print("I can bark! Woof woof!!")
#lion
class Lion(Animal):
    def roar(self):
        print("I can roar!!! ahahah")
#Create object of the Dog class
dog1 = Dog()
lion1= Lion()
# Calling numbers of the base class
dog1.eat()
dog1.sleep()
#Calling number of the derived class
dog1.bark()

#For the lion
lion1.eat()
lion1.sleep
lion1.roar()