#classes are similar to us combining a date structure like a dict w functions
#but it also will allow us to create copies of these structures(instances) that maintain sepreate data values, while
#mainting the same type of data. 



class Person: 
    #attributes/fields
    name="Miriana" 
    age=20

#classes are like blueprints. we can use variables within a class to act as a "master copy" that can br overriden 
#we make an instance of that class. 

#when we use a class we call this making an instance or instantiating 

instance1 = Person() #create the instance of the class above

#to access fields inside of the class we use dot notation 
print(instance1.name)
print(instance1.age)

#we can change the data after making the instance
instance2 = Person() 

instance2.name = "Allison" 
instance2.age = 15

print(instance2.name)
print(instance2.age)

#CLASS VS INSTANCE VAR

#classes can represent real world objects with data and behavior that can be modifiyed and changed
#for instance we want all dogs to have a name and age
#but each dog will have a different name and age
#but maybe all dogs can say woof

#we can actually leave our attributes and fields blank to allow us to insert data upon the creation od the
#instance. we do this when we know that the data will ne different for eaach instance od a class
#(i.e. dogs name and age) 
#these are called instance variables

#however there may be a variable that is always consistent no matter how many instances of a class you make
#ie all ogres health is 50 HP
#in our case... all our dogs can say woof of all dogs are animals
#we call these class variables

class Dog:
    #class variable
    animal = "dog"
    #anytime we create a new Dog instance, animal will always be dog
#constructors = initialize the instance of a class with some data that the user or other parts of the program 
#provide

def _init_(dog,name,age):
    #take in an argument and set it the instance own data values ie for itself
    Dog.name = name
    Dog.age = age

#we can also define not only common types of data, but also common behavior. ie all dogs bark.. we can make
#functions

def bark(self):
    print("WOOF!")

#create instance of a class... put the name and age in the () just like a function argument
dog1 = Dog("Kilo", 6)
dog2 = Dog("Tito", 8)

print(dog1.name)
print(dog1.age)
print(dog1.animal)

print(dog2.name)
print(dog2.age)
print(dog2.animal)

#remember all of our dogs can bark

dog1.bark()
dog2.bark()