class Category:
    def __init__(self, fname, lname, Food, Clothing, Car, Education, Entertainment):
        self.fname = fname
        self.lmane = lname
        self.Food = Food
        self.Clothing = Clothing
        self.Car = Car
        self.Education = Education
        self.Entertainment = Entertainment

    # check your budget amounts
    def check_balance(self):
        print('Budget for', self.fname)     
        print('Food Budget: $', self.Food)
        print('Clothing Budget: $', self.Clothing)
        print('Car Budget: $', self.Car)
        print('Education Budget: $', self.Education)
        print('Entertainment Budget: $', self.Entertainment)
        print('Toatl Budget: $', self.Food+self.Clothing+self.Car+self.Education+self.Entertainment)

    # Deposit to your budget
    def deposit(self):
        print('(1) Food')
        print('(2) Clothing')
        print('(3) Car')
        print('(4) Education')
        print('(5) Entertainment')
        deposit_category = input('What category would you like to increase? \n')
        deposit_amt = input('How much would you like to add to this budget? \n')

        if int(deposit_category) == 1:
            print('Your new food budget is $', self.Food + int(deposit_amt))
        elif int(deposit_category) == 2:
            print('Your new clothing budget is $', self.Clothing + int(deposit_amt))
        elif int(deposit_category) == 3:
            print('Your new clothing budget is $', self.Car + int(deposit_amt))
        elif int(deposit_category) == 4:
            print('Your new clothing budget is $', self.Education + int(deposit_amt))
        elif int(deposit_category) == 5:
            print('Your new clothing budget is $', self.Entertainment + int(deposit_amt))
        else:
            print('Not a valid option')

    # Withdraw from your budget/add an expense
    def withdraw(self):
        print('(1) Food')
        print('(2) Clothing')
        print('(3) Car')
        print('(4) Education')
        print('(5) Entertainment')
        withdraw_category = input('What category would you like to withdraw from? \n')
        withdraw_amt = input('How much would you like to subtract from this budget? \n')

        if int(withdraw_category) == 1:
            print('Your new food budget is $', self.Food - int(withdraw_amt))
        elif int(withdraw_category) == 2:
            print('Your new clothing budget is $', self.Clothing - int(withdraw_amt))
        elif int(withdraw_category) == 3:
            print('Your new clothing budget is $', self.Car - int(withdraw_amt))
        elif int(withdraw_category) == 4:
            print('Your new clothing budget is $', self.Education - int(withdraw_amt))
        elif int(withdraw_category) == 5:
            print('Your new clothing budget is $', self.Entertainment - int(withdraw_amt))
        else:
            print('Not a valid option')

    # Transfer from one budget to another
    def transfer(self):
        print('(1) Food')
        print('(2) Clothing')
        print('(3) Car')
        print('(4) Education')
        print('(5) Entertainment')
        transfer_from_category = input('What category would you like to transfer from? \n')
        transfer_to_category = input('What category would you like to transfer to? \n')
        transfer_amt = input('How much would you like to subtract from this budget? \n')

        if int(transfer_from_category) == 1:
            transfer_from_category = self.Food
        elif int(transfer_from_category) == 2:
            transfer_from_category = self.Clothing
        elif int(transfer_from_category) == 3:
            transfer_from_category = self.Car
        elif int(transfer_from_category) == 4:
            transfer_from_category = self.Education
        elif int(transfer_from_category) == 5:
            transfer_from_category = self.Entertainment
        else:
            print('Not a valid option')

        if int(transfer_to_category) == 1:
            transfer_to_category = self.Food
        elif int(transfer_to_category) == 2:
            transfer_to_category = self.Clothing
        elif int(transfer_to_category) == 3:
            transfer_to_category = self.Car
        elif int(transfer_to_category) == 4:
            transfer_to_category = self.Education
        elif int(transfer_to_category) == 5:
            transfer_to_category = self.Entertainment
        else:
            print('Not a valid option')
        
        new_balance_1 = transfer_from_category - int(transfer_amt)
        new_balance_2 = transfer_to_category + int(transfer_amt)
        print('Your new balances are $', new_balance_1, 'and $', new_balance_2)

        
        

Peter_budget = Category('Peter', 'Godoy',50,25,100,75,30)
Mike_budget = Category('Mike', 'Toohey',40,50,90,60,50)
David_budget = Category('David', 'Viellgas',60,15,110,50,45)
Eric_budget = Category('Eric', 'Gee',55,30,95,65,55)

Peter_budget.check_balance()
Mike_budget.deposit()
David_budget.withdraw()    
Eric_budget.transfer()