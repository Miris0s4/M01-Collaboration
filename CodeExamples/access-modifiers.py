#create a class called Bank Account
#Bank account will have a name and bank balance field

class Bank_Account:
    #all names and balances are different
    def __init__(self,name, balance):
        #we want to make our fields private - aka only the class and class functions can access the data
        self.__name = name
        self.__balance = balance

        #this means we cannot access or change any data without first creating a function to access that data
        #this seems redundant at first or over complicated but it allows it to create like name functions between 
        #classes that do the same thing
        #it also allows for us to create instance of a class in other classes and have them only have access to certain 
        #functions or data

        #we often call this methods to grab or change data getters and setters

        def get_name(self):
            return self.__name 
        def get_balance(self):
            return self.__balance
        
        def set_name(self, name):
            self__name = name

        def set_balance(self, balance):
            self.__balance = balance 

        acct1 = Bank_Account("Miriana", 100.00)
        print(acct1.get_name())
        print(acct1.get_balance())