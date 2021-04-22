class Category:
    
    #constructor
    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount
            
    #methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def check_balance(self, amount):
        #this should return a True or False, it checks if amount is less or greater than self.amount
        if amount <= self.amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        #reverse of deposit, will use check_balance to see if enough budget to withdraw        
        if self.check_balance(amount) is True:
            self.amount -= amount
            return "You have successfully withdrawn {} in {} category".format(amount, self.category)
        else:
            return "You don't have enough funds to withdraw"

    def transfer(self, amount, category):
        #transfer between two instantiated categories, will use check_balance to see if enough budget to transfer
        if self.check_balance(amount) is True:
            return self.withdraw(amount) + ' ' + category.deposit(amount)
        else:
            return "You don't have enough funds in " + self.category + " to transfer"
        
        
food_category = Category('Food Budget', 500)
clothing_category = Category('Clothing Budget', 300)
car_category = Category('Car Budget', 600)
education_category = Category('Education Budget', 250)

print(food_category.deposit(250))
print(food_category.budget_balance())
print(food_category.check_balance(600))
print(food_category.withdraw(400))
print(food_category.budget_balance())
print(food_category.transfer(600, car_category))



