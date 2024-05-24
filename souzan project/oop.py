class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Interest rate: {self.interest_rate}")
        print(f"Current balance: {self.balance}")
    
def main():
  id = BankAccount("2790230", "souzzan alhalabi")
  print("Bank Account:")
  print(f"Initial balance: {id.get_balance()}")
  id.deposit(1000)
  print(f"Balance after deposit: {id.get_balance()}")
  id.withdraw(500)
  print(f"Balance after withdrawal: {id.get_balance()}")

  ids = SavingsAccount("2790230", "souzzan alhalabi", 0.03)  
  print("\nSavings Account:")
  print(f"Initial balance: {ids.get_balance()}")
  ids.deposit(2000)
  print(f"Balance after deposit: {ids.get_balance()}")
  ids.apply_interest()
  
main()







