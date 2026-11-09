#function -> directly -> file 
#class -> holder of a functional aspect

class Animal: 
    def eat(self):
        print("Animal is eating")

class  Dog(Animal): 
    def bark(self):
        print("Dog is barking")

# here we didn't call the function 
# bark() -> we need to create an object of Dog class to call the function bark()
# eat() -> we can call this function directly because it is inherited from the Animal class

# for example, if we create an object of Dog class, we can call both eat() and bark() functions
# bur if we create an object of Animal class, we can only call the eat() function, not the bark() function

# for calling a function, we need to create an object of the class and then call the function using that object
    # d-> object of Dog class (self is passed automatically when we call the function using the object)
    # Dog() is class name, d is object of Dog class, eat() is function name
# Dog.eat(d) -> this is also a way to call the function eat() using the object of Dog class, but it is not recommended because it is not a good practice to call a function using the class name and passing the object as an argument
d = Dog() # creating an object of Dog class
d.eat() # calling the eat() function using the object of Dog class
d.bark() # calling the bark() function using the object of Dog class