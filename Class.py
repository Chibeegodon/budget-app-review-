class category():

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(name, amount):
        """
        The deposit method allows funds to be deposited to each of the
        category mentioned.
        """
        balance = all(amount)
        return balance

    def withdraw(self, amount):
        balance = all(amount)
        return balance

    def transfer(self, amount, category):
        self.withdraw(amount, "transfer to" + category.name)
        category.deposit(amount, "transfer from" + self.name)
        return True
        return False


def init():
    print("Welcome to your Budget App")
    menu()

def menu():
    try:
        user = int(input("What task will you like to perform? \n Press (1)Depost funds (2) Withdraw fund (3)transfer Balance amounts between Categories.'"))
    except:
     print("Invalid input")