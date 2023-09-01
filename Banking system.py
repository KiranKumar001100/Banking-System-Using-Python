class customer:
    def __init__(self, name, account_number, password, balance):
        self.name = name
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Successfully {amount} Rs Deposited, Your Current Balance {self.balance} Rs')
            print('')
        else:
            print('Invalid Amount')
            print('')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Successfully {amount} Rs Withdrawn, Your Current Balance {self.balance} Rs')
            print('')
        else:
            print('Insufficient Balance')
            print('')

    def get_balance(self):
        return self.balance

class bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, name, account_number,password, intial_balance):
        if account_number not in self.customers:
            new_customer = customer(name, account_number, password, intial_balance)
            self.customers[account_number] = new_customer
            print('Successfully Account Created')
            print('')
        else:
            print('Account Number Already Exist, Please Enter New Account Number')
            print('')

    def view_balance(self, account_number):
        if account_number in self.customers:
            customer = self.customers[account_number]
            print(f'Name : {customer.name}')
            print(f'Account Number : {customer.account_number}')
            print(f'Current Balance : {customer.balance}')
            print('')
        else:
            print('Account Number Not Found, ')
            print('')

    def transaction(self, account_number, transaction_type, amount):
        if account_number in self.customers:
            customer = self.customers[account_number]
            if transaction_type == 'deposit':
                customer.deposit(amount)
            elif transaction_type == 'withdraw':
                customer.withdraw(amount)
            else:
                print('Invalid Transaction Type')
                print('')
        else:
            print('Account Number Not Found')
            print('')

if __name__ == '__main__':
    bank = bank()
    while True:
        print('1. Create New Account Number')
        print('2. View Balance')
        print('3. Deposit')
        print('4. Withdraw')
        print('5. Exit')
        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            name = input('Enter Customer Name : ')
            account_number = input('Enter Account Number : ')
            pin = int(input('Enter Password : '))
            intial_balance = float(input('Enter Amount To Deposit : '))
            bank.create_account(name, account_number, pin, intial_balance)
        elif choice == 2:
            account_number = input('Enter Account Number : ')
            password = int(input('Enter Password : '))
            if password != pin:
                print('Wrong Password')
                break
            else:
                print('')
            bank.view_balance(account_number)
        elif choice == 3:
            account_number = input('Enter Account Number : ')
            password = int(input('Enter Password : '))
            if password != pin:
                print('Wrong Password')
                break
            else:
                print('')
            amount = float(input('Enter Deposit Amount : '))
            bank.transaction(account_number,'deposit', amount)
        elif choice == 4:
            account_number = input('Enter Account Number : ')
            password = int(input('Enter Password : '))
            if password != pin:
                print('Wrong Password')
                break
            else:
                print('')
            amount = float(input('Enter Withdrawal Amount : '))
            bank.transaction(account_number, 'withdraw', amount)
        elif choice == 5:
            print('Thank You For Using Our Banking System')
            break
        else:
            print('Invalid Choice, Please Try Again')