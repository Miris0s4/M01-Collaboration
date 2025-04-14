#we will make a quick app that will randomly pick from a list of restaurants to go to. 

#things we need to know
#1 - how to grab a module from an outside library or the standard library from python
#2 - how to implement our own custom modules

#to import any module or package we use the import keyword


from random import choice

#list of restaurants
places = ["mcdonalds", "tacobell", "subway", "popeyes"]

def pick():
    return choice(places)
