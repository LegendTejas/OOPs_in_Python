# Duck Typing
# "If it walks like a duck and quacks like a duck, it’s a duck."
# The actual type of the object doesn't matter, only the presence of the required method.

class Bird:
    def fly(self):
        print("Bird is flying.")

class Airplane:
    def fly(self):
        print("Airplane is flying.")

class Fish:
    def swim(self):
        print("Fish is swimming.")

def make_it_fly(entity):
    entity.fly()  # Works as long as 'entity' has fly() method

make_it_fly(Bird())
make_it_fly(Airplane())
# make_it_fly(Fish())  # This will cause AttributeError
