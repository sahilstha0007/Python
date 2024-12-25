class Parrot :
    # class attribute
    name = " "
    age = 0

# Create parrot1 object
parrot1 = Parrot()
parrot1.name = "parry"
parrot1.age = 10

# Create another object parrot2
parrot2 = Parrot()
parrot2.name = "blue"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")